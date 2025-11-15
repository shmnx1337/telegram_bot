import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
def gen_moneta():
    elements_moneta = ['орел', 'решка']  
    moneta = random.choice(elements_moneta)
    return moneta