from django.contrib import admin

from .models import User, Mobile, MobileMessage, ServerMessage

admin.site.register(User)
admin.site.register(Mobile)
admin.site.register(MobileMessage)
admin.site.register(ServerMessage)
