from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import Comment

# MPTTModelAdmin ap fè kòmantè yo parèt ak yon ti espas (indentation)
# pou w wè klè kilès ki repons kilès
admin.site.register(Comment, MPTTModelAdmin)