# -*- coding:utf-8 -*-

from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.db.models import Sum
from wear.models import Cloth, SizeCount, Size, Category


def wear_list(request):
    context = RequestContext(request)
    return render_to_response('wear_list.html', {'wears': Cloth.objects.all()}, context)


def wear_detail(request, cloth_id):
    context = RequestContext(request)
    sizes = SizeCount.objects.filter(item_id=cloth_id)
    context.update(sizes.aggregate(all_count=Sum('count')))
    cloth = get_object_or_404(Cloth, id=cloth_id)
    return render_to_response('wear_detail.html', {
        'wear': cloth,
        'cat': cloth.category,
        'sizes': sizes,
    }, context)


def wear_list_cat(request, cat_id):
    context = RequestContext(request)
    cat = get_object_or_404(Category, id=cat_id)
    return render_to_response('wear_list.html', {
        'wears': Cloth.objects.filter(category=cat_id),
        'cat': cat
    }, context)


def cart_add(request, cloth_id):
    if "cloth" in request.session:
        request.session["cloth"] += [Cloth.objects.get(id=cloth_id).id]
        return redirect('/cart/')
    else:
        request.session.set_expiry(60)  # Для тестов. Не забыть исправить, а лучше использовать что-нибудь другое
        request.session["cloth"] = [Cloth.objects.get(id=cloth_id).id]
        return redirect('/')


def cart_view(request):
    context = RequestContext(request)
    if "cloth" in request.session:
        return render_to_response('cart.html', {
            'wears': Cloth.objects.filter(id__in=request.session["cloth"]),
            'sizes': SizeCount.objects.filter(item_id__in=request.session["cloth"]),
            'items': request.session["cloth"],
            'length': len(request.session["cloth"]),
        }, context)
    else:
        return render_to_response('cart.html', context)