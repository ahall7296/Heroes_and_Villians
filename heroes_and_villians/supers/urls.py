from django.urls import path

from .views import SuperListCreateAPIView, SuperRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", SuperListCreateAPIView.as_view(), name="Super_list_create"),
    path("<int:pk>/", SuperRetrieveUpdateDestroyAPIView.as_view(), name="Super_ret_updt_dest"),
]