from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Keys 모듈 추가
import time

# 크롬 드라이버 실행
driver = webdriver.Chrome()

# 원하는 URL로 접속
url = 'https://www.google.co.kr/maps/?entry=ttu'
driver.get(url)

# 검색어 입력
search_box = driver.find_element(By.NAME, 'q')
search_box.send_keys('마다가스카르 여행')
search_box.send_keys(Keys.RETURN)

time.sleep(10)

# 특정 클래스 이름을 가진 요소들 찾기
class_name = "hfpxzc"
elements_with_class = driver.find_elements(By.CLASS_NAME, class_name)
print(1)
# 각 요소의 aria-label 값을 가져와 리스트에 저장
aria_labels = []
print(2)
for element in elements_with_class:
    aria_label = element.get_attribute("aria-label")
    if aria_label:
        aria_labels.append(aria_label)
print(3)
# 출력
for label in aria_labels:
    print(1)
    print("aria-label 속성의 값:", label)