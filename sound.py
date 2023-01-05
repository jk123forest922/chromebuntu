import wave
import numpy as np
import matplotlib.pyplot as plt

wav_obj = wave.open('/workspace/chromebuntu/LRMonoPhase4.wav', 'rb')
sample_freq = wav_obj.getframerate()
n_samples = wav_obj.getnframes()
n_channels = wav_obj.getnchannels()
signal_wave = wav_obj.readframes(n_samples)
t_audio = n_samples/sample_freq

print(t_audio)
print(sample_freq)
print(n_samples)
print(n_channels)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

l_channel = signal_array[0::2]
r_channel = signal_array[1::2]

times = np.linspace(0, n_samples/sample_freq, num=n_samples)

plt.figure(figsize=(15, 5))
plt.plot(times, l_channel)
plt.title('Left Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.savefig("L_channel")

plt.figure(figsize=(15, 5))
plt.plot(times, r_channel)
plt.title('Right Channel')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.savefig("R_channel")

plt.figure(figsize=(15, 5))
plt.specgram(l_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Right Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.savefig("L_channel_spec")

plt.figure(figsize=(15, 5))
plt.specgram(r_channel, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Right Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.savefig("R_channel_spec")