from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
# using router for Company Viewset as no custom URL's are required
router.register(r"company", views.CompanyViewSet, basename="company")

# Binding other viewsets explicitly so as to assign custom URLs

# for Team Viewsets
team_list = views.TeamViewSet.as_view({"get": "list"})
team_create = views.TeamViewSet.as_view({"post": "create"})
team_detail = views.TeamViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

# for listing all the companies and their teams
all_team_list = views.ListAllTeamsViewset.as_view({"get": "list"})
all_team_detail = views.ListAllTeamsViewset.as_view({"get": "retrieve"})

urlpatterns = [
    path("", views.api_root, name="api-root"),
    path("api-auth/", include("rest_framework.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # for company viewset
    path("", include(router.urls)),
    # create a team by specifying company id in path
    path("team/create/<uuid:company_id>/", team_create, name="team-create"),
    path("team/", team_list, name="team-list"),
    path("team/<uuid:team_id>/", team_detail, name="team-detail"),
    # lisiting all the teams of all the companies
    path("team/all/", all_team_list, name="all-teams-list"),
    # list all teams of given company
    path("team/all/<uuid:company_id>/", all_team_detail, name="all-teams-detail"),
]
