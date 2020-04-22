from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

@admin.register(cdc)
@admin.register(stuCourseData)
@admin.register(courseOffered)
@admin.register(courseList)
@admin.register(regSem)

class cdcAdmin(ImportExportModelAdmin):
	pass
class stuCourseDataAdmin(ImportExportModelAdmin):
	pass
class courseListAdmin(ImportExportModelAdmin):
	pass
class courseOfferedAdmin(ImportExportModelAdmin):
	pass
