from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CollectableForm
from .models import Collectable


def staff_check(user):
    if not user.is_staff:
        raise PermissionDenied
    return True


def collectable_list(request):
    items = Collectable.objects.order_by("order", "name")
    return render(
        request,
        "collectables/collectable_list.html",
        {"items": items},
    )


@user_passes_test(staff_check)
def collectable_create(request):
    if request.method == "POST":
        form = CollectableForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(
                request,
                (
                    f'Collectable "{item.name}" '
                    "created successfully."
                ),
            )
            return redirect("collectable_list")
    else:
        form = CollectableForm()

    return render(
        request,
        "collectables/collectable_form.html",
        {"form": form},
    )


@user_passes_test(staff_check)
def collectable_update(request, pk):
    item = get_object_or_404(Collectable, pk=pk)

    if request.method == "POST":
        form = CollectableForm(
            request.POST,
            request.FILES,
            instance=item,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                (
                    f'Collectable "{item.name}" '
                    "updated successfully."
                ),
            )
            return redirect("collectable_list")
    else:
        form = CollectableForm(instance=item)

    return render(
        request,
        "collectables/collectable_form.html",
        {
            "form": form,
            "item": item,
        },
    )


@user_passes_test(staff_check)
def collectable_delete(request, pk):
    item = get_object_or_404(Collectable, pk=pk)

    if request.method == "POST":
        item.delete()
        messages.success(
            request,
            (
                f'Collectable "{item.name}" '
                "deleted successfully."
            ),
        )
        return redirect("collectable_list")

    return render(
        request,
        "collectables/collectable_confirm_delete.html",
        {"item": item},
    )
