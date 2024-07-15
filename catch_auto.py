from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# 定义 URL 和查询条件
url = "https://iftp.chinamoney.com.cn/english/bmkbvl/"
params = {
    "Bond Type": "Treasury Bond",
    "Issue Year": "2023"
}

driver = webdriver.Chrome()                         # 初始化 WebDriver
driver.get(url)
driver.implicitly_wait(10)                          # 等待表格加载（你可能需要调整等待时间）


table = driver.find_element(By.TAG_NAME, 'table')   # 查找表格


headers = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]   # 解析表格数据
rows = []
for row in table.find_elements(By.TAG_NAME, 'tr')[1:]:
    rows.append([cell.text for cell in row.find_elements(By.TAG_NAME, 'td')])


df = pd.DataFrame(rows, columns=headers)           # 创建 DataFrame 并过滤

required_columns = ["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"]
df = df[required_columns]

df.to_csv('Q1_catch_auto.csv', index=False)
print("数据已成功保存！")

driver.quit()                                     # 关闭 WebDriver