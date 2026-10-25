from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .forms import VisitorStatusForm

from visitors.models import Visitor


def is_staff(user):
    return user.is_active and user.is_staff


@login_required
@user_passes_test(is_staff, login_url="/dashboard/connexion/")
def dashboard_home(request):

    visitors = Visitor.objects.all()

    context = {
        "total_visitors": visitors.count(),

        "total_trials": visitors.filter(
            visit_type=Visitor.VisitType.TRIAL
        ).count(),

        "total_dropins": visitors.filter(
            visit_type=Visitor.VisitType.DROP_IN
        ).count(),

        "total_converted": visitors.filter(
            status=Visitor.Status.CONVERTED
        ).count(),

        "recent_visitors": visitors.order_by("-created_at")[:10],
    }

    return render(
        request,
        "dashboard/home.html",
        context
    )


@login_required
@user_passes_test(is_staff, login_url="/dashboard/connexion/")
def visitor_list(request):

    visitors = Visitor.objects.all()

    # Recherche
    search_query = request.GET.get("q", "").strip()

    if search_query:
        visitors = visitors.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(phone__icontains=search_query) |
            Q(email__icontains=search_query)
        )

    # Filtre par type de visite
    visit_type = request.GET.get("type", "")

    if visit_type in Visitor.VisitType.values:
        visitors = visitors.filter(visit_type=visit_type)

    # Filtre par statut
    status = request.GET.get("status", "")

    if status in Visitor.Status.values:
        visitors = visitors.filter(status=status)

    # Pagination : 20 visiteurs par page
    paginator = Paginator(visitors, 20)
    page_obj = paginator.get_page(request.GET.get("page"))

    context = {
        "page_obj": page_obj,
        "search_query": search_query,
        "selected_type": visit_type,
        "selected_status": status,
        "visit_types": Visitor.VisitType.choices,
        "statuses": Visitor.Status.choices,
    }

    return render(
        request,
        "dashboard/visitor_list.html",
        context
    )

@login_required
@user_passes_test(is_staff, login_url="/dashboard/connexion/")
def visitor_detail(request, visitor_id):

    visitor = get_object_or_404(
        Visitor,
        id=visitor_id
    )

    if request.method == "POST":

        form = VisitorStatusForm(
            request.POST,
            instance=visitor
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Le statut du visiteur a été mis à jour."
            )

            return redirect(
                "visitor_detail",
                visitor_id=visitor.id
            )

    else:
        form = VisitorStatusForm(instance=visitor)

    context = {
        "visitor": visitor,
        "form": form,
    }

    return render(
        request,
        "dashboard/visitor_detail.html",
        context
    )