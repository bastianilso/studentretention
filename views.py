from django.shortcuts import render

from .models import Student, Predictor
from django.db.models import Max
import datetime
# Create your views here.

def index(request):

    study = 'Medialogi'
    cohort = '2017'
    semester = '2'

    if request.method == 'POST':
        dataset = request.POST.get("dataset","")
        study, cohort, semester = dataset.split(',')

#   find out which semester is the current semester.
    max_sem = (
        Student.objects
        .aggregate(max_sem=Max('modelsemester'))['max_sem']
    )

#   filter the students so only students from the current semester are retreived
    cur_student_list = (
        Student.objects
        .filter(modelsemester=semester)
        .filter(startaar=cohort)
        .filter(ramme_retning=study)
    )

#   count how many students are in risk between 0.75 - 1.00
    risk_count = (
        cur_student_list
        .exclude(risk__isnull=True)
        .filter(risk__range=(0.90, 1.0))
        .count()
    )
    dropout_count = (
        cur_student_list
        .exclude(udmeld_aarsag__exact='')
        .exclude(udmeld_aarsag__isnull=True)
        .count()
    )
    student_count = (
        cur_student_list
        .count()
    )

    cohort_list = (
            Student.objects
            .values('startaar')
            .distinct()
        )
    semester_list = (
            Student.objects
            .values('modelsemester')
            .distinct()
        )

    predictor_list = ()

    if (semester is '0'):
        predictor_list = (
            Predictor.objects
            .filter(nameshort__in=['hsMAT'])
        )
    elif (semester is '1'):
        predictor_list = (
            Predictor.objects
            .filter(nameshort__in=['1_T_atnBy', '1_T_mGPA', '1_Pr_mGPA'])
        )
    elif (semester is '2'):
        predictor_list = (
            Predictor.objects
            .filter(nameshort__in=['2_T_atnBy', '2_Pr_mGPA'])
        )

    last_update = (
        predictor_list
        .aggregate(last_update=Max('daterun'))['last_update']
    )

    context = {
        'student_list': cur_student_list,
        'predictor_list': predictor_list,
        'student_count': student_count,
        'students_at_risk': risk_count,
        'dropout_count': dropout_count,
        'cohort_list': cohort_list,
        'semester_list': semester_list,
        'cur_sem': semester,
        'cur_cohort': cohort,
        'cur_study': study,
        'last_update': last_update

    }
    return render(request, 'studentrisk/index.html', context)