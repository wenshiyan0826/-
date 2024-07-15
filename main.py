import requests
from bs4 import BeautifulSoup
import csv

# 网址
url = 'https://iftp.chinamoney.com.cn/english/bdInfo/'

# 发送请求
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 假设数据在一个具有特定 ID 的表格中，您需要替换 'table_id' 为实际的 ID
# 由于网页结构未知，这里假设表格的 ID 是 'table_id'
# 实际操作中，需要根据网页源代码确定正确的表格 ID
table = soup.find('table', {'id': 'table_id'})
rows = table.find_all('tr') if table else []

# 准备数据列表
data = []

# 遍历表格行
for row in rows:
    cells = row.find_all('td')
    if cells:  # 防止空行
        bond_type = cells[3].text.strip()  # 假设“债券类型”在第四列
        issue_year = cells[4].text.strip()  # 假设“发行年份”在第五列
        if bond_type == 'Treasury Bond' and issue_year == '2023':
            # 处理和输出符合条件的行
            data.append({
                'ISIN': cells[0].text.strip(),
                'Bond Code': cells[1].text.strip(),
                'Issuer': cells[2].text.strip(),
                'Bond Type': bond_type,
                'Issue Date': cells[5].text.strip(),
                'Latest Rating': cells[6].text.strip()
            })

# 保存数据到 CSV 文件
csv_file_path = 'D:\Pycharm_poject\AAA_demo\\bond_data.csv'

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['ISIN', 'Bond Code', 'Issuer', 'Bond Type', 'Issue Date', 'Latest Rating'])
    writer.writeheader()
    writer.writerows(data)


