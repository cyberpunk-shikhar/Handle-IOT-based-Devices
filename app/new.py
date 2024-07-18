from django import forms
from .models import ArduinoData

class ArduinoDataForm(forms.ModelForm):
    class Meta:
        model = ArduinoData
        fields = "__all__"
        
