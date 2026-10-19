from django.contrib import admin
from .models import Visitor


@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):

    list_display = ( #Définit les colonnes affichées dans la liste des visiteurs.
        "first_name",
        "last_name",
        "phone",
        "visit_type",
        "discovery_source",
        "status",
        "created_at",
    )

    list_filter = ( # Permet de filtrer les visiteurs, par exemple pour afficher uniquement les personnes venues pour un essai.
        "visit_type",
        "status",
        "discovery_source",
        "created_at",
    )

    search_fields = ( # Ajoute une barre de recherche permettant de retrouver une personne par son nom, son téléphone ou son e-mail.
        "first_name",
        "last_name",
        "phone",
        "email",
    )

    readonly_fields = ( # Empêche de modifier manuellement la date d'inscription.
        "created_at",
    )