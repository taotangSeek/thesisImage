import numpy as np
import matplotlib.pyplot as plt

# 自定义的上升函数
def custom_rising_function(x):
    return x ** 2  # 这里以平方函数作为示例

# 生成随机数据
def generate_rising_data(rising_func, size):
    u = np.random.uniform(0, 1, size)  # 生成均匀分布的随机数
    x = np.sort(rising_func(u))  # 通过逆变换法将均匀分布转换为具有上升趋势的随机数
    return x

# 生成数据并绘制CDF图
data = generate_rising_data(custom_rising_function, 1000)
x = np.linspace(min(data), max(data), 100)
y = np.linspace(0, 1, 100)  # 对于上升函数，y 值范围在 [0, 1] 之间

plt.plot(x, y, label='Custom CDF')
plt.legend()
plt.xlabel('RTT(ms)', fontsize=20)
plt.ylabel('CDF', fontsize=25)
plt.tick_params(axis='both', labelsize=15)

plt.show()