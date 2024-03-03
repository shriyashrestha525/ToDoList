from django.db import models
import uuid
from django.utils import timezone

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key = True, editable = False, default ='some_default_value')
    created_at = models.DateTimeField(auto_now = True)
    

    class Meta:
        abstract = True