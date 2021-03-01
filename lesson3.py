# 1 создать класс Human(имя и возраст)
# и два класса Prince и Cinderella которые наследуются от Human
# у принца должен быть размер туфельки и  метод который принимает лист золушек и выводит какой золушки подошла туфелька

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    def __init__(self, name, age, size):
        super(Cinderella, self).__init__(name, age)
        self.size = size

    def __str__(self):
        return f"{self.name} -- {self.age} -- {self.size}"


class Prince(Human):
    def __init__(self, name, age, size):
        super(Prince, self).__init__(name, age)
        self.size = size

    def find_cinderella(self, candidates):
        for candidate in candidates:
            if self.size == candidate.size:
                print(candidate.__dict__)
                return candidate.__dict__


candidates = [Cinderella("olena", 23, 37), Cinderella("Nadia", 19, 39), Cinderella("Olia", 19, 35)]
prince = Prince("Ivan", 24, 35)
prince.find_cinderella(candidates)


######################################################################################


# 2 Создать класс Rectangle:
# -конструктор принимает две стороны x,y
# -описать арифметические методы:
#   + сума площадей двух экземпляров класса
#   - разница площадей
#   == или площади равны
#   != не равны
#   >, < меньше или больше
#   при вызове метода len() подсчитывать сумму сторон

class Rectangle:
    def __init__(self, abscissa, ordinate):
        self.ordinate = ordinate
        self.abscissa = abscissa

    def area(self):
        return self.ordinate * self.abscissa

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False

    def __ne__(self, other):
        if self.area() != other.area():
            return True
        return False

    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        return False

    def __len__(self):
        return (self.ordinate + self.abscissa) * 2


a1 = Rectangle(50, 2)
a2 = Rectangle(10, 2)
print(a1 > a2)
print(len(a1))


######################################################################################



x1 = lambda x: sorted([int(i) for i in x.split(" ")])
print(x1("1 16 2 45 4"))
