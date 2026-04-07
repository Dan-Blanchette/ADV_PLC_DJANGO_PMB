from django.db import models
from django.urls import reverse

# Create your models here.
class PLC_Tags(models.Model):
    # If you use choices for a field, Django automatically generates a method
    # called get_method_name_display() which we use in the index to get all entries from the database
    reg_type = models.IntegerField(choices=[(0, "coil"), (1, "holding_register")])
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now=True)
    # helper function to get data by register type and timestamp
    def get_absolute_url(self):
        if self.reg_type == 0:
            return reverse("database_manager:coil_detail", args=[self.pk])
        elif self.reg_type == 1:
            return reverse("database_manager:holding_register_detail", args=[self.pk])
        