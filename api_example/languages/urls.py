from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)
router.register('paradigm', views.ParadigmView)
router.register('programmers', views.ProgrammersView)

urlpatterns = [
     path('', include(router.urls))
]
