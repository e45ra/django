from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from duapp import views

router = routers.DefaultRouter()
router.register('persondata', views.PersonDataView)
router.register('drug', views.DrugView)
router.register('store', views.StoreView)
router.register('cage', views.CageView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]
