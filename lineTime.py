import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 设置字体，包含全角右括号
prop = fm.FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc')  # 修改为你系统中存在的字体文件路径
plt.rcParams['font.family'] = prop.get_name()

# 数据
ports = ['HTTP1', 'HTTP2', 'HTTP3']
categories = ['100KB', '1MB', '5MB', 'small', 'medium', 'large']

data = [
    [1.46, 1.52, 1.52],
    [27.26, 30.09, 29.96],
    [165.67, 30.27, 146.01],
    [12.56, 11.66, 9.23],
    [16.32, 83.98, 11.80],
    [185.99, 218.61, 219.59]
]

# 转置数据矩阵
transposed_data = np.array(data).T.tolist()

# 绘图
fig, ax = plt.subplots()

for i, port in enumerate(ports):
    plt.plot(categories, transposed_data[i], label=port, marker='o')

# 设置标签
ax.set_xlabel("文件大小")
ax.set_ylabel("时间（秒）")

# 添加图例
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

plt.grid(True)
# 设置图表标题
plt.title("文件传输时间")

# 保存图表到文件
output_file_path = "./lineTime.png"  # 替换为你希望保存的文件路径和名称
plt.savefig(output_file_path, bbox_inches="tight")

# 显示图表
plt.show()
