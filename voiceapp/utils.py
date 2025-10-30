# import librosa
# import numpy as np
# from pydub import AudioSegment
# import tempfile
# import os
# import time

# def feature_extraction(audio_path):
#     """
#     Extracts acoustic features with robust file handling
#     """
#     temp_files_to_cleanup = []  # Track files we create
    
#     try:
#         print(f"DEBUG: Processing file: {audio_path}")
        
#         current_file = audio_path
        
#         # Convert WebM to WAV if needed
#         if audio_path.lower().endswith('.webm'):
#             print("DEBUG: Converting WebM to WAV...")
            
#             try:
#                 # Load WebM using pydub
#                 audio = AudioSegment.from_file(audio_path, format="webm")
                
#                 # Create a new temporary file for WAV
#                 with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_wav:
#                     wav_path = tmp_wav.name
#                     audio.export(wav_path, format="wav")
                
#                 temp_files_to_cleanup.append(wav_path)
#                 current_file = wav_path
#                 print("DEBUG: WebM converted to WAV successfully")
                
#             except Exception as e:
#                 raise Exception(f"WebM conversion failed: {str(e)}")
        
#         # Load with librosa
#         try:
#             y, sr = librosa.load(current_file, sr=22050)
#             print(f"DEBUG: Audio loaded - Length: {len(y)}, Sample rate: {sr}")
#         except Exception as e:
#             raise Exception(f"Could not load audio file: {str(e)}")
        
#         # Check if audio has content
#         if len(y) == 0:
#             raise Exception("Audio file is empty")
        
#         # Extract features
#         energy = np.mean(librosa.feature.rms(y=y))
#         zcr = np.mean(librosa.feature.zero_crossing_rate(y))
#         spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=y, sr=sr))
        
#         print(f"DEBUG: Features extracted successfully")
        
#         return {
#             "energy": float(energy),
#             "zero_crossing_rate": float(zcr),
#             "spectral_centroid": float(spectral_centroid)
#         }
        
#     except Exception as e:
#         print(f"DEBUG: Error in feature_extraction: {e}")
#         raise Exception(f"Feature extraction failed: {str(e)}")
        
#     finally:
#         # Clean up any temporary files we created
#         for temp_file in temp_files_to_cleanup:
#             safe_delete(temp_file)

# def safe_delete(file_path, max_retries=3, delay=0.1):
#     """
#     Safely delete a file with retry mechanism for Windows
#     """
#     for attempt in range(max_retries):
#         try:
#             if os.path.exists(file_path):
#                 os.unlink(file_path)
#                 print(f"DEBUG: Successfully deleted {file_path}")
#                 return True
#         except PermissionError:
#             if attempt < max_retries - 1:
#                 time.sleep(delay)
#             else:
#                 print(f"WARNING: Could not delete {file_path} after {max_retries} attempts")
#                 return False
#     return False