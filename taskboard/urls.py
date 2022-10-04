from rest_framework import routers # cria a rota
from django.urls import path, include
from .views import BoardViewSets, TaskViewSets, index, board_page, new_board, new_task, edit_task


router = routers.DefaultRouter()
router.register(r'boards', BoardViewSets)
router.register(r'tasks', TaskViewSets)


urlpatterns = [
    path('', index, name='homepage'),
    path('<int:board_id>', board_page, name='boardpage'),
    path('new-board', new_board, name='newboard'),
    path('new-task', new_task, name='newtask'),
    path('edit-task', edit_task, name='edittask'),
    path('api/', include(router.urls))
]
