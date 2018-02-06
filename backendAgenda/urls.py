
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from accounts import urls as accUrls
from django.contrib.auth.views import password_reset_confirm


#api
from rest_framework import routers
from tasks.views import TasksViewSet
from accounts.views import ProfileViewSet
from meeting.views import MeetingViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TasksViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'meeting',MeetingViewSet)

urlpatterns = [
    url(
    regex=r'^media/(?P<path>.*)$',
    view = serve,
    kwargs={'document_root':settings.MEDIA_ROOT}
    ),
    path('admin/', admin.site.urls),
    #api
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/', include(accUrls, namespace='api-urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^', include('django.contrib.auth.urls')),

]
