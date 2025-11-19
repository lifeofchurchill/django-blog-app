from django.contrib import admin
from .models import Category, Post, Tag, Comment, Profile, Bookmark, Like

# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Bookmark)
admin.site.register(Like)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'status', 'author')
    search_fields = ['content', 'content']
    list_filter = ('category', 'status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags',)

admin.site.register(Post, PostAdmin)
