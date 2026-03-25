from django.db import models
from cloudinary.models import CloudinaryField

class Resume(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)

    resume = CloudinaryField(
        resource_type='raw',
        folder='resumes',
        use_filename=True,
        unique_filename=True
    )

    filename = models.CharField(max_length=255, blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name