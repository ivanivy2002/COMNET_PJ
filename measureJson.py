import json
import os

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 针对一个 URL 测量页面加载时间
def measure_load_time(file, url, endpoint, num_iterations=5):
    with open(file, "a") as file:
        # file.truncate()
        file.write(f"Measuring performance for {endpoint}:\n")
        file.write(f"URL: {url}\n")
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
                # 记录页面加载开始时间
                start_time = time.time()
                # 等待页面加载完成，这里使用了隐式等待，最长等待时间为10秒
                driver.implicitly_wait(10)
                # 等待页面完全加载
                # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
                WebDriverWait(driver, 10).until(lambda driver: driver.execute_script(
                    'return document.readyState') == 'complete')
                # 记录页面加载结束时间
                end_time = time.time()
                # 计算页面加载时间
                page_load_time = end_time - start_time
                # 获取资源加载时间
                resource_load_time = driver.execute_script(
                    "return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart;"
                ) / 1000  # 转换为秒

                # # 获取所有资源的性能数据
                # resource_entries = driver.execute_script(
                #     """
                #     var entries = window.performance.getEntriesByType('resource');
                #     return entries.map(function(entry) {
                #         return {
                #             name: entry.name,
                #             startTime: entry.startTime,
                #             duration: entry.duration
                #         };
                #     });
                #     """
                # )
                # # 打印每个资源的加载时间
                # for entry in resource_entries:
                #     print(f"Resource: {entry['name']}, Start Time: {entry['startTime']}, Duration: {entry['duration']}")

                print(f"[{_ + 1}] Page Load Time: {page_load_time:.2f} s ")
                print(f"[{_ + 1}] Res Load Time: {resource_load_time:.2f} s\n")
                file.write(f"[{_ + 1}] Page Load Time: {page_load_time:.2f} s ")
                file.write(f"[{_ + 1}] Res Load Time: {resource_load_time:.2f} s\n")
                # 累加总时间
                total_page_load_time += page_load_time
                total_resource_load_time += resource_load_time

            except Exception as e:
                file.write(f"[{_ + 1}] Exception: {e}")
            finally:
                # 关闭当前窗口而不是整个浏览器
                driver.close()

        # 计算平均值
        average_page_load_time = total_page_load_time / num_iterations
        average_resource_load_time = total_resource_load_time / num_iterations

        file.write(f"Avg Page Load Time: {average_page_load_time:.2f} s ")
        file.write(f"Avg Res Load Time: {average_resource_load_time:.2f} s\n")


def measure_performance(dir, endpoints, port):
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
            # 此处可以添加你的性能测量逻辑
            file = dir + "/" + str(port) + "_" + endpoint + ".txt"
            if endpoint != "large":
                measure_load_time(file, sub_url, endpoint, 5)
            # if endpoint == "large":
            #     measure_load_time(file, sub_url, endpoint, 3)
            # else:
            #     measure_load_time(file, sub_url, endpoint, numeration)
        else:
            url = url.replace("{port}", str(port))
            # 处理普通的 URL（例如 "100KB", "1MB", "5MB"）
            print(f"\nMeasuring performance for {endpoint}:")
            print(f"URL: {url}")

            # 此处可以添加你的性能测量逻辑
            file = dir + "/" + str(port) + "_" + endpoint + ".txt"
            if endpoint != "5MB":
                measure_load_time(file, url, endpoint, 5)
            # if endpoint == "5MB":
            #     measure_load_time(file, url, endpoint, 3)
            # else:
            #     measure_load_time(file, url, endpoint, numeration)


if __name__ == "__main__":
    # 读取 endpoints.json 文件
    with open("./endpoints.json", "r") as f:
        endpoints_data = json.load(f)

    # 创建输出目录
    directory_path = "./lag25_drop5_out"
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    port = 8443
    measure_performance(directory_path,endpoints_data, port)
    port = 443
    measure_performance(directory_path,endpoints_data, port)
    port = 80
    measure_performance(directory_path,endpoints_data, port)

    # 专门一个
    # port = 443
    # measure_load_time("./out/443_medium.txt", "https://111.229.132.28:443/speed-test-medium.html", "medium", 5)
