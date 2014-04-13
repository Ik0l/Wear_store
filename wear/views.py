# -*- coding:utf-8 -*-

from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext

from wear.models import Cloth, SizeCount, Category


def index(request):  # index пока пустой, скорее всего тут будут новости, или просто страница приветствия
    context = RequestContext(request)
    context.update({'message': 'Ололо, ололо, я водитель НЛО.'})
    return render_to_response('wear_list.html', context)


def wear_list_cat(request, cat_id):
    context = RequestContext(request)
    if cat_id:
        cat = get_object_or_404(Category, id=cat_id)
        return render_to_response('wear_list.html', {
            'wears': Cloth.objects.filter(category=cat_id),
            'cat': cat
        }, context)
    else:
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


def cart_add(request, cloth_id):
    if "cloth" in request.session:
        request.session["cloth"] += [Cloth.objects.get(id=cloth_id).id]
        return redirect('/cart/')
    else:
        request.session.set_expiry(60)  # Для тестов. Не забыть исправить, а лучше использовать что-нибудь другое
        # сделай в зависимости от settings.DEBUG или свою переменную сделай к примеру setttings.COOKIE_DEBUG
        # и пускай у тебя будет что то подобное...
        # if settings.COOKIE_DEBUG:
        #     request.session.set_expiry(60)
        request.session["cloth"] = [Cloth.objects.get(id=cloth_id).id]
        return redirect('/')


def cart_view(request):
    context = RequestContext(request)
    if "cloth" in request.session:
        return render_to_response('cart.html', {
            'wears': Cloth.objects.filter(id__in=request.session["cloth"]),
            'sizes': SizeCount.objects.filter(item_id__in=request.session["cloth"]),
            'items': request.session["cloth"],
        }, context)
    else:
        return render_to_response('cart.html', context)
