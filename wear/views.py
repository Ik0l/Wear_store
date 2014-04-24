# -*- coding:utf-8 -*-

from django.db.models import Sum
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.core.context_processors import csrf

from store import settings
from wear.models import Cloth, SizeCount, Category, Comments
from forms import CommentForm

def index(request):  # index пока пустой, скорее всего тут будут новости, или просто страница приветствия
    context = RequestContext(request)
    context.update({'message': 'Ололо, ололо, я водитель НЛО.'})
    return render_to_response('wear_list.html', context)


def wear_list_cat(request, cat_id):
    context = RequestContext(request)
    if cat_id:
        cat = get_object_or_404(Category, id=cat_id, is_published=True)
        return render_to_response('wear_list.html', {
            'wears': Cloth.objects.published(category=cat_id),
            'cat': cat
        }, context)
    else:
        return render_to_response('wear_list.html', {'wears': Cloth.objects.published()}, context)


def wear_detail(request, cloth_id):
    context = RequestContext(request)
    comment_form = CommentForm
    sizes = SizeCount.objects.filter(item_id=cloth_id)
    context.update(sizes.aggregate(all_count=Sum('count')))
    context.update(csrf(request))
    cloth = get_object_or_404(Cloth, id=cloth_id, is_published=True)
    return render_to_response('wear_detail.html', {
        'wear': cloth,
        'sizes': sizes,
        'comments': Comments.objects.filter(item_id = cloth_id),
        'form': comment_form,
    }, context)


def cart_add(request, cloth_id):
    if "cloth" in request.session:
        request.session["cloth"] += [
            {
                'item': Cloth.objects.get(id=cloth_id, is_published=True).id,
                'size': 'size_def',
                'count': 1
            }
        ]
        return redirect('/cart/')
    else:
        # Для тестов. Не забыть исправить, а лучше использовать что-нибудь другое
        if settings.COOKIE_DEBUG:
            request.session.set_expiry(60)
            request.session["cloth"] = [
                {
                    'item': Cloth.objects.get(id=cloth_id, is_published=True).id,
                    'size': 'size_def',
                    'count': 1
                }
            ]
        return redirect('/cart/')


def cart_view(request):
    context = RequestContext(request)
    if "cloth" in request.session:
        items_list = []
        for item in request.session["cloth"]:
            items_list += [item['item']]
        return render_to_response('cart.html', {
            'wears': Cloth.objects.published(id__in=items_list),
            'sizes': SizeCount.objects.filter(item_id__in=items_list),
            'items': request.session["cloth"]
        }, context)
    else:
        return render_to_response('cart.html', context)


def add_comment(request, cloth_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = Cloth.objects.get(id=cloth_id, is_published=True)
            form.save()
    return redirect('/wear/detail/%s/' % cloth_id)


def cart_purchase(request):   # Testing
    if request.POST:
        print('session here:')
        for x in request.session["cloth"]:
            print x
            print 'item %s' %x['item']
        print request.session["cloth"]
    return redirect('/')