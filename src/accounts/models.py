from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Model representing a custom user with additional security features."""

    # Champs pour la question secrète unique et la réponse associée
    secret_question = models.CharField("Question secrète", max_length=255, blank=False, null=False)
    secret_answer = models.CharField("Réponse secrète", max_length=255, blank=False, null=False)

    def __str__(self):
        """String representation of the custom user."""
        return self.username