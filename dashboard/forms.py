from django import forms
from visitors.models import Visitor


class VisitorStatusForm(forms.ModelForm):

    class Meta:
        model = Visitor

        fields = ["status"]

        widgets = {
            "status": forms.Select(attrs={
                "class": "status-select"
            })
        }