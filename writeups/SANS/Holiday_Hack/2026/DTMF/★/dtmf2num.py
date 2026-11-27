import numpy as np
from scipy.io import wavfile
from scipy.signal import find_peaks

sr, data = wavfile.read("train_station.wav")
data = data.astype(float)

low = [697, 770, 852, 941]
high = [1209, 1336, 1477, 1633]

keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

def detect_tone(start, end):
    # 指定時間の音声を切り出す
    segment = data[int(start*sr):int(end*sr)]

    # FFT
    window = np.hanning(len(segment))
    spectrum = np.abs(
        np.fft.rfft(segment * window)
    )
    freq = np.fft.rfftfreq(len(segment), 1/sr)

    # 指定周波数付近のピークを取得
    def nearest_peak(targets):
        results = []

        for target in targets:
            idx = np.where(
                (freq >= target-20) &
                (freq <= target+20)
            )[0]

            results.append(
                (target, spectrum[idx].max())
            )

        return max(results, key=lambda x: x[1])[0]

    l = nearest_peak(low)
    h = nearest_peak(high)

    return keys[low.index(l)][high.index(h)]

times = [
    (62.10, 62.41),
    (62.64, 62.94),
    (63.26, 63.47),
    (63.68, 63.96),
    (64.20, 64.52),
    (64.73, 65.05),
    (65.27, 65.55),
    (65.80, 66.10)
]

code = "".join(
    detect_tone(start, end)
    for start, end in times
)

print("DTMF Code:", code)
