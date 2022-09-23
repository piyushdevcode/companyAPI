from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _

# if any modification are required for User Model in future
class CustomUser(AbstractUser):
    pass


class Company(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(_("Company Name"), max_length=100)
    # / can use our custom model as FOREIGN KEY here
    ceo_name = models.CharField(_("Ceo Name"), max_length=50)
    address = models.TextField()
    inception_date = models.DateField()

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self) -> str:
        return f"{self.name} | {self.ceo_name}"


# / if Team also has some date field then we can create a base model containing uid and date
class Team(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    company_id = models.ForeignKey(
        to=Company, on_delete=models.CASCADE, related_name="teams"
    )
    team_lead = models.CharField(_("Team Lead Name"), max_length=100)

    def __str__(self) -> str:
        return f"lead by {self.team_lead} of {self.company_id}"
