from django.contrib import admin
from blog.models import Tag,Category,WriterProfile,BlogPost,BlogComment,About,Roles

admin.site.register(Tag)
admin.site.register(WriterProfile)
admin.site.register(BlogComment)
admin.site.register(About)
admin.site.register(Roles)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title','author','date_posted','slug']
    prepopulated_fields = {'slug':('title',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'author', 'slug', 'price',
#                     'in_stock', 'created', 'updated']
#     list_filter = ['in_stock', 'is_active']
#     list_editable = ['price', 'in_stock']
#     prepopulated_fields = {'slug': ('title',)}
