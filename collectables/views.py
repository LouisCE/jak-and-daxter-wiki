from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Collectable
from .forms import CollectableForm
from django.core.exceptions import PermissionDenied


def staff_check(user):
    if not user.is_staff:
        raise PermissionDenied
    return True


def collectable_list(request):
    items = Collectable.objects.order_by('order', 'name')
    return render(request, 'collectables/collectable_list.html', {'items': items})


@user_passes_test(staff_check)
def collectable_create(request):
    if request.method == 'POST':
        form = CollectableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('collectable_list')
    else:
        form = CollectableForm()
    return render(request, 'collectables/collectable_form.html', {'form': form})


@user_passes_test(staff_check)
def collectable_update(request, pk):
    item = get_object_or_404(Collectable, pk=pk)
    if request.method == 'POST':
        form = CollectableForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('collectable_list')
    else:
        form = CollectableForm(instance=item)
    return render(request, 'collectables/collectable_form.html', {'form': form, 'item': item})


@user_passes_test(staff_check)
def collectable_delete(request, pk):
    item = get_object_or_404(Collectable, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('collectable_list')
    return render(request, 'collectables/collectable_confirm_delete.html', {'item': item})
