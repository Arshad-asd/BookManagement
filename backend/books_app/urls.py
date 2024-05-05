from django.urls import path
from books_app.views import *

urlpatterns = [
    path('create/',BookCreateAPIView.as_view(),name='book-create'),
    path('list/',UserBooksListAPIView.as_view(),name='user-book-list'),
    path('list-all/',AllBooksListAPIView.as_view(),name='list-all-books'),
    path('update/<int:pk>/',BookUpdateAPIView.as_view(),name='books-update'),
    path('delete/<int:pk>/',BookDeleteAPIView.as_view(),name='book-delete'),
    path('reading-list/create/',ReadingListCreateAPIView.as_view(),name='reading-list-create'),
    path('reading-list/update/<int:pk>/',ReadingListUpdateView.as_view(),name='reading-list-update'),
    path('reading-list/all/',UserReadingListView.as_view(),name='user-related-all-readinglists'),
    path('reading-list/delete/<int:pk>/',UserReadingListDeleteView.as_view(),name='user-related-list-delete'),
    path('reading-list/add-item/<int:reading_list_id>/',AddBookToReadingListView.as_view(),name='reading-list-add-item'),
    path('reading-list/<int:reading_list_id>/books/<int:book_id>/delete/',DeleteBookFromReadingListView.as_view(),name='reading-list-delete')
]
