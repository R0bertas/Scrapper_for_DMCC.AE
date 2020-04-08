from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")  ## can be firefox or any other browser

# driver.get("https://www.dmcc.ae/business-search?directory=1&submissionGuid=9c0954d2-8d9c-4f94-a10a-276e858db841")
driver.get(
    "https://dmcc.secure.force.com/Business_directory_Page?initialWidth=987&childId=pym-0&parentTitle=List%20of%20Companies%20Registered%20in%20Dubai%2C%20DMCC%20Free%20Zone&parentUrl=https%3A%2F%2Fwww.dmcc.ae%2Fbusiness-search%3Fdirectory%3D1%26submissionGuid%3D9c0954d2-8d9c-4f94-a10a-276e858db841")

# creating csv file to upload database
filename = "customerDataDMCC.csv"
# opening file
f = open(filename, "w", encoding='utf-8')

# adding header
#f.write("ID, Name, Phone, Email")  ## THERE IS NO ID , you can create easily in excel
f.write( " Name, Phone, Email")
f.write("\n")
# waiting 10sec for iframe to load
time.sleep(5)
identify=0

def scrapedata(identify):
    time.sleep(1)
    listing=""
    for i in range(1,11):
        identify += 1
        #info = str(identify) +","
        info= " "
        try:
            comp_name = driver.find_element_by_xpath(
                '//*[@id="directory_list"]/div/div[ ' + str(i) + ']/div/div[1]/h4').get_attribute("innerHTML")
            info += comp_name
        except:
            comp_name = " "
            info += comp_name
            print("error1 - NO name " + str(i))
        ## number
        info += ","
        try:
            number = driver.find_element_by_xpath('//*[@id="directory_list"]/div/div[' + str(
                i) + ']/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute("innerHTML")
            info += number
        except:
            number = " "
            info += number
            print("error2 - no phone")
        ## email
        info += ","
        try:
            email = driver.find_element_by_xpath(' // *[ @ id = "directory_list"] / div / div[' + str(
                i) + '] / div / div[2] / div[2] / table / tbody / tr[3] / td[2] / a').get_attribute("innerHTML")
            info += email
        except:
            email = " "
            info += email
            print("error3 - no email")
        info += "\n"
        listing+=info

    print(listing)

    return listing


try:
    ## name   second div changes
    for i in range(20):
        time.sleep(1)
       # print(str(i+1)+ "," + scrapedata())
        f.write(scrapedata(identify))

        driver.find_element_by_xpath("/html/body/div[5]/div/ul/li[13]/a").click()


except:
    print("fail")
    # if exception occurs we close our csv file
    f.close()

f.close()
