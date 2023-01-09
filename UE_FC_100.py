import matplotlib.pyplot as plt

# 设置默认字体，选择支持中文的字体以避免出现中文乱码情况
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

MEDL = [100, 100, 97.0,94.6,90.9,90.1,89.2,87.7,85.3,83.2,80.1,77.3,74.8,72.0,69.1,65.6,61.8,57.4,49.9]
MTEDL = [100, 100, 99.8,99.0,98.7,98.0,96.7,94.8,91.8,89.1,85.4,82.3,79.5,77.7,76.7,76.5,76.4,76.4,76.4]
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
