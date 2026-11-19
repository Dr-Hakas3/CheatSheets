import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

sr, data = wavfile.read("train_station.wav")

# 正規化
data = data.astype(float) / 32768

# スペクトログラム
f, t, S = spectrogram(
    data,
    sr,
    nperseg=4096,
    noverlap=3616
)

plt.figure(figsize=(15, 6))
plt.pcolormesh(t, f, 10*np.log10(S + 1e-12),
               shading="auto")
plt.ylim(600, 1700)
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency (Hz)")
plt.colorbar(label="Power (dB)")
plt.show()
