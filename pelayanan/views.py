from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from aitc_service.views import *
from aitc_service.forms import *
from .forms import PelayananForm, StatusForm, DeletePelayananForm
from .models import *
from .filters import PelayananFilter

# Create your views here.
@login_required(login_url='login')
def pelayanan(request):
    pengaduan = Pengaduan.objects.all()
    client = Client.objects.all()

    # pengaduans = pengaduan.order_set.all()

    myFilter = PelayananFilter(request.GET, queryset=pengaduan)

    context = {'pengaduan':pengaduan, 'client':client, 'myFilter':myFilter}
    return render(request, 'pelayanan.html', context)

@login_required(login_url='login')
def tambahpelayanan(request):
    form = PelayananForm()
    if request.method == 'POST':
        form = PelayananForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Ditambahkan')
            return redirect('pelayanan')

    context = {'form':form}
    return render(request, 'tambah_pelayanan.html', context)

@login_required(login_url='login')
def editstatus(request, pk):
    pengaduan = Pengaduan.objects.get(id=pk)
    form = StatusForm(instance=pengaduan)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=pengaduan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data Berhasil Diubah')
            return redirect('pelayanan')

    context = {'form':form, 'pengaduan':pengaduan}
    return render(request, 'edit_status.html', context)

@login_required(login_url='login')
def detailpelayanan(request, pk):
    pengaduan = Pengaduan.objects.get(id=pk)
    respon = Respon.objects.get(id=pk)
    form = PelayananForm(instance=pengaduan)

    context = {'pengaduan':pengaduan, 'form':form, 'respon':respon}
    return render(request, 'detail_pelayanan.html', context)

@login_required(login_url='login')
def detaildaftar(request, pk):
    # pengaduan = Pengaduan.objects.get(id=pk)
    respon = Respon.objects.get(id=pk)
    form = PelayananForm(instance=respon)

    context = {'form':form, 'respon':respon}
    return render(request, 'detail_daftar.html', context)

@login_required(login_url='login')
def deletepelayanan(request, pk):
    pengaduan = Pengaduan.objects.get(id=pk)
    form = DeletePelayananForm()

    if request.method == 'POST':
        pengaduan.delete()
        messages.success(request, 'Data Berhasil Dihapus')
        return redirect('pelayanan')
