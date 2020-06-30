from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages

from .forms import CreateUserForm, AdminForm, PenangananForm, MasalahForm
from .models import *
from .filters import PengaduanFilter
from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='client')
            user.group.add(group)

            messages.success(request, 'Akun berhasil dibuat ' +  username)
            return redirect('login')

    context = {'form':form}
    return render(request, 'web/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username atau Password Salah')

    context = {}
    return render(request, 'web/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@admin_only
def home(request):
    penanganan = Penanganan.objects.all()
    client = Client.objects.all()

    tot_client = client.count()
    tot_penanganan = penanganan.count()
    tot_selesai = penanganan.filter(status='Selesai').count()
    tot_proses = penanganan.filter(status='Online').count()

    myFilter = PengaduanFilter()

    context = {'penanganan':penanganan, 'client':client, 'tot_client':tot_client, 'tot_penanganan':tot_penanganan,
    'tot_selesai':tot_selesai, 'tot_proses':tot_proses, 'myFilter': myFilter}
    return render(request, 'web/dashboard.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def det_penanganan(request, pk):
    penanganan = Penanganan.objects.get(id=pk)
    form = PenangananForm(instance=penanganan)
    if request.method == 'POST':
        form = PenangananForm(request.POST, instance=penanganan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Dikirim')
            return redirect('/')

    context = {'form':form, 'penanganan':penanganan}
    return render(request, 'web/penanganan.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def edit_status(request, pk):
    penanganan = Penanganan.objects.get(id=pk)
    form = PenangananForm(instance=penanganan)
    if request.method == 'POST':
        form = PenangananForm(request.POST, instance=penanganan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('/')

    context = {'form':form}
    return render(request, 'web/edit_status.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def pengsel(request):
    penanganan = Penanganan.objects.all()
    penanganan1 = penanganan.filter(status='Selesai')
    client = Client.objects.all()
    context = {'penanganan1':penanganan1, 'client':client}
    return render(request, 'web/pengsel.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def akun(request):
    admin = request.user.admin
    form = AdminForm(instance=admin)

    if request.method == 'POST':
        form = AdminForm(request.POST, request.FILES, instance=admin)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'web/akun.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['client'])
def user_page(request):
    context = {}
    return render(request, 'web/user_page.html', context)

def deletePeng(request, pk):
    penanganan = Penanganan.objects.get(id=pk)
    form = PenangananForm()

    if request.method == 'POST':
        penanganan.delete()
        return redirect('pengsel')
