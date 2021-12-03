import names
import random


def name_generator():
    return names.get_full_name()


def name_generator_firstname():
    return names.get_first_name()


def name_generator_female():
    return names.get_full_name(gender='female')


def name_generator_firstname_female():
    return names.get_first_name(gender="female")


def name_generator_male():
    return names.get_full_name(gender="male")


def name_generator_firstname_male():
    return names.get_first_name(gender="male")


def choice_function(number):
    if number == 1:
        my_funclist = [name_generator, name_generator_firstname]
        nickname = random.choice(my_funclist)()

    if number == 2:
        my_funclist = [name_generator_female, name_generator_firstname_female]
        nickname = random.choice(my_funclist)()

    if number == 3:
        my_funclist = [name_generator_male, name_generator_firstname_male]
        nickname = random.choice(my_funclist)()

    return nickname





