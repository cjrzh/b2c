from django import template
from front.models import Category

register = template.Library()

@register.inclusion_tag('front/cats.html')
def get_category_list():
    categories=Category.objects.all()
    context={'cats':Category.objects.all()}
    # for c in categories:
    #     print(c)
    return context