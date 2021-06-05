from django.contrib import admin
from blog.models import Post
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Post, BlogAdmin)
