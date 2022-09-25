from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _

# if any modification are required for User Model in future
class CustomUser(AbstractUser):
    pass


class Company(models.Model):
    """
    stores information about company
    columns: uid, name, ceo_name, address, inception_date
    """

    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(_("Company Name"), max_length=100)
    ceo_name = models.CharField(_("Ceo Name"), max_length=50)
    address = models.TextField()
    inception_date = models.DateField()

    class Meta:
        verbose_name_plural = "Companies"

        # company name might be repeating but not with same CEO name
        unique_together = ["name", "ceo_name"]

    def __str__(self) -> str:
        return f"{self.name} | CEO: {self.ceo_name}"


class Team(models.Model):
    """
    stores information of team inside a company
    columns: uid, company_id, team_lead_name
    """

    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)

    company_id = models.ForeignKey(
        to=Company, on_delete=models.CASCADE, related_name="teams"
    )

    team_lead_name = models.CharField(_("Team Lead Name"), max_length=100)

    def __str__(self) -> str:
        return f"Team lead by {self.team_lead_name} of {self.company_id}"
