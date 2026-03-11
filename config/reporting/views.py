
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Report

def report_list(request):
	reports = Report.objects.all()
	return render(request, 'reporting/report_list.html', {'reports': reports})

def report_detail(request, pk):
	report = get_object_or_404(Report, pk=pk)
	return render(request, 'reporting/report_detail.html', {'report': report})

def report_create(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		description = request.POST.get('description')
		Report.objects.create(title=title, description=description)
		return redirect('report_list')
	return render(request, 'reporting/report_form.html')

def report_update(request, pk):
	report = get_object_or_404(Report, pk=pk)
	if request.method == 'POST':
		report.title = request.POST.get('title')
		report.description = request.POST.get('description')
		report.save()
		return redirect('report_detail', pk=report.pk)
	return render(request, 'reporting/report_form.html', {'report': report})

def report_delete(request, pk):
	report = get_object_or_404(Report, pk=pk)
	if request.method == 'POST':
		report.delete()
		return redirect('report_list')
	return render(request, 'reporting/report_confirm_delete.html', {'report': report})
