from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Super
from .serializers import SuperSerializer
# Create your views here.
class SuperListCreateAPIView(ListCreateAPIView):
    """
    this list all Supers available base on the queryset provided
    """
    serializer_class = SuperSerializer
    queryset = Super.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        type = self.request.query_params.get("type")
        if type == "villian":
            queryset = queryset.filter(super_type__type__icontains=type)
            return Response(self.get_serializer(queryset, many=True).data)
        elif type == "hero":
            queryset = queryset.filter(super_type__type__icontains=type)
            return Response(self.get_serializer(queryset, many=True).data)
    
        heroes_queryset = queryset.filter(super_type__type__icontains="hero")
        villain_queryset = queryset.filter(super_type__type__icontains="villian")
        return Response({"heroes": self.get_serializer(heroes_queryset, many=True).data,
                         "villians": self.get_serializer(villain_queryset, many=True).data, })

class SuperRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    this is used to get the detail of a Super,
    delete the Super, and also update a Super
    """
    serializer_class = SuperSerializer
    queryset = Super.objects.all()
    lookup_field = "pk"
    
    def update(self, request, *args, **kwargs):
        """This is used to override the existing update and return the status code of 200"""
        instance = self.get_object()
        # the partial true prevent the user from having to pass all fields
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=200)