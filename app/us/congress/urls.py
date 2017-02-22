from django.conf.urls import include, url

from . import views
states = ['AK','AL','AR','AZ','CA','CO','CT','DE','FL','GA','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MI','MN','MO','MS','MT','NC','ND','NE','NH','NJ','NM','NV','NY','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VA','VT','WA','WI','WV','WY',]
state_regex = "(" + "|".join(states) + ")(?i)"

urlpatterns = [
    url(r'^$', views.index, name='us_congress_index'),
    url(r'senate/?$', views.senate_index, name='us_senate_index'),
    url(r'house/?$', views.house_index, name='us_house_index'),
    url(r'senate/%s/?$' % state_regex, views.senate_state, name='us_senate_state'),
    url(r'senate/%s/([a-zA-Z]*)_([a-zA-Z]*)/?$' % state_regex, views.senate_individual, name='us_senate_individual'),
    url(r'senate/committees/?$', views.senate_committees, name='us_senate_committees'),
]