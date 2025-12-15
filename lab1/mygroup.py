# Список студентов с именем, фамилией, списком экзаменов и оценками
groupmates = [
    {
        "name": "Андрей",
        "surname": "Карпов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Кузнецова",
        "exams": ["Математика", "Физика", "Химия"],
        "marks": [3, 4, 4]
    },
    {
        "name": "Дмитрий",
        "surname": "Соколов",
        "exams": ["Биология", "География", "Литература"],
        "marks": [5, 4, 5]
    }
]

def print_students(students):
    """
    Функция выводит список студентов в виде таблицы.
    Используется выравнивание через ljust для читаемости.
    """
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(30), u"Оценки".ljust(20))
    for student in students:
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20)
        )

def filter_students_by_average(threshold):
    """
    Фильтрует студентов по среднему баллу, выше заданного порога.
    Средний балл вычисляется как сумма оценок, делённая на их количество.
    """
    filtered = []
    for student in groupmates:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > threshold:
            filtered.append(student)
    return filtered

# Основной блок программы
if __name__ == "__main__":
    # Запрашиваем у пользователя порог среднего балла
    try:
        threshold = float(input("Введите порог среднего балла: "))
        filtered_group = filter_students_by_average(threshold)
        print("\nСтуденты со средним баллом выше", threshold, ":")
        print_students(filtered_group)
    except ValueError:
        print("Ошибка: введите корректное число.")