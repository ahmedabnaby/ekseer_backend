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

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")

        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")
        return self.create_user(email, password, **extra_fields)


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
    # iqama_number_regex = r'^[1-2][0-9]{9}$'
    # iqama_number_validator = RegexValidator(
    #     regex=iqama_number_regex,
    #     message='IQAMA number must start with 1 or 2 and be 10 digits long.'
    # )
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


    # password = models.CharField(
    #     max_length=128,
    #     help_text='The password should be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one number.',
    #     default='',
    #     blank=False,
    #     null=False,
    #     validators=[RegexValidator(
    #         regex='^.{8,128}$',
    #         message='The password must be at least 8 characters long and no more than 128 characters long.',
    #     )],
    # )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)

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
    
    def image_img(self):
        if self.copy_of_iqama_number:
            return u'<img src="%s" width="50" height="50" />'% self.copy_of_iqama_number.url
        else:
            return '(Sin Imagen)'
    image_img.short_description = "Thumb"
    image_img.allowed_tags = True

    def has_module_perms(self, app_label):
        return True

    def has_perm(self, perm, obj=None):
        return True
