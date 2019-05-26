from django.contrib import admin
from core.models import *

# Register your models here.
admin.site.register(Namespace)
admin.site.register(Project)
admin.site.register(ProjectDoc)
admin.site.register(SystemUser)
admin.site.register(Task)
admin.site.register(ProjectStage)
