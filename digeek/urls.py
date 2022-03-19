from django.urls import re_path

from digeek import views

urlpatterns = [
    re_path(r'^imagen$', views.ImagenApi.as_view(), name='imagen'),
    re_path(r'^imagen/([0-9]+)$', views.ImagenAApi.as_view()),
    re_path(r'^digeek$', views.DigeekApi.as_view()),
    re_path(r'^digeek/([0-9]+)$', views.DigeekAApi.as_view()),
    re_path(r'^evento$', views.EventosApi.as_view()),
    re_path(r'^evento/([0-9]+)$', views.EventosAApi.as_view()),
    re_path(r'^expositor$', views.ExpositorApi.as_view()),
    re_path(r'^expositor/([0-9]+)$', views.ExpositorAApi.as_view()),
    re_path(r'^redessociales$', views.RedesSocialesApi.as_view()),
    re_path(r'^redessociales/([0-9]+)$', views.RedesSocialesAApi.as_view()),
    re_path(r'^visitante$', views.VisitanteApi.as_view()),
    re_path(r'^visitante/([0-9]+)$', views.VisitanteAApi.as_view()),
    re_path(r'^registrodigeek$', views.RegistroDigeekApi.as_view()),
    re_path(r'^registrodigeek/(?P<digeekid>[0-9]+)/(?P<visitanteid>[0-9]+)$', views.RegistroDigeekAApi.as_view()),
]