# this file is used to read the template from the data, and match the template with the data
# and extract the best-match pulse position

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import signal
import os

# Get the directory of the current Python file
current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)

data_file_name = os.path.join(current_dir, "../csv/phase_noise_8ppm_d2psk_1024GHz.csv")
df = pd.read_csv(data_file_name)
df = df.iloc[:10240, :]
df['data'] = df['data'] / df['data'].abs().max()
print(df.head())
#            time      data
# 0  0.000000e+00  0.000841
# 1  9.765625e-13 -0.002205
# 2  1.953125e-12 -0.005035
# 3  2.929688e-12 -0.007642
# 4  3.906250e-12 -0.010017

# template_file_name = os.path.join(current_dir, "../csv/template.csv")
# tdf = pd.read_csv(template_file_name)
# currently we don't have the template, so generate some fake template for testing
times = np.linspace(0, 750e-12, 1024)
phase0 = np.sin(2*np.pi*times*4e9)
phase1 = np.cos(2*np.pi*times*4e9)

tdf = pd.DataFrame({'phase0': phase0, 'phase1': phase1})
print(tdf.head())
#    phase0  phase1
# 0     1.0    -1.0
# 1     1.0    -1.0
# 2     1.0    -1.0
# 3     1.0    -1.0
# 4     1.0    -1.0


def template_matching_correlate(data, template):
    """
    Template matching using numpy correlate (most elegant method)
    
    Parameters:
    data: 1D numpy array - input data
    template: 1D numpy array - template data
    
    Returns:
    correlation: 1D numpy array - correlation score at each position
    """
    # Use full mode to get complete correlation results
    correlation = np.correlate(data, template, mode='same')
    correlation /= np.max(correlation)
    return correlation


def template_matching_scipy(data, template):
    """
    Template matching using scipy signal correlate (more powerful)
    
    Parameters:
    data: 1D numpy array - input data  
    template: 1D numpy array - template data
    
    Returns:
    correlation: 1D numpy array - correlation score at each position
    """
    # scipy correlate provides more options, such as algorithm selection (fft, direct, etc.)
    correlation = signal.correlate(data, template, mode='full')
    return correlation


def find_best_matches(correlation, num_peaks=5):
    """
    Find the best matching positions
    
    Parameters:
    correlation: 1D numpy array - correlation scores
    num_peaks: int - number of top matches to return
    
    Returns:
    best_positions: 1D numpy array - indices of best matching positions
    best_scores: 1D numpy array - corresponding correlation scores
    """
    # Find the largest peaks
    best_indices = np.argpartition(correlation, -num_peaks)[-num_peaks:]
    # Sort by score from high to low
    best_indices = best_indices[np.argsort(correlation[best_indices])[::-1]]
    
    best_positions = best_indices
    best_scores = correlation[best_indices]
    
    return best_positions, best_scores


# do the template matching
print("\n=== Template Matching Example ===")

# Extract data
data = df['data'].values
template_phase0 = tdf['phase0'].values
template_phase1 = tdf['phase1'].values

print(f"Data length: {len(data)}")
print(f"Template length: {len(template_phase0)}")

# Method 1: Using numpy correlate (recommended)
print("\n--- Using numpy.correlate ---")
correlation_np = template_matching_correlate(data, template_phase0)
print(f"Correlation result length: {len(correlation_np)}")
print(f"Maximum correlation value: {np.max(correlation_np):.6f}")

# Method 2: Using scipy correlate
print("\n--- Using scipy.signal.correlate ---")  
correlation_scipy = template_matching_scipy(data, template_phase0)
print(f"Correlation result length: {len(correlation_scipy)}")
print(f"Maximum correlation value: {np.max(correlation_scipy):.6f}")

# Visualization of results
def plot_template_matching_results(data, template, correlation, title="Template Matching Results"):
    """
    Plot template matching results
    """
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
    
    # Original data
    ax1.plot(data)
    ax1.set_title('Original Data')
    ax1.set_ylabel('Amplitude')
    ax1.grid(True)
    
    # Template
    ax2.plot(template)
    ax2.set_title('Template')
    ax2.set_ylabel('Amplitude')
    ax2.grid(True)
    
    # Data vs. Score
    ax3.plot(data, label='Data')
    ax3.plot(correlation, label='Score')
    ax3.set_title('Data vs. Score')
    ax3.set_xlabel('Position')
    ax3.set_ylabel('Value')
    ax3.grid(True)
    ax3.legend()
    
    plt.tight_layout()
    plt.suptitle(title, y=1.02)
    plt.show()

# Plot results
print("\n=== Plotting Results ===")
if len(template_phase0) <= len(data):
    plot_template_matching_results(data, template_phase0, correlation_np, 
                                "Template Matching: Phase0 Template")
