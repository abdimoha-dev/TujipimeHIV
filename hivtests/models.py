from django.db import models

class Tests(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    gender =models.CharField(max_length=30)
    dob = models.DateField('date of birth')
    date_tested = models.DateField('date tested')
    test_result = models.CharField(max_length=30)
    picked_test = models.CharField(max_length=3, default=False)
