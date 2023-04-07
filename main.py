
import time

from googletrans import Translator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.add_argument("start-maximized")
options.add_argument("disable-extensions")
options.add_experimental_option("detach", True)
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

options = webdriver.ChromeOptions()


driver.get("https://www.classcentral.com")

transolator  = Translator()





arr = driver.execute_script(r"""
        return (()=>{
             var array = [];

            var elements = document.getElementsByTagName("*");

            for(var i = 0; i < elements.length; i++) {
               var current = elements[i];

                if(current.children.length === 0  && current.textContent.replace(/ |\n/g,'') !== '') {
                   // check the element has no children && that it is not empty
                   array.push(current);
                }
            } 
            return array
        })()
        """)

for x in arr:

    st = " ".join(x.text.split())

    if st != None and st != "":
        translated_text = transolator.translate(text=st, dest='hi').text
        st = "arguments[0].innerText = '" + translated_text + "';"
        inner_text = driver.execute_script(st, x)

arr = driver.execute_script(r"""
        return (()=>{

  var array = [];
           elements =   document.querySelectorAll("nav span");

for(var i = 0; i < elements.length; i++) {
               var current = elements[i];

                if(current.children.length === 0  && current.textContent.replace(/ |\n/g,'') !== '') {
                   // check the element has no children && that it is not empty
                   array.push(current);
                }
            }
            return array 
        })()
        """)

for x in arr:
    st = x.text

    translated_text = transolator.translate(text=st, dest='hi').text
    st = "arguments[0].innerText = '" + translated_text + "';"
    inner_text = driver.execute_script(st, x)






