from django.contrib.auth.models import User
from django.db import models


def upload_to(instance, filename):
    return '/'.join([filename])


class News(models.Model):
    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    link = models.URLField(null=True, blank=True, verbose_name='ссылка')
    image = models.ImageField(null=True, blank=True, upload_to=upload_to)

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, related_name='images')
    image = models.ImageField(null=True, blank=True, upload_to=upload_to)


class FavoriteNews(models.Model):
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class LawCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Law(models.Model):
    class Meta:
        verbose_name = 'Закон'
        verbose_name_plural = 'Законы'
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(LawCategory, on_delete=models.CASCADE, related_name='category')

    def __str__(self):
        return self.title


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text

    def view_answers(self):
        return AdminAnswer.objects.filter(text=self)


class AdminAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True, related_name='answers')
    text = models.TextField()


class LibraryCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Library(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    category = models.ForeignKey(LibraryCategory, on_delete=models.CASCADE, related_name='lib_category')

    def __str__(self):
        return self.title


class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=255)


class AboutUs(models.Model):
    text = models.TextField()
    images = models.ImageField(null=True, blank=True, upload_to=upload_to)

