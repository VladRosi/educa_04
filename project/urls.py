from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from accounts.views import logout_view

urlpatterns = [
  path("admin/", admin.site.urls),
  # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
  path('accounts/logout/', logout_view, name='logout'),
  path('course/', include('courses.urls')),
  path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
