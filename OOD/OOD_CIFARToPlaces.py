import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(color_codes=True)
plt.figure(figsize=(9, 6))
fig, ax = plt.subplots(dpi=1000)  # fig表示整张图片，ax表示图片中的各个图表
n = 5
X = np.arange(n) + 1.0
width = 0.45
# X是1,2,3,4,5,6,7,8,柱的个数
# numpy.random.uniform(low=0.0, high=1.0, size=None), normal
# uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
MEDL = [0,13,15,32,440]
MTEDL = [0,0,0,43,457]
plt.bar(X - width / 2, MEDL, width=width, label="MEDL")
# width:柱的宽度
plt.bar(X + width / 2, MTEDL, width=width,label="MTEDL")
uncertainty_intervel = ['[0.0,0.2)','[0.2,0.4)','[0.4,0.6)','[0.6,0.8)','[0.8,1.0)']
index = np.arange(len(uncertainty_intervel))
# 水平柱状图plt.barh，属性中宽度width变成了高度height
# 打两组数据时用+
# facecolor柱状图里填充的颜色
# edgecolor是边框的颜色
# 想把一组数据打到下边，在数据前使用负号
# plt.bar(X, -Y2, width=width, facecolor='#ff9999', edgecolor='white')
# 给图加text
for x, y in zip(X, MEDL):
    plt.text(x - width / 2, y + 0.05, y, ha='center', va='bottom')

for x, y in zip(X, MTEDL):
    plt.text(x + width / 2, y + 0.05,  y, ha='center', va='bottom')
plt.xticks(index+1, uncertainty_intervel,fontsize=12)
plt.legend(fontsize=15)
ax.set_xlabel("Uncertainty Intervel", fontsize=13)  # 横坐标标签
ax.set_ylabel("Number of Samples", fontsize=13)  # 纵坐标标签
plt.title(r'${\rm\;CIFAR-FS\rightarrow Places\;(OOD\;samples)}$',fontsize=15)
plt.show()