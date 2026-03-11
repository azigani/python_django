from django.shortcuts import render, get_object_or_404, redirect
from .models import Delivery

def delivery_list(request):
    deliveries = Delivery.objects.all()
    return render(request, 'deliveries/delivery_list.html', {'deliveries': deliveries})

def delivery_detail(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    return render(request, 'deliveries/delivery_detail.html', {'delivery': delivery})

def delivery_create(request):
    if request.method == 'POST':
        order_id = request.POST.get('order')
        delivery_date = request.POST.get('delivery_date')
        status = request.POST.get('status')
        Delivery.objects.create(order_id=order_id, delivery_date=delivery_date, status=status)
        return redirect('delivery_list')
    return render(request, 'deliveries/delivery_form.html')

def delivery_update(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    if request.method == 'POST':
        delivery.order_id = request.POST.get('order')
        delivery.delivery_date = request.POST.get('delivery_date')
        delivery.status = request.POST.get('status')
        delivery.save()
        return redirect('delivery_detail', pk=delivery.pk)
    return render(request, 'deliveries/delivery_form.html', {'delivery': delivery})

def delivery_delete(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    if request.method == 'POST':
        delivery.delete()
        return redirect('delivery_list')
    return render(request, 'deliveries/delivery_confirm_delete.html', {'delivery': delivery})
