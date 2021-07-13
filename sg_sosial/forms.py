from datetime import datetime
from django import forms
from django.db.models import fields
from .models import IniUsrProfile, KomenGuna, StatusGuna
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'password', 'email')

class IniProfileForm(forms.ModelForm):
    class Meta():
        model = IniUsrProfile
        fields = ('nama_depan', 'nama_belakang', 'foto_profile')

class StsUsr(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username',)

class StsForm(forms.ModelForm):
    class Meta():
        model = StatusGuna
        fields = (
            'status',
            'status_foto',
            'status_video',
        )

class KomenForm(forms.ModelForm):
    isiKomen = forms.CharField(required=True)
    class Meta():
        model = KomenGuna
        fields = (
            'isiKomen',
            'stData',
        )