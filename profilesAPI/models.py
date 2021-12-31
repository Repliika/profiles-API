from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):  # class to manipulate the data
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a user profile"""
        if not email:
            raise ValueError('Must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=60, unique=True)
    name = models.CharField(max_length=60)
    date_joined = models.DateTimeField(
        verbose_name="date joined", auto_now_true=True)  # always be the fist time
    last_login = models.DateTimeField(
        verbose_name="last login", auto_now=True)  # always be the latest time
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_name(self):
        """Retrieve name for user"""
        return self.name

    def get_last_login(self):
        """Retrieve last login time for user"""
        return self.last_login

    def __str__(self):
        """Return string representation of user"""
        return self.email
