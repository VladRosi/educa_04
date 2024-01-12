from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from accounts.views import logout_view
from courses.views import CourseListView

urlpatterns = [
  path("admin/", admin.site.urls),
  # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('accounts/logout/', logout_view, name='logout'),
  path('course/', include('courses.urls')),
  path('students/', include('students.urls')),
  path('api/', include('courses.api.urls', namespace='api')),
  path('chat/', include('chat.urls', namespace='chat')),
  path("__reload__/", include("django_browser_reload.urls")),
  path('__debug__/', include('debug_toolbar.urls')),
  path('', CourseListView.as_view(), name='course_list'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
