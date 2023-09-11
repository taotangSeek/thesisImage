import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# 字体
mpl.rcParams['font.family'] = 'Times New Roman'
# 从CSV文件读取数据
data = pd.read_csv('../data/combined_data.csv')
label_name = [ 'RSRP', 'RSRQ', 'SNR', 'CQI','RSSI' , 'DL_bitrate']

# 计算Pearson相关系数
corr_matrix = data.corr()

# 获取相关系数矩阵的值
corr_values = corr_matrix.values

# 绘制热力图
plt.imshow(corr_values, cmap='coolwarm', vmin=-1, vmax=1, interpolation='nearest')

# 添加颜色栏并设置字体大小、分度值和边框
cbar = plt.colorbar(extend='neither', ticks=np.arange(-1, 1.1, 0.2))
cbar.ax.tick_params(labelsize=16)
cbar.outline.set_visible(False)

# 设置颜色映射范围为-1到1，分度值为0.1
plt.clim(-1, 1)
plt.gca().set_xticks(np.arange(len(data.columns)))
plt.gca().set_yticks(np.arange(len(data.columns)))

# 去除黑色边框
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

# 设置坐标轴标签
data_names = data.columns.tolist()
plt.xticks(np.arange(len(data_names)), data_names, rotation=45)
plt.yticks(np.arange(len(data_names)), data_names)

# 在热力图每个单元格中心位置添加文本标签
for i in range(len(data_names)):
    for j in range(len(data_names)):
        plt.text(j, i, f'{corr_values[i, j]:.2f}', ha='center', va='center', color='white', fontsize = 14)


# 将数字坐标转换为对应的数据名称
ax = plt.gca()
ax.set_xticklabels(label_name, fontsize = 15)
ax.set_yticklabels(label_name, fontsize = 18)

plt.tight_layout()
# 显示图形
plt.show()