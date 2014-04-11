# -*- coding:utf-8 -*-

from wear.models import Category


def menu(request):
    categoryes = Category.objects.all()
    return {"category_list": categoryes}
    cat = Category.objects.filter(id=1)
    return {
        "category_list": categoryes,
        "catcatcat": cat,
    }
