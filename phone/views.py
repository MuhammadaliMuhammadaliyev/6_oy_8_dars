from functools import partial

from django.core.serializers import serialize
from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from .serializers import PhonesSerializer
from .models import Phones
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, \
    GenericAPIView


# class ListView(APIView):
#     def get(self, request):
#         phones = Phones.objects.all()
#         serializer = PhonesSerializer(phones, many=True)
#         data = {
#             'status': status.HTTP_200_OK,
#             'Message': 'Phones',
#             'count': len(phones),
#             'products': serializer.data
#         }
#         return Response(data)
#
#
# class DetailView(APIView):
#     def get(self, request, pk):
#         phone = Phones.objects.filter(pk=pk).first()
#         serializer = PhonesSerializer(phone)
#         if phone:
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'Message': 'Phone detail',
#                 'product': serializer.data
#             }
#             return Response(data)
#         return Response({
#             "success": False,
#             'message': 'Bunday maxsulot mavjud emas',
#             'status': status.HTTP_204_NO_CONTENT
#         })
#
#
# class DeleteView(APIView):
#     def delete(self, request, pk):
#         product = Phones.objects.filter(pk=pk).first()
#         if product:
#             product.delete()
#             return Response({"message": "Tugadi"})
#         return Response({"message": "Malumot yoq"})
#
#
# class CreateView(APIView):
#     def post(self, request):
#         serializer = PhonesSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_201_CREATED,
#                 'message': 'Product yaratildi',
#                 'product': serializer.data
#             }
#             return Response(data)
#
#         data = {
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Product yaratilmadi',
#             'eror': serializer.errors
#         }
#         return Response(data)
#
#
# class UpdateView(APIView):
#     def put(self, request, pk):
#         phone = Phones.objects.filter(pk=pk).first()
#         serializer = PhonesSerializer(phone, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Product ozgartirildi',
#                 'product': serializer.data
#             }
#             return Response(data)
#
#         data = {
#             'status': status.HTTP_400_BAD_REQUEST,
#             'message': 'Product ozgartirilmadi',
#             'error': serializer.errors
#         }
#         return Response(data)
#
#     def patch(self, request, pk):
#         phone = Phones.objects.filter(pk=pk).first()
#         if not phone:
#             data = {
#                 'status': status.HTTP_400_BAD_REQUEST,
#                 'message': 'Product mavjud emas',
#             }
#             return Response(data)
#         serializer = PhonesSerializer(instance=phone, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Product ozgartirildi',
#                 'product': serializer.data
#             }
#             return Response(data)







class ListView(GenericAPIView):
    serializer_class = PhonesSerializer
    queryset = Phones.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            'count': len(serializer.data),
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Product yaratildi',
                'product': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'error': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )




class DetailDeleteUpdate(GenericAPIView):
    serializer_class = PhonesSerializer
    queryset = Phones.objects.all()

    def get_object(self, pk):
        try:
            return Phones.objects.get(pk=pk)
        except Phones.DoesNotExist:
            raise NotFound("Bu id dagi maxsulot mavjud emas")

    def get(self, request, pk):
        phone = self.get_object(pk)
        serializer = self.get_serializer(phone)
        data = {
            'status': status.HTTP_200_OK,
            'data': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        phone = self.get_object(pk)
        phone.delete()
        data = {
            'status': status.HTTP_200_OK,
            'message': 'O‘chirildi'
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        phone = self.get_object(pk)
        serializer = self.get_serializer(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Product o‘zgartirildi',
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Product o‘zgartirilmadi',
                'error': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, pk):
        phone = self.get_object(pk)
        serializer = self.get_serializer(phone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Product o‘zgartirildi',
                'product': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'error': serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )


