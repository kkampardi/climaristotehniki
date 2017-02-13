
from portfolio.models import Project

def show_fp_projects(request):
    fp_projects = Project.objects.all()[:3]
    latest_project = Project.objects.all()[:1]
    return {
        'fp_projects': fp_projects,
        'latest_project': latest_project,
        }
