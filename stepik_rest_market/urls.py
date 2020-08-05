"""stepik_rest_market URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('market.urls')),
    path('', include('recipient.urls')),
    path('', include('order.urls')),
    ]

# Доступные URI

# admin/
# api-auth/
# ^product-sets/?$ [name='product-sets-list']  -> GET список продуктов
# ^product-sets/(?P<pk>[^/.]+)/?\.(?P<format>[a-z0-9]+)/?$ [name='product-sets-detail'] -> GET Продукт по рк
#
# ^recipients/?$ [name='recipient-list'] -> GET Список получателей
# ^recipients/(?P<pk>[^/.]+)/?$ [name='recipient-detail'] -> GET Получатель по рк PATCH и PUT все кроме фамилии
# ^recipients/(?P<pk>[^/.]+)/change_surname/?$ [name='recipient-change-surname'] -> смена фамилии Получателя по рк PATCH
#
# ^orders/?$ [name='orders-list'] -> GET cписок oрдеров
# ^orders/filter_order/?$ [name='orders-filter-order'] -> фильтр по продукту и по времени создания ордера
# ^orders/(?P<pk>[^/.]+)/?$ [name='orders-detail'] -> GET ордер по рк PATCH и PUT для update доступны status только "created" "cancelled"
# orders/filter_order/ ->  фильтр по продукту и по времени создания ордера вводить ?data_order=%Y-%m-%d"