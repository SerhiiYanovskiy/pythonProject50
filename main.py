import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import config
import pyautogui

error_list = []

data = [{
    'tranid': '2683825:3615422394',
    'post': 'НП',
    'city': 'киев',
    'index': 'Київська область, с. Велика Олександрівка , вул. Озерна 44, склад №1',
    'phone': '+380 (67) 123-45-67',
    'name': 'Фамилия Имя',
    'Сумма заказа': '345,00',
    'info_status': '1-3',
    'istok': 'сайт',
    'field18': 'Нейлон',
    'field23': 'Белый',
    'field20': '5*5см',
    'field2': 'Красный',
    'field9': '12+3пар',
    'Чей': 'Влад',
    'file_1': 'https://tupwidget.com/e2b66c/IMG_20ilda11958553.webp',
}, {
    'tranid': '2683825:3616162284',
    'post': 'НП',
    'city': 'киев',
    'index': 'Київська область, с. Велика Олександрівка , вул. Озерна 44, склад №1',
    'phone': '+380 (67) 123-45-67',
    'name': 'Фамилия Имя',

},
    {
        'tranid': '2683825:3612773434',
        'post': 'НП',
        'city': 'киев',
        'index': 'Київська область, с. Велика Олександрівка , вул. Озерна 44, склад №1',
        'phone': '+380 (67) 123-45-67',
        'name': 'Фамилия Имя',
        'Сумма заказа': '345,00',
        'info_status': '1-3',
        'istok': 'сайт',
        'field18': 'Нейлон',
        'field23': 'Белый',
        'field20': '5*5см',
        'field2': 'Красный',
        'field9': '12+3пар',
        'Чей': 'Влад',
        'file_1': 'https://tupwidget.com/e2b66c/IMG_20ilda11958553.webp',
    },

    {
        'tranid': '',
        'post': 'НП',
        'phone': '+380 (67) 123-45-67',
        'info_status': '3-3',
        'istok': 'сайт',
        'field18': 'Нейлон',
        'field23': 'Белый',
        'field20': '5*5см',
        'field2': 'Красный',
        'field9': '12+3пар',
        'Чей': 'Влад',
    },

    {
        'tranid': '',
        'post': 'НП',
        'phone': '+380 (67) 123-45-67',
        'info_status': '3-3',
        'istok': 'сайт',
        'field18': 'Нейлон',
        'field23': 'Белый',
        'field20': '5*5см',
        'field2': 'Красный',
        'field9': '12+3пар',
        'Чей': 'Влад',
    },

    {
        'tranid': '',
        'post': 'НП',
        'phone': '+380 (67) 123-45-67',
        'info_status': '3-3',
        'istok': 'сайт',
        'field18': 'Нейлон',
        'field23': 'Белый',
        'field20': '5*5см',
        'field2': 'Красный',
        'field9': '12+3пар',
        'Чей': 'Влад',
    },

    {
        'tranid': '',
        'post': 'НП',
        'phone': '+380 (67) 123-45-67',
        'info_status': '3-3',
        'istok': 'сайт',
        'field18': 'Нейлон',
        'field23': 'Белый',
        'field20': '5*5см',
        'field2': 'Красный',
        'field9': '12+3пар',
        'Чей': 'Влад',
    }
]


def start_webdriwer(data):
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
    browser.find_element(by=By.ID, value="send").click()
    time.sleep(2)
    browser.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[2]/div[3]/button").click()
    browser.find_element(by=By.XPATH, value="/html/body/div[6]/div/div[2]/div[3]/a[2]").click()
    browser.find_element(by=By.XPATH, value="/html/body/div[2]/div[2]/div[2]/table/tbody/tr/td[1]/a").click()
    pyautogui.moveTo(1000, 1000, _pause=False)
    pyautogui.scroll(-500)
    time.sleep(2)
    pyautogui.scroll(-500)
    time.sleep(2)

    time.sleep(1)
    for tranid in data:
        if len(tranid["tranid"]) < 1:

            main_page = browser.page_source
            soup = BeautifulSoup(main_page, "html")
            soup = soup.find("span", class_="tcrm-tabs-item__cnt js-cnt-active-leads")
            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[4]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]").click()

            browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[4]/div[2]/div/select").click()
            time.sleep(1)
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
                print("pass")
            try:
                browser.find_element(by=By.XPATH,
                                 value="//html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[7]/div[2]/input").send_keys(
                tranid["phone"])
            except:
                print("pass")
            time.sleep(1)
            try:
                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[10]/div[2]/textarea").click()
            except:
                print("pass")
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
                print("pass")
            try:
                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[10]/div[2]/textarea").send_keys(
                tranid['info_status'])
            except:
                print("pass")
            time.sleep(1)
            try:
                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[14]/div[2]/div/select").click()
            except:
                print("pass")
            time.sleep(1)
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
                print("pass")
            try:
                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[15]/div[2]/div/select").click()
            except:print("pass")
            try:
                if tranid['field23'] == "нет":
                    pyautogui.press(['enter'])
                if tranid['field23'] == "Белый":
                    pyautogui.press(['down', 'enter'])
                if tranid['field23'] == "Черный":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['field23'] == "Желт":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Прозрачный":
                    pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Крем":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Серый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Розовый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Голубой":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Светлорозовый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Красный":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Молоч":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field23'] == "Беж":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'enter'])
                if tranid['field23'] == "Шоколад":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'enter'])
                if tranid['field23'] == "Зеленый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'enter'])
                if tranid['field23'] == "Синий":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Крафт":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "глянец":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "мат":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "черный+белый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Разноцвет":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Малин":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Сирен":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "Лаванда":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'enter'])
                if tranid['field23'] == "Шампань":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'enter'])
                if tranid['field23'] == "Cветл.серый":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'enter'])
                if tranid['field23'] == "свет.беж":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'enter'])
                if tranid['field23'] == "золото":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'enter'])
                if tranid['field23'] == "серебро":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                         'down',
                         'down', 'down', 'down', 'down', 'enter'])
            except:
                print("pass")
            try:
                browser.find_element(by=By.XPATH,
                                     value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[16]/div[2]/textarea").send_keys(
                    tranid["field20"])
            except:
                print("pass")
            try:

                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[17]/div[2]/div/select").click()
            except:
                print("pass")
            time.sleep(1)
            try:
                if tranid['field2'] == "Черный":
                    pyautogui.press(['enter'])
                if tranid['field2'] == "Красный":
                    pyautogui.press(['down', 'enter'])
                if tranid['field2'] == "Синий":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['field2'] == "Фиол":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Желт":
                    pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Зеленый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Мята":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Белый":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Малин":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Роз":
                    pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Сирен":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Оранж":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Серый":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'enter'])
                if tranid['field2'] == "Корич":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'enter'])
                if tranid['field2'] == "Золото":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'enter'])
                if tranid['field2'] == "Серебро":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "золото/серебро":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "черный/белый":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "сереб/черн":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "черн/зол/сер":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "черн/бел/золото":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "черн/бел/серебро":
                    pyautogui.press(
                        ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                if tranid['field2'] == "Разноцвет":
                    pyautogui.press(
                    ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                     'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
            except:
                print("pass")
            time.sleep(1)
            try:
                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[16]/div[2]/textarea").click()
            except:
                print("pass")

            pyautogui.press(["pagedown", "pagedown"])
            try:

                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[19]/div[2]/textarea").send_keys(
                tranid['field9'])
            except:
                print("pass")
            try:
                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[20]/div[2]/select").click()
            except:
                print("pass")
            try:

                if tranid['Чей'] == "Влад":
                    pyautogui.press(['down', 'down', 'enter'])
                if tranid['Чей'] == "Алиса":
                    pyautogui.press(['down', 'enter'])
                if tranid['Чей'] == "Vlad":
                    pyautogui.press(['down', 'down', 'down', 'enter'])
            except:
                print("pass")

            try:
                browser.find_element(by=By.XPATH,
                                 value="/html/body/div[2]/div[10]/div/div/form/div[2]/div/div/div[29]/input").click()
            except:
                print("pass")
            time.sleep(2)

            soup1 = BeautifulSoup(main_page, "html")
            soup1 = soup1.find("span", class_="tcrm-tabs-item__cnt js-cnt-active-leads").text

            if soup == soup1:
                with open("error_tranid.txt", "a") as file:
                    file.write(f"{tranid}  error \n")
                error_list.append(tranid)

        if len(tranid["tranid"]) > 1:
            main_page = browser.page_source
            soup = BeautifulSoup(main_page, "html")
            soup = soup.find_all("div",
                                 class_="tcrm-list-item tcrm-clear js-lead-item ui-draggable ui-draggable-handle")

            for elem in soup:
                if tranid["tranid"] in elem.text:
                    line = elem.text[30::]
                    browser.find_element(by=By.ID, value=elem["id"]).click()
                    time.sleep(1)
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[5]/div[2]/div/select").click()
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
                        time.sleep(1)
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[6]/div[2]/textarea").clear()
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[6]/div[2]/textarea").send_keys(
                        tranid['city'])
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[7]/div[2]/textarea").clear()
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[7]/div[2]/textarea").send_keys(
                        tranid['index'])
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[8]/div[2]/input").clear()
                    except:
                        print("pass")
                    try:

                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[8]/div[2]/input").send_keys(
                        tranid["phone"])
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[9]/div[2]/input").clear()
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[9]/div[2]/input").send_keys(
                        tranid["name"])
                    except:
                        print("pass")
                    pyautogui.press(["tab", "tab", "tab"])
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[10]/div[2]/input").clear()
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[10]/div[2]/input").send_keys(
                        tranid["Сумма заказа"])
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[11]/div[2]/textarea").clear()
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[11]/div[2]/textarea").send_keys(
                        tranid["info_status"])
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[11]/div[2]/textarea").click()
                    except:
                        print("pass")
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
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[15]/div[2]/div/select").click()
                    except:
                        print("pass")
                    time.sleep(1)
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
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
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
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
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
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field18'] == "CиликонСтанд":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'enter'])
                    except:
                        print("pass")
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="//html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[16]/div[2]/div/select").click()
                    except:
                        print("pass")
                    pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', "enter"])
                    try:
                        if tranid['field23'] == "нет":
                            pyautogui.press(['enter'])
                        if tranid['field23'] == "Белый":
                            pyautogui.press(['down', 'enter'])
                        if tranid['field23'] == "Черный":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['field23'] == "Желт":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Прозрачный":
                            pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Крем":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Серый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Розовый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Голубой":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Светлорозовый":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Красный":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Молоч":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'enter'])
                        if tranid['field23'] == "Беж":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'enter'])
                        if tranid['field23'] == "Шоколад":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'enter'])
                        if tranid['field23'] == "Зеленый":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'enter'])
                        if tranid['field23'] == "Синий":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Крафт":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "глянец":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "мат":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "черный+белый":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Разноцвет":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Малин":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Сирен":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "Лаванда":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'enter'])
                        if tranid['field23'] == "Шампань":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'enter'])
                        if tranid['field23'] == "Cветл.серый":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'enter'])
                        if tranid['field23'] == "свет.беж":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'enter'])
                        if tranid['field23'] == "золото":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'enter'])
                        if tranid['field23'] == "серебро":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down',
                             'down', 'down', 'down', 'down', 'enter'])
                    except:
                        print("pass")
                    pyautogui.press(["enter"])

                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[13]/div[2]/textarea").click()

                    pyautogui.press(["pagedown", ])
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[17]/div[2]/textarea").clear()

                    try:

                        browser.find_element(by=By.XPATH,
                                             value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[17]/div[2]/textarea").send_keys(
                        tranid["field20"])
                    except:
                        print("pass")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[18]/div[2]/div/select").click()
                    time.sleep(1)
                    pyautogui.press(['up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up', 'up',
                                     'up', 'up', 'up', 'up', "enter"])
                    try:

                        if tranid['field2'] == "Черный":
                            pyautogui.press(['enter'])
                        if tranid['field2'] == "Красный":
                            pyautogui.press(['down', 'enter'])
                        if tranid['field2'] == "Синий":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['field2'] == "Фиол":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Желт":
                            pyautogui.press(['down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Зеленый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Мята":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Белый":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Малин":
                            pyautogui.press(['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Роз":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Сирен":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Оранж":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'enter'])
                        if tranid['field2'] == "Серый":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'enter'])
                        if tranid['field2'] == "Корич":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'enter'])
                        if tranid['field2'] == "Золото":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Серебро":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "золото/серебро":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "черный/белый":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "сереб/черн":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "черн/зол/сер":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "черн/бел/золото":
                            pyautogui.press(
                                ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "черн/бел/серебро":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'enter'])
                        if tranid['field2'] == "Разноцвет":
                            pyautogui.press(
                            ['down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down', 'down',
                             'enter'])
                    except:
                        print("pass")
                    pyautogui.press(["tab"])
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[20]/div[2]/textarea").clear()

                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[20]/div[2]/textarea").send_keys(
                        tranid['field9'])
                    except:
                        print("pass")
                    time.sleep(1)
                    pyautogui.press(["tab", "tab", "tab", "tab"])
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[21]/div[2]/select").click()

                    pyautogui.press(['up', 'up', 'up', 'up', "enter"])
                    try:

                        if tranid['Чей'] == "Влад":
                            pyautogui.press(['down', 'down', 'enter'])
                        if tranid['Чей'] == "Алиса":
                            pyautogui.press(['down', 'enter'])
                        if tranid['Чей'] == "Vlad":
                            pyautogui.press(['down', 'down', 'down', 'enter'])
                    except:
                        print("pass")
                    browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[24]/div[2]/textarea").clear()
                    try:
                        browser.find_element(by=By.XPATH,
                                         value="/html/body/div[2]/div[11]/div/div/div[1]/div[2]/div[2]/form/div/div[24]/div[2]/textarea").send_keys(
                        tranid['file_1'])
                    except:
                        print("pass")
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
                            line1 = elem.text[30::]
                            if line1 == line:
                                with open("error_tranid.txt", "a") as file:
                                    file.write(f"{tranid}  error \n")
                                error_list.append(tranid)
                                print(line1)


start_webdriwer(data)
time.sleep(300)
start_webdriwer(error_list)
