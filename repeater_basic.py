import sounddevice as sd

# Set parameters for recording
duration = 5  # seconds
sample_rate = 44100  # samples per second

# Start recording
print("Recording...")
audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1)

# Wait for recording to complete
sd.wait()

# Start playback
print("Playing back...")
sd.play(audio_data, sample_rate)

# Wait for playback to complete
sd.wait()

# Done!
print("Done.")
