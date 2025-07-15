# read the ..\csv\8DPSK_500Mbps_5u.csv
# change the header to be time,data
# make sure the time starts from 0
# save it to ..\csv\8DPSK_500Mbps_5u_t0.csv

import pandas as pd
import os

input_path = 'v6_250708/csv/8PPM_D2PSK_500Mbps.csv'
output_path = 'v6_250708/csv/8PPM_D2PSK_500Mbps_t0.csv'

# 读取原CSV文件
input_file = os.path.join(input_path)
output_file = os.path.join(output_path)

# 读取CSV文件
df = pd.read_csv(input_file)

# 获取列名并重命名为time和data
columns = df.columns.tolist()
df.columns = ['time', 'data']

# 确保时间从0开始
if len(df) > 0:
    time_start = df['time'].iloc[0]
    df['time'] = df['time'] - time_start

# 保存处理后的文件
df.to_csv(output_file, index=False)

print(f"原文件: {input_file}")
print(f"输出文件: {output_file}")
print(f"原header: {columns}")
print(f"新header: ['time', 'data']")
print(f"数据行数: {len(df)}")
if len(df) > 0:
    print(f"时间范围: {df['time'].min()} 到 {df['time'].max()}")
print("处理完成！")
