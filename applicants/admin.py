from django.contrib import admin
from .models import Applicant, Reference, Attachment
from cms.admin.placeholderadmin import PlaceholderAdminMixin
# Register your models here.

class ApplicantsAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
 
admin.site.register(Applicant, ApplicantsAdmin)

class ReferencesAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
 
admin.site.register(Reference, ReferencesAdmin)

class AttachmentAdmin(PlaceholderAdminMixin, admin.ModelAdmin):
    pass
 
admin.site.register(Attachment, AttachmentAdmin)