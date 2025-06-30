from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class signup(models.Model):
    first_name = models.CharField(max_length= 255)
    last_name = models.CharField(max_length= 255)
    email = models.EmailField(max_length= 255)
    password = models.CharField(max_length= 255)
    confirm_password = models.CharField(max_length= 255)

    def save(self, *args, **kwargs):
        # Hash password before saving only if it's not already hashed
        if not self.password.startswith('pbkdf2_'):  # Avoid re-hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        # Hash password before saving only if it's not already hashed
        if not self.confirm_password.startswith('pbkdf2_'):  # Avoid re-hashing
            self.confirm_password = make_password(self.confirm_password)
        super().save(*args, **kwargs)
