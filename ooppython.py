











#Полиморфизм

#  class Mother():

#     def __init__(self):
#         pass
    
#     def __str__(self):
#         return self.get_str()

#     def get_str(self):
#         return 'I am mother'

# class Daughter(Mother):

#     def get_str(self):
#         return 'I am a daugther'
    

# a = Mother()
# print(a)
# d = Daughter()
# print(d)


#Inheritation

# class Shape():
#     def __init__(self, height, width):
#         self.w = width
#         self.h = height


# class Rectangle(Shape):

#     # def __init__(self, height, width):
#     #     super().__init__(height, width)

#     def area(self):
#         print( 0.5*(self.w*self.h))
    

# a = Rectangle(10,5)
# a.area()