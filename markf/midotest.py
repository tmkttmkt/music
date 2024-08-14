from mido import Message, MidiFile, MidiTrack

# 新しいMIDIファイルの作成
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Cメジャースケールのノート番号
notes = [60, 62, 64, 65, 67, 69, 71, 72]  # C, D, E, F, G, A, B, C

# ノートを順番に追加
for note in notes:
    track.append(Message('note_on', note=note, velocity=64, time=0))
    track.append(Message('note_off', note=note, velocity=64, time=480))  # 480 ticks later

# MIDIファイルを保存
mid.save('c_major_scale.mid')
