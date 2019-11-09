from django.db import models
from core import models as core_models

class List(core_models.TimeStampedModel):

    """ List Model Definition """

    name = models.CharField(max_length=80)
    rooms = models.ManyToManyField("rooms.Room", blank=True)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name