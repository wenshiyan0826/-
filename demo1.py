import requests
from bs4 import BeautifulSoup
import pandas as pd

# 定义URL和查询条件
url = "https://iftp.chinamoney.com.cn/english/bmkbvl/"
params = {
    "Bond Type": "Treasury Bond",
    "Issue Year": "2023"
}

# 发送HTTP请求
response = requests.get(url, params=params)

# 检查响应状态码
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找表格
    table = soup.find('table')

    if table is None:
        print("未找到表格元素，请检查URL和查询参数是否正确，或网页结构是否发生变化。")
    else:
        # 解析表格数据
        headers = [header.text for header in table.find_all('th')]
        rows = []
        for row in table.find_all('tr')[1:]:
            rows.append([cell.text for cell in row.find_all('td')])

        # 创建DataFrame
        df = pd.DataFrame(rows, columns=headers)

        # 过滤需要的列
        required_columns = ["ISIN", "Bond Code", "Issuer", "Bond Type", "Issue Date", "Latest Rating"]
        df = df[required_columns]

        # 保存为CSV文件
        df.to_csv('treasury_bonds_2023.csv', index=False)
        print("数据已成功保存为 treasury_bonds_2023.csv")
else:
    print(f"请求失败，状态码: {response.status_code}")