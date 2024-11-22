from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    if request.method == 'GET':
        context = request.GET.get('sort')
        if context == 'name':
            context = {'phones': phones.order_by('name')}
            return render(request, template, context)
        elif context == 'min_price':
            context = {'phones': phones.order_by('price')}
            return render(request, template, context)
        elif context == 'max_price':
            context = {'phones': phones.order_by('-price')}
            return render(request, template, context)
        else:
            context = {'phones': phones}
            return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.filter(slug__iexact=slug).values()[0]}
    return render(request, template, context)