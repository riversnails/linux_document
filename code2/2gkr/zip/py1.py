code = 1000

def main(args):
    age=10
    name='Hong'
    job='student'
    msg="""
    Good Luck-!
    """
    
    msg2="""
    Good-----
    -----Good
    """
        
    print("age =", age, type(age), id(age))
    print("name =", name)
    print("job =", job)
    print("msg =", msg)
    print("msg2=", msg2)
    age='A'
    print("arg=", age, ord(age))
    
    print("age = %s" %age)
    print("ABC", 12345, "GOOD")
    print("age = %s, name = %s" %(age, name))
    
    print(100, 'age')
    print("aa", 123)
    
    global code
    print("code =", code)
    code+=1
    print("code =", code)
    
    value = input('What you are name?')
    print("value =", value, type(name))
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

