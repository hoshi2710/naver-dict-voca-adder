# bot.py
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import os
import time

dir = os.path.dirname(__file__)
driver = webdriver.Chrome(dir+"/chromedriver")

def login(): #로그인
    id = input("아이디 : ") #아이디 입력
    pw = input("패스워드 : ") #패스워드 입력
    driver.get("https://nid.naver.com/nidlogin.login") #로그인 창 로그인
    driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'") #아이디 필드에 입력
    driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'") #패스워드 필드에 입력
    login_btn = driver.find_element_by_css_selector('input[title="로그인"]') 
    login_btn.click() #로그인 버튼 클릭
    time.sleep(2)
 
    

def find_and_add_voca(word, voca_name): #단어를 찾아 단어장에 추가하는 함수 (검색할 단어, 저장할 단어장 이름)
    driver.get("https://en.dict.naver.com/#/search?range=all&query="+word) #단어 검색
    driver.implicitly_wait(2)
    open_tab = driver.find_elements_by_class_name("unit_add_wordbook")[0] #단어장에 저장 탭 열기
    open_tab.click()
    time.sleep(1)
    i=0
    voca_element = driver.find_elements_by_css_selector(".folder_label .name")[0]   #단어장 검색 준비
    while(voca_element.text != voca_name): #저장할 단어장 검색
        i += 1
        voca_element = driver.find_elements_by_css_selector(".folder_label .name")[i]
    voca_element.click()
    save_btn = "click_event = new CustomEvent('click'); document.querySelector('._btn_common_default_add').dispatchEvent(click_event);"
    driver.execute_script(save_btn) #저장 버튼 클릭
    time.sleep(1)

login()
voca_list = "".join(open("voca.txt","r")).split('\n') #단어가 적힌 텍스트 파일 목록을 불러옴
voca_save_list = input("저장할 단어장 명을 입력하세요 : ") #저장할 단어장 명 입력
input("voca.txt 파일에 있는 단어가 저장되오니 파일을 열어 저장할 단어들을 엔터키를 눌러 구별해 적어주기 바랍니다.\n모두 적었다면 엔터키를 누르면 시작됩니다.")
print("====== 추 가 중 . . . ======")
i=1
for voca in voca_list: #단어 추가 작업 시작
    find_and_add_voca(voca,voca_save_list) #단어를 추가하도록 함수에 요청
    print("추가완료 : " + voca + "["+str(i)+"/"+ str(len(voca_list))+"]") #진행률 표시
    i += 1
print("============================")
print("완료 되었습니다!")
