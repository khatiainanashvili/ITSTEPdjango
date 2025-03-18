from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from books.models import Books
from .serializers import BookSerializer
from rest_framework.generics import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['GET'])
def test(request):
    return Response({'Hello': 'World'}, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='GET',
    operation_summary='List All Books',
    operation_description='This function retrieve all books from database',
    responses={
        status.HTTP_200_OK: BookSerializer,
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description='Bad Request',
            examples={'application/json': {'message': 'Bad Request'}},
        )
    }
)
@api_view(['GET'])
def book_list(request):
    events = Books.objects.all()

    serializer = BookSerializer(events, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method='POST',
    operation_summary='Create New Book',
    operation_description='new event',
    request_body=BookSerializer,
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description='Successfull Request',
            examples={'application/json': {'message': 'Book Added successfully', 'data': {
               "authors": "khatia",
                "cover": "someimage",
                "description": "seomething",
                "genre": "some genre",
                id: 148,
                "price": 478,
                "purchase": 1,
                "title": "some title"
            }}}
        ),
        status.HTTP_422_UNPROCESSABLE_ENTITY: openapi.Response(
            description='Bad Request',
            examples={'application/json': {
                    "title": [
                        "This field is required."
                    ],
                    "description": [
                        "This field is required."
                    ],
                    "location": [
                        "This field is required."
                    ],
                    "max_attendees": [
                        "This field is required."
                    ],
                    "category": [
                        "This field is required."
                    ]
                }
            }
        )
    }
)
@api_view(['POST'])
def create_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        book = serializer.save()
        return Response({'message': 'Book added successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['PUT'])
def update_book(request, pk):
    event = get_object_or_404(Books, pk=pk)

    event_serializer = BookSerializer(event, data=request.data)

    if event_serializer.is_valid():
        event_serializer.save()

        return Response({'message': f'Book with pk {pk} updated successfully', 'data': event_serializer.data}, status=status.HTTP_200_OK)

    return Response(event_serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@api_view(['DELETE'])
def delete_book(request, pk):
    event = get_object_or_404(Books, pk=pk)

    event.delete()

    return Response({'message': 'Book Deleted successfully'}, status=status.HTTP_204_NO_CONTENT)