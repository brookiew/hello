
import skilstak.colors as c 
import time

"""This is my Hello world program.""" 

def print_plain(message): 
    print("Hello World") 

def print_forever(message):
    while True: 
         print("Hello World") 

def print_random_color(message):
    print(c.random() + "Hello World") 

def parse_args():
    from sys import argv
    
    name = "world" 
    option = ""  
    message = "Aloha" + name + "!" 
       
    if len(argv) == 2:
        if argv[1].startswith("-"):
            option = argv[1]
        else:
            name = argv[1]
    elif len(argv) > 2:
        option = argv[1] 
        name = argv[2] 

 


