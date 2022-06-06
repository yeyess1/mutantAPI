
from django.urls import path
from .views import MutantApiView, StatsApiView


urlpatterns = [
    path('mutant/', MutantApiView.as_view(), name= 'members' ),
    path('stats/', StatsApiView.as_view(), name= 'members'  )

]