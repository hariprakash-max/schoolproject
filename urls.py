from django.urls import path
from finance.views import feecollection
from finance.views import feeduesreport
from finance.views import feecollectionreport

urlpatterns = [    
    path('feecoll/', feecollection),  
    path('duesreport/', feeduesreport),  
    path('collectionreport/', feecollectionreport),  

]  

