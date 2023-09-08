from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.WordsView.as_view(), name="words"),
    path("<int:pk>/", views.WordsDetailView.as_view(), name="meaning"),
    path("allwords/", views.WordsListView.as_view(), name="allwords")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)