#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# URL : http://localhost:8080/cgi-bin/bmi_web.py
"""
# 모듈 로딩 ---------------------------------------------------
import cgi, sys, codecs, os
from pydoc import html

# WEB 인코딩 설정 ---------------------------------------------
#sys.stdout=codecs.getwriter('utf-8')(sys.stdout.detach())

# 함수 선언 --------------------------------------------------
# WEB 페이지 출력 --------------------------------------------
def displayWEB(result=""):
    #print("Content-Type: text/html; charset=utf-8")
    print("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>비만 여부 판별</title>
    </head>
    <body align="center">
    <h2>[ 비만 상태 체크 ]</h2>
    <form>
        <div style='text-align:center; background-color:#D5D5D5;border-radius:10px;width:60%; margin: auto;padding:50px;'>
            <input id="height" type="text" placeholder="키" name="height"> &nbsp&nbsp
            <input id="weight" type="text" placeholder="몸무게" name="weight">
            <input type="submit" value="판정"></br>
            <p><font color='blue'>{}</font></p>
        </div>
    </form></body></html>""".format(result))

# 판정 --------------------------------------------------------
def detect_bmi(w, h):
    w = int(w)
    h = int(h)
    h = h / 100
    re = w / h**2
    
    if re < 18.5: return "thin"
    elif re < 23: return "normal"
    elif re < 25: return "smallfat"
    else: return "fat"
    

# 기능 구현 -----------------------------------------------------
# (1) WEB 페이지 <Form> -> <INPUT> 리스트 가져오기
form = cgi.FieldStorage()
height_value = form.getvalue('height')
weight_value = form.getvalue('weight')

# (2) 판정 하기
if height_value is not None and weight_value is not None:
    bmi_dic = {"fat": "비만", "smallfat": "과체중", "normal": "정상체중", "thin": "저체중"}
    result = detect_bmi(weight_value, height_value)
    result = '키 {}, 몸무게 {} => {}입니다.'.format(height_value, weight_value, bmi_dic[result])
else:
    result ='측정된 결과가 없습니다.'

# (3) WEB 출력하기
displayWEB(result)
