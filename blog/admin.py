from django.contrib import admin
from models import Post, Picture
from sorl.thumbnail.admin import AdminImageMixin

class PictureInline(AdminImageMixin, admin.TabularInline):
    model = Picture 
    extra = 1

class PostAdmin(AdminImageMixin, admin.ModelAdmin):
    inlines = [PictureInline]
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
