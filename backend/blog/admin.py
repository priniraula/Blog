from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost

class BlogPostAdmin(SummernoteModelAdmin):
    list_per_page = 20;
    list_display = ('id', 'title', 'date_created')
    list_display_links = ('id', 'title')
    exclude = ('slug', )

    summernote_fields = ('content', )

admin.site.register(BlogPost, BlogPostAdmin)