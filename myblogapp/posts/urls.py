from django.conf.urls import url

from . import views
# from . import views 同じ階層の中からviewsを呼ぶ

urlpatterns = [url(r'^$',views.index, name="index")]
