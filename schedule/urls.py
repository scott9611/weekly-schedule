from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from app.views import WeeklyScheduleViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from app.views import protected_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

router = DefaultRouter()
router.register(r'weeklyschedules', WeeklyScheduleViewSet)

schema_view = get_schema_view(
   openapi.Info(
      title="Weekly Schedule API",
      default_version='v1',
      description="API for managing weekly schedules",
      terms_of_service="https://www.yourapp.com/terms/",
      contact=openapi.Contact(email="contact@yourapp.com"),
      license=openapi.License(name="Your License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   authentication_classes=(),
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('protected/', protected_view, name="protected"),
    path('accounts/', include('django.contrib.auth.urls')),
]
