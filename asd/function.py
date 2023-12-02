from flask import Flask, render_template, request

from datetime import date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import datetime as dt

def airplane(result):
    print(result)
    print(type(result["start_date"]))
    print(type(result["end_date"]))
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/travel/flights?hl=ko")
    time.sleep(1)

    # 출발지 입력
    driver.find_element(
        By.CSS_SELECTOR,
        "#i21 > div.e5F5td.BGeFcf > div > div > div.cQnuXe.k0gFV > div > div > input",
    ).click()
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR,
        "#i21 > div.ZGEB9c.yRXJAe.P0ukfb.a4gL0d.TFC9me.PRvvEd.Otspu.iWO5td.BDJ8fb > div:nth-child(3) > div.lJj3Hd.PuaAn > div.peGo5b.ozeT5c > div > input",
    ).send_keys(result["start_airplane"])
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#c15 > div.CwL3Ec").click()
    time.sleep(2)

    # 도착지 입력
    driver.find_element(
        By.CSS_SELECTOR,
        "#i21 > div.e5F5td.vxNK6d > div > div > div.cQnuXe.k0gFV > div > div > input",
    ).click()
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR,
        "#i21 > div.ZGEB9c.yRXJAe.P0ukfb.a4gL0d.TFC9me.PRvvEd.WKeVIb.Otspu.iWO5td.BDJ8fb > div:nth-child(3) > div.lJj3Hd.PuaAn > div.peGo5b.ozeT5c > div > input",
    ).send_keys(result["end_airplane"])
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#c27 > div.CwL3Ec").click()
    time.sleep(2)

    # 가는날 선택
    driver.find_element(
        By.CSS_SELECTOR,
        "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.AJxgH > div > div.rIZzse > div.bgJkKe.K0Tsu > div > div > div.cQnuXe.k0gFV > div > div > div:nth-child(1) > div > div.oSuIZ.YICvqf.kStSsc.ieVaIb > div > input",
    ).click()
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR,
        "#ow79 > div.ZGEB9c.yRXJAe.P0ukfb.icWGef.bgJkKe.BtDLie.iWO5td > div > div.rj7qGc.ksI2Bc.P0ukfb > div.X4feqd.wDt51d > div.AotkO.uknidb > div.oSuIZ.YICvqf.kStSsc.ieVaIb > div > input",
    ).send_keys(result["start_date"])
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR,
        "#ow79 > div.ZGEB9c.yRXJAe.P0ukfb.icWGef.bgJkKe.BtDLie.iWO5td > div > div.rj7qGc.ksI2Bc.P0ukfb > div.X4feqd.wDt51d > div.AotkO.uknidb > div.oSuIZ.YICvqf.lJODHb.qXDC9e > div > input",
    ).send_keys(result["end_date"])
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR,
        "#ow79 > div.ZGEB9c.yRXJAe.P0ukfb.icWGef.bgJkKe.BtDLie.iWO5td > div > div.rj7qGc.ksI2Bc.P0ukfb > div.X4feqd.wDt51d > div.AotkO.uknidb > div.oSuIZ.YICvqf.lJODHb.qXDC9e > div > input",
    ).send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR,
        "#ow79 > div.ZGEB9c.yRXJAe.P0ukfb.icWGef.bgJkKe.BtDLie.iWO5td > div > div.akjk5c.FrVb0c > div.WXaAwc > div > button",
    ).click()
    time.sleep(2)

    driver.find_element(
        By.CSS_SELECTOR,
        "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.vg4Z0e > div:nth-child(1) > div.SS6Dqf.POQx1c > div.MXvFbd > div > button",
    ).click()

    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(6) > ul > li.ZVk93d > div > span.XsapA",
        ).click()
    except Exception as e:
        pass
    time.sleep(2)

    # opt_air = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(4) > ul')
    # other_air = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(6) > ul')
    li = []
    test = driver.find_elements(
        By.CSS_SELECTOR,
        "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(4) > ul > li",
    )
    for i in range(len(test)):
        tmp = driver.find_element(
            By.CSS_SELECTOR,
            "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(4) > ul > li:nth-child({}) > div > div.JMc5Xc".format(
                i + 1
            ),
        ).get_attribute("aria-label")
        li.append(tmp)
        test[i] = test[i].text  # %%
    time.sleep(2)
    driver.find_element(
        By.CSS_SELECTOR,
        "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(4) > ul > li:nth-child(1) > div",
    ).click()
    time.sleep(2)  # %%
    ed_li = []
    ed_opt = driver.find_elements(
        By.CSS_SELECTOR,
        "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(4) > ul > li",
    )
    ed_other = driver.find_elements(
        By.CSS_SELECTOR,
        "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(5) > ul > li",
    )

    for i in range(len(ed_opt)):
        tmp = driver.find_element(
            By.CSS_SELECTOR,
            "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(4) > ul > li:nth-child({}) > div > div.JMc5Xc".format(
                i + 1
            ),
        ).get_attribute("aria-label")
        ed_li.append(tmp)
        ed_opt[i] = ed_opt[i].text
    time.sleep(2)  # %%
    driver.find_element(
        By.CSS_SELECTOR,
        "#yDmH0d > c-wiz.zQTmif.SSPGKf > div > div:nth-child(2) > c-wiz > div.cKvRXe > c-wiz > div.PSZ8D.EA71Tc > div.FXkZv > div:nth-child(4) > ul > li:nth-child(1) > div",
    ).click()

    return ed_opt, 


def places(result):  # 지역 명소 크롤링
    # 크롬 드라이버 실행

    driver = webdriver.Chrome()

    # 원하는 URL로 접속
    url = "https://www.google.co.kr/maps/?entry=ttu"
    driver.get(url)

    # 검색어 입력
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(result + " 명소")
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)

    time.sleep(2)
    a1 = driver.find_element(By.CLASS_NAME, "drGLxe")
    time.sleep(5)
    a1.click()

    a2 = driver.find_element(By.XPATH, '//*[@id="action-menu"]/div[7]')
    time.sleep(5)
    a2.click()

    max_try = 5

    for _ in range(max_try):
        element_to_scroll_to = driver.find_element(
            By.XPATH,
            '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]',
        )
        element_to_scroll_to.send_keys(Keys.PAGE_DOWN)
        element_to_scroll_to.send_keys(Keys.PAGE_DOWN)
        element_to_scroll_to.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    # 특정 클래스 이름을 가진 요소들 찾기
    class_name = "hfpxzc"
    elements_with_class = driver.find_elements(By.CLASS_NAME, class_name)

    # 각 요소의 aria-label 값을 가져와 리스트에 저장
    aria_labels = []

    for element in elements_with_class:
        aria_label = element.get_attribute("aria-label")
        if aria_label:
            aria_labels.append(aria_label)

    # 출력
    for label in aria_labels:
        print("aria-label 속성의 값:", label)

    # df = pd.DataFrame(aria_labels)
    return aria_labels


def sub_date(result):  # 날짜 차이 계산
    start = result["start_date"]
    end = result["end_date"]

    start = start.split("-")
    end = end.split("-")

    start_date = date(int(start[0]), int(start[1]), int(start[2]))
    end_date = date(int(end[0]), int(end[1]), int(end[2]))

    print(start_date)
    print(end_date)

    diff = (end_date - start_date).days

    print(diff)


def hotel(result):
    driver = webdriver.Chrome()
    driver.get(
        "https://www.agoda.com/ko-kr/search?city=14690&site_id=1891442&tag=782b98b0-e95a-0318-464c-9df2f46883a7&nhakw=1&gad=1&device=c&network=g&adid=577294658636&rand=10811873334794923270&expid=&adpos=&aud=aud-951004860236%3Akwd-321247717620&gclid=Cj0KCQjw-pyqBhDmARIsAKd9XINVq9Dyz2VhSt_UehLOyXgVAz8np5YIvOBgizfG7qqCnMH8aFm7VMQaAhz6EALw_wcB&checkIn=2023-11-15&checkOut=2023-11-16&adults=1&rooms=1&pslc=1&ds=cJadpOCWpF1Ik%2FR3"
    )
    search_box = driver.find_element(
        By.XPATH, "//*[@id='autocomplete-box']/div/div/div/div[1]"
    )

    search_box.click()
    time.sleep(2)
    search = driver.find_element(By.XPATH, '//*[@id="textInput"]')
    search.clear()
    search.send_keys(result["place"])
    time.sleep(1)

    print(type(result["start_date"]))
    print(type(result["end_date"]))
    # 날짜
    start_date = change_to_date(result["start_date"])
    end_date = change_to_date(result["end_date"])
    print(start_date)
    print(end_date)
    # test
    driver.find_element(By.CSS_SELECTOR, "#check-in-box").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[aria-label="{}"]'.format(start_date)).click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[aria-label="{}"]'.format(end_date)).click()
    time.sleep(2)

    # 인원입력칸 클릭
    driver.find_element(By.XPATH, '//*[@id="occupancy-box"]/div').click()
    time.sleep(1)

    #성인 증가
    for i in range(3):
        driver.find_element(By.XPATH, '//*[@id="occupancy-selector"]/div/div/div[2]/div[2]/div[3]').click()
        time.sleep(2)

    # # 아동 증가
    for i in range(2):
        driver.find_element(By.XPATH,'//*[@id="occupancy-selector"]/div/div/div[3]/div[2]/div[3]').click()
        time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="SearchBoxContainer"]/div/div/button').click()
    time.sleep(5)

    max_try = 3

    for _ in range(max_try):
        element_to_scroll_to = driver.find_element(
            By.XPATH,
            "/html",
        )
        element_to_scroll_to.send_keys(Keys.PAGE_DOWN)
        element_to_scroll_to.send_keys(Keys.PAGE_DOWN)
        element_to_scroll_to.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    name = driver.find_elements(By.CSS_SELECTOR, "h3.sc-jrAGrp.sc-kEjbxe.eDlaBj.dscgss")
    review = driver.find_elements(
        By.CSS_SELECTOR,
        "p.Typographystyled__TypographyStyled-sc-j18mtu-0.Hkrzy.kite-js-Typography",
    )
    elements_with_class = driver.find_elements(
        By.CLASS_NAME, "sc-jrAGrp.sc-kEjbxe.eDlaBj.fRhhIV.sc-dQppl.cQZIoF"
    )

    position = []

    for element in elements_with_class:
        aria_label = element.get_attribute("label")
        if aria_label:
            position.append(aria_label)
    name_lst = []
    for i in range(int(len(name))):
        name_lst.append(name[i].text)

    review_lst = []
    for i in range(int(len(review))):
        review_lst.append(review[i].text)
    review_lst.pop(0)
    data = {"숙소": name_lst, "평점": review_lst, "위치": position}
    df = pd.DataFrame(data)

def change_to_date(input_date):
    print(type(input_date))
    date_to_split = input_date.split('-')
    date = dt.datetime(int(date_to_split[0]), int(date_to_split[1]), int(date_to_split[2]))

    month = date.strftime("%B")[:3]
    day = date.strftime("%A")[:3]
    string_date = day + " "  + month  + " " +  date_to_split[2] + " " + date_to_split[0]
    return string_date