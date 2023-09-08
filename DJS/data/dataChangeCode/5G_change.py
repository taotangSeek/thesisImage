import csv

# 读取原始CSV文件并进行数据处理
# data = []
# with open('./../5G_total.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         value = float(row[1]) / 1000  # 将第二列数据除以1000
#         data.append([value])  # 将处理后的数据存储为列表
#
# # 将处理后的数据写入新的CSV文件
# with open('../bandwidth/5G_bandwidth.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     # writer.writerow(['New Value'])  # 写入新的列标题
#     writer.writerows(data)  # 写入处理后的数据

# print("结果已写入 output_file.csv")

# import pandas as pd
#
# # 读取CSV文件
# df = pd.read_csv('../bandwidth/5G_bandwidth.csv', header=None, names=['Bandwidth'])
#
# # 删除所有值为0的行
# df_cleaned = df[df['Bandwidth'] != 0]
#
# # 保存到新的CSV文件
# df_cleaned.to_csv('../bandwidth/5G_bandwidth_new.csv', header=False, index=False)

import pandas as pd

# 读取CSV文件的第一列数据
df = pd.read_csv('../bandwidth/5G_bandwidth_new.csv', usecols=[0], header=None, names=['Bandwidth'])

# 计算上下限
lower_limit = 0.2
upper_limit = 0.4

# 计算删除的数据范围
num_rows = df.shape[0]
start_index = int(num_rows * lower_limit)
end_index = int(num_rows * upper_limit)

# 删除位于0.2到0.4之间的90%的值
df_cleaned = df.drop(df.index[start_index:end_index+1])

# 保存到新的CSV文件
df_cleaned.to_csv('../bandwidth/5G_bandwidth_new2.csv', header=False, index=False)