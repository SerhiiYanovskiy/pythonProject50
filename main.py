import random
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import config
import pyautogui
import easygui as e

error_list = []


def infoo():
    data = [
        {
            'tranid': '',
            'post': 'НП',  # #список
            'city': 'kvejvei',
            'index': 'Київська область, с. Велика Олександрівка , вул. Озерна 44, склад №1',
            'phone': '+380 (67) 123-45-67',  # текст
            'name': 'Фамилия Имя',
            'Sum': '345,00',
            'info_status': '1-3',
            'istok': 'сайт',  # список
            'vber': '+380507',
            'field18':'Нейлон',

            # Материал  #список
            'field231': 'Белый',  # Фон1  #список
            'field201': '5см',  # Размер    #текст
            'field278': 'Красный',  # Цвет печати  #список
            'field985': 'kdijvi',  # Количество
            'kto': 'Влад',  # (Ответственный)  #список
            'file': 'fkjjoiwajp',  # текст ссылки
            'file_1': 'dkcn;lkdjcda11958553.webp',  # текст ссылки
            'file_2': 'https:#tupwidget.com/e2b66c/IMG_20ilda11958553.webp',  # текст ссылки
    },
    {
        'tranid': '',
        'post': 'УП',  # #список
        'city': 'киев',
        'index': 'Київська область, с. Велика Олександрівка , вул. Озерна 44, склад №1',
        'phone': '+380 (67) 123-45-67',  # текст
        'name': 'Фамилия Имя',
        'Sum': '2,00',

        'info_status': '2-3',
        'istok': 'сайт',  # список
        'vber': '+380501234567',
        'field18': 'Нейлон',  # Материал  #список
        'field231': 'Белый',  # Фон1  #список
        'field201': '5*5см',  # Размер    #текст
        'field278': 'Красный',  # Цвет печати  #список
        'field985': '12+3пар',  # Количество
        'kto': 'Влад',  # (Ответственный)  #список
        'file': 'https:#tupwidget.com/e2b66c/IMG_20ilda11958553.webp',  # текст ссылки
        'file_1': 'https:#tupwidget.com/e2b66c/IMG_20ilda11958553.webp',  # текст ссылки
        'file_2': 'https:#tupwidget.com/e2b66c/IMG_20ilda11958553.webp',  # текст ссылки
    },
    {
        'tranid': '',
        'post': 'НП',  # #список
        'phone': '+380 (67) 123-45-67',  # текст
        'info_status': '3-3',
        'istok': 'сайт',  # список
        'field18': 'Нейлон',  # Материал  #список
        'field231': 'Белый',  # Фон1  #список
        'field201': '5*5см',  # Размер    #текст
        'field278': 'Красный',  # Цвет печати  #список
        'field985': '12+3пар',  # Количество
        'kto': 'Влад',  # (Ответственный)  #список
    }
    ]

    return (data)


def start_webdriwer(NN):
    if NN == 0:
        try:
            data = infoo()
        except:
            e.msgbox(f"INFO ERROR:(", "Error")

    if NN == 1:
        data = error_list


    with open("error_tranid.txt", "w") as file:
        file.write("")
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1800,1000")
    options.add_argument(
                "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36")
    browser = webdriver.Chrome(executable_path=config.CHROME_DRRIVER_PATH, options=options)
    browser.get("https://tilda.cc/login/")
    time.sleep(12)
    browser.find_element(by=By.XPATH, value="/html/body/div/div/div/form/div/div[1]/label/input").send_keys(
        config.EMAIL)
    browser.find_element(by=By.XPATH, value="/html/body/div/div/div/form/div/div[2]/label/input").send_keys(
        config.PASSWORD)
    browser.find_element(by=By.ID, value="send").click()# авторизация( войти)
    time.sleep(2)
    browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[3]/button").click()
    browser.find_element(by=By.XPATH, value="/html/body/div[6]/div/div[2]/div[3]/a[2]").click()
    browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/a").click() # dыбор таблицы
    pyautogui.moveTo(800, 800, _pause=False)
    pyautogui.scroll(-4000)
    time.sleep(2)
    pyautogui.scroll(-4000)
    time.sleep(2)

    time.sleep(1
               )
    for tranid in data:
        if len(tranid["tranid"]) < 1:
            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[4]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]").click()

            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[7]/div[2]/div/select").click()
            try:

                if tranid['post'] == 'НП':
                    pyautogui.press(['enter'])
                if tranid['post'] == 'УП':
                    pyautogui.press(['down', 'enter'])
                if tranid['post'] == 'другое':
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['post'] == 'за наш счет НП':
                    pyautogui.press(['down', 'down', 'down', 'enter'])
                if tranid['post'] == 'за наш счет УП':
                    pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                if tranid['post'] == 'ПАШТОМАТ':
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['post'] == 'за наш счет ПАШТОМАТ':
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
            except:
                print("")

            try:
                browser.find_element(by=By.XPATH,

                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[8]/div[2]/textarea").send_keys(
                    tranid["city"])

            except:
                print("")

            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[9]/div[2]/textarea").send_keys(
                    tranid["index"])
            except:
                print("")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[10]/div[2]/input").send_keys(
                    tranid["phone"])
            except:
                print("")

            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[10]/div[2]/input").click()
            pyautogui.press(["pagedown"])

            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[11]/div[2]/input").send_keys(
                    tranid["name"])

            except:
                print("")

            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[13]/div[2]/input").send_keys(
                    tranid["Sum"])

            except:
                print("")

            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[16]/div[2]/textarea").send_keys(
                    tranid["info_status"])
            except:
                print("")

            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[16]/div[2]/textarea").click()
            pyautogui.press(["pagedown"])
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[20]/div[2]/textarea").send_keys(
                    tranid["vber"])
            except:
                print("")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[21]/div[2]/div/select").click()
            except:
                print("")
            try:

                if tranid["istok"] == "новый":
                    pyautogui.press(['enter'])
                if tranid["istok"] == "ua":
                    pyautogui.press(['down', 'enter'])
                if tranid["istok"] == "shop":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid["istok"] == "kids":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
                if tranid["istok"] == "сайт":
                    pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                if tranid["istok"] == "сайтUA":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid["istok"] == "конструктор":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid["istok"] == "коафта":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid["istok"] == "viber":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid["istok"] == "звонок":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid["istok"] == "другое":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
            except:
                print("")
            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[26]/div[2]/textarea").click()
            pyautogui.press(["pagedown"])
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[28]/div[2]/div/select").click()
            except:
                print("")

            try:
                if tranid['field18'] == ".":
                    pyautogui.press(['enter'])
                if tranid['field18'] == "Сатин":
                    pyautogui.press(['down', 'enter'])
                if tranid['field18'] == "Ткан.край":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['field18'] == "Нейлон":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Силикон":
                    pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Наклейки":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Бирки":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Бирки+Шнурки":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Открытки":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Визитки":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Размерники":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Бирки+Наклейки":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field18'] == "Термо":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field18'] == "Термостик":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'enter'])
                if tranid['field18'] == "Ножки":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'enter'])
                if tranid['field18'] == "Термо+ножки":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Приш+ножки":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Для предметов":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Для Канцел":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Мини набор":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Мини набор(термо)":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Старт набор":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Старт набор 2":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Для школы(термо)":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field18'] == "Для школы(приш)":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field18'] == "Для школы2":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'enter'])
                if tranid['field18'] == "приш+терм":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'enter'])
                if tranid['field18'] == "нейлон наклейки":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "ТермРазноц+стикеры":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "конв":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Шнурк":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "СтартМини":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Старт30":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Старт100":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "Браслет":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field18'] == "CиликонСтанд":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
            except:
                print("")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[29]/div[2]/div/select").click()
            except:
                print("")
            try:
                if tranid['field231'] == "нет":
                    pyautogui.press(['enter'])
                if tranid['field231'] == "Белый":
                    pyautogui.press(['down', 'enter'])
                if tranid['field231'] == "Черный":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['field231'] == "Желт":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Прозрачный":
                    pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Крем":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Серый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Розовый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Голубой":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Светлорозовый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Красный":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Молоч":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field231'] == "Беж":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'enter'])
                if tranid['field231'] == "Шоколад":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'enter'])
                if tranid['field231'] == "Зеленый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'enter'])
                if tranid['field231'] == "Синий":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Крафт":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "глянец":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "мат":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "черный+белый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Разноцвет":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Малин":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Сирен":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "Лаванда":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field231'] == "Шампань":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'enter'])
                if tranid['field231'] == "Cветл.серый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'enter'])
                if tranid['field231'] == "свет.беж":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'enter'])
                if tranid['field231'] == "золото":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'enter'])
                if tranid['field231'] == "серебро":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'enter'])
            except:
                print("")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[30]/div[2]/textarea").send_keys(
                    tranid["field201"])
            except:
                print("")
            try:

                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[31]/div[2]/div/select").click()
            except:
                print("")
            try:
                if tranid['field278'] == "Черный":
                    pyautogui.press(['enter'])
                if tranid['field278'] == "Красный":
                    pyautogui.press(['down', 'enter'])
                if tranid['field278'] == "Синий":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['field278'] == "Фиол":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Желт":
                    pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Зеленый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Мята":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Белый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Малин":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Роз":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Сирен":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Оранж":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field278'] == "Серый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field278'] == "Корич":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'enter'])
                if tranid['field278'] == "Золото":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'enter'])
                if tranid['field278'] == "Серебро":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "золото/серебро":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "черный/белый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "сереб/черн":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "черн/зол/сер":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "черн/бел/золото":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "черн/бел/серебро":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field278'] == "Разноцвет":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
            except:
                print("")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[16]/div[2]/textarea").click()
            except:
                print("")
            try:

                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[34]/div[2]/textarea").send_keys(
                    tranid['field985'])
            except:
                print("")
            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[34]/div[2]/textarea").click()
            pyautogui.press(["pagedown"])

            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[34]/div[2]/textarea").click()
            except:
                print("")
            try:

                if tranid['Kto'] == "Влад":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['Kto'] == "Алиса":
                    pyautogui.press(['down', 'enter'])
                if tranid['Kto'] == "Vlad":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
            except:
                print("")

            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[40]/div[2]/textarea").send_keys(
                    tranid["file"])
            except:
                print("")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[41]/div[2]/textarea").send_keys(
                    tranid["file_1"])
            except:
                print("")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[42]/div[2]/textarea").send_keys(
                    tranid["file_2"])
            except:
                print("")
            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[42]/div[2]/textarea").click()
            pyautogui.press(["pagedown"])


            number = [random.choice('abc123' if i != 5 else 'ABC') for i in range(6)]
            number = "".join(number)


            browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[44]/div[2]/textarea").send_keys(number)
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[46]/input").click()
            except:
                print("")
            time.sleep(2)
            main_page = browser.page_source
            soup = BeautifulSoup(main_page, "html")
            soup = soup.find("div", class_="tcrm-list-item tcrm-clear js-lead-item ui-draggable ui-draggable-handle")
            if number in soup.text:
                continue
            else:
                with open("error_tranid.txt", "a") as file:
                    file.write(f"{tranid}  error \n")
                error_list.append(tranid)
                print(f"{tranid} error")
                e.msgbox(f"{tranid}An error has occured! :(", "Error")


        if len(tranid["tranid"]) > 1:
            main_page = browser.page_source
            soup = BeautifulSoup(main_page, "html")
            soup = soup.find_all("div",
                                 class_="tcrm-list-item tcrm-clear js-lead-item ui-draggable ui-draggable-handle")

            for elem in soup:
                if tranid["tranid"] in elem.text:
                    line = elem.text[25::]
                    browser.find_element(by=By.ID, value=elem["id"]).click()
                    time.sleep(1)
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[8]/div[2]/div/select").click()
                    except:
                        print("pass")

                    time.sleep(1)

                    pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', "enter"])
                    try:
                        if tranid['post'] == 'НП':
                            pyautogui.press(['enter'])
                        if tranid['post'] == 'УП':
                            pyautogui.press(['down', 'enter'])
                        if tranid['post'] == 'другое':
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['post'] == 'за наш счет НП':
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                        if tranid['post'] == 'за наш счет УП':
                            pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                        if tranid['post'] == 'ПАШТОМАТ':
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['post'] == 'за наш счет ПАШТОМАТ':
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])

                    except:
                        print("")

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[9]/div[2]/textarea").clear()
                    except:
                        print("")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[9]/div[2]/textarea").send_keys(
                            tranid["city"])
                    except:
                        print("")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[9]/div[2]/textarea").click()
                    pyautogui.press(["pagedown"])
                    time.sleep(5)

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[9]/div[2]/textarea").clear()
                    except:
                        print("")

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[9]/div[2]/textarea").send_keys(
                            tranid["index"])

                    except:
                        print("")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[11]/div[2]/input").clear()
                    except:
                        print("")

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[11]/div[2]/input").send_keys(
                            tranid["phone"])
                    except:
                        print("")

                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[11]/div[2]/input").click()
                    pyautogui.press(["pagedown"])

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[12]/div[2]/input").clear()
                    except:
                        print("")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[12]/div[2]/input").send_keys(
                            tranid["name"])
                    except:
                        print("")

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[14]/div[2]/input").clear()
                    except:
                        print("")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[14]/div[2]/input").send_keys(
                            tranid["Sum"])
                    except:
                        print("")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[14]/div[2]/input").click()
                    pyautogui.press(["pagedown"])

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[17]/div[2]/textarea").clear()
                    except:
                        print("")

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[17]/div[2]/textarea").send_keys(
                            tranid["info_status"])
                    except:
                        print("")

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[21]/div[2]/textarea").clear()
                    except:
                        print("")

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[21]/div[2]/textarea").send_keys(
                            tranid["vber"])
                    except:
                        print("")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="//html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[22]/div[2]/div/select").click()
                    except:
                        print("")
                    pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', "enter"])
                    try:
                        if tranid["istok"] == "новый":
                            pyautogui.press(['enter'])
                        if tranid["istok"] == "ua":
                            pyautogui.press(['down', 'enter'])
                        if tranid["istok"] == "shop":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid["istok"] == "kids":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                        if tranid["istok"] == "сайт":
                            pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                        if tranid["istok"] == "сайтUA":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid["istok"] == "конструктор":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid["istok"] == "коафта":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid["istok"] == "viber":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid["istok"] == "звонок":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid["istok"] == "другое":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                    except:
                        print("")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[29]/div[2]/div/select").click()
                    except:
                        print("")

                    pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', "enter"])
                    try:
                        if tranid['field18'] == ".":
                            pyautogui.press(['enter'])
                        if tranid['field18'] == "Сатин":
                            pyautogui.press(['down', 'enter'])
                        if tranid['field18'] == "Ткан.край":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['field18'] == "Нейлон":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Силикон":
                            pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Наклейки":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Бирки":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Бирки+Шнурки":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Открытки":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Визитки":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Размерники":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field18'] == "Бирки+Наклейки":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field18'] == "Термо":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'enter'])
                        if tranid['field18'] == "Термостик":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'enter'])
                        if tranid['field18'] == "Ножки":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'enter'])
                        if tranid['field18'] == "Термо+ножки":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Приш+ножки":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Для предметов":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Для Канцел":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Мини набор":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Мини набор(термо)":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Старт набор":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Старт набор 2":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field18'] == "Для школы(термо)":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field18'] == "Для школы(приш)":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'enter'])
                        if tranid['field18'] == "Для школы2":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'enter'])
                        if tranid['field18'] == "приш+терм":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'enter'])
                        if tranid['field18'] == "нейлон наклейки":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "ТермРазноц+стикеры":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "конв":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Шнурк":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "СтартМини":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Старт30":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Старт100":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "Браслет":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field18'] == "CиликонСтанд":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                    except:
                        print("")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[30]/div[2]/div/select").click()
                    except:
                        print("")
                    pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', "enter"])
                    try:
                        if tranid['field231'] == "нет":
                            pyautogui.press(['enter'])
                        if tranid['field231'] == "Белый":
                            pyautogui.press(['down', 'enter'])
                        if tranid['field231'] == "Черный":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['field231'] == "Желт":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Прозрачный":
                            pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Крем":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Серый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Розовый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Голубой":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Светлорозовый":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Красный":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field231'] == "Молоч":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field231'] == "Беж":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'enter'])
                        if tranid['field231'] == "Шоколад":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'enter'])
                        if tranid['field231'] == "Зеленый":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'enter'])
                        if tranid['field231'] == "Синий":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Крафт":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "глянец":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "мат":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "черный+белый":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Разноцвет":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Малин":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "Сирен":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field231'] == "Лаванда":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field231'] == "Шампань":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'enter'])
                        if tranid['field231'] == "Cветл.серый":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'enter'])
                        if tranid['field231'] == "свет.беж":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'enter'])
                        if tranid['field231'] == "золото":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'enter'])
                        if tranid['field231'] == "серебро":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down',
                                 'down', 'down', 'down', 'down', 'enter'])
                    except:
                        print("")
                    pyautogui.press(["enter"])
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[28]/div[2]/textarea").click()

                    pyautogui.press(["pagedown"])

                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[31]/div[2]/textarea").clear()

                    try:

                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[31]/div[2]/textarea").send_keys(
                            tranid["field201"])
                    except:
                        print("")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[32]/div[2]/div/select").click()

                    pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', "enter"])
                    try:

                        if tranid['field278'] == "Черный":
                            pyautogui.press(['enter'])
                        if tranid['field278'] == "Красный":
                            pyautogui.press(['down', 'enter'])
                        if tranid['field278'] == "Синий":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['field278'] == "Фиол":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Желт":
                            pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Зеленый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Мята":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Белый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Малин":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Роз":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Сирен":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field278'] == "Оранж":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field278'] == "Серый":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'enter'])
                        if tranid['field278'] == "Корич":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'enter'])
                        if tranid['field278'] == "Золото":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "Серебро":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "золото/серебро":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "черный/белый":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "сереб/черн":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "черн/зол/сер":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "черн/бел/золото":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field278'] == "черн/бел/серебро":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                        if tranid['field278'] == "Разноцвет":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                                 'enter'])
                    except:
                        print("")
                    pyautogui.press(["tab"])
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[35]/div[2]/textarea").clear()

                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[35]/div[2]/textarea").send_keys(
                            tranid['field985'])
                    except:
                        print("")

                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[37]/div[2]/select").click()

                    pyautogui.press(['up', 'up', 'up', 'up', "enter"])
                    try:

                        if tranid["Kto"] == "Влад":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['Kto'] == "Алиса":
                            pyautogui.press(['down', 'enter'])
                        if tranid['Kto'] == "Vlad":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                    except:
                        print("")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[35]/div[2]/textarea").click()
                    pyautogui.press(["pagedown"])

                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[41]/div[2]/textarea").clear()
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[41]/div[2]/textarea").send_keys(
                            tranid['file'])
                    except:
                        print("")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[42]/div[2]/textarea").clear()
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[42]/div[2]/textarea").send_keys(
                            tranid['file_1'])
                    except:
                        print("")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[43]/div[2]/textarea").clear()
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[43]/div[2]/textarea").send_keys(
                            tranid['file_2'])
                    except:
                        print("")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[1]/div/div[1]/input[1]").click()
                    main_page = browser.page_source
                    soup1 = BeautifulSoup(main_page, "html")
                    soup1 = soup1.find_all("div",
                                           class_="tcrm-list-item tcrm-clear js-lead-item ui-draggable ui-draggable-handle")
                    time.sleep(2)
                    main_page = browser.page_source
                    soup1 = BeautifulSoup(main_page, "html")
                    soup1 = soup1.find_all("div",
                                           class_="tcrm-list-item tcrm-clear js-lead-item ui-draggable ui-draggable-handle")

                    for elem in soup1:
                        if tranid["tranid"] in elem.text:
                            line1 = elem.text[25::]
                            if line1 == line:
                                with open("error_tranid.txt", "a") as file:
                                    file.write(f"{tranid}  error \n")
                                error_list.append(tranid)
                                print(f"{tranid} error")
                                e.msgbox(f"{tranid}An error has occured! :(", "Error")


start_webdriwer(0)
time.sleep(300)
start_webdriwer(1)
