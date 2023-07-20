from django.shortcuts import get_object_or_404, render
from courses.models import Category, Course
from django.views.generic import TemplateView


def course(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    courses = Product.objects.filter(category=category)
    return render(request, 'courses/category.html', {'category': category, 'courses': courses})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_active=True)
    return render(request, 'courses/single.html', {'course': course})

def course_display(request):
    display = Course.objects.all()
    return render(request, 'courses/courses.html', {'display':display})
