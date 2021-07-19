from django.contrib import admin

from .models import NewsImage, News, Law, LawCategory, Question, AdminAnswer, LibraryCategory, Library, FAQ


class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 0


class NewsAdmin(admin.ModelAdmin):
    inlines = [
        NewsImageInline
    ]


admin.site.register(News, NewsAdmin)

admin.site.register(Law)
admin.site.register(LawCategory)
admin.site.register(Question)
admin.site.register(AdminAnswer)
admin.site.register(LibraryCategory)
admin.site.register(Library)
admin.site.register(FAQ)