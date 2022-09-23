from django.shortcuts import render
from rest_framework import generics, status
from .models import Sticker
from .serializers import StickerListSerializer, StickerDetailSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


class StickerList(generics.ListCreateAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerListSerializer
    permission_classes = []


class StickerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sticker.objects.all()
    serializer_class = StickerListSerializer
    permission_classes = []


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'stickers/': reverse('all-stickers', request=request, format=format),
    })