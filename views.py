from django.template import loader
from django.shortcuts import render

from .models import Student
# Create your views here.


def index(request):
    student_list = Student.objects.order_by('-dropout_risk')
    context = {
        'student_list': student_list,
    }
    return render(request, 'studentrisk/index.html', context)
