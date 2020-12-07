code = 1000

def main(args):
    msg=input('Enter message :')
    
    # 문자열 처리
    print("len msg = %s" %len(msg))
    print("msg[0] = %s, msg[-1] = %s" %(msg[0], msg[-1]))
    print("msg[1:3] = %s" %msg[1:3])
    print("msg[1:] = %s" %msg[1:])
    print("msg[:-2] = %s" %msg[:-2])
    
    # 문자열 클래스의 함수
    print("msg.upper() = ", msg.upper())
    print("msg.split() = ", msg.split(' '))
    print("'-'.join('HAPPY')=", '-'.join('HAPPY'))
    
    # 문자열 포맷팅 함수
    print("{}year {}month {}day".format(2020, 10, 28))
    print("{1}year {2}month {0}day".format(2020, 10, 28))
    count = 1
    print("picture_{:02}.jpg".format(count))
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))


