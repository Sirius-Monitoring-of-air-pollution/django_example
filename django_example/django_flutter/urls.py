from django.urls import path

from . import views

urlpatterns = [
    path('<path:path>', views.flutter_view),
]
