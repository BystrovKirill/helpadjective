from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(Invalid)
admin.site.register(Volunteer)
admin.site.register(HelpRequest)