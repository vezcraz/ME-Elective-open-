from django.contrib import admin
from .models import Student_Info
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.



class Student_InfoAdmin(UserAdmin, ImportExportModelAdmin):
	list_display = ('Identity','name','p')
	search_fields = ('Identity','name',)
	readonly_fields=()
	ordering=()
	filter_horizontal = ()
	list_filter=()
	fieldsets = ()

	
admin.site.register(Student_Info, Student_InfoAdmin)
	

