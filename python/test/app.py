from selenium import webdriver
import time

# 环境地址
URL = "https://cn.bing.com"


def start(driver):
    # 浏览器最大化
    driver.maximize_window()

    # 访问环境地址
    driver.get(URL)
    time.sleep(1)

    # 输入搜索内容
    searchElement = driver.find_element_by_id("sb_form_q")
    searchElement.send_keys("测试网教程")
    time.sleep(1)

    # 点击查询
    driver.find_element_by_id("sb_form_go").click() 
    time.sleep(2)

    driver.find_element_by_link_text("测试教程网").click()
    time.sleep(5)

    # 刷新浏览器
    driver.refresh()
    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    driver = webdriver.Chrome("./chromedriver.exe")
    # driver = webdriver.Chrome()
    start(driver)
    driver.close
