'''
Hello world module
'''
def say_hello(name):
    '''
    Function to say hello
    '''
    return name

NAME = input('What is your name?')
print (f"Hello {NAME}")
print(f'Hello {say_hello(NAME)}')
