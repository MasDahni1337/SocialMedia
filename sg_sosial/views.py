from os import stat
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, request
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .models import IniUsrProfile, KomenGuna, StatusGuna
from .forms import  KomenForm, StsForm, StsUsr, UserForm, IniProfileForm
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        ambil_dt = IniUsrProfile.objects.filter(user=request.user.id).first()
        data = {
            'bio' : ambil_dt
        }
        return render(request, 'home.html', data)
    return render(request, 'home.html')


@login_required
def su(request):
    return render(request, 'home.html')

@login_required
def keluar(request):
    logout(request)
    return render(request, 'login.html')


def daftar(request):
    if request.user.is_authenticated:
        return redirect('/')
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = IniProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            print(profile.user)
            if 'foto_profile' in request.FILES:
                print(request.FILES['foto_profile'])
                profile.foto_profile = request.FILES['foto_profile']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = IniProfileForm()
    return render(request, 'daftar.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

def masuk(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    if request.method == 'POST':
        cek_user= request.POST.get('username')
        cek_pass = request.POST.get('password')
        user = authenticate(username=cek_user, password=cek_pass)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('/home/')
            else:
                print("akun anda tidak aktif")
        else:
            print("ada yang mencoba login")
            print("dengan username : {} dan password : {}".format(cek_user, cek_pass))
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def home(request):
    if request.user.is_authenticated:
        ambil_dt = IniUsrProfile.objects.filter(user=request.user.id).first()
        ambil_stts = StatusGuna.objects.all().select_related('user', 'st')
        ambil_komen = KomenGuna.objects.all().select_related('user', 'stData')
        hitung_komen = KomenGuna.objects.all().select_related('stData').count()
        data = {
            'bio' : ambil_dt,
            'st_dt' : ambil_stts,
            'komen' : ambil_komen,
            'hitung' : hitung_komen,
        }
        print(ambil_dt.foto_profile)
        print(ambil_stts)
        print("ini komen")
        print(ambil_komen)
       
        print(data)
        if request.method == "POST":
            user_status =  ambil_dt.user
            user_st = ambil_dt
            dt_usr_status = StsForm(data=request.POST)
            dt_km = KomenForm(data=request.POST)
            if 'sv_status' in request.POST:
                user = user_status
                st = user_st
                data_status = dt_usr_status.save(commit=False)
                data_status.user = user
                data_status.st = st
                if 'status_foto' in request.FILES:
                    print(request.FILES['status_foto'])
                    data_status.status_foto = request.FILES['status_foto']
                    print(data_status.status_foto)
                elif 'status_video' in request.FILES:
                    print(request.FILES['status_vieeo'])
                    data_status.status_video = request.FILES['status_video']
                    print(data_status.status_video)
                data_status.save()
            else:
                print(dt_usr_status.errors)
            
            if 'isiKomen' in request.POST:
                print("ini request komen")
                print(request.POST['isiKomen'])
                user = user_st
                user_p = ambil_dt.user
                data_komen = dt_km.save(commit=False)
                data_komen.st_profile = user
                data_komen.user = user_p
                print(data_komen)
                data_komen.save()
            else:
                print(dt_km.errors)

        else:
            user_status = StsUsr()
            dt_usr_status = StsForm()
            dt_km = KomenForm()
        return render(request, 'home.html', data)
    else:
        return redirect('/')