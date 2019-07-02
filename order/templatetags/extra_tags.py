from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def suffix(value):
    return value.split(".")[-1]

@register.filter
@stringfilter
def filename(value):
    return value.split("/")[-1]