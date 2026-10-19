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