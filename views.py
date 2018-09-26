from django.shortcuts import render

from .models import Student, Predictor
from django.db.models import Max
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def update_comment(request):
    comment = request.GET.get('comment', None)
    studienr = int(request.GET.get('studienr', None))
    student = Student.objects.filter(studienr=studienr)
    #print(student.count())
    student.update(comment=comment)
    date = datetime.today().strftime('%Y-%m-%d')
    student.update(commentdate=date)
    data = {
        'success': 'it worked'
    }
    #print(comment)
    #print(date)
    #print(studienr)
    return JsonResponse(data)

@login_required
def update_checkbox(request):
    state = int(request.GET.get('statfrom django.utils import formatse', None) == 'true')
    studienr = int(request.GET.get('studienr', None))
    student = Student.objects.filter(studienr=studienr)
    #print(student.count())
    student.update(checked=state)
    # Queryset where
    # Student.objects.
    data = {
        'success': 'it worked'
    }
    return JsonResponse(data)

@login_required
def index(request):

    study = Student.objects.last().ramme_retning
    cohort = Student.objects.last().startaar
    semester = Student.objects.last().modelsemester

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

    cur_predictor_list = (
        Predictor.objects
        .filter(semester=semester)
        .filter(cohortyear=cohort)
        # TODO: Sort so lowest PredNumber comes first.
        #.filter(educationID=study)
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

    pred_count = (
        cur_predictor_list
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

#    predictor_list = ()

#    if (semester is '0'):
#        predictor_list = (
#            Predictor.objects
#            .filter(nameshort__in=['hsMAT'])
#        )
#    elif (semester is '1'):
#        predictor_list = (
#            Predictor.objects
#            .filter(nameshort__in=['1_T_atnBy', '1_T_mGPA', '1_Pr_mGPA'])
#        )
#    elif (semester is '2'):
#        predictor_list = (
#            Predictor.objects
#            .filter(nameshort__in=['2_T_atnBy', '2_Pr_mGPA'])
#        )

#    last_update = (
#        cur_predictor_list
#        .aggregate(last_update=Max('daterun'))['last_update']
#    )

    context = {
        'student_list': cur_student_list,
        'predictor_list': cur_predictor_list,
        'student_count': student_count,
        'students_at_risk': risk_count,
        'dropout_count': dropout_count,
        'cohort_list': cohort_list,
        'semester_list': semester_list,
        'cur_sem': semester,
        'cur_cohort': cohort,
        'cur_study': study,
        'pred_count': pred_count,
        'last_update': '1111-11-11'#last_update

    }
    return render(request, 'studentrisk/index.html', context)
