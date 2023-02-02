from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import AddProductsForm, UpdateProductForm, RegisterForm


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories,
    }
    return render(request, "inventory/inventory_list.html", context=context)


@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context = {
        'inventory': inventory,
    }

    return render(request, "inventory/per_product.html", context=context)


@login_required
def add_product(request):
    if request.method == "POST":
        add_form = AddProductsForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.input = float(add_form.data['price']) * float(add_form.data['quantity'])
            new_inventory.save()
            return redirect("/inventory/")
    else:
        add_form = AddProductsForm()

    return render(request, "inventory/inventory_add.html", {"form": add_form})


@login_required
def delete_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect("/inventory/")


@login_required
def update_product(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        updateForm = UpdateProductForm(data=request.POST)
        if updateForm.is_valid():
            inventory.itemClass = updateForm.data['itemClass']
            inventory.name = updateForm.data['name']
            inventory.model = updateForm.data['model']
            inventory.quantity = updateForm.data['quantity']
            inventory.cost_per_piece = float(updateForm.data['cost_per_piece'])
            inventory.price = float(updateForm.data['price']) * float(inventory.quantity)
            inventory.save()
            return redirect(f"/inventory/product/{pk}")
    else:
        updateForm = UpdateProductForm(instance=inventory)
    context = {
        "form": updateForm
    }
    return render(request, "inventory/update_product.html", context=context)
