% Initialize parameters
raw_sample_rate = 16e9;
sample_rate = 40e9;
carrier_freq = 4e9;
symbol_rate = 500e6;
window_len = int32(750e-12 * sample_rate);