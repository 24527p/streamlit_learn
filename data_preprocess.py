import pandas as pd

pd.set_option('display.unicode.east_asian_width', True)

penguin_df = pd.read_csv('penguins-chinese.csv', encoding='gbk')

penguin_df.dropna(inplace=True)

output = penguin_df['企鹅的种类']

features = penguin_df[['企鹅栖息的岛屿', '喙的长度','喙的深度', '翅膀的长度', '身体质量', '性别']]

features = pd.get_dummies(features)

output_codes, output_uniques = pd.factorize(output)

print('下面是去重后，目标输出变量的数据：')
print(output_uniques)
print('下面是独热编码后，特征列的数据：')
print(features.head())