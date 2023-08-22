from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator, EmailValidator, FileExtensionValidator



class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The email is not given.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractBaseUser):
    full_name = models.CharField(max_length=255, null=False, blank=False,
            help_text='Full name should contain only letters.',
        validators=[
        RegexValidator(
            regex='^[A-Za-z ]+$',
            message='Full name should contain only letters.',
            code='invalid_full_name'
        )
    ])

    iqama_number = models.CharField(
        max_length=10,
        unique=True,
        help_text='IQAMA number must start with 1 or 2 and be 10 digits long.',
        validators=[RegexValidator(
        regex=r'^[1-2][0-9]{9}$',
        message='IQAMA number must start with 1 or 2 and be 10 digits long.'
    )]
    )
    copy_of_iqama_number = models.ImageField(
        upload_to='copy_of_iqama_number',
        max_length=512,
        null=False,
        blank=False,
        # validators=[FileExtensionValidator(allowed_extensions=["pdf",'png','jpg','jpeg'])]    
    )
    mobile_number = models.CharField(
        max_length=9,
        unique=True,
        help_text='The mobile number should start with 5 and be 9 digits long.',
        default='',
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex='^5\d{8}$',
                message='The mobile number should start with 5 and be 9 digits long.',
            ),
        ],
    )
    email = models.EmailField(
        unique=True,
        help_text='The email address should be unique and valid.',
        default='',
        blank=False,
        null=False,
        validators=[
            EmailValidator
        ],
    )
    date_of_birth = models.DateField(
        blank=False,
        null=False,
    )
    nationality = models.CharField(
        max_length=255,
        help_text='The nationality should be a valid country code.',
        default='',
        blank=False,
        null=False,
    )
    password = models.CharField(max_length=128, null=True)

    scfhs_registration = models.CharField(max_length=255, null=True, blank=True)
    copy_of_scfhs_registration_card = models.ImageField(
        upload_to='copy_of_scfhs_registration_card',
        max_length=512,
        null=True,
        blank=True,
    )
    cv = models.FileField(
        upload_to='doctors_cv',
        max_length=512,
        null=True,
        blank=True,
    )
    personal_photo = models.ImageField(
        upload_to='doctors_personal_photo',
        max_length=512,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_doctor = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_actived = models.BooleanField(default=False)

    USERNAME_FIELD = 'iqama_number'
    REQUIRED_FIELDS = [
    'full_name',
    'copy_of_iqama_number', 
    'mobile_number', 
    'email', 
    'date_of_birth', 
    'nationality',
    'password']

    objects = UserManager()

    def __str__(self):
        return self.iqama_number
    
    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True

class Call(models.Model):
    id = models.AutoField(primary_key=True)
    meeting_id = models.CharField(max_length=255,null=True,blank=True)
    patient_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    doctor_id = models.IntegerField(null=True,blank=True)
    is_new = models.BooleanField(default=True)

