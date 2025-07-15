import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r".\phase_noise_data_1.csv")

plt.plot(df['time'], df['data'])
plt.show()
