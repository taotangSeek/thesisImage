import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

'''
    数据输入
'''
x_label = ['Stall rate(%)', 'Stall rate(%)', 'Stall rate(%)', 'Stall rate(%)']
y_label = ['Throughput(Mbps)', 'Throughput(Mbps)', 'Throughput(Mbps)', 'Throughput(Mbps)']
Sub_title = ['High-quality', 'Low-quality', 'WiFi', '4G']
x_data = [[1.8, 2.1, 2.4, 2.83], [0.5, 1.2, 1.8, 2.5], [1.2, 1.5, 1.8, 2.1], [0.8, 1.5, 1.9, 2.3]]
y_data = [[2.5, 3, 2.6, 3.2], [2.8, 2.2, 2.5, 2.9], [0.9, 1.2, 1.5, 1.8], [2.8, 2.4, 2.7, 2.9]]
features = ['Feature 1', 'Feature 2', 'Feature 3', 'Feature 4']
ellipse_width = [[1, 1.2, 1.5, 2], [0.8, 0.9, 1.1, 1.3], [1.2, 1.5, 1.8, 2.1], [0.9, 1, 1.2, 1.4]]
ellipse_height = [[0.7, 1.2, 1.5, 0.9], [0.6, 1, 1.3, 0.8], [0.9, 1.2, 1.5, 1.8], [0.8, 0.9, 1.1, 1.3]]
ellipse_angle = [[30, 90, 120, 50], [45, 60, 75, 90], [60, 120, 180, 240], [30, 45, 60, 75]]


'''
    代码部分
    默认四个图 可自行修改
'''


colors = ['orange', 'lime', 'violet', 'deepskyblue']
out_colors = ['navajowhite', 'lightgreen', 'plum', 'skyblue']

sizes = [100, 100, 100, 100]
markers = ['o', 's', '^', '*']

label_markers = ['(a)', '(b)', '(c)', '(d)']
# 子图创建
fig, axes = plt.subplots(nrows=1, ncols=4, figsize=(16, 4))

for i, ax in enumerate(axes):
    for j in range(len(x_label)):

        # 椭圆中心点
        ax.scatter(x_data[i][j], y_data[i][j], c=colors[j], s=sizes[j], label=features[j],
                   marker=markers[j], edgecolors='black',linewidths=1)

        # 创建椭圆对象
        ellipse = Ellipse((x_data[i][j], y_data[i][j]), width=ellipse_width[i][j], height=ellipse_height[i][j],
                          angle=ellipse_angle[i][j],
                          facecolor=out_colors[j], alpha=0.5)  # Set alpha value for transparency

        # 添加椭圆对象
        ax.add_artist(ellipse)


        # ax.scatter(x_data[i][j], y_data[i][j], c=colors[j], s=sizes[j], marker=markers[j], edgecolors='black',
        #            linewidths=1, label=features[j])

    # 子图标签和title
    ax.set_xlabel(x_label[i], fontsize=15)
    ax.set_ylabel(y_label[i], fontsize=15)
    ax.set_title(Sub_title[i], fontsize=18)

    # 添加刻度线
    ax.yaxis.grid(True, linestyle='dashed', linewidth=0.3)
    ax.xaxis.grid(True, linestyle='dashed', linewidth=0.3)


    ax.set_xlim(1, 4)
    ax.set_ylim(1, 4)

    # 添加 (a), (b), (c), (d) 标签
    ax.text(0.5, -0.25, label_markers[i] + Sub_title[i], transform=ax.transAxes, fontsize=16, va='top', ha='center')


# Show the plot
plt.tight_layout()
plt.show()