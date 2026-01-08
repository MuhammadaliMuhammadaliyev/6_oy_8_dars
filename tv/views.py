from rest_framework.views import APIView
from .serializers import TvSerializer
from .models import Tv
from rest_framework.response import Response
from rest_framework import status



class ListCreateView(APIView):
    def post(self,request):
        serializer = TvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_201_CREATED,
                'message': 'Product yaratildi',
                'product': serializer.data
            }
            return Response(data)

        data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Product yaratilmadi',
            'eror': serializer.errors
        }
        return Response(data)

    def get(self, request):
        tv = Tv.objects.all()
        serializer = TvSerializer(tv, many=True)
        data = {
            'status': status.HTTP_200_OK,
            'Message': "Tv's",
            'count': len(tv),
            'products': serializer.data
        }
        return Response(data)

class DetailUpdateDeleteView(APIView):
    def delete(self, request, pk):
        product = Tv.objects.filter(pk=pk).first()
        if product:
            product.delete()
            return Response({"message": "O'chirildi"})
        return Response({"message": "Malumot yoq"})

    def get(self, request, pk):
        tv = Tv.objects.filter(pk=pk).first()
        serializer = TvSerializer(tv)
        if tv:
            data = {
                'status': status.HTTP_200_OK,
                'Message': 'Tv detail',
                'product': serializer.data
            }
            return Response(data)
        return Response({
            "success": False,
            'message': 'Bunday maxsulot mavjud emas',
            'status': status.HTTP_204_NO_CONTENT
        })

    def put(self, request, pk):
        tv = Tv.objects.filter(pk=pk).first()
        serializer = TvSerializer(tv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Product ozgartirildi',
                'product': serializer.data
            }
            return Response(data)

        data = {
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Product ozgartirilmadi',
            'error': serializer.errors
        }
        return Response(data)

    def patch(self, request, pk):
        tv = Tv.objects.filter(pk=pk).first()
        if not tv:
            data = {
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Product mavjud emas',
            }
            return Response(data)
        serializer = TvSerializer(instance=tv, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': status.HTTP_200_OK,
                'message': 'Product ozgartirildi',
                'product': serializer.data
            }
            return Response(data)