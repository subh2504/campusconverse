from django.contrib import admin

# Register your models here.
from campus.models import *


class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
    fields = ('campus_owner','campus_name','campus_address','campus_locality','campus_city','campus_country','campus_pincode','campus_logo','image_tag')
    readonly_fields = ('image_tag',)


admin.site.register(CampusDetail, ImageAdmin)
admin.site.register(CampusCourseDepart)
admin.site.register(MasterCourse)
admin.site.register(MasterDepart)
