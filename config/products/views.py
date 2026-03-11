
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def product_list(request):
	products = Product.objects.all()
	return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		price = request.POST.get('price')
		stock = request.POST.get('stock')
		description = request.POST.get('description')
		Product.objects.create(name=name, price=price, stock=stock, description=description)
		return redirect('product_list')
	return render(request, 'products/product_form.html')

def product_update(request, pk):
	product = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		product.name = request.POST.get('name')
		product.price = request.POST.get('price')
		product.stock = request.POST.get('stock')
		product.description = request.POST.get('description')
		product.save()
		return redirect('product_detail', pk=product.pk)
	return render(request, 'products/product_form.html', {'product': product})

def product_delete(request, pk):
	product = get_object_or_404(Product, pk=pk)
	if request.method == 'POST':
		product.delete()
		return redirect('product_list')
	return render(request, 'products/product_confirm_delete.html', {'product': product})
