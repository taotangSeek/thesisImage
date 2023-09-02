import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
'''
    数据输入
'''

# 数据输入
x = np.arange(1, 40)  # 生成1到20的整数数组
y1 = np.random.normal(0, 0.5, len(x))
y2 = np.random.normal(0, 0.5, len(x))
y3 = np.random.normal(0, 0.5, len(x))
y4 = np.random.normal(0, 0.5, len(x))

# 轴名称 以及 标签
title = 'this is title'
x_label = 'this is x_label'
y_label = 'this is y_label'
# 标签内容：
label1 = 'label1'
label2 = 'testZLabel2'
label3 = 'label3'
label4 = 'label4'



'''
    代码区域
    有需要自动修改
'''
# 字体
mpl.rcParams['font.family'] = 'Times New Roman'

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(10, 5))
# 绘制折线图
line1, = ax.plot(x, y1, color='goldenrod', linewidth=3, marker='o', markersize=6, label=label1)
line2, = ax.plot(x, y2, color='seagreen', linewidth=3, marker='s', markersize=6, label=label2)
line3, = ax.plot(x, y3, color='indigo', linewidth=3, marker='D', markersize=6, label=label3)
# line4, = ax.plot(x, y4, color='seagreen', linewidth=3, marker='^', markersize=6, label=label4)

# 设置标题和标签
ax.set_title(title, fontsize=25)
ax.set_xlabel(xlabel=x_label, fontsize=15)
ax.set_ylabel(ylabel=y_label, fontsize=15)

# 设置刻度标签的字体大小
ax.tick_params(axis='both', labelsize=15)

# 设定y轴 指定的上下界
plt.ylim(-2.5, 1.4)

# 添加网格线
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# 添加图例
ax.legend(loc='best')

## 不好用，自行p图设计
# # 添加圆圈标志
# plt.scatter(x[5], y1[5], marker='o', color='red')  # 在索引为5的位置添加圆圈标志
#
# # 添加椭圆标志
# plt.scatter(x[10], y1[10], marker='o', color='red', s=300, facecolors='none', edgecolors='red')  # 在索引为10的位置添加椭圆标志，设置大小为100
#
# # 添加标注文字
# plt.annotate('Point 1', xy=(x[5], y1[5]), xytext=(x[5]+1, y1[5]+0.5),
#              arrowprops=dict(arrowstyle='->'))  # 在圆圈标志位置添加标注文字，设置箭头样式
#
# plt.annotate('Point 2', xy=(x[10], y1[10]), xytext=(x[10]-2, y1[10]+0.5),
#              arrowprops=dict(arrowstyle='->'))  # 在椭圆标志位置1添加标注文字，设置箭头样式
#

# 显示图表
plt.show()

'''
## 自行涉及注释
# 1. 转折点标记选项：
        'o'：圆形标记 (默认)
        's'：正方形标记
        'D'：菱形标记
        '^'：上三角形标记
        'v'：下三角形标记
        '+'：加号标记
        'x'：叉号标记
'''