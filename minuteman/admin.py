from django.contrib import admin
from minuteman.models import *

admin.site.register(Client)
admin.site.register(Contractor)
admin.site.register(Project)
admin.site.register(Log)