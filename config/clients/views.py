from django.shortcuts import render, get_object_or_404, redirect
from .models import Client

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})

def client_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        Client.objects.create(name=name, email=email, phone=phone, address=address)
        return redirect('client_list')
    return render(request, 'clients/client_form.html')

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.name = request.POST.get('name')
        client.email = request.POST.get('email')
        client.phone = request.POST.get('phone')
        client.address = request.POST.get('address')
        client.save()
        return redirect('client_detail', pk=client.pk)
    return render(request, 'clients/client_form.html', {'client': client})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/client_confirm_delete.html', {'client': client})
