from django.urls import path
from .views import StudyItemViews

# Define url patterns to return all studies or id based studies
urlpatterns = [
    path('study-items/', StudyItemViews.as_view()),
    path('study-items/<int:id>', StudyItemViews.as_view())
]