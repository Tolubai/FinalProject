from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.response import Response

from .models import News, Law, LawCategory, Question, Library, LibraryCategory, FAQ
from .serializers import NewsSerializer, NewsShortSerializer, LawShortSerializer, LawSerializer, LawCategorySerializer, \
    QuestionSerializer, LibraryShortSerializer, LibraryCategorySerializer, LibrarySerializer, FAQSerializer


class NewsList(ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsShortSerializer


class NewsDetail(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class LawsList(ListCreateAPIView):
    queryset = Law.objects.all()
    serializer_class = LawShortSerializer


class LawsCategoryList(ListCreateAPIView):
    queryset = LawCategory.objects.all()
    serializer_class = LawCategorySerializer


class LawsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Law.objects.all()
    serializer_class = LawSerializer


class QuestionAPIView(ListCreateAPIView):
    serializer_class = QuestionSerializer


class LibraryList(ListCreateAPIView):
    queryset = Library.objects.all()
    serializer_class = LibraryShortSerializer


class LibraryCategoryList(ListCreateAPIView):
    queryset = LibraryCategory.objects.all()
    serializer_class = LibraryCategorySerializer


class LibraryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class FAQ(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
