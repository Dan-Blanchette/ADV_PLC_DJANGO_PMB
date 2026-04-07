from django.db import models

# Create your models here.
class PLC_Tags(models.Model):
    reg_type = models.IntegerField(choices=[(0, "coil"), (1, "holding_register")])
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)