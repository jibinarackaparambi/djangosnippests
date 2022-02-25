from django.contrib import admin

from myapp.models import Snippests, Tag

admin.site.register(Tag)
admin.site.register(Snippests)
