from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#오늘 날짜가 며칠인지 점검하는 함수
def get_today():
    today = time.strftime('%Y.%m.%d', time.localtime(time.time()))
    return today[-2:]

def get_keywords():
    #오늘 날짜를 우선 점검함 : 01, 11 , 21일때만 상품리스트를 가져오게
    if get_today() == '1' or get_today() == '11' or get_today() == '21':
    #창 열기 쇼핑인사이트
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = chrome_options )
        driver.get(url = 'https://datalab.naver.com/shoppingInsight/sCategory.naver')
    #카테고리 = 디지털가전
        category = '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/ul/li[4]/a'
        Keywords = []
        driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/div/div[1]/div/div[1]/span').click()
        driver.find_element(By.XPATH, category).click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="18_device_0"]').click()
        driver.find_element(By.XPATH, '//*[@id="19_gender_0"]').click()
        driver.find_element(By.XPATH, '//*[@id="20_age_0"]').click()
        driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div/div[1]/div/a').click()

        for j in range(1, 6):
            path = f'//*[@id="content"]/div[2]/div/div[2]/div[2]/div/div/div[1]/ul/li[{j}]/a'
            time.sleep(0.1)
            result = driver.find_element(By.XPATH, path).text

            Keywords.append(result.split('\n')[1])
            time.sleep(1)
        #print(Keywords)
        driver.close()
        return Keywords
    else :
        return None


#print(get_keywords())