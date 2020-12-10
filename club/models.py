from django.db import models
from django.http import HttpResponseRedirect
from django.urls import reverse
import uuid

from django.utils import timezone


class Member(models.Model):
    first_name = models.CharField(max_length=100, unique=True, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=10, null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    join_date = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    ROLE = (
        ('A', 'Administrator'),
        ('C', 'Client'),
    )
    role = models.CharField(default='C', choices=ROLE, max_length=1, null=True, blank=True)
    LEVEL = (
        ('b', 'Beginner'),
        ('m', 'Middle'),
        ('p', 'professional'),
    )
    level = models.CharField(default='b', choices=LEVEL, max_length=1, null=True, blank=True)

    class Meta:
        ordering = ["join_date"]

    """After add member show name of the member instance show ( Member Object 1) """

    def __str__(self):
        return self.first_name


class Field(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(help_text="Please Enter Field Description Text Here.",
                                   default="It's a test text For Field Description.")

    class Meta:
        ordering = ["name"]

    """After add field show name of the field instance show ( Field Object 1) """

    def __str__(self):
        return self.name


class CoursesInProgress(models.Model):
    name = models.ForeignKey(Field, on_delete=models.CASCADE)
    CLASS_DAY = (
        ('EV', 'Every Days'),
        ('E', 'Even Days'),
        ('O', 'Odd Days'),
    )
    class_day = models.CharField(max_length=2, choices=CLASS_DAY, null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    class Meta:
        ordering = ["class_day"]

    """After add Progressing Course show name of the Course instance show ( CoursesInProgress Object 1) """

    def __str__(self):
        return self.class_day


class Championship(models.Model):
    """Name Of Winner"""
    hero = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now(), null=True, blank=True)

    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True)
    """Position: 1 | 2 | 3 ?"""
    POSITION = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
    )
    position = models.CharField(choices=POSITION, max_length=100, null=True, blank=True)
    """tournament: Provincial, National, Continental and Global"""
    TOURNAMENT = (
        ('P', 'Provincial'),
        ('N', 'National'),
        ('C', 'Continental'),
        ('G', 'Global')
    )
    tournament = models.CharField(choices=TOURNAMENT, max_length=300, null=True, blank=True)

    class Meta:
        ordering = ["position"]

    def __str__(self):
        return self.position


class AboutUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(help_text="Please Enter 'About Us' Text Here.",
                                   default="It's a test text for About Us.", null=True, blank=True)
    img_url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    text = models.TextField(max_length=1500, help_text="Enter Here Question", null=True, blank=True)
    date = models.DateTimeField(timezone.now(), null=True, blank=True)
