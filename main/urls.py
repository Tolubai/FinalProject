from django.urls import path


from .views import NewsList, NewsDetail, LawsCategoryList, LawsList, LawsDetail, QuestionAPIView, LibraryCategoryList, \
    LibraryList, LibraryDetail, FAQ

urlpatterns = [
    path('news/', NewsList.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('lawcategory/', LawsCategoryList.as_view()),
    path('laws/', LawsList.as_view()),
    path('laws/<int:pk>/', LawsDetail.as_view()),
    path('ask_question/', QuestionAPIView.as_view()),
    path('librarycategory/', LibraryCategoryList.as_view()),
    path('library/', LibraryList.as_view()),
    path('library/<int:pk>/', LibraryDetail.as_view()),
    path('faq/', FAQ.as_view())
]
