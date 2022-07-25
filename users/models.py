from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, is_superuser=True, is_staff=True, **kwargs)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"

    @property
    def has_module_perms(self):
        return lambda x: True

    @property
    def has_perm(self):
        return lambda x: True

    def __str__(self):
        return f"<User {self.id} {self.email}>"
