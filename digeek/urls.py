from django.urls import re_path

from digeek import views

urlpatterns = [
    re_path(r'^imagen$', views.ImagenApi.as_view(), name='imagen'),
    re_path(r'^imagen/([0-9]+)$', views.ImagenAApi.as_view()),
    re_path(r'^digeek$', views.DigeekApi.as_view()),
    re_path(r'^digeek/([0-9]+)$', views.DigeekAApi.as_view()),
    re_path(r'^evento$', views.EventosApi),
    re_path(r'^evento/([0-9]+)$', views.EventosAApi),
    re_path(r'^expositor$', views.ExpositorApi),
    re_path(r'^expositor/([0-9]+)$', views.ExpositorAApi),
    re_path(r'^redessociales$', views.RedesSocialesApi),
    re_path(r'^redessociales/([0-9]+)$', views.RedesSocialesAApi),
    re_path(r'^visitante$', views.VisitanteApi),
    re_path(r'^visitante/([0-9]+)$', views.VisitanteAApi),
    re_path(r'^registrodigeek$', views.RegistroDigeekApi),
    re_path(r'^registrodigeek/(?P<digeekid>[0-9]+)/(?P<visitanteid>[0-9]+)$', views.RegistroDigeekAApi),
]