from django.contrib import admin
from .models import Article  # Импортируем нашу модель Article

# Класс для настройки отображения модели Article в админке
class ArticleAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке статей в админке
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
    # Включение метода get_excerpt в список отображаемых полей

# Регистрируем модель Article в административном интерфейсе
# ArticleAdmin определяет, как модель будет отображаться
admin.site.register(Article, ArticleAdmin)
