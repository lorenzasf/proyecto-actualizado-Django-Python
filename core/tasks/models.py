# from django.db import models
# from authentication.models import CustomUser

# # Create your models here.
# class Priority(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Task(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     title = models.CharField(max_length=150, null=False)
#     description = models.TextField(null=True, blank=True)
#     is_completed = models.BooleanField(default=False)
#     priority = models.ForeignKey(Priority, on_delete=models.PROTECT)

#     def __str__(self):
#         return f"{self.title} {self.user}"

from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Priority(models.Model):
    """
        Modelo para Catálogo de Prioridades.
        1: Baja
        2: Media
        3: Alta
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.title} {self.user}"