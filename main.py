from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe")


#driver.get("https://www.dmcc.ae/business-search?directory=1&submissionGuid=9c0954d2-8d9c-4f94-a10a-276e858db841")
driver.get("https://dmcc.secure.force.com/Business_directory_Page?initialWidth=987&childId=pym-0&parentTitle=List%20of%20Companies%20Registered%20in%20Dubai%2C%20DMCC%20Free%20Zone&parentUrl=https%3A%2F%2Fwww.dmcc.ae%2Fbusiness-search%3Fdirectory%3D1%26submissionGuid%3D9c0954d2-8d9c-4f94-a10a-276e858db841")
time.sleep(10) # waiting 10sec for iframe to load
print(time)
#print(driver.find_element(By.XPATH("//a"))  )
try:
    print(driver.find_element_by_xpath("//*[@id='directory_list']/div/div[1]/div/div[1]/h4").get_attribute("innerHTML"))
    print(driver.find_element_by_xpath("//*[@id='directory_list']/div/div[2]/div/div[1]/h4").get_attribute("innerHTML"))
    print(driver.find_element_by_xpath('//*[@id="directory_list"]/div/div[3]/div/div[1]/h4').get_attribute("innerHTML"))

    print(driver.find_element_by_xpath('//*[@id="directory_list"]/div/div[6]/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute("innerHTML"))

except:
    print("fail")

#print(driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[1]/div/div[1]/h4").get_attribute("innerHTML"))
#print(driver.find_element_by_xpath("/html/body/div/section[1]/div[1]/div/div[1]/div/div/h2/span").get_attribute("innerHTML"))
#   //*[@id="directory_list"]/div/div[1]/div/div[1]/h4
#print(driver.find_element(By.XPATH.startswith('https://www.dmcc.ae/')))
#/iframe[starts-with(@src,'https://www.dmcc.ae/')]