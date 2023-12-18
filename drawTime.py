import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
# 设置字体，包含全角右括号
prop = fm.FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc')  # 修改为你系统中存在的字体文件路径
plt.rcParams['font.family'] = prop.get_name()
# 数据
ports = ['HTTP1:80', 'HTTP2:443', 'HTTP3:8443']
categories = ['100KB', '1MB', '5MB', 'small', 'medium', 'large']

data = [
    [1.46, 1.52, 1.52],
    [27.26, 30.09, 29.96],
    [165.67, 30.27, 146.01],
    [12.56, 11.66, 9.23],
    [16.32, 83.98, 11.80],
    [185.99, 218.61, 219.59]
]

# 绘图
fig, ax = plt.subplots()
im = ax.imshow(data, cmap="Blues")

# 设置轴标签
ax.set_xticks(np.arange(len(ports)))
ax.set_yticks(np.arange(len(categories)))
ax.set_xticklabels(ports)
ax.set_yticklabels(categories)

# 在矩阵单元格中显示数值
for i in range(len(categories)):
    for j in range(len(ports)):
        text = ax.text(j, i, "{:.2f}".format(data[i][j]), ha="center", va="center", color="black")

# 设置标签
ax.set_xlabel("端口")
ax.set_ylabel("文件大小")

# 显示颜色条
cbar = ax.figure.colorbar(im, ax=ax, cmap="Blues")
cbar.set_label("时间（秒）")

# 设置图表标题
plt.title("文件传输时间")

# 保存图表到文件
output_file_path = "./drawTime.png"  # 替换为你希望保存的文件路径和名称
plt.savefig(output_file_path, bbox_inches="tight")


# 显示图表
plt.show()
