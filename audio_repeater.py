import sounddevice as sd
import numpy as np
import librosa

# Set the sampling frequency and duration of the recording
fs = 44100
duration = 5

# Record the audio using sounddevice
print("Recording...")
audio = sd.rec(int(fs * duration), samplerate=fs, channels=1)
sd.wait()

# Convert the audio data to a one-dimensional array
audio = np.squeeze(audio)

# Apply noise reduction using the Wiener filter
noise = np.random.randn(len(audio))
audio_n = audio + 0.5 * noise
audio_nr = librosa.decompose.nn_filter(audio_n, aggregate=np.median, metric='cosine', width=int(librosa.time_to_samples(0.025, sr=fs)))

# Play back the denoised audio using sounddevice
print("Playing Back...")
sd.play(audio_nr, samplerate=fs)

# Wait for the playback to finish
sd.wait()
