from ttime_handlers import seconds
from Figures.circle.code import circle_perimeter, circle_area
from Figures.square.code import square_perimeter, square_area
from Figures.triangle.code import triangle_perimeter, triangle_area
print("TASK_1")
print(seconds(4252))

print("TASK_2")
def number(x):
    num_first = (x % 10**3) // 10**(3-1)
    num_second = (x % 10 ** 2) // 10
    if num_second == 0:
        pass
    num_third = x % 10
    overall = num_third + num_second + num_first
    return overall

print(number(108))


print("TASK_3")
print("circle perimeter:", circle_perimeter(), "circle area:", circle_area())
print("square perimeter:", square_perimeter(), "square area:",  square_area())
print("triangle perimeter:", triangle_perimeter(), "triangle area:", triangle_area())



print('TASK_4')
print("TASK_4.1")
# reversed sequence 8kyu:
def reverse_seq(n):
    return [i for i in range(n, 0, -1)]
print(reverse_seq(5))

print("TASK_4.2")
# Grasshopers: create the rooms
# You are creating an "Escape the room" game.
# The first step is to create a hash table called rooms that contains all of the rooms of the game.
# There should be at least 3 rooms inside it, each being a hash table with at least three properties (e.g. name, description, completed).
rooms = {'room_1': {'name':  'room_1', 'description': 'amazing', 'completed': 'idkwhattowritehere'},
         'room_2': {'name': 'room_2', 'description': 'blue', 'completed': 'idkwhattowriteheretoo'},
         'room_3': {'name': 'room_3', 'description': 'fresh', 'completed': 'idkwhattowritehereagain'},
         }
print(rooms)

print("TASK_4.3")
# The growth of population (7kyu)
def nb_year(p0, percent, aug, p):
        one_year_result = p0 + p0 * percent // 100 + aug
        st = one_year_result - p0  # общий прирост населения за первый год
        next = st + 1
        total = 0
        year_counter = 1  # прирост на 70 человек в первый год
        lst = [one_year_result]
        while total < p:
            total = one_year_result + next
            one_year_result = total
            next += 1
            lst.append(total)
            year_counter += 1
        print("The town needs", year_counter, "years to  see its population greater or equal to", p, ":")
        print(lst)
        return year_counter


print(nb_year(1000, 2, 50, 1500))




print("TASK_4.3")
# The growth of population (7kyu)
def nb_year(p0, percent, aug, p):
    one_year_result = p0 + p0 * percent // 100 + aug
    st = one_year_result - p0  # общий прирост населения за первый год
    total = 0
    year_counter = 1  # прирост на 70 человек в первый год
    lst = [one_year_result]
    while total < p:
        p0 = one_year_result
        one_year_result = p0 + p0 * percent // 100 + aug
        year_counter += 1
        total = one_year_result
        lst.append(one_year_result)

    print("The town needs", year_counter, "years to  see its population greater or equal to", p, ":")
    print(lst)
    return year_counter


print(nb_year(1000, 2, 50, 1200))



