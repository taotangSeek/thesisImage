import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

def compute_cdf(data):
    n = len(data)
    x = np.sort(data)
    y = np.arange(1, n+1) / n
    return x, y

def pad_cdf(cdf, k):
    x, y = cdf
    if x[0] > k:
        x = np.insert(x, 0, k)
        y = np.insert(y, 0, 0)
    elif x[-1] < k:
        x = np.append(x, k)
        y = np.append(y, 1)
    return x, y

# 3G 数据提取
bandwidth_3G_data = []
with open('../data/bandwidth/3G_bandwidth.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        bandwidth = float(row[0])
        bandwidth_3G_data.append(bandwidth)

# 4G 提取
bandwidth_4G_data = []
with open('../data/bandwidth/4G_bandwidth.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        bandwidth = float(row[0])
        bandwidth_4G_data.append(bandwidth)

# 5G 提取
bandwidth_5G_data = []
with open('../data/bandwidth/5G_bandwidth_new2.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        bandwidth = float(row[0])
        bandwidth_5G_data.append(bandwidth)


#NYU
bandwidth_NYU_data = []
with open('../data/bandwidth/NYU_dataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # if len(row) == 0 or row[0] == '':
        #     continue  # 跳过空行
        try:
            bandwidth = float(row[0])
            bandwidth_NYU_data.append(bandwidth)
        except ValueError:
            continue  # 跳过无法解析为浮点数的行

#Cellular Traffic
bandwidth_CTAM_data = []
row_count = 0  # 计数器变量
with open('../data/bandwidth/CTAM_total.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) == 0 or row[0] == '':
            continue  # 跳过空行
        try:
            bandwidth = float(row[0]) / 1000
            bandwidth_CTAM_data.append(bandwidth)
            row_count += 1  # 计数器递增
            if row_count == 180000:
                break  # 达到18万行，停止提取数据
        except ValueError:
            continue  # 跳过无法解析为浮点数的行

# 计算cdf：
cdf_3g = compute_cdf(bandwidth_3G_data)
cdf_4g = compute_cdf(bandwidth_4G_data)
cdf_5g = compute_cdf(bandwidth_5G_data)
cdf_NYU = compute_cdf(bandwidth_NYU_data)
cdf_CTAM = compute_cdf(bandwidth_CTAM_data)

# 填充到k值
end_x = 350  # 设置end_x值  最大的x值

cdf_3g = pad_cdf(cdf_3g, end_x)
cdf_4g = pad_cdf(cdf_4g, end_x)
cdf_5g = pad_cdf(cdf_5g, end_x)
cdf_NYU = pad_cdf(cdf_NYU, end_x)
cdf_CTAM = pad_cdf(cdf_CTAM, end_x)
# 画图
plt.plot(cdf_3g[0], cdf_3g[1], label='3G_HSDPA', color='firebrick', linewidth=2.5)
plt.plot(cdf_4g[0], cdf_4g[1], label='4G_LTE', color='seagreen',linewidth=2.5)
plt.plot(cdf_5g[0], cdf_5g[1], label='5G', color='royalblue',linewidth=2.5)
plt.plot(cdf_NYU[0], cdf_NYU[1], label='NYU_Mets', color='goldenrod',linewidth=2.5)
plt.plot(cdf_CTAM[0], cdf_CTAM[1], label='Cellular Traffic', color='mediumpurple',linewidth=2.5)



# 添加网格线
plt.grid(True, linestyle='--', linewidth=1, alpha=0.7)

plt.xlim([0, end_x])
plt.ylim([0.7, 1.04])

plt.xlabel('Bandwidth(Mbps)', fontsize=20)
plt.ylabel('CDF', fontsize=20)

# 设置x轴和y轴刻度的字体大小
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

plt.legend(fontsize=18)

# 在绘制折线的同时添加标记
num_points = 8  # 每条折线上要添加的标记数量
x_points = np.linspace(0, end_x, num_points)  # 在x轴上均匀选择要添加标记的位置

for x in x_points:
    y_3g = np.interp(x, cdf_3g[0], cdf_3g[1])
    y_4g = np.interp(x, cdf_4g[0], cdf_4g[1])
    y_5g = np.interp(x, cdf_5g[0], cdf_5g[1])
    y_NYU = np.interp(x, cdf_NYU[0], cdf_NYU[1])
    y_CTAM = np.interp(x, cdf_CTAM[0], cdf_CTAM[1])

    plt.scatter(x, y_3g, marker='s', edgecolors='firebrick', s=100, linewidths=3, facecolors='none', label='3G_HSDPA')
    plt.scatter(x, y_4g, marker='D', edgecolors='seagreen', s=100, linewidths=3, facecolors='none', label='4G_LTE')
    plt.scatter(x, y_5g, marker='^', edgecolors='royalblue', s=100, linewidths=3, facecolors='none', label='5G')
    plt.scatter(x, y_NYU, marker='o', edgecolors='goldenrod', s=100, linewidths=3, facecolors='none', label='NYU_Mets')
    plt.scatter(x, y_CTAM, marker='*', edgecolors='mediumpurple', s=120, linewidths=3, facecolors='none', label='Cellular Traffic')

plt.tight_layout()

plt.show()