import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

def fetch_bond_data(url):
    # 发送HTTP GET请求
    response = requests.get(url)
    # 解析HTML页面
    soup = BeautifulSoup(response.text, 'html.parser')
    # 定位表格数据（您需要根据实际HTML结构调整这部分代码）
    table = soup.find('table', class_='your-table-class')  # 请根据实际页面结构调整
    headers = [th.text.strip() for th in table.find_all('th')]
    rows = table.find_all('tr')

    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        if cols:
            data.append(cols)

    return headers, data

def filter_and_save_data(headers, data, filename='bonds.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # 写入列名
        writer.writerow(headers)
        # 遍历数据
        for row in data:
            # 根据条件筛选数据
            bond_type = row[headers.index('Bond Type')]
            issue_year = row[headers.index('Issue Date')].split('-')[0]
            if bond_type == 'Treasury Bond' and issue_year == '2023':
                writer.writerow(row)

# 主程序入口
if __name__ == "__main__":
    url = "https://iftp.chinamoney.com.cn/english/bdInfo/"  # 更改为实际URL
    headers, data = fetch_bond_data(url)
    filter_and_save_data(headers, data)
