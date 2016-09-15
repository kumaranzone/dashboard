from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Tag, Entry

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Tag)
admin.site.register(Entry)