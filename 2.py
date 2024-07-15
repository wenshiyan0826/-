import re    # 导入Python的re模块来使用正则表达式功能
def reg_search(text, regex_list):
    results = []
    # 遍历正则表达式字典
    for key, regex in regex_list.items():
        # 使用正则表达式搜索文本
        matches = re.findall(regex, text)
        # 如果找到匹配项，则添加到结果中
        if matches:
            results.append({key: matches})
    return results

# 定义文本
text = '''
标的证券：本期发行的证券为可交换为发行人所持中国长江电力股份
有限公司股票（股票代码：600900.SH，股票简称：长江电力）的可交换公司债券。
换股期限：本期可交换公司债券换股期限自可交换公司债券发行结束
之日满 12 个月后的第一个交易日起至可交换债券到期日止，即 2023 年 6 月 2
日至 2027 年 6 月 1 日止。
'''

# 定义正则表达式列表
regex_list = {
    '标的证券': r'\d{6}\.\w{2}',  # 匹配股票代码，如 "600900.SH"
    '换股期限': r'\d{4} 年 \d{1,2} 月 \d{1,2} 日'  # 匹配日期
}

# 调用函数并打印结果
result = reg_search(text, regex_list)
print(result)