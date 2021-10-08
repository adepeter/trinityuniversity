from django import forms

from ..models import VisitorSchedule


class VisitorScheduleForm(forms.ModelForm):
    class Meta:
        model = VisitorSchedule
        fields = '__all__'
