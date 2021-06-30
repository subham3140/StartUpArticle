from django import template
from django.utils.safestring import mark_safe
from django.utils.html import format_html

register = template.Library()

@register.filter
def index(indexable):
    result = ''
    for i in range(len(indexable)):
        if i == 0:
            result += "<h3>" + indexable[0] + "</h3><br>"
        else:
            result += f'<div id="innerlist"><i class="fas fa-hand-point-right"></i><h3>'+ indexable[i] + '</h3></div><br>'   
    return mark_safe(result)