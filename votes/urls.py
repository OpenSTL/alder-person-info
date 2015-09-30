from django.conf.urls import url
from votes import views

# TODO remove 'votes' word from url by using namespace from parent urls.py file

urlpatterns = [
    url(r'^votes/$', views.VoteList.as_view()),
    url(r'^votes/(?P<pk>[0-9]+)/$', views.VoteDetail.as_view()),
    url(r'^votes/wards/$', views.WardList.as_view()),

    """
    /votes
        /votes/?alderman=baringer
        /votes/?ward=14
        /votes/?bill=
    /bills
    /voting_rounds
    /wards
    /aldermen

    """
]
