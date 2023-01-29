
def about(name, age, likes):
    sentence = 'Meet {}! They are {} years old and they like {}.'.format(name, age, likes)
    return sentence

dictionary = {
    'age': 23,
    'name': 'Evelyn',
    'likes': 'Python'
}

# print(about(**dictionary))

def foo (**kwargs):
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))

foo(huda = 'Female', ziyad = 'Male', john = 'male')