a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
my_list = [a,b,c]

def my_func(a,b,c):
    b_1 = max(my_list)
    my_list.remove(b_1)
    b_2 = max(my_list)
    print(b_1*b_2)
    print(b_1)
    print(b_2)

my_func(a,b,c)