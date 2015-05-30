# -*- coding: utf-8 -*-
from django.forms import ModelForm

from models import BplanEinwendung


class BplanEinwendungForm(ModelForm):
    class Meta:
        model = BplanEinwendung
        fields = '__all__'
