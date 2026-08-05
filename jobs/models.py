from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models


class JobApplication(models.Model):
    class Status(models.TextChoices):
        APPLIED = "Applied", "Applied"
        INTERVIEW = "Interview", "Interview"
        OFFER = "Offer", "Offer"
        ACCEPTED = "Accepted", "Accepted"
        REJECTED = "Rejected", "Rejected"

    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    job_location = models.CharField(max_length=150)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0, message="Salary cannot be negative.")],
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.APPLIED
    )
    application_date = models.DateField()
    deadline = models.DateField()
    notes = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.position} at {self.company_name}"

    def clean(self):
        super().clean()
        if self.deadline and self.application_date:
            if self.deadline < self.application_date:
                raise ValidationError(
                    {"deadline": "Deadline cannot be earlier than the application date."}
                )
        if self.salary is not None and self.salary < 0:
            raise ValidationError({"salary": "Salary cannot be negative."})
