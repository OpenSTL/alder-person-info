from django.conf.urls import url
from votes import views

urlpatterns = [
    url(r'^votes/$', views.VoteList.as_view()),
]