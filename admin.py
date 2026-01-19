from django.contrib import admin
from .models import *


class Requirentments_TabularInline(admin.TabularInline):
    model = Requirentments

class Video_TabularInline(admin.TabularInline):
    model = Video
class what_you_learn_TabularInline(admin.TabularInline):
    model = what_you_learn

class course_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline,Requirentments_TabularInline,Video_TabularInline)


admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(Course,course_admin)
admin.site.register(Level)
admin.site.register(Requirentments)
admin.site.register(what_you_learn)
admin.site.register(Video)
admin.site.register(Lesson)
# Register your models here.
