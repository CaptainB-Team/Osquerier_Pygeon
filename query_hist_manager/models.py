from django.db import models
from django.urls import reverse

# Django model for storing a single element from the query history
class QueryHistItem(models.Model):
    id = models.AutoField(primary_key=True)
    query_text = models.TextField()
    response_text = models.TextField()
    time_issued = models.DateTimeField(auto_now_add=True)
