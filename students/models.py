from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    program = models.CharField(max_length=120, blank=True)
    university = models.CharField(max_length=120, blank=True)
    bio = models.TextField(blank=True)
    profile_url = models.URLField(blank=True, help_text="Optional: LinkedIn/Personal site")
    photo_url = models.URLField(blank=True, help_text="Temporary: external image URL")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
