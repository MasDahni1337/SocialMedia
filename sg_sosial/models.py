from SimpleGuna.settings import MEDIA_DIR
from django.db import models
from django.db.models.fields import NullBooleanField
from django.http import request
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
import os
from django import forms

class UserAkun(models.Model):
    nm_depan = models.TextField(max_length=150)
    nm_belakang = models.TextField(max_length=150)
    username = models.TextField(max_length=150)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password

    def get_nm_depan(self):
        return self.nm_depan
    
    def get_nm_belakang(self):
        return self.nm_belakang
    
    def get_session(self):
        self.ambilsesi = request.session[self.username]
        return self.ambilsesi


def fldr_usr_pp(instance, filename):
    flder_usr ='{}/{}'.format(MEDIA_DIR, instance.user)
    if not os.path.exists(flder_usr):
        os.mkdir(flder_usr)
    elif not os.path.exists(flder_usr+'/poto_profile/'):
        os.mkdir(flder_usr+'/poto_profile/')
    fldernya = '{0}/poto_profile/{1}'.format(instance.user, filename)
    return fldernya

class IniUsrProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_depan = models.CharField(max_length=200, blank=True, null=True)
    nama_belakang = models.CharField(max_length=200, blank=True, null=True)
    foto_profile = models.ImageField(upload_to=fldr_usr_pp, blank=True, null = True)

    def __str__(self):
        return self.user.username

def fldr_usr_foto(instance, filename):
    flder_usr = '{}/{}'.format(MEDIA_DIR, instance.user)
    if not os.path.exists(flder_usr):
        os.mkdir(flder_usr)
    elif not os.path.exists(flder_usr+'/sts_foto/'):
        os.mkdir(flder_usr+'/sts_foto/')
    fldernya = '{0}/sts_foto/{1}'.format(instance.user, filename)
    return fldernya

def fldr_usr_video(instance, filename):
    flder_usr = '{}/{}'.format(MEDIA_DIR, instance.user)
    if not os.path.exists(flder_usr):
        os.mkdir(flder_usr)
    elif not os.path.exists(flder_usr+'/sts_video/'):
        os.mkdir(flder_usr+'/sts_video/')
    fldernya = '{0}/sts_video/{1}'.format(instance.user, filename)
    return fldernya

class StatusGuna(models.Model):
    user = models.ForeignKey(User, related_name="StatusGuna", on_delete=models.CASCADE)
    st = models.ForeignKey(IniUsrProfile, related_name="StatusGuna", on_delete=models.CASCADE)
    foto_profile = models.ImageField(upload_to=fldr_usr_pp, blank=True, null = True)
    status = models.CharField(max_length=300, blank=True, null=True)
    status_foto = models.ImageField(upload_to=fldr_usr_foto, blank=True, null=True)
    status_video = models.FileField(upload_to=fldr_usr_video, blank=True, null=True)
    status_tanggal = models.DateField(default=timezone.now)
    status_suka = models.PositiveIntegerField(null=True)
    status_komen = models.ManyToManyField(IniUsrProfile, related_name="status_komen", blank=True)
    status_bagi = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.user.username

    def hitungsuka(self):
        return self.status_suka.count()

class KomenGuna(models.Model):
    stData = models.ForeignKey(StatusGuna, on_delete=models.CASCADE, related_name="KomenGuna")
    st_profile = models.ForeignKey(IniUsrProfile, related_name='KomenGuna', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='KomenGuna', on_delete=models.CASCADE)
    isiKomen = models.CharField(max_length=300, null=True, blank=True)
    tanggal_komen = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.username