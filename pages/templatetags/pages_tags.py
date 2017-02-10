from django.shortcuts import render, get_object_or_404, render_to_response
from django import template
from pages.models import Slider, Page
from products.models import Category, Product
register = template.Library()


#add tag for home slider
@register.inclusion_tag('slider.html')
def show_slides(slides):
    slides = Slider.objects.all()
    return { 'slides' : slides }

@register.inclusion_tag('page/pages_menu.html')
def show_pages_menu(pages_menu):
    pages_menu = Page.objects.all()
    return { 'pages_menu' : pages_menu }


@register.inclusion_tag('footer-categories.html')
def category_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return ({
            'category': category,
            'categories': categories,
            'products': products,
        })
