from django.db import models

# Create your models here.


bgcolor = {
    "problematic": "c9d7f0",
    "concerning": "e2eafa",
    "warning": "f5f8ff",
    "pass": "ffffff",
    "unknown": "ffffff",
    "dropout": "edeeef"
}


class Student(models.Model):
    studienr = models.IntegerField(blank=True, primary_key=True)
    startaar = models.IntegerField(blank=True, null=True)
    courselocation = models.IntegerField(db_column='CourseLocation', blank=True, null=True)  # Field name made lowercase.
    modelsemester = models.IntegerField(db_column='modelSemester', blank=True, null=True)  # Field name made lowercase.
    modeltraincohort = models.IntegerField(db_column='modelTrainCohort', blank=True, null=True)  # Field name made lowercase.
    risk = models.FloatField(blank=True, null=True)
    p1 = models.IntegerField(blank=True, null=True)
    p2 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p3 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p4 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p5 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p6 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p7 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p8 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p9 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p10 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p11 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p12 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p13 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p14 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p15 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p16 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p17 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p18 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p19 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    p20 = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    email = models.CharField(max_length=23, blank=True, null=True)
    fullname = models.CharField(db_column='fullName', max_length=38, blank=True, null=True)  # Field name made lowercase.
    campusname = models.CharField(db_column='campusName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ramme_retning = models.TextField(blank=True, null=True)
    fra_dato = models.TextField(blank=True, null=True)
    til_dato = models.TextField(blank=True, null=True)
    adgangsgrundlag = models.TextField(blank=True, null=True)
    udmeld_aarsag = models.TextField(blank=True, null=True)
    udmeld_begrundelse = models.TextField(blank=True, null=True)
    comment = models.TextField(blank=True, null=False)
    commentdate = models.DateField(db_column='commentDate', blank=True, null=False)  # Field name made lowercase.
    checked = models.IntegerField(blank=True, null=False)
    educationid = models.IntegerField(db_column='educationID', blank=True, null=True)  # Field name made lowercase.

    def get_bgcolor(self):
        color = bgcolor['unknown']
        if self.risk is not None:
            if self.risk > 0.90:
                color = bgcolor['problematic']
            elif self.risk > 0.75:
                color = bgcolor['concerning']
            elif self.risk > 0.5:
                color = bgcolor['warning']
            elif self.risk > 0.0:
                color = bgcolor['pass']
        if self.udmeld_aarsag is not None and self.udmeld_aarsag is not '':
            color = bgcolor['dropout']
        print(str(self.risk) + ' and' + color + ': ' + self.fullname)
        return '#' + color

    class Meta:
        managed = False
        db_table = 'studentrisk_student5'


class Predictor(models.Model):
    modelpredictorid = models.IntegerField(db_column='modelPredictorID', primary_key=True)  # Field name made lowercase.
    nameshort = models.TextField(db_column='predictorShortName', blank=True, null=True)  # Field name made lowercase.
    predictorexplanations = models.TextField(db_column='PredictorExplanations', blank=True, null=True)  # Field name made lowercase.
    modelpredictorsid = models.IntegerField(db_column='modelPredictorsID')  # Field name made lowercase.
    modelid = models.IntegerField(db_column='modelID')  # Field name made lowercase.
    coef = models.FloatField(blank=True, null=True)
    exp_coef_field = models.FloatField(db_column='exp.coef.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pvalue = models.FloatField(blank=True, null=True)
    errortoohighinteractionpredictor = models.IntegerField(db_column='ErrorTooHighInteractionPredictor', blank=True, null=True)  # Field name made lowercase.
    prednumber = models.BigIntegerField(db_column='predNumber')  # Field name made lowercase.
    semester = models.IntegerField(blank=True, null=True)
    cohortyear = models.IntegerField(db_column='cohortYear', blank=True, null=True)  # Field name made lowercase.
    campusid = models.IntegerField(db_column='campusID', blank=True, null=True)  # Field name made lowercase.
    educationid = models.IntegerField(db_column='educationID', blank=True, null=True)  # Field name made lowercase.

    #pred = models.IntegerField(db_column='Pred ID', null=True)
    #name = models.CharField(db_column='Name', max_length=31, blank=True, null=True)
    #nameshort = models.CharField(db_column='nameShort', max_length=10, blank=True, null=True)
    #explanation = models.CharField(max_length=200, blank=True, null=True)
    #predictorytypeid = models.IntegerField(db_column='predictoryTypeID', null=True)
    #modelid = models.IntegerField(db_column='modelID', blank=True, null=True)
    #coef = models.FloatField(blank=True, null=True)
    #exp_coef_field = models.FloatField(db_column='exp.coef.', blank=True, null=True)
    #pvalue = models.FloatField(blank=True, null=True)
    #modelpredictorid = models.IntegerField(db_column='modelPredictorID', blank=True, null=True)
    #source = models.CharField(max_length=200, blank=True, null=True)
    #daterun = models.DateTimeField(db_column='dateRun', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modelPredictors'
