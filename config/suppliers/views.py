from django.shortcuts import render, get_object_or_404, redirect
from .models import Supplier

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'suppliers/supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'suppliers/supplier_detail.html', {'supplier': supplier})

def supplier_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Supplier.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_form.html')

def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.name = request.POST.get('name')
        supplier.email = request.POST.get('email')
        supplier.phone = request.POST.get('phone')
        supplier.address = request.POST.get('address')
        supplier.save()
        return redirect('supplier_detail', pk=supplier.pk)
    return render(request, 'suppliers/supplier_form.html', {'supplier': supplier})

def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'suppliers/supplier_confirm_delete.html', {'supplier': supplier})
