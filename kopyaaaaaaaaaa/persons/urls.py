from django.urls import path

from .views import person_create_view,load_yayinevi,load_tyt_ayt,load_type,load_ders,load_isim,load_gethtml

urlpatterns = [
    path('add/', person_create_view, name='person_add'),
    # path('<int:pk>/', person_update_view, name='person_change'),
    path('ajax/load-yayinevi/', load_yayinevi, name='ajax_load_yayinevi'), # AJAX
    path('ajax/load-tyt-ayt/', load_tyt_ayt, name='ajax_load_tyt_ayt'), # AJAX
    path('ajax/load-type/', load_type, name='ajax_load_type'), # AJAX
    path('ajax/load-ders/', load_ders, name='ajax_load_ders'), # AJAX
    path('ajax/load-isim/', load_isim, name='ajax_load_isim'), # AJAX
    path('ajax/load-gethtml/', load_gethtml, name='ajax_load_gethtml'), # AJAX
]