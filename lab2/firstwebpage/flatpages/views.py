from django.http import HttpResponse
from django.shortcuts import render

# Представление для главной страницы с использованием шаблона
def home(request):
    # Возвращаем шаблон index.html
    return render(request, 'index.html')

# Представление для страницы /hello/ с использованием шаблона static_handler.html
def hello(request):
    # Возвращаем шаблон static_handler.html с подключенным CSS
    return render(request, 'static_handler.html')
