from django.shortcuts import render, get_object_or_404, redirect
from .models import Invoice

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'invoices/invoice_list.html', {'invoices': invoices})

def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'invoices/invoice_detail.html', {'invoice': invoice})

def invoice_create(request):
    if request.method == 'POST':
        client_id = request.POST.get('client')
        sale_id = request.POST.get('sale')
        amount = request.POST.get('amount')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        Invoice.objects.create(client_id=client_id, sale_id=sale_id, amount=amount, due_date=due_date, status=status)
        return redirect('invoice_list')
    return render(request, 'invoices/invoice_form.html')

def invoice_update(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.client_id = request.POST.get('client')
        invoice.sale_id = request.POST.get('sale')
        invoice.amount = request.POST.get('amount')
        invoice.due_date = request.POST.get('due_date')
        invoice.status = request.POST.get('status')
        invoice.save()
        return redirect('invoice_detail', pk=invoice.pk)
    return render(request, 'invoices/invoice_form.html', {'invoice': invoice})

def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'invoices/invoice_confirm_delete.html', {'invoice': invoice})
