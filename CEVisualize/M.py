import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams


config = {"font.family" : 'Times New Roman', "font.size": 24 , "mathtext.fontset": 'stix'}
rcParams.update(config)

# 示例数据
categories = [r'$\mathcal{O}_{gT,0}$', r'$\mathcal{O}_{gT,1}$', r'$\mathcal{O}_{gT,2}$', r'$\mathcal{O}_{gT,3}$', r'$\mathcal{O}_{gT,4}$', r'$\mathcal{O}_{gT,5}$', r'$\mathcal{O}_{gT,6}$', r'$\mathcal{O}_{gT,7}$']
num_categories = len(categories)

x = np.arange(num_categories)  # 标签的位置
y_data = [1, 2, 3, 4, 5]
yy_data = [0.2, 0.4, 0.6, 0.8, 1.2, 1.4, 1.6, 1.8, 2.2, 2.4, 2.6, 2.8, 3.2, 3.4, 3.6, 3.8, 4.2, 4.4, 4.6, 4.8, 5.2, 5.4]

width = 0.12  # 柱子的宽度



# 具体数据
data_3TeV_1ab = [0.434, 0.403, 0.346, 0.346, 0.53, 0.493, 0.409, 0.423]
data_10TeV_10ab = [1.44,  1.31, 1.10,  1.13, 1.75,  1.6, 1.34 , 1.38]
data_14TeV_10ab = [1.87,  1.72,1.43 , 1.48,  2.28,  2.1, 1.76, 1.81]
data_14TeV_20ab = [2.01, 1.85, 1.54, 1.59, 2.46, 2.26, 1.89, 1.95]
data_30TeV_10ab = [3.34, 3.07, 2.57, 2.64,  4.09, 3.75,  3.14, 3.23]
data_30TeV_90ab = [4.29, 3.94, 3.29,  3.39, 5.25, 4.81, 4.03, 4.14]

# 创建画布
fig, ax = plt.subplots(figsize=(14, 8))

# 添加虚线
for i in range(1, num_categories):
    plt.axvline(x=i - 0.5, color='silver', alpha=0.7, linestyle='--', linewidth=2, zorder=1)
for j in y_data:
    plt.axhline( y=j, color='lightgray', linestyle='-', linewidth=2, zorder=1)
for k in yy_data:
    plt.axhline( y=k, color='gainsboro', linestyle='--', linewidth=0.7, zorder=1)


# 画柱形图，调整颜色的透明度
bars1 = ax.bar(x - 2.5 * width, data_3TeV_1ab, width, label='3 TeV  1 ab$^{-1}$', color='gold',alpha=0.9,   zorder=2)
bars2 = ax.bar(x - 1.5 * width, data_10TeV_10ab, width, label='10 TeV  10 ab$^{-1}$', color='limegreen',alpha=0.9,  zorder=2)
bars3 = ax.bar(x - 0.5 * width, data_14TeV_10ab, width, label='14 TeV  10 ab$^{-1}$', color='coral',alpha=0.9, zorder=2)
bars4 = ax.bar(x + 0.5 * width, data_14TeV_20ab, width, label='14 TeV  20 ab$^{-1}$', color='red',alpha=0.9, zorder=2)
bars5 = ax.bar(x + 1.5 * width, data_30TeV_10ab, width, label='30 TeV  10 ab$^{-1}$', color='dodgerblue',alpha=0.9, zorder=2)
bars6 = ax.bar(x + 2.5 * width, data_30TeV_90ab, width, label='30 TeV  90 ab$^{-1}$', color='steelblue',alpha=0.9, zorder=2)

#font = {'family' : 'Times New Roman' , 'weight' : 'normal' , 'size' : 24}
#matplotlib.rc("font", **font)

# 添加标签和标题
ax.set_ylabel('$\mathit{M}$ $\mathrm{[TeV]}$')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=24)
ax.legend(loc='upper left', bbox_to_anchor=(0.83, 1.01), fontsize=14)


"""
# 获取所有x轴标签并设置特定标签的字体大小
xtick_labels = ax.get_xticklabels()
xtick_labels[0].set_fontsize(24)  # 调整第一个标签（$\mathcal{O}_{gT,0}$）的字体大小
xtick_labels[1].set_fontsize(24)
xtick_labels[2].set_fontsize(24)
xtick_labels[3].set_fontsize(24)
xtick_labels[4].set_fontsize(24)
xtick_labels[5].set_fontsize(24)
xtick_labels[6].set_fontsize(24)
xtick_labels[7].set_fontsize(24)
"""

# 加粗外框
for spine in ax.spines.values():
    spine.set_linewidth(1.3)  # 设置外框线宽



# 调整布局
plt.tight_layout()

# 保存为PDF文件
plt.savefig('M.pdf', format='pdf')

# 显示图表
#plt.show()
