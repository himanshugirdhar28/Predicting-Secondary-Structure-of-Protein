from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as p
import requests as rq
import time

url="https://ebi.ac.uk/pdbe/search/pdb/select?q=all_assembly_type:tetramer&fl=pdb_id&rows=1000"
response=rq.get(url)
data=response.json()
print(data)
data=data['response']
l=[]
for i in data['docs']:
    l.append(i['pdb_id'])
l=set(l)
l=list(l)
options=Options()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
s=Service('v:\\BIGMAE\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.maximize_window()
v=0
x,y=p.size()
x=x/2
y=y/2
for i in l[202:303]:
    driver.get("https://files.rcsb.org/view/"+i+".pdb")
    # WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/pre"))) 
    # mytext = driver.find_element(By.XPATH,"/html/body/pre").text
    # print(mytext)
    time.sleep(1)
    p.click(x,y)
    p.hotkey("ctrlleft","a")
    p.hotkey("ctrlleft","c")
    # /html/body/font/form/font/p[3]/font/b
    driver.get("http://bioinformatica.isa.cnr.it/SUSAN/DSSP-web/")
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/font/form/font/font/font/font/input"))) 
    Protein_name=driver.find_element(By.XPATH,"/html/body/font/form/font/p[1]/input")
    Protein_name.send_keys(i)
    # mytext = driver.find_element(By.XPATH,"/html/body/font/form/font/p[3]/font/b").text
    # mytext = clipboard. paste()
    structure=driver.find_element(By.XPATH,"/html/body/font/form/font/p[2]/textarea")
    structure.click()
    p.hotkey("ctrlleft","v")
    # driver.find_element(By.XPATH,"/html/body/font/form/font/p[2]/textarea").send_keys(mytext)
    # Protein_name=driver.find_element(By.XPATH,"/html/body/font/form/font/p[1]/input")
    # Protein_name.send_keys(i)
    check_box=driver.find_element(By.XPATH,"/html/body/font/form/font/font/input")
    check_box.click()
    send=driver.find_element(By.XPATH,"/html/body/font/form/font/font/font/font/input")
    send.click()
    WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/font/pre")))
    p.click(x,y)
    p.hotkey("ctrlleft","a")
    p.hotkey("ctrlleft","c")
    p.hotkey("altleft","tab")
    time.sleep(2)
    # if(v==0):
    #     p.click(100,200)
    p.hotkey("ctrlleft","v")
    p.hotkey("altleft","tab")
