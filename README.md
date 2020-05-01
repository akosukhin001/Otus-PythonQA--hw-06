# Домашнее задание 06 - Реализуем ООП на практике

## Цель: Научиться работать с парадигмой ООП, потренировать объектное мышение, поучиться писать тесты.

### Создать класс геометрической фигуры.
### Реализовать на его основе классы фигур Треугольник, Прямоугольник, Квадрат, Круг.

1 Часть.
```
Фигура должна иметь атрибуты:
name - название фигуры,
area - выводить площадь,
angles - выводить количество углов
perimeter - выводить периметр (сумму длин сторон, длину окружности)

Фигура должна реализовать метод add_square() который должен принимать другую фигуру и выводить сумму площадей этих фигур. 
Если передана не геометрическая фигура, то нужно выдавать ошибку и сообщать что передан неправильный класс.
```

2. Часть.
```
Написать тесты с использованием pytest на эти классы.
По одному тесту на каждый метод каждой фигуры. 
Т.е. будет четыре тестовых модуля по 5 тестов на каждый. 
Можно написать и больше. :)

Задача: Потренировать объектно-ориентированное мышление, и написание тестов на собственный код.
Критерии оценки: Будет оцениваться глубина использования парадигмы ООП. 
Встроенные декораторы, наследование, отсутствие дублирования кода. 
Если какой-то метод выполняет одно и тоже во всех классах наследниках, то он должен принадлежать родительскому классу.
```
