from django.db import models
from common.models import CommonModel
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(CommonModel):

    """ Review from a User to a Room or Experience """

    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.room", null=True, blank=True, on_delete=models.CASCADE)
    experience = models.ForeignKey("experiences.experience", null=True, blank=True, on_delete=models.CASCADE)
    payload = models.TextField()
    rating = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"