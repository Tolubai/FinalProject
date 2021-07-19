from django.contrib.auth.models import User
from rest_framework import serializers
from .models import FavoriteNews, NewsImage, News, LawCategory, Law, Question, AdminAnswer, LibraryCategory, FAQ


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsImage
        fields = '__all__'


class NewsShortSerializer(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = 'id title short_description image created_date  is_favourite'.split()

    def get_is_favourite(self, obj):
        if FavoriteNews.objects.filter(news=obj, user=self.context['request'].user):
            return True
        return False

    def get_short_description(self, obj):
        return obj.description[:100]


class NewsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = 'id title description image created_date link images is_favourite'.split()

    def get_is_favourite(self, obj):
        if FavoriteNews.objects.filter(news=obj, user=self.context['request'].user):
            return True
        return False


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = 'id username'.split()


class FavoriteNewsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    news = NewsSerializer()

    class Meta:
        model = FavoriteNews
        fields = 'id user news'.split()


class LawCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LawCategory
        fields = '__all__'


class LawSerializer(serializers.ModelSerializer):
    category = LawCategorySerializer()

    class Meta:
        model = Law
        fields = 'id title description created_date category'.split()


class LawShortSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = Law
        fields = 'id title short_description created_date'.split()

    def get_short_description(self, obj):
        return obj.description[:50]


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = 'id text answers'.split()

    def get_answers(self, obj):
        answers = AdminAnswer.objects.filter(question=obj)
        return AdminAnswerSerializer(answers, many=True).data


class AdminAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAnswer
        fields = 'id text'.split()


class LibraryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCategory
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    category = LibraryCategorySerializer()

    class Meta:
        model = Law
        fields = 'id title description created_date category'.split()


class LibraryShortSerializer(serializers.ModelSerializer):
    short_description = serializers.SerializerMethodField()

    class Meta:
        model = Law
        fields = 'id title short_description created_date'.split()

    def get_short_description(self, obj):
        return obj.description[:50]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'
