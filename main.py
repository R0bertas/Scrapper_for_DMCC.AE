from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="C:\Driver\chromedriver.exe") ## can be firefox or any other browser


#driver.get("https://www.dmcc.ae/business-search?directory=1&submissionGuid=9c0954d2-8d9c-4f94-a10a-276e858db841")
driver.get("https://dmcc.secure.force.com/Business_directory_Page?initialWidth=987&childId=pym-0&parentTitle=List%20of%20Companies%20Registered%20in%20Dubai%2C%20DMCC%20Free%20Zone&parentUrl=https%3A%2F%2Fwww.dmcc.ae%2Fbusiness-search%3Fdirectory%3D1%26submissionGuid%3D9c0954d2-8d9c-4f94-a10a-276e858db841")


# creating csv file to upload database
filename = "customerDataDMCC.csv"
# opening file
f = open(filename, "w", encoding='utf-8')

# adding header
f.write("ID, Name, Phone, Email" )
f.write( "\n")
# waiting 10sec for iframe to load
time.sleep(10)

#print(driver.find_element(By.XPATH("//a"))  )
try:
    ## name   second div changes
    for i in range(11):
        comp_name=""
        number=""
        email=""
        try:
           comp_name =driver.find_element_by_xpath('//*[@id="directory_list"]/div/div[ '+ str(i) +']/div/div[1]/h4').get_attribute(  "innerHTML")

        except:
            name = " "
            print("error1 - NO name ")
        ## number
        try:
            number =driver.find_element_by_xpath('//*[@id="directory_list"]/div/div['+ str(i) + ']/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute("innerHTML")
        except:
            number =" "
            print("error2 - no phone")
           ## email
        try:
               email = driver.find_element_by_xpath(' // *[ @ id = "directory_list"] / div / div['+ str(i) + '] / div / div[2] / div[2] / table / tbody / tr[3] / td[2] / a').get_attribute("innerHTML")

        except:
            email =" "
            print("error3 - no email")
        f.write ( str(i) + "," + str(comp_name) + "," +str(number) + ","+ str(email)+ "\n")

except :
    print("fail")
    # if exception occurs we close our csv file
    f.close()



#print(driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/div/div[1]/div/div[1]/h4").get_attribute("innerHTML"))
#print(driver.find_element_by_xpath("/html/body/div/section[1]/div[1]/div/div[1]/div/div/h2/span").get_attribute("innerHTML"))
#   //*[@id="directory_list"]/div/div[1]/div/div[1]/h4
#print(driver.find_element(By.XPATH.startswith('https://www.dmcc.ae/')))
#/iframe[starts-with(@src,'https://www.dmcc.ae/')]