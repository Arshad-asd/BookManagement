from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import *
from rest_framework import generics

class BookCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = BookSerializer(data=request.data, context={'request': request})  # Pass the request context
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            # Ensure that only the book owner can update it
            if book.user != request.user:
                return Response({"error": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Book.objects.get(pk=pk, user=user)
        except Book.DoesNotExist:
            raise Http404("Book does not exist")

    def delete(self, request, pk):
        book = self.get_object(pk, request.user)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserBooksListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Book.objects.filter(user=request.user)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllBooksListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ReadingListCreateAPIView(generics.CreateAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]


class ReadingListUpdateView(generics.UpdateAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]


class UserReadingListView(generics.ListAPIView):
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ReadingList.objects.filter(user=user)


class UserReadingListDeleteView(generics.DestroyAPIView):
    queryset = ReadingList.objects.all()
    serializer_class = ReadingListSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
            try:
                reading_list = self.get_object()
                if reading_list.user == request.user:
                    list_name = reading_list.name
                    list_id = reading_list.id
                    reading_list.delete()
                    return Response({"message": f"Reading list '{list_name}' with ID {list_id} has been deleted."}, status=status.HTTP_204_NO_CONTENT)
                else:
                    return Response({"detail": "You don't have permission to delete this reading list."}, status=status.HTTP_403_FORBIDDEN)
            except:
                return Response({"detail": "Reading list not found."}, status=status.HTTP_404_NOT_FOUND)


class AddBookToReadingListView(APIView):
    def post(self, request, reading_list_id):
        try:
            reading_list = ReadingList.objects.get(id=reading_list_id)
        except ReadingList.DoesNotExist:
            return Response({"message": "Reading list not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AddBookToReadingListSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.validated_data['book']
            # Check if the book is already in the reading list
            if reading_list.books.filter(id=book.id).exists():
                return Response({"message": "Book already exists in the reading list"}, status=status.HTTP_400_BAD_REQUEST)

            # Add the book to the reading list
            reading_list_item = ReadingListItem.objects.create(
                book=book,
                reading_list=reading_list
            )
            return Response({"message": "Book added to reading list successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteBookFromReadingListView(APIView):
    def delete(self, request, reading_list_id, book_id):
        try:
            reading_list = ReadingList.objects.get(id=reading_list_id)
            book = reading_list.books.get(id=book_id)
        except ReadingList.DoesNotExist:
            return Response({"message": "Reading list not found"}, status=status.HTTP_404_NOT_FOUND)
        except ReadingListItem.DoesNotExist:
            return Response({"message": "Book not found in the reading list"}, status=status.HTTP_404_NOT_FOUND)

        # Delete the book from the reading list
        reading_list_item = ReadingListItem.objects.get(book=book, reading_list=reading_list)
        reading_list_item.delete()

        return Response({"message": "Book deleted from reading list successfully"}, status=status.HTTP_204_NO_CONTENT)