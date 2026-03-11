
from django.shortcuts import render, get_object_or_404, redirect
from .models import Payment

def payment_list(request):
	payments = Payment.objects.all()
	return render(request, 'payments/payment_list.html', {'payments': payments})

def payment_detail(request, pk):
	payment = get_object_or_404(Payment, pk=pk)
	return render(request, 'payments/payment_detail.html', {'payment': payment})

def payment_create(request):
	if request.method == 'POST':
		user_id = request.POST.get('user')
		amount = request.POST.get('amount')
		method = request.POST.get('method')
		Payment.objects.create(user_id=user_id, amount=amount, method=method)
		return redirect('payment_list')
	return render(request, 'payments/payment_form.html')

def payment_update(request, pk):
	payment = get_object_or_404(Payment, pk=pk)
	if request.method == 'POST':
		payment.user_id = request.POST.get('user')
		payment.amount = request.POST.get('amount')
		payment.method = request.POST.get('method')
		payment.save()
		return redirect('payment_detail', pk=payment.pk)
	return render(request, 'payments/payment_form.html', {'payment': payment})

def payment_delete(request, pk):
	payment = get_object_or_404(Payment, pk=pk)
	if request.method == 'POST':
		payment.delete()
		return redirect('payment_list')
	return render(request, 'payments/payment_confirm_delete.html', {'payment': payment})
