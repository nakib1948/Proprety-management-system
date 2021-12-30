from django.forms import ModelForm
from .models import Projects


class ProjectsForm(ModelForm):
    class Meta:
        model = Projects
        # exclude = ['project_priority_sl']
        fields = ['title', 'featured_image',
                  'location', 'price', 'status']
        # fields = '__all__'
