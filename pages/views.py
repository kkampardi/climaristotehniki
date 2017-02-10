from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Faq, Category, Page
def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'page/page_detail.html', {'page': page})


def faq(request):
    faqs = Faq.objects.all()
    categories = Category.objects.all()
    return render(request, 'faq.html', {
        'faqs': faqs,
        'categories': categories,
        })
