import numpy as np
import matplotlib.pyplot as plt

def apply_adsr(wave, attack_time, decay_time, sustain_level, release_time, sample_rate):#まだ
    """
    ADSR エンベロープを波形に適用します。
    
    パラメータ:
    - wave: numpy 配列、入力波形。
    - attack_time: float、アタックフェーズの持続時間（秒）。
    - decay_time: float、ディケイフェーズの持続時間（秒）。
    - sustain_level: float、サステインフェーズの振幅レベル（0.0 から 1.0）。
    - release_time: float、リリースフェーズの持続時間（秒）。
    - sample_rate: int、波形のサンプリングレート（サンプル/秒）。
    
    戻り値:
    - numpy 配列、ADSR が適用された波形。
    """

    total_samples = len(wave)
    attack_samples = int(sample_rate * attack_time)
    decay_samples = int(sample_rate * decay_time)
    release_samples = int(sample_rate * release_time)
    sustain_samples = total_samples - (attack_samples + decay_samples + release_samples)

    if sustain_samples < 0:
        raise ValueError("アタック、ディケイ、リリース時間の合計が波形の長さを超えています。")

    # ADSR エンベロープを作成
    attack_curve = np.linspace(0, 1, attack_samples)
    decay_curve = np.linspace(1, sustain_level, decay_samples)
    sustain_curve = np.full(sustain_samples, sustain_level)
    release_curve = np.linspace(sustain_level, 0, release_samples)

    # フェーズを連結
    adsr_envelope = np.concatenate([attack_curve, decay_curve, sustain_curve, release_curve])

    # エンベロープを波形に適用
    processed_wave = wave[:len(adsr_envelope)] * adsr_envelope

    return processed_wave

sample_rate = 44100  # 44.1 kHz
duration = 2.0   
wave=np.ones(int(sample_rate*duration))
attack_time = 0.1    # 100ms
decay_time = 0.1     # 100ms
sustain_level = 0.7  # サステインレベル 70%
release_time = 0.2   # 200ms

exwave=apply_adsr(wave, attack_time, decay_time, sustain_level, release_time, sample_rate)
# グラフ表示
plt.figure(figsize=(10, 6))
plt.plot(exwave, color='blue')
plt.title('Blackman-Harris Window')
plt.grid(True)

plt.tight_layout()
plt.show()
