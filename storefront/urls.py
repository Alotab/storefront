
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

admin.site.site_header = 'Storefront Admin'
admin.site.index_title = 'Admin'
urlpatterns = [
    # path("", include("playground.urls")),
    path('store/', include('store.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))
]  + debug_toolbar_urls()