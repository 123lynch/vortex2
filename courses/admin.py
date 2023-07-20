from django.contrib import admin
from courses.models import Category, CourseAuthor, Course ,CourseImage
from mptt.admin import MPTTModelAdmin

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(CourseAuthor)

class CourseImageInline(admin.TabularInline):
    model = CourseImage

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    inlines = [
        CourseImageInline,
    ]