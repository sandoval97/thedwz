from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords


class User(AbstractUser):

    history = HistoricalRecords(
        excluded_fields=['username_validator'])
