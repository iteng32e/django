from django.contrib import admin
from . import models


@admin.register(models.Member)
class MemberAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Field)
class FieldAdmin(admin.ModelAdmin):
    pass


@admin.register(models.CoursesInProgress)
class CoursesInProgressAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Championship)
class ChampionshipAdmin(admin.ModelAdmin):
    pass


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
