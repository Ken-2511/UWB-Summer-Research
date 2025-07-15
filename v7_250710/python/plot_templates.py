import pandas as pd
import matplotlib.pyplot as plt

# File paths
template1_path = "../csv/template1.csv"
template2_path = "../csv/template2.csv"

# Read the template CSV files
df_template1 = pd.read_csv(template1_path)
df_template2 = pd.read_csv(template2_path)

print(f"Template 1 shape: {df_template1.shape}")
print(f"Template 2 shape: {df_template2.shape}")

# Create plots
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