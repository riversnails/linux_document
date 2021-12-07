import RPi.Gpio

code = 1000

def main(args):
    # 리스트저장
    data=['abc', 10, 12.34]
    data2=[]
    
    # 리스트 출력
    print("data[0]={}, data[1]={}, data[2]={}".format(data[0],data[1],data[2]))
    
    # 데이터 추가 & 출력
    data2.append("Good")
    data2.append(12.345)
    print("data2[0]={}, data2[1]={}".format(data2[0],data2[1]))
    
    # 데이터 변경
    data2[0]=10004
    print("data2[0]={}, data2[1]={}".format(data2[0],data2[1]))
    
    # 튜플 생성
    tdata=(1,2,3)
    
    # 요소 출력
    print("tdata[0]={}, tdata[2]={}".format(tdata[0],tdata[2]))
    
    #값 변경
    #tdata[0] = 'Good' 불가능 
    print("tdata[0]={}, tdata[2]={}".format(tdata[0],tdata[2]))
    
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))



