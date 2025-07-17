import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp
from dataclasses import dataclass, field

period = 127
# Read CSV file
df = pd.read_csv('v8_250715/python/bit_sequence_8psk.csv')


for i in range(len(df)-period):
    if df['8psk_bit'][i] != df['8psk_bit'][i+period]:
        print("not repeated at", i)

print("all repeated")