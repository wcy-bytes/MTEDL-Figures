import matplotlib.pyplot as plt

# 设置默认字体，选择支持中文的字体以避免出现中文乱码情况
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

MEDL = [100, 100, 99.0,96.5,94.7,93.6,92.2,90.9,89.9,88.7,87.9,85.6,83.8,82.5,81.7,79.7,78.5,76.3,69.8]
MTEDL = [100, 100, 100,99.7,99.1,98.4,97.4,96.0,94.6,92.8,91.0,88.9,87.0,85.5,84.8,84.6,84.6,84.6,84.6]
threshold = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
fig, ax = plt.subplots(dpi=1000)  # fig表示整张图片，ax表示图片中的各个图表
ax.set_xlabel("Uncertainty Threshold u", fontsize=13)  # 横坐标标签
ax.set_ylabel("ACC", fontsize=13)  # 纵坐标标签
ax.plot(threshold, MEDL, marker='s', label='MEDL', markersize=7)  # 横坐标数据+纵坐标数据+图例
ax.plot(threshold, MTEDL, marker='^', label='MTEDL', markersize=10)

plt.legend(fontsize=15)  # 让图例生效
# 添加网格线
plt.grid(True, alpha=0.7, axis='both', linestyle=':')
plt.show(dpi=600)
