"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# Register REST API routes using DRF routers so /api/... endpoints exist.
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API root (exact '/api/') returns a listing from views.api_root
    path('api/', views.api_root, name='api-root'),
    # Include router-managed viewsets under /api/
    path('api/', include(router.urls)),
    # Optionally add DRF login for the browsable API
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('', views.api_root),  # This makes the root URL point to the API
]
