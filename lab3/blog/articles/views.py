from django.shortcuts import render
from .models import Article  # Импортируем модель Article

# Представление для отображения архива всех статей
def archive(request):
    # Получаем все статьи из базы данных
    # Article.objects.all() - Django ORM запрос, возвращающий все объекты Article
    posts = Article.objects.all()
    
    # Рендерим шаблон archive.html, передавая статьи в контексте
    # Контекст - это словарь данных, которые будут доступны в шаблоне
    return render(request, 'archive.html', {"posts": posts})
