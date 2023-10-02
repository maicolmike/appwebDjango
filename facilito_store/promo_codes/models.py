from django.db import models

# Create your models here.
class PromoCode(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.FloatField(default=0.0)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #objects = PromoCodeManager()

    def __str__(self):
        return self.code

    def use(self):
        #self.used = True
        self.save()