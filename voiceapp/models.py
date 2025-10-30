# # models.py
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError("The Username field must be set")
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

# class VoiceUser(AbstractBaseUser):
#     username = models.CharField(max_length=150, unique=True)
#     password = models.CharField(max_length=128)
#     voice_note = models.FileField(upload_to='voice_notes/')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     objects = CustomUserManager()
    
#     USERNAME_FIELD = 'username'
    
#     def __str__(self):
#         return self.username