from django.urls import include, path

from api.v1.parks.routers import router

app_name = 'api'
urlpatterns = [path('', include(router.urls))]
