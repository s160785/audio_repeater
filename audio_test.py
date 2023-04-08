import librosa
import soundfile as sf

# Load the two audio files
y1, sr1 = librosa.load('audio1.mp3', sr=None)
y2, sr2 = librosa.load('audio2.mp3', sr=None)

# Calculate the pitch ratio between the two audio files
pitch_ratio = librosa.piptrack(y=y1, sr=sr1)[0].max() / librosa.piptrack(y=y2, sr=sr2)[0].max()

# Apply the pitch conversion using the phase vocoder algorithm
y2_pitch_shifted = librosa.effects.pitch_shift(y2, sr=sr2, n_steps=librosa.hz_to_midi(pitch_ratio * sr1/sr2) - librosa.hz_to_midi(pitch_ratio), bins_per_octave=12)

# Save the pitch-shifted audio file to disk
# librosa.output.write_wav('output.wav', y2_pitch_shifted, sr2)
sf.write('output.wav',y2_pitch_shifted,sr2)