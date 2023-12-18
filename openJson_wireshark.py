import json
import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time


# 针对一个 URL 测量页面加载时间
def open(url, num_iterations=5):
    total_page_load_time = 0
    total_resource_load_time = 0
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-application-cache")  # 禁用应用程序缓存
    for _ in range(num_iterations):
        # 启动浏览器
        driver = webdriver.Chrome(options=options)
        try:
            # 打开网页
            driver.get(url)
            driver.delete_all_cookies()
            # 等待页面加载完成，这里使用了隐式等待，最长等待时间为10秒
            driver.implicitly_wait(10)
            # 等待页面完全加载
            # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
            WebDriverWait(driver, 10).until(lambda driver: driver.execute_script(
                'return document.readyState') == 'complete')
        except Exception as e:
            print(f"[{_ + 1}] Exception: {e}")
        finally:
            # 关闭当前窗口而不是整个浏览器
            driver.close()
def port_open(endpoints, port):
    numeration = 5
    for endpoint, url in endpoints.items():
        if isinstance(url, dict):
            # 处理包含详细信息的对象（例如 "small", "medium", "large"）
            sub_url = url["url"].replace("{port}", str(port))
            num_resources = url["numResources"]
            size = url["size"]
            print(f"\nMeasuring performance for {endpoint}:")
            print(f"URL: {sub_url}")
            print(f"Number of Resources: {num_resources}")
            print(f"Size: {size} bytes")
            open(sub_url, numeration)
        else:
            url = url.replace("{port}", str(port))
            # 处理普通的 URL（例如 "100KB", "1MB", "5MB"）
            print(f"\nMeasuring performance for {endpoint}:")
            print(f"URL: {url}")
            open(url, numeration)


if __name__ == "__main__":
    # 读取 endpoints.json 文件
    with open("./endpoints.json", "r") as f:
        endpoints_data = json.load(f)

    # 创建输出目录
    directory_path = "./out"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    # 假设端口号为 8443
    # port = 8443
    # # 测量性能
    # port_open(endpoints_data, port)
    # port = 443
    # port_open(endpoints_data, port)
    port = 80
    port_open(endpoints_data, port)
