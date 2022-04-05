from django.urls import re_path

from digeek import views

urlpatterns = [
    re_path(r'^imagen$', views.ImagenApiGet.as_view(), name='imagen'),
    re_path(r'^imagen/([0-9]+)$', views.ImagenAApiGet.as_view()),
    re_path(r'^imagenByExpositor/([0-9]+)$', views.ImagenAApiByExpositorGet.as_view()),
    re_path(r'^digeek$', views.DigeekApiGet.as_view()),
    re_path(r'^digeek/([0-9]+)$', views.DigeekAApiGet.as_view()),
    re_path(r'^evento$', views.EventosApiGet.as_view()),
    re_path(r'^evento/([0-9]+)$', views.EventosAApiGet.as_view()),
    re_path(r'^eventoMasterclass$', views.EventosAApiMasterclassGet.as_view()),
    re_path(r'^expositor$', views.ExpositorApiGet.as_view()),
    re_path(r'^expositor/([0-9]+)$', views.ExpositorAApiGet.as_view()),
    re_path(r'^redessociales$', views.RedesSocialesApiGet.as_view()),
    re_path(r'^redessociales/([0-9]+)$', views.RedesSocialesAApiGet.as_view()),
    re_path(r'^redessocialesByExpositor/([0-9]+)$', views.RedesSocialesApiByExpositorGet.as_view()),
    re_path(r'^visitante$', views.VisitanteApiGet.as_view()),
    re_path(r'^visitante/([0-9]+)$', views.VisitanteAApiGet.as_view()),
    re_path(r'^registrodigeek$', views.RegistroDigeekApiGet.as_view()),
    re_path(r'^registrodigeek/(?P<digeekid>[0-9]+)/(?P<visitanteid>[0-9]+)$', views.RegistroDigeekAApiGet.as_view()),
    re_path(r'^registrodigeekInsert$', views.RegistrarVisitanteBien.as_view()),
    re_path(r'^editor/imagen$', views.ImagenApi.as_view(), name='imagen'),
    re_path(r'^editor/imagen/([0-9]+)$', views.ImagenAApi.as_view()),
    re_path(r'^editor/imagenByExpositor/([0-9]+)$', views.ImagenAApiByExpositor.as_view()),
    re_path(r'^editor/digeek$', views.DigeekApi.as_view()),
    re_path(r'^editor/digeek/([0-9]+)$', views.DigeekAApi.as_view()),
    re_path(r'^editor/evento$', views.EventosApi.as_view()),
    re_path(r'^editor/evento/([0-9]+)$', views.EventosAApi.as_view()),
    re_path(r'^editor/eventoMasterclass$', views.EventosAApiMasterclass.as_view()),
    re_path(r'^editor/expositor$', views.ExpositorApi.as_view()),
    re_path(r'^editor/expositor/([0-9]+)$', views.ExpositorAApi.as_view()),
    re_path(r'^editor/redessociales$', views.RedesSocialesApi.as_view()),
    re_path(r'^editor/redessociales/([0-9]+)$', views.RedesSocialesAApi.as_view()),
    re_path(r'^editor/visitante$', views.VisitanteApi.as_view()),
    re_path(r'^editor/visitante/([0-9]+)$', views.VisitanteAApi.as_view()),
    re_path(r'^editor/registrodigeek$', views.RegistroDigeekApi.as_view()),
    re_path(r'^editor/registrodigeek/(?P<digeekid>[0-9]+)/(?P<visitanteid>[0-9]+)$', views.RegistroDigeekAApi.as_view()),
    re_path(r'^editor/registrodigeekInsert$', views.RegistrarVisitanteBien.as_view()),
    re_path(r'^editor/test$', views.CreatePost.as_view()),
    re_path(r'^editor/UserAdminApp/(?P<user>[0-9]+)$', views.UserAdminAppApi.as_view()),

]