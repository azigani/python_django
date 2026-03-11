
from django.shortcuts import render, get_object_or_404, redirect
from .models import UserProfile

def user_list(request):
	users = UserProfile.objects.all()
	return render(request, 'users/user_list.html', {'users': users})

def user_detail(request, pk):
	user = get_object_or_404(UserProfile, pk=pk)
	return render(request, 'users/user_detail.html', {'user': user})

def user_create(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		UserProfile.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
		return redirect('user_list')
	return render(request, 'users/user_form.html')

def user_update(request, pk):
	user = get_object_or_404(UserProfile, pk=pk)
	if request.method == 'POST':
		user.username = request.POST.get('username')
		user.email = request.POST.get('email')
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.save()
		return redirect('user_detail', pk=user.pk)
	return render(request, 'users/user_form.html', {'user': user})

def user_delete(request, pk):
	user = get_object_or_404(UserProfile, pk=pk)
	if request.method == 'POST':
		user.delete()
		return redirect('user_list')
	return render(request, 'users/user_confirm_delete.html', {'user': user})
