import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions  # 实现规避检测风险

if __name__ == "__main__":
    run_code = 0
    s = Service("./chromedriver")
    chrome_options = ChromeOptions()
    # 规避检测
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get(
        """
        https://auth.oc.portal.klarna.com/auth/realms/merchants/protocol/openid-connect/auth?client_id=merchant-portal&redirect_uri=https%3A%2F%2Fportal.klarna.com%2F&state=3e7ea0c1-42db-4cdb-a302-d44942ea2277&response_mode=fragment&response_type=code&scope=openid&nonce=ee8d0440-fbc2-4999-8ff6-ef2dddc5f365&code_challenge=MZYjxCkdrbxGu8jk-A4FRQajRUPEqlsRNHLo7ANQE0c&code_challenge_method=S256
        """)  # 打开网站
    print(browser)
    browser.maximize_window()
    username = browser.find_element(by=By.XPATH, value='//*[@id="username"]')
    username.send_keys("cuilian.hu@orderplus.com")
    password = browser.find_element(by=By.XPATH, value='//*[@id="password"]')
    password.send_keys("AUB88#mciK")
    #
    time.sleep(2)
    #
    a_login = browser.find_element(by=By.XPATH, value='//*[@id="loginBtn"]')
    #
    a_login.click()
    windows = browser.window_handles  # 把新的页面赋值给windows
    browser.switch_to.window(windows[-1])  # 把窗口windwos中的最后一个窗口为当前窗口

    print(browser)
    time.sleep(10)
    # 点击Orders
    order_click = browser.find_element(by=By.XPATH, value='//*[@id="sidebar-orders-fe"]')
    #
    order_click.click()

    windows = browser.window_handles  # 把新的页面赋值给windows
    browser.switch_to.window(windows[-1])  # 把窗口windwos中的最后一个窗口为当前窗口

    time.sleep(10)

    # # 点击导出
    # export_click = browser.find_element(by=By.XPATH, value='//*[@id="action-export"]/option[2]')
    # #
    # export_click.click()
    result = browser.find_element(by=By.XPATH, value='//*[@id="search-result-row-0"]')

    print(result.text)
    browser.close()



