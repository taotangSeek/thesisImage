import pandas as pd

def print_values_greater_than(file_path, threshold):
    # 读取CSV文件
    df = pd.read_csv(file_path)

    # 获取大于阈值的值
    filtered_values = df[df > threshold].dropna().values

    # 打印结果
    for value in filtered_values:
        print(value)

# 使用示例
file_path = '../bandwidth/NYU_total_new.csv'
threshold = 120

print_values_greater_than(file_path, threshold)