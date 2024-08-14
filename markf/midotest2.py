import mido

# MIDIファイルの読み込み
mid = mido.MidiFile('c_major_scale.mid')
aa:mido.messages.messages.Message=mid.tracks[0][0]
print(aa.time)
print(aa.note)
print(aa.velocity)