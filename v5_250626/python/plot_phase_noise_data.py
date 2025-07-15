import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_phase_noise_data():
    """
    读取并绘制相位噪声数据
    """
    # 读取CSV文件
    file_path = '../matlab/phase_noise_data_1.csv'
    
    try:
        # 读取CSV数据
        data = pd.read_csv(file_path)
        
        # 提取时间和数据列
        time = data['Time']
        signal_data = data['Data']
        
        # 创建图形
        plt.figure(figsize=(12, 8))
        
        # 绘制时域信号
        plt.subplot(2, 1, 1)
        plt.plot(time, signal_data, 'b-', linewidth=0.8, alpha=0.7)
        plt.title('相位噪声数据 - 时域图', fontsize=14, fontweight='bold')
        plt.xlabel('时间 (秒)', fontsize=12)
        plt.ylabel('幅值', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xlim(time.min(), time.max())
        
        # 添加统计信息
        mean_val = signal_data.mean()
        std_val = signal_data.std()
        plt.text(0.02, 0.98, f'均值: {mean_val:.6f}\n标准差: {std_val:.6f}', 
                transform=plt.gca().transAxes, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        # 绘制数据分布直方图
        plt.subplot(2, 1, 2)
        plt.hist(signal_data, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
        plt.title('数据分布直方图', fontsize=14, fontweight='bold')
        plt.xlabel('幅值', fontsize=12)
        plt.ylabel('频次', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # 调整布局
        plt.tight_layout()
        
        # 保存图形
        plt.savefig('phase_noise_analysis.png', dpi=300, bbox_inches='tight')
        
        # 显示图形
        plt.show()
        
        # 打印基本统计信息
        print("="*50)
        print("数据统计信息:")
        print(f"数据点总数: {len(signal_data)}")
        print(f"时间范围: {time.min():.2e} ~ {time.max():.2e} 秒")
        print(f"数据范围: {signal_data.min():.6f} ~ {signal_data.max():.6f}")
        print(f"均值: {mean_val:.6f}")
        print(f"标准差: {std_val:.6f}")
        print(f"非零数据点: {np.count_nonzero(signal_data)}")
        print("="*50)
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {file_path}")
        print("请确认文件路径是否正确")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")

def plot_detailed_analysis():
    """
    详细分析和可视化
    """
    file_path = '../matlab/phase_noise_data_1.csv'
    
    try:
        data = pd.read_csv(file_path)
        time = data['Time']
        signal_data = data['Data']
        
        # 创建更详细的分析图
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. 完整时域信号
        axes[0, 0].plot(time, signal_data, 'b-', linewidth=0.5, alpha=0.8)
        axes[0, 0].set_title('完整时域信号', fontweight='bold')
        axes[0, 0].set_xlabel('时间 (秒)')
        axes[0, 0].set_ylabel('幅值')
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. 放大非零区域
        non_zero_indices = signal_data != 0
        if non_zero_indices.any():
            time_nz = time[non_zero_indices]
            data_nz = signal_data[non_zero_indices]
            axes[0, 1].plot(time_nz, data_nz, 'r-', linewidth=0.8)
            axes[0, 1].set_title('非零数据区域放大', fontweight='bold')
            axes[0, 1].set_xlabel('时间 (秒)')
            axes[0, 1].set_ylabel('幅值')
            axes[0, 1].grid(True, alpha=0.3)
        
        # 3. 数据分布
        axes[1, 0].hist(signal_data, bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
        axes[1, 0].set_title('数据分布', fontweight='bold')
        axes[1, 0].set_xlabel('幅值')
        axes[1, 0].set_ylabel('频次')
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. 累积分布函数
        sorted_data = np.sort(signal_data)
        cumulative = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        axes[1, 1].plot(sorted_data, cumulative, 'purple', linewidth=2)
        axes[1, 1].set_title('累积分布函数 (CDF)', fontweight='bold')
        axes[1, 1].set_xlabel('幅值')
        axes[1, 1].set_ylabel('累积概率')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('detailed_phase_noise_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    except Exception as e:
        print(f"详细分析时发生错误: {e}")

if __name__ == "__main__":
    print("开始绘制相位噪声数据...")
    plot_phase_noise_data()
    
    print("\n生成详细分析图...")
    plot_detailed_analysis()
    
    print("\n绘图完成！图像已保存为 'phase_noise_analysis.png' 和 'detailed_phase_noise_analysis.png'") 