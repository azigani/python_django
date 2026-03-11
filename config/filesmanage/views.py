
from django.shortcuts import render, get_object_or_404, redirect
from .models import ManagedFile

def file_list(request):
	files = ManagedFile.objects.all()
	return render(request, 'filesmanage/file_list.html', {'files': files})

def file_detail(request, pk):
	file = get_object_or_404(ManagedFile, pk=pk)
	return render(request, 'filesmanage/file_detail.html', {'file': file})

def file_create(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		uploaded_file = request.FILES.get('file')
		ManagedFile.objects.create(name=name, file=uploaded_file)
		return redirect('file_list')
	return render(request, 'filesmanage/file_form.html')

def file_update(request, pk):
	file = get_object_or_404(ManagedFile, pk=pk)
	if request.method == 'POST':
		file.name = request.POST.get('name')
		uploaded_file = request.FILES.get('file')
		if uploaded_file:
			file.file = uploaded_file
		file.save()
		return redirect('file_detail', pk=file.pk)
	return render(request, 'filesmanage/file_form.html', {'file': file})

def file_delete(request, pk):
	file = get_object_or_404(ManagedFile, pk=pk)
	if request.method == 'POST':
		file.delete()
		return redirect('file_list')
	return render(request, 'filesmanage/file_confirm_delete.html', {'file': file})
