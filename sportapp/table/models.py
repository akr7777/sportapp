from django.db import models
from django.contrib.auth.models import User

class Methods(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    method_name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.method_name)

class Heart_rates(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    heart_interval = models.CharField(max_length=50)
    def __str__(self):
        return str(self.heart_interval)

class Results(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    heart_rate_id = models.ForeignKey(Heart_rates, on_delete=models.CASCADE)
    method_id = models.ForeignKey(Methods, on_delete=models.CASCADE)
    result = models.IntegerField()
    def __str__(self):
        return str(self.id)



