from django.urls import path
from views import FetchAndMergeDataView

# from django.views.generic import FetchAndMergeDataView

urlpatterns = [
    path('fetch-and-merge/', FetchAndMergeDataView.as_view(), name='fetch-and-merge'),
]
