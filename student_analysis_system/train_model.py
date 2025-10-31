# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import joblib

print("开始模型训练...")

# 1. 加载数据
# 假设CSV文件和这个脚本在同一个目录下
file_path = 'student_data_adjusted_rounded.csv'
try:
    data = pd.read_csv(file_path)
    print("数据加载成功！")
    print("数据前5行:\n", data.head())
except FileNotFoundError:
    print(f"错误：找不到文件 {file_path}。请确保文件路径正确。")
    exit()

# 2. 数据预处理
# 处理类别特征：性别和专业
# 使用 LabelEncoder 将文本转换为模型可以理解的数字
le_gender = LabelEncoder()
le_major = LabelEncoder()

data['性别'] = le_gender.fit_transform(data['性别'])
data['专业'] = le_major.fit_transform(data['专业'])

# 保存这些 Encoder，因为预测时需要用它们把用户的输入转换成同样的数字
joblib.dump(le_gender, 'gender_encoder.joblib')
joblib.dump(le_major, 'major_encoder.joblib')
print("标签编码器已保存。")

# 3. 定义特征 (X) 和目标 (y)
# 我们用除了'学号'和'期末考试分数'之外的所有列来预测'期末考试分数'
features = ['性别', '专业', '每周学习时长（小时）', '上课出勤率', '期中考试分数', '作业完成率']
target = '期末考试分数'

X = data[features]
y = data[target]

print("\n特征 (X) 的前5行:\n", X.head())
print("\n目标 (y) 的前5行:\n", y.head())

# 4. 划分训练集和测试集
# 这样我们可以在一部分数据上训练模型，在另一部分上评估模型性能
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("\n数据已划分为训练集和测试集。")
print(f"训练集大小: {X_train.shape[0]} 行")
print(f"测试集大小: {X_test.shape[0]} 行")

# 5. 选择并训练模型 (优化版，减小模型体积)
# 我们通过减少树的数量和限制树的深度来简化模型
print("\n正在使用参数优化后的随机森林回归器进行训练以减小模型体积...")
model = RandomForestRegressor(
    n_estimators=20,         # 大幅减少树的数量 (原为 100)。这是减小体积最关键的一步。
    max_depth=10,            # 限制每棵树的最大深度，防止树长得过于复杂。
    min_samples_leaf=5,      # 规定一个叶节点上最少需要有5个样本，这也能有效简化树的结构。
    random_state=42
)
model.fit(X_train, y_train)
print("模型训练完成！")


# ... (评估代码) ...

# 7. 保存训练好的模型 (增加压缩)
model_filename = 'model.joblib'
# 使用 joblib 的压缩功能，compress 参数值从 1 到 9，数字越大压缩率越高，但保存和加载会稍慢
joblib.dump(model, model_filename, compress=3) 

print(f"\n模型已成功应用压缩并保存为 {model_filename}")