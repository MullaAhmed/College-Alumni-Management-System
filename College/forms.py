from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import PDEU


class PDEUCreationForm(UserCreationForm):

    class Meta:
        model = PDEU
        fields = ('email','number','college','branch','passing_year')


class PDEUChangeForm(UserChangeForm):

    class Meta:
        model = PDEU
        fields = ('email','number','college','branch','passing_year')
