from django.urls import include, path
from rest_framework.routers import DefaultRouter
from issue.views import IssueViewSet

router = DefaultRouter()
router.register("issues", IssueViewSet, "issues")

urlpatterns = [path('api/', include(router.urls))]
