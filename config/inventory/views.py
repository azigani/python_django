
from django.shortcuts import render, get_object_or_404, redirect
from .models import InventoryItem

def inventory_list(request):
	items = InventoryItem.objects.all()
	return render(request, 'inventory/inventory_list.html', {'items': items})

def inventory_detail(request, pk):
	item = get_object_or_404(InventoryItem, pk=pk)
	return render(request, 'inventory/inventory_detail.html', {'item': item})

def inventory_create(request):
	if request.method == 'POST':
		product_id = request.POST.get('product')
		quantity = request.POST.get('quantity')
		location = request.POST.get('location')
		InventoryItem.objects.create(product_id=product_id, quantity=quantity, location=location)
		return redirect('inventory_list')
	return render(request, 'inventory/inventory_form.html')

def inventory_update(request, pk):
	item = get_object_or_404(InventoryItem, pk=pk)
	if request.method == 'POST':
		item.product_id = request.POST.get('product')
		item.quantity = request.POST.get('quantity')
		item.location = request.POST.get('location')
		item.save()
		return redirect('inventory_detail', pk=item.pk)
	return render(request, 'inventory/inventory_form.html', {'item': item})

def inventory_delete(request, pk):
	item = get_object_or_404(InventoryItem, pk=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('inventory_list')
	return render(request, 'inventory/inventory_confirm_delete.html', {'item': item})
