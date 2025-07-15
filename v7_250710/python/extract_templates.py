up_fs_num = 1024  # 1024 GHz upsampled rate in numerical form

csv_path_up = "v7_250710/csv/phase_noise_8ppm_d2psk_1024GHz.csv"
template1 = "v7_250710/csv/template1.csv"
template2 = "v7_250710/csv/template2.csv"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_loaded = pd.read_csv(csv_path_up)
print(f"Loaded data from '{csv_path_up}'")
print(df_loaded.head())

t1_start = 431;
t2_start = 250+2048*4
template_len = 1024;

df_loaded.iloc[t1_start:t1_start+template_len].to_csv(template1, index=False)
df_loaded.iloc[t2_start:t2_start+template_len].to_csv(template2, index=False)


# Plot the saved templates
try:
	# Read the template CSV files
	df_template1 = pd.read_csv(template1)
	df_template2 = pd.read_csv(template2)
	
	print(f"\nTemplate 1 shape: {df_template1.shape}")
	print(f"Template 2 shape: {df_template2.shape}")
	
	# Create template plots
	plt.figure(figsize=(14, 8))
	
	# Plot 1: Both templates overlaid
	plt.subplot(2, 1, 1)
	plt.plot(df_template1['time'] * 1e9, df_template1['data'], 'b-', label='Template 1', linewidth=1.5)
	plt.plot(df_template2['time'] * 1e9, df_template2['data'], 'r-', label='Template 2', linewidth=1.5)
	plt.xlabel('Time (ns)')
	plt.ylabel('Signal Value')
	plt.title('Template 1 vs Template 2 Comparison')
	plt.legend()
	plt.grid(True, alpha=0.3)
	
	# Plot 2: Templates side by side
	plt.subplot(2, 2, 3)
	plt.plot(df_template1['time'] * 1e9, df_template1['data'], 'b-', linewidth=1.5)
	plt.xlabel('Time (ns)')
	plt.ylabel('Signal Value')
	plt.title('Template 1')
	plt.grid(True, alpha=0.3)
	
	plt.subplot(2, 2, 4)
	plt.plot(df_template2['time'] * 1e9, df_template2['data'], 'r-', linewidth=1.5)
	plt.xlabel('Time (ns)')
	plt.ylabel('Signal Value')
	plt.title('Template 2')
	plt.grid(True, alpha=0.3)
	
	plt.tight_layout()
	plt.show()
	
	# Print some basic info about the templates
	print(f"\nTemplate 1 data range: {df_template1['data'].min():.6f} to {df_template1['data'].max():.6f}")
	print(f"Template 2 data range: {df_template2['data'].min():.6f} to {df_template2['data'].max():.6f}")

except Exception as e:
	print(f"Error reading or plotting templates: {e}")
	


# Plot the complete loaded dataset
try:
	plt.figure(figsize=(15, 8))
	
	# Filter data to show only first 8 ns
	first_8ns_mask = df_loaded['time'] <= 200e-9  # 8 nanoseconds
	first_8ns_data = df_loaded[first_8ns_mask]
	
	# Plot 1: First 8 ns of signal
	plt.subplot(2, 1, 1)
	plt.plot(first_8ns_data['time'] * 1e9, first_8ns_data['data'], 'b-', linewidth=0.8, label='First 8 ns of Signal')
	plt.xlabel('Time (ns)')
	plt.ylabel('Signal Value')
	plt.title('First 8 ns of Phase Noise/Time Jitter Signal')
	plt.grid(True, alpha=0.3)
	plt.legend()
	
	# Plot 2: Same 8 ns view with template extraction regions highlighted
	plt.subplot(2, 1, 2)
	plt.plot(first_8ns_data['time'] * 1e9, first_8ns_data['data'], 'b-', linewidth=0.8, label='Signal')
	
	# Highlight template extraction regions (if they fall within the 8 ns window)
	t1_start = 431
	t2_start = 2479
	template_len = 1024
	
	# Check if template regions fall within the 8 ns window
	if t1_start < len(first_8ns_data) and t1_start + template_len <= len(df_loaded):
		template1_region = df_loaded.iloc[t1_start:t1_start+template_len]
		# Only plot the part that falls within 8 ns
		template1_in_window = template1_region[template1_region['time'] <= 8e-9]
		if len(template1_in_window) > 0:
			plt.plot(template1_in_window['time'] * 1e9, template1_in_window['data'], 'r-', linewidth=2, 
					label=f'Template 1 (samples {t1_start}-{t1_start+template_len})')
	
	if t2_start < len(first_8ns_data) and t2_start + template_len <= len(df_loaded):
		template2_region = df_loaded.iloc[t2_start:t2_start+template_len]
		# Only plot the part that falls within 8 ns
		template2_in_window = template2_region[template2_region['time'] <= 8e-9]
		if len(template2_in_window) > 0:
			plt.plot(template2_in_window['time'] * 1e9, template2_in_window['data'], 'g-', linewidth=2, 
					label=f'Template 2 (samples {t2_start}-{t2_start+template_len})')
	
	plt.xlabel('Time (ns)')
	plt.ylabel('Signal Value')
	plt.title('First 8 ns with Template Extraction Regions Highlighted')
	plt.grid(True, alpha=0.3)
	plt.legend()
	
	plt.tight_layout()
	plt.show()
	
	print(f"\nDataset info:")
	print(f"Total samples in dataset: {len(df_loaded)}")
	print(f"Samples in first 8 ns: {len(first_8ns_data)}")
	print(f"Complete signal duration: {(df_loaded['time'].max() - df_loaded['time'].min()) * 1e9:.3f} ns")
	print(f"Data range (first 8 ns): {first_8ns_data['data'].min():.6f} to {first_8ns_data['data'].max():.6f}")
	print(f"Data range (complete): {df_loaded['data'].min():.6f} to {df_loaded['data'].max():.6f}")

except Exception as e:
	print(f"Error plotting df_loaded: {e}")