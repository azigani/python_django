
from django.shortcuts import render, get_object_or_404, redirect
from .models import AuditLog

def audit_list(request):
	logs = AuditLog.objects.all()
	return render(request, 'audit/audit_list.html', {'logs': logs})

def audit_detail(request, pk):
	log = get_object_or_404(AuditLog, pk=pk)
	return render(request, 'audit/audit_detail.html', {'log': log})

def audit_create(request):
	if request.method == 'POST':
		action = request.POST.get('action')
		user = request.POST.get('user')
		details = request.POST.get('details')
		AuditLog.objects.create(action=action, user=user, details=details)
		return redirect('audit_list')
	return render(request, 'audit/audit_form.html')

def audit_update(request, pk):
	log = get_object_or_404(AuditLog, pk=pk)
	if request.method == 'POST':
		log.action = request.POST.get('action')
		log.user = request.POST.get('user')
		log.details = request.POST.get('details')
		log.save()
		return redirect('audit_detail', pk=log.pk)
	return render(request, 'audit/audit_form.html', {'log': log})

def audit_delete(request, pk):
	log = get_object_or_404(AuditLog, pk=pk)
	if request.method == 'POST':
		log.delete()
		return redirect('audit_list')
	return render(request, 'audit/audit_confirm_delete.html', {'log': log})
