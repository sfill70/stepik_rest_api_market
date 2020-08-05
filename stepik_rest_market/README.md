Доступные URI

# Доступные URI


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

Скрипт для наполнения базы данных
```
python3 manage.py load_data
python manage.py load_data  - WIN
```



