from django.db import models
from django.contrib.auth.models import User

# Модель для представления статей в блоге
class Article(models.Model):
    # Поле для заголовка статьи, максимальная длина - 200 символов
    title = models.CharField(max_length=200)
    
    # Связь с моделью User (автор статьи)
    # on_delete=models.CASCADE означает, что при удалении пользователя 
    # все его статьи также будут удалены
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Текст статьи, поле без ограничения длины
    text = models.TextField()
    
    # Дата создания статьи, автоматически устанавливается при создании
    created_date = models.DateField(auto_now_add=True)

    # Метод для строкового представления объекта
    def __str__(self):
        # Возвращает строку в формате "имя_автора: заголовок_статьи"
        return "%s: %s" % (self.author.username, self.title)

    # Метод для получения краткого описания статьи
    def get_excerpt(self):
        # Если текст статьи длиннее 140 символов, возвращаем первые 140 символов с многоточием
        # Иначе возвращаем весь текст
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
