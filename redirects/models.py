from django.db import models

class Redirect(models.Model):
    AVAILABILITY_CHOICES = [
        ('web_only', 'Web Only'),
        ('phone_only', 'Phone Only'),
        ('both', 'Both'),
    ]

    image_phone = models.ImageField(upload_to='images/phone/')
    image_web = models.ImageField(upload_to='images/web/')
    redirect_url_phone = models.URLField()
    redirect_url_web = models.URLField()
    title_phone = models.CharField(max_length=255)
    title_web = models.CharField(max_length=255)
    position = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f"{self.title_web} / {self.title_phone}"
