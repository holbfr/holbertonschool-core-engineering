#!/usr/bin/env python3


from safe_print_list_integers import safe_print_list_integers

mylist = [1, 2, 3, 4]
x = len(mylist)
safe_print_list_integers(mylist, x)
print("----------------------------")
print()


mylist = [1, 2, 3, 4]
x = len(mylist) - 2
safe_print_list_integers(mylist, x)
print("----------------------------")
print()


my_list = [1, 2, 3, 4]
x = 0
safe_print_list_integers(mylist, x)
print("----------------------------")
print()



my_list = []
x = 0
safe_print_list_integers(mylist, x)
print("----------------------------")
print()



mylist = [1, 2, 3, 4]
x = len(mylist) + 4
safe_print_list_integers(mylist, x)
print("----------------------------")
print()



mylist = [1, 2, "H", 3, 4]
x = len(mylist)
safe_print_list_integers(mylist, x)
print("----------------------------")
print()



mylist = [1, 2, 3, "H", 4]
x = len(mylist) - 2
safe_print_list_integers(mylist, x)
print("----------------------------")
print()



mylist = ["Holberton", 1, 2, "H", 3, 4, [1, 2, 3,4]]
x = len(mylist)
safe_print_list_integers(mylist, x)
print("----------------------------")
print()


print("----------------------------")
print("----------------------------")


my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
