from django.shortcuts import render, get_object_or_404, redirect
from .models import Tax

def tax_list(request):
    taxes = Tax.objects.all()
    return render(request, 'taxes/tax_list.html', {'taxes': taxes})

def tax_detail(request, pk):
    tax = get_object_or_404(Tax, pk=pk)
    return render(request, 'taxes/tax_detail.html', {'tax': tax})

def tax_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rate = request.POST.get('rate')
        product_id = request.POST.get('product')
        Tax.objects.create(name=name, rate=rate, product_id=product_id)
        return redirect('tax_list')
    return render(request, 'taxes/tax_form.html')

def tax_update(request, pk):
    tax = get_object_or_404(Tax, pk=pk)
    if request.method == 'POST':
        tax.name = request.POST.get('name')
        tax.rate = request.POST.get('rate')
        tax.product_id = request.POST.get('product')
        tax.save()
        return redirect('tax_detail', pk=tax.pk)
    return render(request, 'taxes/tax_form.html', {'tax': tax})

def tax_delete(request, pk):
    tax = get_object_or_404(Tax, pk=pk)
    if request.method == 'POST':
        tax.delete()
        return redirect('tax_list')
    return render(request, 'taxes/tax_confirm_delete.html', {'tax': tax})
