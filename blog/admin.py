from django.contrib import admin
from .models import Post 
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','body','author')
    list_filter=('title','author')
    search_fields=('title',)


