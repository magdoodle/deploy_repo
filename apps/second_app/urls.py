from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^success$', views.success),
    # url(r'^tothecreatepage$', views.to_create),
    # url(r'^create$', views.create_wish),
    url(r'^addFriend$', views.addFriend),
    url(r'^remove/(?P<id>\d+)$', views.remove_friend),
    # # url(r'^show/(?P<id>\d+)$', views.show_item)
    url(r'^profile/(?P<id>\d+)$', views.profile_info)
  
]