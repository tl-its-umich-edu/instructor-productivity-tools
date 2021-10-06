# Register your models here.

from django.contrib import admin
from backend.canvas_app_explorer.models import LtiTool, CanvasPlacement, QuillPost

class LtiToolAdmin(admin.ModelAdmin):
    pass
admin.site.register(LtiTool, LtiToolAdmin)

class CanvasPlacementAdmin(admin.ModelAdmin):
    pass
admin.site.register(CanvasPlacement, CanvasPlacementAdmin) 

class QuillPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(QuillPost)