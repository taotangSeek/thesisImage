import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch
import matplotlib as mpl

'''
    数据输入
    格式类似
'''
# 数据
data = {'Meet':
            {
                'RTP ML': [-0.11, -0.05, 0.05, 0.15],
                'RTP Heuristic': [-0.13, -0.05, 0.05, 0.16],
                'IP/UDP ML': [-0.14, 0.01, 0.12, 0.25],
                'IP/UDP Heuristic': [-0.01, 0.08, 0.18, 0.51]
            },
        'Teams':
            {
                'RTP ML': [-0.11, -0.05, 0.05, 0.15],
                'RTP Heuristic': [-0.13, -0.05, 0.05, 0.16],
                'IP/UDP ML': [-0.14, -0.01, 0.09, 0.21],
                'IP/UDP Heuristic': [-0.15, -0.01, 0.09, 0.21]
            },
        'Webex':
            {
                'RTP ML': [-0.05, -0.025, 0.025, 0.05],
                'RTP Heuristic': [-0.051, -0.025, 0.025, 0.051],
                'IP/UDP ML': [-0.052, 0.01, 0.03, 0.1],
                'IP/UDP Heuristic':[-0.052, 0.01, 0.03, 0.12]
            },
        }

y_label= 'Bitrate Relative Error'



'''
    代码区域
    有需要自行修改
'''
# 颜色
colors = ['darkslategray', 'darkslateblue', 'palevioletred', 'sandybrown']
percentages = [0.1, 0.2, 0.3, 0.4]

mpl.rcParams['font.family'] = 'Times New Roman'

# 绘制箱线图
fig = plt.figure(figsize=(12 ,7))
ax = fig.add_subplot(1,1,1)

for i,(app_name,data_dict) in enumerate(data.items()):
    for j,(algo_name,data_list) in enumerate(data_dict.items()):
        bp = ax.boxplot(data_list,
                       positions=[i*len(data_dict)+j+1],
                       widths=0.6,
                       patch_artist=True,
                       boxprops=dict(facecolor=colors[j],linewidth=4),
                       medianprops=dict(color='black',linewidth=4),
                       whiskerprops=dict(linewidth=4),
                       capprops=dict(linewidth=4),
                       flierprops=dict(markersize=8))
        # 在箱图上方添加数据
        for k in range(len(bp['medians'])):
            box = bp['medians'][k]
            print(box)
            x = box.get_xdata().mean()
            y = bp['whiskers'][k * 2 + 1].get_ydata()[1]
            ax.text(x - 0.35, y + 0.015, f"{percentages[k]*100:.0f}%", fontsize=21,  weight='bold')  #精确度

# 设置 x 轴刻度和标签
x_ticks = [1.5 + i * len(data_dict) + (len(data_dict) - 1) / 2 for i in range(len(data))]
ax.set_xticks(x_ticks)
ax.set_xticklabels(list(data.keys()), fontsize=28)

# 设置 y 轴标签
ax.set_ylabel(y_label, fontsize=40)

# 添加图例
legend = fig.legend(
    handles=[plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(colors))],
    labels=list(data.values())[0].keys(),
    loc='upper center',
    bbox_to_anchor=(0.56, 0.96),
    ncol=2,
    prop={'size': 25, 'weight': 'bold'}
)
# Remove the frame of the legend
legend.get_frame().set_linewidth(0.0)

# Add a black border around the legend patches
for patch in legend.get_patches():
    patch.set_edgecolor('black')
    patch.set_linewidth(4)

# 设置y轴上限和下限，增加空白地区
ax.set_ylim(bottom=-0.2, top=0.6)
# 添加刻度线
ax.yaxis.grid(True, linewidth=3)

# 隐藏上方和右侧边框线
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# 增粗下方和左侧边框线
ax.spines['bottom'].set_linewidth(2.5)
ax.spines['left'].set_linewidth(2.5)
# 调整子图位置和间距
plt.subplots_adjust(top=0.74)
# 设置 y 轴刻度字体大小和加粗
ax.tick_params(axis='y', labelsize=20, width=2, length=6, pad=8)
# 显示图像
plt.show()
