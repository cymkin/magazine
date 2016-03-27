from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^home/$', views.home, name = "home"),
    url(r'^contact/$', views.contact, name = "contact"),
    url(r'^order/$', views.orderNew, name = "order"),
    url(r'^order2/$', views.order2, name = "order"),
    url(r'^orderthanks/$', views.orderthx, name = "thanks"),
    url(r'^contactthanks/$', views.contactthx, name = "thanks"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
