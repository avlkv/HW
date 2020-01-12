from django.contrib import admin
from.models import *
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    fields = ['id_book', 'name_book', 'genre_book', 'writer_book']
    list_filter = ['id_book', 'name_book', 'genre_book', 'writer_book']
    list_display = ['id_book', 'name_book', 'genre_book', 'writer_book']
    search_fields = ['id_book', 'name_book', 'genre_book', 'writer_book']
    list_per_page = 10


class IssuanceAdmin(admin.ModelAdmin):
    fields = ['book_name', 'username', 'review']
    list_filter = ['book_name', 'username']
    list_display = ['book_name', 'username', 'review']
    search_fields = ['book_name', 'username', 'review']
    list_per_page = 10


admin.site.register(Book, BooksAdmin)
admin.site.register(Issuance, IssuanceAdmin)
admin.site.site_url = '/main/'
admin.site.site_header = 'Django Администрация'
admin.site.index_title = 'Администрирование'
