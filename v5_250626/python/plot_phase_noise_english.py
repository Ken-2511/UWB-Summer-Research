import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_phase_noise_data():
    """
    Read and plot phase noise data
    """
    # Read CSV file
    file_path = '../matlab/phase_noise_data_1.csv'
    
    try:
        # Read CSV data
        data = pd.read_csv(file_path)
        
        # Extract time and data columns
        time = data['Time']
        signal_data = data['Data']
        
        # Create figure
        plt.figure(figsize=(12, 8))
        
        # Plot time domain signal
        plt.subplot(2, 1, 1)
        plt.plot(time, signal_data, 'b-', linewidth=0.8, alpha=0.7)
        plt.title('Phase Noise Data - Time Domain', fontsize=14, fontweight='bold')
        plt.xlabel('Time (seconds)', fontsize=12)
        plt.ylabel('Amplitude', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xlim(time.min(), time.max())
        
        # Add statistics
        mean_val = signal_data.mean()
        std_val = signal_data.std()
        plt.text(0.02, 0.98, f'Mean: {mean_val:.6f}\nStd Dev: {std_val:.6f}', 
                transform=plt.gca().transAxes, verticalalignment='top',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        # Plot data distribution histogram
        plt.subplot(2, 1, 2)
        plt.hist(signal_data, bins=50, alpha=0.7, color='skyblue', edgecolor='black')
        plt.title('Data Distribution Histogram', fontsize=14, fontweight='bold')
        plt.xlabel('Amplitude', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        plt.savefig('phase_noise_analysis_en.png', dpi=300, bbox_inches='tight')
        
        # Show figure
        plt.show()
        
        # Print basic statistics
        print("="*50)
        print("Data Statistics:")
        print(f"Total data points: {len(signal_data)}")
        print(f"Time range: {time.min():.2e} ~ {time.max():.2e} seconds")
        print(f"Data range: {signal_data.min():.6f} ~ {signal_data.max():.6f}")
        print(f"Mean: {mean_val:.6f}")
        print(f"Standard deviation: {std_val:.6f}")
        print(f"Non-zero data points: {np.count_nonzero(signal_data)}")
        print("="*50)
        
    except FileNotFoundError:
        print(f"Error: File not found {file_path}")
        print("Please check if the file path is correct")
    except Exception as e:
        print(f"Error reading file: {e}")

def plot_detailed_analysis():
    """
    Detailed analysis and visualization
    """
    file_path = '../matlab/phase_noise_data_1.csv'
    
    try:
        data = pd.read_csv(file_path)
        time = data['Time']
        signal_data = data['Data']
        
        # Create detailed analysis plots
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        
        # 1. Complete time domain signal
        axes[0, 0].plot(time, signal_data, 'b-', linewidth=0.5, alpha=0.8)
        axes[0, 0].set_title('Complete Time Domain Signal', fontweight='bold')
        axes[0, 0].set_xlabel('Time (seconds)')
        axes[0, 0].set_ylabel('Amplitude')
        axes[0, 0].grid(True, alpha=0.3)
        
        # 2. Zoom in on non-zero region
        non_zero_indices = signal_data != 0
        if non_zero_indices.any():
            time_nz = time[non_zero_indices]
            data_nz = signal_data[non_zero_indices]
            axes[0, 1].plot(time_nz, data_nz, 'r-', linewidth=0.8)
            axes[0, 1].set_title('Non-Zero Data Region (Zoomed)', fontweight='bold')
            axes[0, 1].set_xlabel('Time (seconds)')
            axes[0, 1].set_ylabel('Amplitude')
            axes[0, 1].grid(True, alpha=0.3)
        
        # 3. Data distribution
        axes[1, 0].hist(signal_data, bins=50, alpha=0.7, color='lightgreen', edgecolor='black')
        axes[1, 0].set_title('Data Distribution', fontweight='bold')
        axes[1, 0].set_xlabel('Amplitude')
        axes[1, 0].set_ylabel('Frequency')
        axes[1, 0].grid(True, alpha=0.3)
        
        # 4. Cumulative distribution function
        sorted_data = np.sort(signal_data)
        cumulative = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        axes[1, 1].plot(sorted_data, cumulative, 'purple', linewidth=2)
        axes[1, 1].set_title('Cumulative Distribution Function (CDF)', fontweight='bold')
        axes[1, 1].set_xlabel('Amplitude')
        axes[1, 1].set_ylabel('Cumulative Probability')
        axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('detailed_phase_noise_analysis_en.png', dpi=300, bbox_inches='tight')
        plt.show()
        
    except Exception as e:
        print(f"Error in detailed analysis: {e}")

def plot_frequency_analysis():
    """
    Frequency domain analysis
    """
    file_path = '../matlab/phase_noise_data_1.csv'
    
    try:
        data = pd.read_csv(file_path)
        time = data['Time']
        signal_data = data['Data']
        
        # Calculate sampling rate
        dt = time[1] - time[0]  # time step
        fs = 1/dt  # sampling frequency
        
        # Perform FFT
        fft_data = np.fft.fft(signal_data)
        freqs = np.fft.fftfreq(len(signal_data), dt)
        
        # Only take positive frequencies
        positive_freqs = freqs[:len(freqs)//2]
        positive_fft = np.abs(fft_data[:len(fft_data)//2])
        
        # Create frequency analysis plot
        plt.figure(figsize=(12, 8))
        
        # Time domain plot
        plt.subplot(2, 1, 1)
        plt.plot(time*1e9, signal_data, 'b-', linewidth=0.8, alpha=0.7)
        plt.title('Phase Noise - Time Domain', fontsize=14, fontweight='bold')
        plt.xlabel('Time (nanoseconds)', fontsize=12)
        plt.ylabel('Amplitude', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        # Frequency domain plot
        plt.subplot(2, 1, 2)
        plt.semilogy(positive_freqs/1e6, positive_fft, 'r-', linewidth=0.8, alpha=0.7)
        plt.title('Phase Noise - Frequency Domain (FFT)', fontsize=14, fontweight='bold')
        plt.xlabel('Frequency (MHz)', fontsize=12)
        plt.ylabel('Magnitude (log scale)', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('phase_noise_frequency_analysis.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"Sampling frequency: {fs/1e9:.2f} GHz")
        print(f"Frequency resolution: {fs/len(signal_data)/1e6:.2f} MHz")
        
    except Exception as e:
        print(f"Error in frequency analysis: {e}")

if __name__ == "__main__":
    print("Starting phase noise data plotting...")
    plot_phase_noise_data()
    
    print("\nGenerating detailed analysis plots...")
    plot_detailed_analysis()
    
    print("\nGenerating frequency domain analysis...")
    plot_frequency_analysis()
    
    print("\nPlotting complete! Images saved as:")
    print("- phase_noise_analysis_en.png")
    print("- detailed_phase_noise_analysis_en.png") 
    print("- phase_noise_frequency_analysis.png") 