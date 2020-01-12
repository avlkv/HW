from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
        id_book = models.AutoField(primary_key=True)
        name_book = models.CharField(max_length=100, verbose_name='Название книги')
        genre_book = models.CharField(max_length=50, default='Жанр неизвестен', verbose_name='Жанр')
        photo = models.ImageField(null=True, blank=True, default='no-image.png', verbose_name='Фото')
        writer_book = models.CharField(max_length=100, verbose_name='Автор')
        year_book = models.IntegerField(verbose_name='Год создания')
        users = models.ManyToManyField(User, through='Issuance', through_fields=('book_name', 'username'))
        # reviews = models.ForeignKey(Issuance,on_delete=models.CASCADE)
        def str(self):
            return '%s, %s' % (str(self.id_book), str(self.name_book))

        def get_users(self):
            return [{'name': user.username} for user in self.users.all()]

        class Meta:
            verbose_name_plural = "Книги"
            verbose_name = "Название книги"

class Issuance(models.Model):
    book_name = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Название книги')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=255, default = 'null', verbose_name='Отзыв')
    def str(self):
        return 'username:%s,  book_name:%s', 'review:%s' % (str(self.username.username), str(self.book_name.name_book), str(self.review))
    # def get_reviews(book):
    #     return Issuance.objects.filter(book_name_id = Book.id_book)
    class Meta:
        verbose_name_plural = "Отзывы"
        verbose_name = "Название книги"
        verbose_name = "Отзыв"


