import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

'''
    代码编辑，根据需求自行修改
'''

# 折线样式 （修改个数，的话，这里要修改）
line_styles = ['-', '--', ':', '-.']
draw_styles = ['steps-pre', 'default', 'default', 'default']
colors_styles = ['red', 'blue', 'green', 'black']

class LineChart:
    def __init__(self, data, x_label, y_label, line_styles, draw_styles, data_label):
        self.data = data
        self.y_label = y_label
        self.x_label = x_label
        self.line_styles = line_styles
        self.draw_styles = draw_styles
        self.data_label = data_label

    def plot(self):
        x = np.arange(len(self.data[0]))
        fig, ax = plt.subplots(figsize=(15, 7))

        for i, (data_list, line_style, draw_style) in enumerate(zip(self.data, self.line_styles, self.draw_styles)):
            ax.plot(x, data_list, linestyle=line_style, linewidth=2.5, color=colors_styles[i])
            ax.lines[i].set_drawstyle(draw_style)

        # 设置刻度间隔，例如每隔 10 个单位一个刻度
        ax.xaxis.set_major_locator(MaxNLocator(nbins=10, integer=True))
        plt.xlim(0, len(self.data[0]))
        ax.set_ylabel(self.y_label, fontsize=34)
        ax.set_xlabel(self.x_label, fontsize=24)

        # 隐藏上方和右侧边框线
        ax.spines['top'].set_linewidth(2.5)
        ax.spines['right'].set_linewidth(2.5)
        # 增粗下方和左侧边框线
        ax.spines['bottom'].set_linewidth(2.5)
        ax.spines['left'].set_linewidth(2.5)

        # 添加刻度线
        ax.yaxis.grid(True, linestyle='dashed', linewidth=0.5)
        ax.xaxis.grid(True, linestyle='dashed', linewidth=0.5)
        # 添加图例
        handles = []
        for i, line_style in enumerate(self.line_styles):
            handle = plt.Line2D([], [], linestyle=line_style, linewidth=2.5, color=colors_styles[i])
            handles.append(handle)

        legend = fig.legend(
            handles=handles,
            labels=self.data_label,
            loc='upper center',
            bbox_to_anchor=(0.49, 1), # 上引用的位置
            ncol=len(self.data[0]),
            prop={'size': 24, 'weight': 'bold'}
        )
        # 移除边框
        legend.get_frame().set_linewidth(0.0)

        # 横纵坐标 的大小
        ax.tick_params(axis='both', which='major', labelsize=20)

        plt.show()


'''
    数据输入：
'''
np.random.seed(42)  # 设置随机种子，以确保结果可重现
data = [np.random.uniform(low=0, high=150, size=100),
        np.random.uniform(low=50, high=60, size=100),
        np.random.uniform(low=100, high=200, size=100),
        np.random.uniform(low=170, high=200, size=100)]

y_label = 'Bandwidth (Kbps)'
x_label = 'Time(s)'
data_label = ['BOB', 'Gemini','HRCC', 'Heuristic']

# 创建 LineChart 对象并绘制折线图
chart = LineChart(data,x_label, y_label, line_styles, draw_styles, data_label)
chart.plot()


