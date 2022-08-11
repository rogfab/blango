from django.contrib import admin

from blog.models import Tag, Post, Comment


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)} #slugify title and record it


admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Post, PostAdmin)