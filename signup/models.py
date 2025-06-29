from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class signup(models.Model):
    fname = models.CharField(max_length= 255)
    lname = models.CharField(max_length= 255)
    email = models.EmailField(max_length= 255)
    password = models.CharField(max_length= 255)
    confirmpassword = models.CharField(max_length= 255)

    def save(self, *args, **kwargs):
        # Hash password before saving only if it's not already hashed
        if not self.password.startswith('pbkdf2_'):  # Avoid re-hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
