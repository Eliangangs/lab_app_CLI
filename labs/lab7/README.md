# Лабораторна робота 7

Цей скрипт для Streamlit виконує наступні завдання:

**Завдання 1**: Графік Y(x) = 2^x * sin(10x)
Мета: Побудувати графік математичної функції.
Інтерфейс: Користувач натискає кнопку для побудови графіка.
Використовуються: numpy для обчислень, matplotlib для побудови графіка.

**Завдання 2**: Гістограма частоти літер у тексті
Мета: Підрахувати частоту кожної літери в введеному тексті.
Інтерфейс: Користувач вводить текст і натискає кнопку для побудови гістограми.
Використовуються: Counter для підрахунку літер, matplotlib для побудови гістограми.

**Завдання 3**: Гістограма частоти типів речень
Мета: Підрахувати кількість звичайних, питальних і окличних речень у введеному тексті.
Інтерфейс: Користувач вводить текст і натискає кнопку для побудови гістограми.
Використовуються: Регулярні вирази для виділення речень, matplotlib для побудови гістограми.
Основні функції:
task_1_ui(): Будує графік функції Y(x) = 2^x * sin(10x)
task_2_ui(): Створює гістограму частоти літер у введеному тексті.
task_3_ui(): Створює гістограму для підрахунку типів речень у тексті (звичайні, питальні, окличні).
Робота:
Для кожного завдання є окремі UI елементи.
Використовуються бібліотеки: matplotlib для побудови графіків і гістограм, Counter для підрахунку частот, re для обробки тексту.
