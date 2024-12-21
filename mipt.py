# Decorators


def swap()


def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)


# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
#     print("Я создаю декораторы! И я получил следующие аргументы:",
#            decorator_arg1, decorator_arg2)
#     def my_decorator(func):
#         print("Я - декоратор. И ты всё же смог передать мне эти аргументы:",
#                decorator_arg1, decorator_arg2)
#         # Не перепутайте аргументы декораторов с аргументами функций!
#         def wrapped(function_arg1, function_arg2):
#             print ("Я - обёртка вокруг декорируемой функции.\n"
#                    "И я имею доступ ко всем аргументам\n"
#                    "\t- и декоратора: {0} {1}\n"
#                    "\t- и функции: {2} {3}\n"
#                    "Теперь я могу передать нужные аргументы дальше"
#                    .format(decorator_arg1, decorator_arg2,
#                            function_arg1, function_arg2))
#             return func(function_arg1, function_arg2)
#         return wrapped
#     return my_decorator

# @decorator_maker_with_arguments("Леонард", "Шелдон")
# def decorated_function_with_arguments(function_arg1, function_arg2):
#     print ("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
#            " {1}".format(function_arg1, function_arg2))

# decorated_function_with_arguments("Раджеш", "Говард")


# def even_2(fun):
    
#     def wrapper(*args):
#         result = fun(*args)
#         if result==0:
#             print('Четных нет')
#         if result>10:
#             print('Очень много четных чисел')
#         else:
#             print(result)
#     return wrapper


# @even_2
# def even(n:list):
#     return len([elem for elem in n if not elem%2  ])


# even([1,2,3,3])






# def fib(n):
    
#     if n in (1,2):
#         return 1
#     return fib(n-1) + fib(n-2)

# def decor(fun):
#     def wrapper():
#         print('A wrapper')
#         print(fun(5))

#     return wrapper

# fib_decor = decor(fib)

# fib_decor()





# import sys
# import argparse

# def fib(n):
#     if n in (1,2):
#         return 1
#     return fib(n-1) + fib(n-2)

# def createParser():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('name', nargs='?', default='world')

#     return parser

# if __name__ == '__main__':
#     parser = createParser()
#     namespace = parser.parse_args()

#     print(namespace)

#     if namespace.name:
#         num = namespace.name
#         print(fib(int(num)))


