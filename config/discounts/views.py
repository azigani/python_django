from django.shortcuts import render, get_object_or_404, redirect
from .models import Discount

def discount_list(request):
    discounts = Discount.objects.all()
    return render(request, 'discounts/discount_list.html', {'discounts': discounts})

def discount_detail(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    return render(request, 'discounts/discount_detail.html', {'discount': discount})

def discount_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        value = request.POST.get('value')
        is_percentage = request.POST.get('is_percentage') == 'on'
        product_id = request.POST.get('product')
        Discount.objects.create(name=name, value=value, is_percentage=is_percentage, product_id=product_id)
        return redirect('discount_list')
    return render(request, 'discounts/discount_form.html')

def discount_update(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == 'POST':
        discount.name = request.POST.get('name')
        discount.value = request.POST.get('value')
        discount.is_percentage = request.POST.get('is_percentage') == 'on'
        discount.product_id = request.POST.get('product')
        discount.save()
        return redirect('discount_detail', pk=discount.pk)
    return render(request, 'discounts/discount_form.html', {'discount': discount})

def discount_delete(request, pk):
    discount = get_object_or_404(Discount, pk=pk)
    if request.method == 'POST':
        discount.delete()
        return redirect('discount_list')
    return render(request, 'discounts/discount_confirm_delete.html', {'discount': discount})
