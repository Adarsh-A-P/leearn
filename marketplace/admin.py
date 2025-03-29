from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'college', 'course', 'department', 'year_of_study', 'academic_period', 'has_cv')
    search_fields = ('user__username', 'college', 'course', 'department')
    list_filter = ('course', 'department', 'year_of_study')

    def has_cv(self, obj):
        return bool(obj.cv)
    has_cv.boolean = True
    has_cv.short_description = 'CV Uploaded'
