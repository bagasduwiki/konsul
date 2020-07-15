from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from aitc_service.views import *
from aitc_service.forms import *
from .models import *
from .forms import AdminForm, ClientForm, UpdateUserForm, CreateUserForm

@login_required(login_url='login')
def accounts(request):
    admin = request.user.admin
    form = AdminForm(instance=admin)

    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES, instance=admin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')

    context = {'form':form}
    return render(request, 'akun.html', context)

@login_required(login_url='login')
def ubahpassword(request):
    user = request.user
    form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            user.set_password(password_1)
            user.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('accounts')

    context = {'form':form}
    return render(request, 'ubahpassword.html', context)

@login_required(login_url='login')
def ubahpassuser(request):
    user = request.user
    form = UpdateUserForm(instance=user)
    if request.method == 'POST':
        password_1 = request.POST['password1']
        password_2 = request.POST['password2']
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            user.set_password(password_1)
            user.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('detailclient')

    context = {'form':form}
    return render(request, 'ubahpassuser.html', context)

@login_required(login_url='login')
def daftarclient(request):
    client = Client.objects.all()

    context = {'client':client}
    return render(request, 'daftarclient.html', context)

@login_required(login_url='login')
def tambahuser(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('tambahclient')

    context = {'form':form}
    return render(request, 'tambah_user.html', context)

@login_required(login_url='login')
def tambahclient(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('daftarclient')

    context = {'form':form}
    return render(request, 'tambah_client.html', context)

@login_required(login_url='login')
def detailclient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm(instance=client)

    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('daftarclient')

    context = {'client':client, 'form':form}
    return render(request, 'detailclient.html', context)

@login_required(login_url='login')
def deleteClient(request, pk):
    client = Client.objects.get(id=pk)
    form = ClientForm()

    if request.method == 'POST':
        client.delete()
        messages.success(request, 'Data Berhasil Dihapus')
        return redirect('daftarclient')
