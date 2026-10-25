from django import forms
from .models import Visitor


class VisitorForm(forms.ModelForm):

    class Meta:
        model = Visitor

        fields = [
            "first_name",
            "last_name",
            "phone",
            "email",
            "visit_type",
            "discovery_source",
            "whatsapp_consent",
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "placeholder": "Votre prénom",
            }),
            "last_name": forms.TextInput(attrs={
                "placeholder": "Votre nom",
            }),
            "phone": forms.TextInput(attrs={
                "placeholder": "+32 470 12 34 56",
                "autocomplete": "tel",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Votre adresse e-mail (facultatif)",
                "autocomplete": "email",
            }),
            "visit_type": forms.RadioSelect(),
        }

    whatsapp_consent = forms.BooleanField(
    required=False,
    label=(
        "J'accepte d'être recontacté(e) par Crossfit Braine "
        "via WhatsApp après ma séance, notamment pour donner "
        "mon avis et recevoir des informations sur les abonnements. "
        "Je peux retirer mon consentement à tout moment."
    ),
    widget=forms.CheckboxInput()
)