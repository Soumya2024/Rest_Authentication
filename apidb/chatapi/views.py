from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import MergedData
from .serializers import MergedDataSerializer
# Create your views here.

class FetchAndMergeDataView(APIView):

    def get(self, request, *args, **kwargs):
        # Fetch data from the first API
        response1 = requests.get('https://api.spacexdata.com/v4/launches/latest')
        if response1.status_code != 200:
            return Response({'error': 'Failed to fetch data from API 1'}, status=status.HTTP_400_BAD_REQUEST)
        data1 = response1.json()

        # Fetch data from the second API
        response2 = requests.get('https://catfact.ninja/fact')
        if response2.status_code != 200:
            return Response({'error': 'Failed to fetch data from API 2'}, status=status.HTTP_400_BAD_REQUEST)
        data2 = response2.json()

        # Merge the data
        merged_data = {**data1, **data2}  # Adjust the merging logic as needed

        # Save the merged data to the database
        merged_data_instance = MergedData(json_data=merged_data)
        merged_data_instance.save()

        # Serialize the saved data
        serializer = MergedDataSerializer(merged_data_instance)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
