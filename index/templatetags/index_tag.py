from django import template
from ..models import Place

register = template.Library()


@register.simple_tag()
def get_places():
    return Place.objects.all()
