from django.db import models
from accounts.models import CollegeUser


class Fee(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    due_date = models.DateField()

    def __str__(self) -> str:
        return self.name


class Payment(models.Model):
    user = models.ForeignKey(
        CollegeUser, on_delete=models.CASCADE, related_name="payments")
    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False)
    payment_date = models.DateField(auto_now=True)

    def name(self):
        return f"{self.user.student_profile}"

    def __str__(self) -> str:
        return f"{self.user.student_profile.name} - {self.fee}"
