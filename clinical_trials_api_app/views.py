from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import StudyItemSerializer
from .models import StudyItem

class StudyItemViews(APIView):
    # Get all objects or only specific objects if id is given
    def get(self, request, id=None):
        if id:
            item = StudyItem.objects.get(id=id)
            serializer = StudyItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = StudyItem.objects.all()
        serializer = StudyItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    # Post request
    def post(self, request):
        serializer = StudyItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    # Patch request for updates     
    def patch(self, request, id=None):
        item = StudyItem.objects.get(id=id)
        serializer = StudyItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
    
    # Delete request    
    def delete(self, request, id=None):
        item = get_object_or_404(StudyItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
        