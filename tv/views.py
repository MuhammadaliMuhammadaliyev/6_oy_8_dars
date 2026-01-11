from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .serializers import TvSerializer
from .models import Tv
from rest_framework.response import Response
from rest_framework import status



# class ListCreateView(APIView):
#     def post(self,request):
#         serializer = TvSerializer(data=request.data)
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
#     def get(self, request):
#         tv = Tv.objects.all()
#         serializer = TvSerializer(tv, many=True)
#         data = {
#             'status': status.HTTP_200_OK,
#             'Message': "Tv's",
#             'count': len(tv),
#             'products': serializer.data
#         }
#         return Response(data)
#
# class DetailUpdateDeleteView(APIView):
#     def delete(self, request, pk):
#         product = Tv.objects.filter(pk=pk).first()
#         if product:
#             product.delete()
#             return Response({"message": "O'chirildi"})
#         return Response({"message": "Malumot yoq"})
#
#     def get(self, request, pk):
#         tv = Tv.objects.filter(pk=pk).first()
#         serializer = TvSerializer(tv)
#         if tv:
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'Message': 'Tv detail',
#                 'product': serializer.data
#             }
#             return Response(data)
#         return Response({
#             "success": False,
#             'message': 'Bunday maxsulot mavjud emas',
#             'status': status.HTTP_204_NO_CONTENT
#         })
#
#     def put(self, request, pk):
#         tv = Tv.objects.filter(pk=pk).first()
#         serializer = TvSerializer(tv, data=request.data)
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
#         tv = Tv.objects.filter(pk=pk).first()
#         if not tv:
#             data = {
#                 'status': status.HTTP_400_BAD_REQUEST,
#                 'message': 'Product mavjud emas',
#             }
#             return Response(data)
#         serializer = TvSerializer(instance=tv, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 'status': status.HTTP_200_OK,
#                 'message': 'Product ozgartirildi',
#                 'product': serializer.data
#             }
#             return Response(data)



class TvViewSet(ViewSet):


    def list(self, request):
        tv = Tv.objects.all()
        serializer = TvSerializer(tv, many=True)
        data = {
            'status': status.HTTP_200_OK,
            'message': "Tv's",
            'count': tv.count(),
            'products': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    def create(self, request):
        serializer = TvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Product yaratildi',
                'product': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Product yaratilmadi',
            'error': serializer.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        tv = Tv.objects.filter(pk=pk).first()
        if not tv:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Bunday maxsulot mavjud emas'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = TvSerializer(tv)
        data = {
            'status': status.HTTP_200_OK,
            'message': 'Tv detail',
            'product': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


    def update(self, request, pk=None):
        tv = Tv.objects.filter(pk=pk).first()
        if not tv:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Product mavjud emas'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = TvSerializer(tv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Product o‘zgartirildi',
                'product': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Product o‘zgartirilmadi',
            'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


    def partial_update(self, request, pk=None):
        tv = Tv.objects.filter(pk=pk).first()
        if not tv:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Product mavjud emas'
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = TvSerializer(tv, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Product o‘zgartirildi',
                'product': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Xatolik',
            'error': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        tv = Tv.objects.filter(pk=pk).first()
        if not tv:
            return Response({
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Maʼlumot yo‘q'
            }, status=status.HTTP_404_NOT_FOUND)

        tv.delete()
        return Response({
            'status': status.HTTP_200_OK,
            'message': "O‘chirildi"
        }, status=status.HTTP_200_OK)
