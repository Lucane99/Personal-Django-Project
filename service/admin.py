from django.contrib import admin
from service.models import Topics
class TopicAdmin(admin.ModelAdmin):
    list_display=('topic_icon','topic_title','topic_description')

admin.site.register(Topics,TopicAdmin)
# Register your models here.
