from django.db import models

# Create your models here.
class GetTime(models.Model):
    current_time = models.TextField()
    # sheidzleba pirdapit datetimefieldis sheqmna da models.DateTimeField(auto_now_add=True)-s gamoyeneba, tumca droebi ar emtxveva.

    def __str__(self) -> str:
        return self.current_time