# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from models import Geoposition
from serializers import GeopositionSerializer
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import render

class GeocodeViewSet(ModelViewSet):
    queryset = Geoposition.objects.all()
    serializer_class = GeopositionSerializer
