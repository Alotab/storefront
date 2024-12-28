from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, Func
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum

from store.models import Customer, Product, OrderItem, Order, Collection



def say_hello(request):
    pass
    # query_set = Product.objects.filter(Q(inventory__lt=20) | Q(unit_price__lt=20))
    # query_set = Product.objects.filter(inventory=F('collection__id'))
    # query_set = Product.objects.order_by('unit_price','-title')
    # product = Product.objects.order_by('unit_price')[0]
    # query_set = Product.objects.filter(collection__id=10).order_by('unit_price','-title')
    # query_set = Product.objects.all()[4:9]
    # query_set = Product.objects.values('id', 'title')
    # query_set = Product.objects.values_list('id', 'title', 'collection__title')
    # query_set = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # query_set = Product.objects.select_related('collection').all()  # the other end of the relationship has one instance - product has one collection

    #prefetch_related is when the other end of the relationship has many relation in this case - Promotion
    # query_set = Product.objects.prefetch_related('promotions').select_related('collection')
    # query_set = Order.objects.select_related('customer').order_by('-placed_at')[:6]
    # result = Product.objects.aggregate(count=Count('id'), min_price=Min('unit_price'))

    # query_set = Customer.objects.annotate(is_new=Value(True))

    # query_set = Customer.objects.annotate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT'))
    # query_set = Customer.objects.annotate(full_name=Concat('first_name', ' ','last_name'))

    # create objects 1
    # collection = Collection.objects.create(title="name", featured_product_id=1)

    ## create objects 2
    # collection = Collection(pk=1)
    # collection.title = "Game Mairo"
    # collection.featured_product = None
    # collection.save()

    ## update objects 2
    # collection = Collection.objects.get(pk=1)
    # collection.title = "Game Bros"
    # collection.save()

    ## update objects 3
    # Collection.objects.filter(pk=1).update(featured_product = None)



    # return render(request, "hello.html", {"query_set": list(query_set)})