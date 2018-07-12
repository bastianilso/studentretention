from django.db import models

# Create your models here.


bgcolor = {
    "problematic": "c9d7f0",
    "concerning": "e2eafa",
    "warning": "f5f8ff",
    "pass": "ffffff",
    "unknown": "fafafa",
}


class Student(models.Model):
    full_name = models.CharField(max_length=120)
    campus = models.CharField(max_length=30)
    cohort = models.DateTimeField('Starting year')
    current_semester = models.IntegerField('Current educational progress.')
    work_hours = models.IntegerField('Reported weekly effort')
    dropout_risk = models.DecimalField(decimal_places=2, max_digits=12)
    growth_mindset = models.DecimalField(decimal_places=2, max_digits=12)
    mathemathical_skill = models.DecimalField(decimal_places=2, max_digits=12)

    def __str__(self):
        return self.full_name

    def get_bgcolor(self):
        color = bgcolor['unknown']
        if self.dropout_risk > 0.75:
            color = bgcolor['problematic']
        elif self.dropout_risk > 0.6:
            color = bgcolor['concerning']
        elif self.dropout_risk > 0.4:
            color = bgcolor['warning']
        elif self.dropout_risk > 0.0:
            color = bgcolor['pass']
        return '#' + color
