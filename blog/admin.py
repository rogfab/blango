from django.contrib import admin

from blog.models import Tag, Post


class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)} #slugify title and record it
  list_display = ("slug", "published_at")


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)