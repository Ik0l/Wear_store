from django.core.context_processors import request
from wear.models import Category


def menu(request):
    categoryes = Category.objects.all()
    return {"category_list": categoryes}