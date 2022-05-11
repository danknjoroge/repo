from django.contrib import admin
from .models import Session, Student, Tm, User
# Register your models here.
from .models import Shedule
class SheduleAdmin(admin.ModelAdmin):
    list = ('day', 'details', 'time')

admin.site.register(Shedule)

admin.site.register(User)
admin.site.register(Tm)
admin.site.register(Student)
admin.site.register(Session)