from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from wear.models import Cloth, SizeCount, Size, Category
from django.core.exceptions import ObjectDoesNotExist


def wear_list(request):
    return render_to_response('wear_list.html', {'wears': Cloth.objects.all(), 'cur_url': request.path,})


def wear_detail(request, cloth_id):
    try:
        count_x = 0
        for x in SizeCount.objects.filter(cloth_id=cloth_id):
            count_x += x.count
        return render_to_response('wear_detail.html', {
            'wear': Cloth.objects.get(id=cloth_id),
            'cat': Category.objects.get(id = Cloth.objects.get(id=cloth_id).category_id),
            'sizes': SizeCount.objects.filter(cloth_id=cloth_id),
            'all_count': count_x,
            'cur_url': request.path,
            }
        )
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')



def wear_list_cat(request, cat):
    try:
        return render_to_response('wear_list.html', {
            'wears': Cloth.objects.filter(category=cat),
            'cat': Category.objects.get(id=cat),
            'cur_url': request.path,
            }
        )
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


def cart_add(request, cloth_id=0):
    if ("cloth" in request.session):
        request.session["cloth"] += [Cloth.objects.get(id=cloth_id).id]
        return redirect('/cart/')
    else:
        request.session.set_expiry(60)
        request.session["cloth"] = [Cloth.objects.get(id=cloth_id).id]
        return redirect('/')


def cart_view(request):
    if ("cloth" in request.session):
        xx = len(request.session["cloth"])
        return render_to_response('cart.html', {
            'wears': Cloth.objects.filter(id__in=request.session["cloth"]),
            'sizes': SizeCount.objects.filter(cloth_id__in=request.session["cloth"]),
            'items': request.session["cloth"],
            'length': xx,
            }
        )
    else:
        return render_to_response('cart.html')