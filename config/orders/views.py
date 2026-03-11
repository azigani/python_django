from django.shortcuts import render, get_object_or_404, redirect
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

def order_create(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        status = request.POST.get('status')
        Order.objects.create(client_id=client_id, product_id=product_id, quantity=quantity, status=status)
        return redirect('order_list')
    return render(request, 'orders/order_form.html')

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.client_id = request.POST.get('client')
        order.product_id = request.POST.get('product')
        order.quantity = request.POST.get('quantity')
        order.status = request.POST.get('status')
        order.save()
        return redirect('order_detail', pk=order.pk)
    return render(request, 'orders/order_form.html', {'order': order})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})
