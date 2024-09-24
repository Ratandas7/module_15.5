from django import forms
from musicians . models import Musician

class MusicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"