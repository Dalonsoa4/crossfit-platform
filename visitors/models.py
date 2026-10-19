from django.db import models

# un modèle est une classe Python qui décrit une table de base de données

class Visitor(models.Model):

    class VisitType(models.TextChoices):
        TRIAL = "trial", "Essai"
        DROP_IN = "drop_in", "Drop-in"

    class DiscoverySource(models.TextChoices):
        INSTAGRAM = "instagram", "Instagram"
        GOOGLE = "google", "Google"
        FRIEND = "friend", "Bouche-à-oreille"
        PASSING = "passing", "En passant devant la box"
        OTHER = "other", "Autre"

    class Status(models.TextChoices):
        NEW = "new", "Nouveau"
        CONTACTED = "contacted", "Contacté"
        CONVERTED = "converted", "Converti en membre"

    first_name = models.CharField(
        max_length=100,
        verbose_name="Prénom"
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name="Nom de famille"
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="Téléphone"
    )

    email = models.EmailField(
        blank=True,
        verbose_name="Adresse e-mail"
    )

    visit_type = models.CharField(
        max_length=10,
        choices=VisitType.choices,
        verbose_name="Type de visite"
    )

    discovery_source = models.CharField(
        max_length=20,
        choices=DiscoverySource.choices,
        verbose_name="Comment avez-vous connu la box ?"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
        verbose_name="Statut"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date d'inscription"
    )

    class Meta:
        verbose_name = "Visiteur"
        verbose_name_plural = "Visiteurs"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"