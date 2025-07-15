import pandas as pd
import matplotlib.pyplot as plt
import numpy as np # Import numpy

# --- Parameters ---
resampling_interval = 1 / 16e9  # Target resampling interval in seconds (e.g., 5e-11 for 20 GHz)
# For 10 GHz, use 1e-10
# For 5 GHz, use 2e-10

# Read the CSV file, skipping the first row (header)
df = pd.read_csv("QDPSK_500Mbps_5u.csv", header=0)

# Select the rows (user had 10000:12000, keeping this selection)
df_subset = df.iloc[10000:17000].copy() # Use .copy() to avoid SettingWithCopyWarning

# Ensure data is numeric and store original time and value
original_time = pd.to_numeric(df_subset.iloc[:, 0])
original_value = pd.to_numeric(df_subset.iloc[:, 1])

# Determine the time range for resampling
start_time = original_time.min()
end_time = original_time.max()

# Create the new time axis for resampling
new_time_axis = np.arange(start_time, end_time, resampling_interval)

# Perform linear interpolation
resampled_value = np.interp(new_time_axis, original_time, original_value)

# Create a figure with two subplots
plt.figure(figsize=(12, 10)) # Adjusted figure size for two plots

# Top subplot: Original data
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(original_time, original_value)
plt.xlabel("Time (Original)")
plt.ylabel("Value (Original)")
plt.title("Original Data (Rows 10000-12000)")
plt.grid(True)

# Bottom subplot: Resampled data
plt.subplot(2, 1, 2)
plt.plot(new_time_axis, resampled_value, marker='.', linestyle='-') # Added marker for clarity
plt.xlabel(f"Time (Resampled at {1/resampling_interval/1e9:.1f} GHz)")
plt.ylabel("Value (Resampled)")
plt.title(f"Resampled Data ({1/resampling_interval/1e9:.1f} GHz using Linear Interpolation)")
plt.grid(True)

plt.tight_layout() # Adjust layout to prevent overlapping titles/labels
plt.show()