import time
import pyautogui
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

driver.get("https://toolzu.com/downloader/instagram/profile/")

time.sleep(3)  # ищем кнопку принятия 


# функция для закрытия гугл ад после нажатия на загрузку фото
def close_ad():
        time.sleep(4)
       
        screen = pyautogui.screenshot()  # Получаем изображение экрана
        location = pyautogui.locateOnScreen(screen, 'Close') # Ищем слово "example" на изображении
        if location:
            center = pyautogui.center(location)
            pyautogui.click(center)
        else:
            print("Слово не найдено")
        
        time.sleep(20)  # Приостанавливаем выполнение на 3 секунды


# цикл при загрузке сайта на принятие кук или политики
try:
    element = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    
except NoSuchElementException:
    element = driver.find_element(By.XPATH, '//html/body/div[1]/div/div/div/div[2]/div/button[2]')
time.sleep(2)
element.click()


# ищем поле для ввода имени профиля и надимаем поиск 
time.sleep(3)
search_box = driver.find_element(By.CSS_SELECTOR, '#instagramdownloaderform-search')
search_box.send_keys("vikon")
search_box.submit()



# надимаем загрузить инфу по профилю
time.sleep(3)
search_box1 = driver.find_element(By.XPATH, '//*[@id="downloader-form"]/div[2]/button')
search_box1.click()


# цикл на перебор фото и нажатие загрузки
time.sleep(10)
num = 1
while True:
    try:
        
        search_box = driver.find_element(By.XPATH, f'/html/body/main/div/div[2]/div/div[2]/div[1]/div/div/div/form[{num}]/div/a/img') # код, который может вызывать ошибку
        search_box.is_displayed()
        print(f"Найден элемент {search_box}")
        search_box.click()
        time.sleep(4)
        close_ad()
        num += 1  # при успешном выполнении добавляем 1 к счетчику
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        break
        # если произошла ошибка, прерываем цикл
print(f"Цикл завершен после {num} итераций.")

time.sleep(20)  # Приостанавливаем выполнение на 3 секунды
driver.quit()
