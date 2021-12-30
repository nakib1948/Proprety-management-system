from .models import Projects, Tag
from django.db.models import Q


def searchProjects(request):

    search_query = ''

    if request.GET.get('search'):
        search_query = request.GET.get('search')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Projects.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(location__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query
