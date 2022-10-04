from rest_framework import routers # cria a rota
from django.urls import path, include
from .views import BoardViewSets, TaskViewSets, index


router = routers.DefaultRouter()
router.register(r'boards', BoardViewSets)
router.register(r'tasks', TaskViewSets)


urlpatterns = [
    path('', index, name='homepage'),
    path('api/', include(router.urls))
]
