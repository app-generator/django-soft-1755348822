# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Student(models.Model):

    #__Student_FIELDS__
    full name = models.TextField(max_length=255, null=True, blank=True)
    reg no = models.CharField(max_length=255, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    #__Student_FIELDS__END

    class Meta:
        verbose_name        = _("Student")
        verbose_name_plural = _("Student")


class Department(models.Model):

    #__Department_FIELDS__
    department = models.CharField(max_length=255, null=True, blank=True)
    date registered = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Department_FIELDS__END

    class Meta:
        verbose_name        = _("Department")
        verbose_name_plural = _("Department")



#__MODELS__END
