from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
     date_hierarchy = 'created_at'
     empty_date_hierarchy = 'empty'
     list_display = ('title', 'content_view', 'status', 'published_at', 'created_at', 'updated_at')
     list_filter  = ('status' ,)
     search_fields = ('title', 'content')
     class Meta:
          ordering = ['-created_at']
admin.site.register(Post, PostAdmin)
