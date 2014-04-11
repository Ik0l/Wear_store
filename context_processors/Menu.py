from django.core.context_processors import request
from wear.models import Category


def menu(request):
    categoryes = Category.objects.all()
    cat = Category.objects.filter(id=1)
    return {"category_list": categoryes, "catcatcat": cat}