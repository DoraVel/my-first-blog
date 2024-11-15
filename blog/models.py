from django.conf import settings    #открывают доступ к коду из других файлов. Так что вместо того, 
from django.db import models        #чтобы копировать и вставлять один и тот же код во все файлы, 
from django.utils import timezone   #ты можешь сослаться на него при помощи from ... import ...


class Post(models.Model):         #эта строка определяет нашу модель (объект) class — это специальное ключевое слово для определения объектов.Post — это имя нашей модели, мы можем поменять его при желании (специальные знаки и пробелы использовать нельзя). Всегда начинай имена классов с прописной буквы.models.Model означает, что объект Post является моделью Django, так Django поймет, что он должен сохранить его в базу данных
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title