import wave


def encode(plain_text):
    
    song = wave.open("output.wav", mode='rb')
    # Reading the frames of the song and converting it into byte array

    audio_frame_bytes = bytearray(list(song.readframes(song.getnframes())))

    #plain_text = 'Oh Captain! My Captain!'



    plain_text = plain_text + int((len(audio_frame_bytes)-(len(plain_text)*8*8))/8) *'#'
    #print(int((len(audio_frame_bytes)-(len(plain_text)*8*8))/8))
    #print(plain_text)
    bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in plain_text])))
    #print(bits[:10])
    # Replace LSB of each byte of the audio data by one bit from the text bit array
    for i, bit in enumerate(bits):
        audio_frame_bytes[i] = (audio_frame_bytes[i] & 254) | bit


    #print(len(bits),len(audio_frame_bytes))
    frame_modified = bytes(audio_frame_bytes)

    # Write bytes to a new wave audio file
    with wave.open('song_encoded.wav', 'wb') as fd:
        fd.setparams(song.getparams())
        fd.writeframes(frame_modified)

    song.close()
