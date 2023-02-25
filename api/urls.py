from rest_framework import routers
from api.views import TodoModelViewSet


router = routers.DefaultRouter()
router.register(r'todo', TodoModelViewSet,basename='todo-api')

urlpatterns = [
    
]
urlpatterns = router.urls
