from django import Forms

from .models import Student

class StudentFilterForm(forms.Form):
    choice = form.CharField()

