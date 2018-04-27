from django.template.defaulttags import register
from django import template

register = template.Library()


@register.filter
def get_key(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_value(dictionary, value):
    return dictionary.get(value)