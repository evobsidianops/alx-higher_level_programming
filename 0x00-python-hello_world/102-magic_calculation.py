import dis

def magic_calculation(a, b):
    return 98, a**b, a+b

dis.dis(magic_calculation)
