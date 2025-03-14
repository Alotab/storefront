from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.db.models import QuerySet
from django.urls import reverse
from . import models

class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value == '<10':
           return queryset.filter(inventory__lt=10)

 

class OrderItemInline(admin.TabularInline): # admin.StackedInline
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10
    model = models.OrderItem
    extra = 0

 
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer']
    inlines = [OrderItemInline]
    list_display = ['id', 'customer', 'placed_at']
    

class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    readonly_fields = ['thumbnail']
 
    def thumbnail(self, instance):
        if instance.image.name != '':
            return format_html(f"<img src='{instance.image.url}' class='thumbnail'/>") 
        return ''


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = ['']
    search_fields = ['product']
    autocomplete_fields = ['collection']
    prepopulated_fields = {
        'slug': ['title']
    }
    actions = ['clear_inventory']
    inlines = [ProductImageInline]
    # inlines = [TagInline]
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter]
    list_per_page = 10
    list_select_related = ['collection']

    # if you want to show a particular field in a collection--lets say title
    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'Ok'
    
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset: QuerySet):
        updated_count = queryset.update(inventory=0)
        self.message_user(
            request, 
            f"{updated_count} products were successfully updated.",
            messages.ERROR
        )
    
    # Load the style sheet on the Product Admin page
    class Media:
        css = {
            'all': ['store/styles.css']
        }



@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        return collection.products.count()

    @admin.display(ordering='products_count')
    def products____count(self, collection):
        url = (reverse('admin:store_product_changelist') 
               + '?' 
               + urlencode({
                   'collection__id': str(collection.id)
               }))
        return format_html('<a href="{}">{}<a/>', url,  collection.products_count)
        # return collection.product_count
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('products')
        )


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name__istartwith', 'last_name__istartwith']
    list_display = ['first_name', 'last_name', 'membership', 'orders']
    list_editable = ['membership']
    ## list_select_related = ['user']
    ordering = ['first_name', 'last_name']
    list_per_page = 10

    @admin.display(ordering='orders_count')
    def orders(self, customer):
        orders_count = customer.orders.count()
        url = reverse('admin:store_order_changelist') + '?' + urlencode({'customer__id': str(customer.id)})
        return format_html('<a href="{}">{} orders</a>', url, orders_count)
        # url = (
        #         reverse('admin:store_order_changelist') #admin:app_model_page -- you targetting the model page or redirect the user to that model (order) page and the exact target page is called changelist
        #         + '?'
        #         + urlencode({
        #     'order__id': str(customer.id)
        # }))
        # return format_html('<a href="{}">{}</a>', url, orders_count)
