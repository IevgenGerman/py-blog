from django.urls import path
from .views import index, PostDetailView

app_name = "blog"  # ОСЬ ЦЬОГО РЯДКА НЕ ВИСТАЧАЄ

urlpatterns = [
    path("", index, name="index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]
