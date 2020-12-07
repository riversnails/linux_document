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
    
    # 서식 지정자
    print("age = %s" %age)
    print("ABC", 12345, "GOOD")
    print("age = %s, name = %s" %(age, name))
    
    # 구분자. 종료문자
    print(100, 'age')
    print("aa", 123, end="\t")
    
    # 전역 사용법
    global code
    print("code =", code)
    code+=1
    print("code =", code)
    
    # 키보드
    value = input('What you are name?')
    print("value =", value, type(name))
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

