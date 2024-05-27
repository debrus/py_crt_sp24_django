from django.contrib import admin
from blogging.models import Post, Category


class CategoryMembersInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryMembersInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ["posts"]
