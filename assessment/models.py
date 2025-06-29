from django.db import models

class Requirement(models.Model):
    CLASS_CHOICES = [
        ('annex_1', 'Annex 1'),
        ('annex_2', 'Annex 2'),
        ('vuln', 'Vulnerability'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirement_class = models.CharField(max_length=20, choices=CLASS_CHOICES)

    def __str__(self):
        return self.title

class Recommendation(models.Model):
    requirement = models.OneToOneField(Requirement, on_delete=models.CASCADE)
    advice = models.TextField()

    def __str__(self):
        return f"Recommendation for: {self.requirement.title}"

class Assessment(models.Model):
    requirement = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    compliant = models.BooleanField()
