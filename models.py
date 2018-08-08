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
    studienr = models.BigIntegerField(blank=True, primary_key=True)
    startaar = models.BigIntegerField(blank=True, null=True)
    courselocation = models.BigIntegerField(db_column='CourseLocation', blank=True, null=True)
    modelsemester = models.BigIntegerField(db_column='modelSemester', blank=True, null=True)
    modeltraincohort = models.FloatField(db_column='modelTrainCohort', blank=True, null=True)
    risk = models.FloatField(blank=True, null=True)
    matgrade = models.BigIntegerField(db_column='MATGrade', blank=True, null=True)
    x1_t_atnby = models.BigIntegerField(db_column='X1_T_atnBy', blank=True, null=True)
    x1_nt_mgpa = models.FloatField(db_column='X1_NT_mGPA', blank=True, null=True)
    x1_pr_mgpa = models.FloatField(db_column='X1_Pr_mGPA', blank=True, null=True)
    x2_t_atnby = models.BigIntegerField(db_column='X2_T_atnBy', blank=True, null=True)
    x2_pr_mgpa = models.FloatField(db_column='X2_Pr_mGPA', blank=True, null=True)
    email = models.CharField(max_length=23, blank=True, null=True)
    fullname = models.CharField(db_column='fullName', max_length=70, blank=True, null=True)
    campusname = models.CharField(db_column='campusName', max_length=45, blank=True, null=True)
    ramme_retning = models.TextField(blank=True, null=True)
    fra_dato = models.TextField(db_column='fra_dato', blank=True, null=True)
    til_dato = models.TextField(db_column='til_dato', blank=True, null=True)
    adgangsgrundlag = models.TextField(blank=True, null=True)
    udmeld_aarsag = models.TextField(blank=True, null=True)
    udmeld_begrundelse = models.TextField(blank=True, null=True)

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
        return '#' + color

    class Meta:
        managed = False
        db_table = 'studentrisk_student'


class Predictor(models.Model):
    pred_id = models.IntegerField(db_column='Pred ID', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    name = models.CharField(db_column='Name', max_length=31, blank=True, null=True)  # Field name made lowercase.
    nameshort = models.CharField(db_column='nameShort', max_length=10, blank=True, null=True)  # Field name made lowercase.
    explanation = models.CharField(max_length=200, blank=True, null=True)
    predictorytypeid = models.IntegerField(db_column='predictoryTypeID')  # Field name made lowercase.
    modelid = models.IntegerField(db_column='modelID', blank=True, null=True)  # Field name made lowercase.
    coef = models.FloatField(blank=True, null=True)
    exp_coef_field = models.FloatField(db_column='exp.coef.', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    pvalue = models.FloatField(blank=True, null=True)
    pred_id_0 = models.BigIntegerField(db_column='Pred.ID', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because of name conflict.
    xpred2 = models.IntegerField(db_column='Xpred2', blank=True, null=True)  # Field name made lowercase.
    xpred3 = models.IntegerField(db_column='Xpred3', blank=True, null=True)  # Field name made lowercase.
    modelpredictorid = models.IntegerField(db_column='modelPredictorID', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(max_length=200, blank=True, null=True)
    daterun = models.DateTimeField(db_column='dateRun', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'studentrisk_predictors'
