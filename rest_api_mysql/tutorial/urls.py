from django.urls import include, path

from . import views


urlpatterns = [
    path('tutorial',views.get_tuturial),
    path('add_tutorial',views.add_tutorial),
    path('tutorial/<int:id_tutorial>', views.tutorials),
]