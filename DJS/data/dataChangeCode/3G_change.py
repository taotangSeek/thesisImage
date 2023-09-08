import csv

# 读取原始CSV文件并进行数据处理
data = []
with open('./../3G_total.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        value = float(row[1]) / 1000  # 将第二列数据除以1000
        data.append([value])  # 将处理后的数据存储为列表

# 将处理后的数据写入新的CSV文件
with open('../bandwidth/3G_bandwidth.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # writer.writerow(['New Value'])  # 写入新的列标题
    writer.writerows(data)  # 写入处理后的数据

print("结果已写入 output_file.csv")