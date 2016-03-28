from django.contrib import admin

from .models import *

admin.site.register(TextBlock)
admin.site.register(Config)
admin.site.register(Version)
admin.site.register(Document)
admin.site.register(Instrument)
admin.site.register(Reports)
admin.site.register(QualityAssurance)
admin.site.register(RegistrationDocumentChanges)
admin.site.register(Requirement)
admin.site.register(Test)
admin.site.register(Validation)

