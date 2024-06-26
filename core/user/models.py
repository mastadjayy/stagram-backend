from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from core.abstract.models import AbstractManager, AbstractModel


class UserManager(BaseUserManager, AbstractManager):
        
    def create_user(self, username, email, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if password is None:
            raise TypeError('User must have a password.')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, username, email, password, **kwargs):
        """Create and return a `User` with superuser (admin)permissions."""
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have a username.')

        user = self.create_user(username, email, password, **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    bio = models.CharField(max_length=150, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/user_avatar', blank=True, null=True)

    posts_liked = models.ManyToManyField("core_post.Post", related_name="liked_by")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def like(self, post):
        """Like `post` if it hasn't been done yet"""
        return self.posts_liked.add(post)
    
    def remove_like(self, post):
        """Remove a like from a `post`"""
        return self.posts_liked.remove(post)
    
    def has_liked(self, post):
        """Return True if the user has liked a `post`; else
        False"""
        return self.posts_liked.filter(pk=post.pk).exists()

