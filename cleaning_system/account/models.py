from django.db import models
from  django.contrib.auth.models  import AbstractBaseUser, BaseUserManager
import uuid
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 1)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)






class  User(AbstractBaseUser):
    class Role(models.IntegerChoices):
        SIMPLE_USER=1
        COMPANY_OWNER=2
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(verbose_name='email',max_length=255,unique=True)
    username=models.CharField(max_length=50,unique=True)
    role=models.IntegerField(choices=Role.choices, default=Role.SIMPLE_USER)
    uuid=models.UUIDField(default = uuid.uuid4,  editable=False,  blank=True)
    is_superuser = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True)

    objects=CustomUserManager()
    
   
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name', 'username','uuid']
    def  __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def is_staff(self):
        return self.is_superuser



