from django.shortcuts import render, redirect
from .forms import VisitorForm

"""
Lorsque le visiteur ouvre la page, son navigateur envoie une requête GET.

Django affiche alors le formulaire vide.

Lorsqu'il clique sur « Valider mon inscription », le navigateur envoie une requête POST.
"""


def visitor_registration(request):

    if request.method == "POST":
        form = VisitorForm(request.POST)

        if form.is_valid(): # verifie les infos
            form.save()
            return redirect("registration_success")

    else:
        form = VisitorForm()

    return render(
        request,
        "visitors/registration.html",
        {"form": form}
    )


def registration_success(request):
    return render(
        request,
        "visitors/success.html"
    )