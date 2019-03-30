from django.contrib import admin
from .models.author import Author
from .models.publisher import Publisher
from .models.book import Book
from .models.series import Series
from .models.series_book import SeriesBook
from subject.models import Subject, SubjectTag
from category.models import Category, CategoryTag


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(SeriesBook)
class SeriesBookAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoryTag)
class CategoryTagAdmin(admin.ModelAdmin):
    pass


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass


@admin.register(SubjectTag)
class SubjectTagAdmin(admin.ModelAdmin):
    pass
