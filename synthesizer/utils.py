import numpy as np

def decode(in_data, channels=1, chunk=1024, dtype=np.int16):
    """
    Convert a byte stream into a 2D numpy array with
    shape (chunk_size, channels)

    Samples are interleaved, so for a stereo stream with left channel
    of [L0, L1, L2, ...] and right channel of [R0, R1, R2, ...], the output
    is ordered as [L0, R0, L1, R1, ...]
    """
    # TODO: handle data type as parameter, convert between pyaudio/numpy types
    result = np.fromstring(in_data, dtype=dtype)

    if(channels != 1):
        result = np.reshape(result, (chunk, channels))
    return result


def encode(signal, dtype=np.int16):
    """
    Convert a 2D numpy array into a byte stream for PyAudio

    Signal should be a numpy array with shape (chunk_size, channels)
    """
    interleaved = signal.flatten()

    # TODO: handle data type as parameter, convert between pyaudio/numpy types
    out_data = interleaved.astype(dtype).tostring()
    return out_data


def to_stereo(input, panning, volume):
    pan_left = (panning + 1)/2.0
    pan_right = 1-pan_left
    result_L = decode(input)
    result_R = result_L.copy()
    result_L = result_L * pan_left * volume
    result_R = result_R * pan_right * volume
    combined = np.vstack((result_L, result_R)).T
    return encode(combined)
