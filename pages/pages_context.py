
from portfolio.models import Project
from products.models import Product, Category

def show_fp_projects(request):
    fp_projects = Project.objects.all()[:3]
    latest_project = Project.objects.all()[:1]
    return {
        'fp_projects': fp_projects,
        'latest_project': latest_project,
        }

def show_fp_products(request):
    fp_products = Product.objects.all()[:4]
    footer_categories = Category.objects.all()[:4]

    return {
        'fp_products': fp_products,
        'footer_categories': footer_categories,
    }
