from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
import time
import keyboard
import os
from termcolor import cprint
#def start(url):




def fun(urls,dir_name,keywords_of_ss):
    k=1    
    for elem in keywords_of_ss:
        for element in urls:
            if(elem in element):
                name_of_ss=k  ############################### COMPLETE THIS
                driver=webdriver.Chrome(executable_path=r"D:\Dhanbad\chromedriver.exe")
                time.sleep(2)
                #if(keyboard.is_pressed('q')):
                #   break
                try:
                    driver.get(element)
                    driver.maximize_window()
                    #print(os.getcwd(),"%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                    driver.save_screenshot(os.getcwd() + "\\Screen-Shots\\" + str(name_of_ss) + "_ss.png")
                    driver.close()
                except:
                    driver.close()
                k+=1

def get(url,lst,depth,tag,attribute,c,name_file,k,l,keywords_of_ss):
    print(c)
    strngs=[]
    if( (lst==[] or lst == None) and k==1):
        f=open(f"./{name_file}/{name_file}_{k}.txt","w")
        driver=webdriver.Chrome(executable_path=r"D:\Dhanbad\chromedriver.exe")
        driver.get(url)
        elem = driver.find_elements_by_tag_name(tag)
        for lnk in elem:
            if(lnk.get_attribute(attribute) != None and lnk.get_attribute(attribute)  != ""):
                if(lnk.get_attribute(attribute) not in lst):
                        if(l):
                            f.write(lnk.get_attribute(attribute)+"\n")
                        lst.append(lnk.get_attribute(attribute))
        f.close()
        driver.close()
        if(tag=="a" and keywords_of_ss  != None and keywords_of_ss != ""):
            fun(lst,c,keywords_of_ss)
        return(lst)
    elif(k<=depth):
        k+=1
        for element in lst:
            f=open(f"./{file_name}/{file_name}_{k}.txt","w")
            driver=webdriver.Chrome(executable_path=r"D:\Dhanbad\chromedriver.exe")
            driver.get(element)
            elem = driver.find_elements_by_tag_name(tag)
            for lnk in elem:
                if(lnk.get_attribut(attribute) not in lst):
                    if(l):
                        f.write(lnk.get_attribute(attribute)+"\n")
                    lst.append(lnk.get_attribute(attribute))
            driver.close()
        if(tag=="a" and keywords_of_ss  != None and keywords_of_ss != ""):
            fun(lst,c,keywords_of_ss)
            f.close()
            return(lst)
