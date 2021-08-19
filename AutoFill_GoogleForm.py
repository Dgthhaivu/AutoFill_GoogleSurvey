from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("--start-maximized")
option.add_experimental_option('excludeSwitches', ['enable-logging'])
option.add_argument("disable-infobars")
option.add_argument("--disable-extensions")
option.add_argument('--headless')
# option.add_argument('--no-sandbox')
# option.add_argument('--disable-dev-shm-usage')
#option.add_argument("disable-gpu")

chromedriver = "C:/Users/Dgthhaivu/Downloads/chromedriver_win32/chromedriver.exe"
link = 'https://docs.google.com/forms/d/e/1FAIpQLSeF7cQlj93ktBAiEw2yN_He1H9Ah16pl7BTOVkEXCLxb2nT5w/viewform'

browser = webdriver.Chrome(executable_path=chromedriver, options=option)
browser.get(link)

count = 0

while(count < 300):
    #page 1
    radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    next=browser.find_element_by_class_name("appsMaterialWizButtonPaperbuttonContent")
    radio_buttons[0].click()
    next.click()

    #page 2
    radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    radio_buttons[0].click()
    next.click()

    #page 3
    radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    radio_buttons[0].click()
    next.click()

    #page 4
    radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    radio_buttons[0].click()
    next.click()

    #page 5
    radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    radio_buttons[0].click()
    next.click()

    # ---------------------------------------------------------------------------------------------------------

    #page 6 _ section 2
    button_range_Q1 = random.randint(0,5)

    button_range_Q2a = random.randint(9,12)
    button_range_Q2b = random.randint(14,17)
    button_range_Q2c = random.randint(24,26)
    button_range_Q2d = random.randint(31,33)
    button_range_Q2e = random.randint(35,39)
    button_range_Q2f = random.randint(42,46)

    button_range_Q3a = random.randint(3,4) #chay 1 so cai 5
    button_range_Q3b = random.randint(6,8)
    button_range_Q3c = random.randint(12,14)
    button_range_Q3d = random.randint(18,19)
    button_range_Q3e = random.randint(24,26)
    button_range_Q3f = random.randint(30,32)

    button_range_Q4 = random.randint(0,4)
    button_range_Q5 = random.randint(0,5)
    button_range_Q6 = random.randint(0,5)

    #Q1_a->d
    radio_buttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    radio_buttons[button_range_Q1].click()
    #Q2
    radio_buttons[button_range_Q2a].click()
    radio_buttons[button_range_Q2b].click()
    radio_buttons[button_range_Q2c].click()
    radio_buttons[button_range_Q2d].click()
    radio_buttons[button_range_Q2e].click()
    radio_buttons[button_range_Q2f].click()

    #Q3 
    question3 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]')
    buttonQuestion3 = question3.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion3[button_range_Q3a].click()
    buttonQuestion3[button_range_Q3b].click()
    buttonQuestion3[button_range_Q3c].click()
    buttonQuestion3[button_range_Q3d].click()
    buttonQuestion3[button_range_Q3e].click()
    buttonQuestion3[button_range_Q3f].click()

    #Q4-Q5-Q6
    question4 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]')
    buttonQuestion4 = question4.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion4[button_range_Q4].click()

    question5 = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]')
    buttonQuestion5 = question5.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion5[button_range_Q5].click()

    question6 = browser.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]')
    buttonQuestion6 = question6.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion6[button_range_Q6].click()

    #next
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    next.click()

    # ---------------------------------------------------------------------------------------------------------
    # page 7 _ section 3
    button_range_Q7a = random.randint(0,2)
    button_range_Q7b = random.randint(5,7)
    button_range_Q7c = random.randint(10,11)
    button_range_Q7d = random.randint(15,19)
    button_range_Q7e = random.randint(20,21)

    button_range_Q8a = random.randint(2,4)
    button_range_Q8b = random.randint(8,9)
    button_range_Q8c = random.randint(10,11)
    button_range_Q8d = random.randint(15,16)
    button_range_Q8e = random.randint(20,22)

    button_range_Q9a = random.randint(0,1)
    button_range_Q9b = random.randint(6,8)
    button_range_Q9c = random.randint(10,11)
    button_range_Q9d = random.randint(15,16)

    button_range_Q10a = random.randint(0,1)
    button_range_Q10b = random.randint(5,6)
    button_range_Q10c = random.randint(10,12)
    button_range_Q10d = random.randint(15,17)

    button_range_Q11a = random.randint(0,2)
    button_range_Q11b = random.randint(5,6)
    button_range_Q11c = random.randint(10,12)
    button_range_Q11d = random.randint(15,17)
    button_range_Q11e = random.randint(20,22)

    question7 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]')
    buttonQuestion7 = question7.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion7[button_range_Q7a].click()
    buttonQuestion7[button_range_Q7b].click()
    buttonQuestion7[button_range_Q7c].click()
    buttonQuestion7[button_range_Q7d].click()
    buttonQuestion7[21].click()

    question8 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]')
    buttonQuestion8 = question8.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion8[button_range_Q8a].click()
    buttonQuestion8[button_range_Q8b].click()
    buttonQuestion8[button_range_Q8c].click()
    buttonQuestion8[button_range_Q8d].click()
    buttonQuestion8[button_range_Q8e].click()

    question9 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]')
    buttonQuestion9 = question9.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion9[button_range_Q9a].click()
    buttonQuestion9[button_range_Q9b].click()
    buttonQuestion9[button_range_Q9c].click()
    buttonQuestion9[button_range_Q9d].click()


    question10 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]')
    buttonQuestion10 = question10.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion10[button_range_Q10a].click()
    buttonQuestion10[button_range_Q10b].click()
    buttonQuestion10[button_range_Q10c].click()
    buttonQuestion10[button_range_Q10d].click()

    question11 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]')
    buttonQuestion11 = question11.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion11[button_range_Q11a].click()
    buttonQuestion11[button_range_Q11b].click()
    buttonQuestion11[button_range_Q11c].click()
    buttonQuestion11[button_range_Q11d].click()
    buttonQuestion11[button_range_Q11e].click()

    #next
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    next.click()

    # ---------------------------------------------------------------------------------------------------------
    # page 8 _ section 4

    button_range_Q13 = random.randint(0,4)

    button_range_Q14a = random.randint(0,1)
    button_range_Q14b = random.randint(5,7)
    button_range_Q14c = random.randint(10,12)
    button_range_Q14d = random.randint(16,18)
    button_range_Q14e = random.randint(20,22)
    button_range_Q14f = random.randint(25,26)
    button_range_Q14g = random.randint(30,31)
    button_range_Q14h = random.randint(37,39)
    button_range_Q14i = random.randint(40,42)
    button_range_Q14j = random.randint(45,46)
    button_range_Q14k = random.randint(52,54)
    button_range_Q14l = random.randint(55,57)
    button_range_Q14m = random.randint(61,62)
    button_range_Q14n = random.randint(65,67)
    button_range_Q14o = random.randint(70,72)
    button_range_Q14p = random.randint(75,76)
    button_range_Q14q = random.randint(80,81)
    button_range_Q14r = random.randint(85,86)
    button_range_Q14s = random.randint(90,91)

    button_range_Q15a = random.randint(0,1)
    button_range_Q15b = random.randint(5,6)
    button_range_Q15c = random.randint(10,12)
    button_range_Q15d = random.randint(15,19)

    #100 no - 300 yes
    question12 = browser.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div')
    question12.click()

    question13 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]')
    buttonQuestion13 = question13.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion13[button_range_Q13].click()

    question14 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]')
    buttonQuestion14 = question14.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion14[button_range_Q14a].click()
    buttonQuestion14[button_range_Q14b].click()
    buttonQuestion14[button_range_Q14c].click()
    buttonQuestion14[button_range_Q14d].click()
    buttonQuestion14[button_range_Q14e].click()
    buttonQuestion14[button_range_Q14f].click()
    buttonQuestion14[button_range_Q14g].click()
    buttonQuestion14[button_range_Q14h].click()
    buttonQuestion14[button_range_Q14i].click()
    buttonQuestion14[button_range_Q14j].click()
    buttonQuestion14[button_range_Q14k].click()
    buttonQuestion14[button_range_Q14l].click()
    buttonQuestion14[button_range_Q14m].click()
    buttonQuestion14[button_range_Q14n].click()
    buttonQuestion14[button_range_Q14o].click()
    buttonQuestion14[button_range_Q14p].click()
    buttonQuestion14[button_range_Q14q].click()
    buttonQuestion14[button_range_Q14r].click()
    buttonQuestion14[button_range_Q14s].click()

    question15 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]')
    buttonQuestion15 = question15.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion15[button_range_Q15a].click()
    buttonQuestion15[button_range_Q15b].click()
    buttonQuestion15[button_range_Q15c].click()
    buttonQuestion15[button_range_Q15d].click()

    #next
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    next.click()

    # ---------------------------------------------------------------------------------------------------------
    # page 9 _ section 5
    button_range_Q16 = random.randint(0,1)
    button_range_Q17 = random.randint(0,1)
    button_range_Q18 = random.randint(0,3)
    button_range_Q19 = random.randint(0,5)
    button_range_Q20 = random.randint(1,4)

    question16 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]')
    buttonQuestion16 = question16.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion16[button_range_Q16].click()

    question17 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]')
    buttonQuestion17 = question17.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion17[button_range_Q17].click()

    question18 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]')
    buttonQuestion18 = question18.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion18[button_range_Q18].click()

    question19 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]')
    buttonQuestion19 = question19.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion19[button_range_Q19].click()

    question20 = browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]')
    buttonQuestion20 = question20.find_elements(By.CLASS_NAME, 'appsMaterialWizToggleRadiogroupOffRadio')
    buttonQuestion20[button_range_Q20].click()

    #next
    next=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    next.click()

    # ---------------------------------------------------------------------------------------------------------
    # page 10 _ submission
    submit=browser.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span')
    submit.click()

    # ---------------------------------------------------------------------------------------------------------
    # page 11 _ confirmation
    get_confirmation_div_text = browser.find_element_by_css_selector('.freebirdFormviewerViewResponseConfirmationMessage')
    if ((get_confirmation_div_text.text) == "Thank you for your response."):
        count = count + 1
        print(count)
        browser.get(link)
browser.quit()
print("Finished !!!")