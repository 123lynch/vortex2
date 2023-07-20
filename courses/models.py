from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from cloudinary.models import CloudinaryField
from account.models import UserBase


class Category(models.Model):
    name = models.CharField(verbose_name=_("Category Name"), max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name =_("Category")
        verbose_name_plural =_("Categories")

    def get_absolute_url(self):
        return reverse("courses:category_list", args=[self.slug])

    def __str__(self):
        return self.name

class CourseAuthor(models.Model):
    user = models.OneToOneField(UserBase, related_name='teacher', on_delete=models.RESTRICT)
    image = CloudinaryField('image', null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=2000)
    slug = models.SlugField(unique=True, max_length=100, null=True)

    def __str__(self):
        return str(self.user)

class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(CourseAuthor, on_delete=models.CASCADE)
    description = models.TextField(verbose_name=_("description"), blank=False)
    slug = models.SlugField(max_length=255, unique=True)
    regular_price = models.DecimalField(verbose_name=_("Regular Price"), max_digits=5, decimal_places=2)
    discount_price = models.DecimalField(verbose_name=_("Discount Price"), max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def get_absolute_url(self):
        return reverse("courses:course_detail", args=[self.slug])

    def __str__(self):
        return self.title

class CourseImage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="course_image")
    image = CloudinaryField('image', null=True, blank=True)
    alt_text = models.CharField(max_length=255, null=True, blank=True)
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name =_("Course Image")
        verbose_name_plural = ("Course Images")