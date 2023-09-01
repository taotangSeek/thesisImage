import matplotlib.pyplot as plt
import numpy as np

# 假设您有四个算法的RTT数据
gcc_rtt = [10, 20, 30, 40, 50]
onrl_rtt = [15, 25, 35, 45, 55]
orca_plus_rtt = [12, 22, 32, 42, 52]
loki_rtt = [18, 28, 38, 48, 58]

# 计算CDF
num_bins = 20
gcc_counts, gcc_bin_edges = np.histogram(gcc_rtt, bins=num_bins)
gcc_cdf = np.cumsum(gcc_counts)
onrl_counts, onrl_bin_edges = np.histogram(onrl_rtt, bins=num_bins)
onrl_cdf = np.cumsum(onrl_counts)
orca_plus_counts, orca_plus_bin_edges = np.histogram(orca_plus_rtt, bins=num_bins)
orca_plus_cdf = np.cumsum(orca_plus_counts)
loki_counts, loki_bin_edges = np.histogram(loki_rtt, bins=num_bins)
loki_cdf = np.cumsum(loki_counts)

# 绘制CDF图
plt.plot(gcc_bin_edges[1:], gcc_cdf / gcc_cdf[-1], color='black', label='GCC')
plt.plot(onrl_bin_edges[1:], onrl_cdf / onrl_cdf[-1], color='red', label='OnRL')
plt.plot(orca_plus_bin_edges[1:], orca_plus_cdf / orca_plus_cdf[-1], color='yellow', label='Orca-plus')
plt.plot(loki_bin_edges[1:], loki_cdf / loki_cdf[-1], color='purple', label='Loki')

plt.xlabel('RTT (ms)')
plt.ylabel('CDF')
plt.legend(loc='best')
plt.show()
