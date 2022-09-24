from .test_setup import TestSetUp
from rest_framework.test import APITestCase, force_authenticate
from api.models import Company, CustomUser, Team
from django.urls import reverse
from rest_framework import status
from faker import Faker
import uuid


class TestApiAccess(TestSetUp):
    """
    tests API only accessible by superuser
    """

    def setUp(self):
        self.regular_user = CustomUser.objects.get(username="user1")
        return super().setUp()

    # Users who are not superadmin can't access the API
    def test_api_root_access_by_non_superadmin(self):
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.get(reverse("api-root"))
        self.assertFalse(self.regular_user.is_superuser)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_api_root_access_by_superadmin(self):
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.get(reverse("api-root"))
        self.assertTrue(self.super_admin.is_superuser)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCompanyViews(TestSetUp):
    """
    tests create , retrieve , list and search functionality for Company Views
    """

    # creating a company instance with API
    def test_create_company(self):
        fake = Faker()
        self.new_company_data = {
            "name": fake.name(),
            "ceo_name": fake.name(),
            "address": fake.address(),
            "inception_date": fake.date(),
        }
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.post(reverse("company-list"), self.new_company_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_company_details(self):
        company_id = Company.objects.first().uid
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.get(
            reverse("company-detail", kwargs={"company_id": company_id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, company_id)

    # search by company name when company by that name exists
    def test_search_company_by_name_company_exists(self):
        company_name = Company.objects.first().name
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.get(reverse("company-list"), {"name": company_name})
        self.assertContains(response, company_name)

    # search by company when company by that name doesn't exist
    def test_search_company_by_name_company_exists(self):
        company_name = "some random company"
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.get(reverse("company-list"), {"name": company_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class TestTeamViews(TestSetUp):
    """
    tests create , list , retrieve , listallteams,
    """

    def setUp(self):
        fake = Faker()
        self.new_team_data = {"team_lead": fake.name()}
        return super().setUp()

    # create a team when a company with that id exists
    def test_create_team_company_id_exists(self):
        company_id = Company.objects.first().uid

        self.client.force_authenticate(user=self.super_admin)
        response = self.client.post(
            reverse("team-create", kwargs={"company_id": company_id}),
            self.new_team_data,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # create a team when a company with that id doesn't exist
    def test_create_team_company_id_not_exists(self):
        company_id = uuid.uuid4()
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.post(
            reverse("team-create", kwargs={"company_id": company_id}),
            self.new_team_data,
        )
        self.assertEqual(
            response.data, {"error": "Company with given UID doesn't exist"}
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # list of all the teams
    def test_get_team_list(self):
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.get(reverse("team-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # in our test database we have entry of 4 teams
        self.assertEqual(len(response.data), 4)

    # details of specific team
    def test_retrieve_team_detail(self):
        team_id = Team.objects.first().uid
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.get(reverse("team-detail", kwargs={"team_id": team_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, team_id)

    def test_list_all_teams_of_all_companies(self):
        self.client.force_authenticate(user=self.super_admin)
        response = self.client.get(reverse("all-teams-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # our test database has entry of 3 companies
        self.assertEqual(len(response.data), 3)

    def test_list_all_teams_of_specific_company(self):
        self.client.force_authenticate(user=self.super_admin)
        company_id = Company.objects.last().uid
        response = self.client.get(
            reverse("all-teams-detail", kwargs={"company_id": company_id})
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # our selected company has 3 teams
        self.assertEqual(len(response.data["teams"]), 3)
