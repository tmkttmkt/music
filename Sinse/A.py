A1_FREQ = 55.0
FREQUENCY = {
    "C": A1_FREQ * 2 ** (-9 / 12.0),
    "C#": A1_FREQ * 2 ** (-8 / 12.0),
    "Db": A1_FREQ * 2 ** (-8 / 12.0),
    "D": A1_FREQ * 2 ** (-7 / 12.0),
    "D#": A1_FREQ * 2 ** (-6 / 12.0),
    "Eb": A1_FREQ * 2 ** (-6 / 12.0),
    "E": A1_FREQ * 2 ** (-5 / 12.0),
    "F": A1_FREQ * 2 ** (-4 / 12.0),
    "F#": A1_FREQ * 2 ** (-3 / 12.0),
    "Gb": A1_FREQ * 2 ** (-3 / 12.0),
    "G": A1_FREQ * 2 ** (-2 / 12.0),
    "G#": A1_FREQ * 2 ** (-1 / 12.0),
    "Ab": A1_FREQ * 2 ** (-1 / 12.0),
    "A": A1_FREQ,
    "A#": A1_FREQ * 2 ** (1 / 12.0),
    "Bb": A1_FREQ * 2 ** (1 / 12.0),
    "B": A1_FREQ * 2 ** (2 / 12.0),
}
def nf(num):
    pa=num%7
    wa=num//7
    base=ord("A")
    base+=pa
    print(num,pa,wa,chr(base))
    return FREQUENCY[chr(base)]*2**(wa-1)
def f(str):
    str=str.upper()
    return FREQUENCY[str[:-1]]*2**(int(str[-1])-1)
normal_stft={
"n_fft" : 2048,           # フーリエ変換に使用するサンプルの数
"hop_length" : 512,       # 隣接するフレーム間のサンプル数
"win_length" : 2048,      # 各フレームに適用されるウィンドウのサイズ
"window" : 'hann',        # ウィンドウ関数
}