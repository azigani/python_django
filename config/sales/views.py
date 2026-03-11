
from django.shortcuts import render, get_object_or_404, redirect
from .models import Sale

def sale_list(request):
	sales = Sale.objects.all()
	return render(request, 'sales/sale_list.html', {'sales': sales})

def sale_detail(request, pk):
	sale = get_object_or_404(Sale, pk=pk)
	return render(request, 'sales/sale_detail.html', {'sale': sale})

def sale_create(request):
	if request.method == 'POST':
		product_id = request.POST.get('product')
		quantity = request.POST.get('quantity')
		total_price = request.POST.get('total_price')
		Sale.objects.create(product_id=product_id, quantity=quantity, total_price=total_price)
		return redirect('sale_list')
	return render(request, 'sales/sale_form.html')

def sale_update(request, pk):
	sale = get_object_or_404(Sale, pk=pk)
	if request.method == 'POST':
		sale.product_id = request.POST.get('product')
		sale.quantity = request.POST.get('quantity')
		sale.total_price = request.POST.get('total_price')
		sale.save()
		return redirect('sale_detail', pk=sale.pk)
	return render(request, 'sales/sale_form.html', {'sale': sale})

def sale_delete(request, pk):
	sale = get_object_or_404(Sale, pk=pk)
	if request.method == 'POST':
		sale.delete()
		return redirect('sale_list')
	return render(request, 'sales/sale_confirm_delete.html', {'sale': sale})
