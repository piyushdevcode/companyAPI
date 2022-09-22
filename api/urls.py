from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet, basename='company')
# router.register(r'team',views.TeamViewSet,basename='team')

# Binding viewsets explicitly so as to custom URLs
team_list = views.TeamViewSet.as_view({
    'get': 'list',
})
team_create = views.TeamViewSet.as_view({
    'post': 'create',
})
team_detail = views.TeamViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    # path('',views.api_root,name='api-root'),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('team/create/<uuid:cid>/',team_create,name='team-create'),
    path('team/',team_list,name='team-list'),
    path('team/<uuid:id>/',team_detail,name='team-detail')

]
