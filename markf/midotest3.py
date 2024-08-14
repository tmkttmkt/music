import mido

def extract_note_info(mid):
    note_data = []
    for track in mid.tracks:
        current_time = 0
        notes_on = {}  # ノートオンの状態を保持する辞書

        for msg in track:
            current_time += msg.time  # 経過時間を加算
            print(type(msg))
            print(msg)
            if msg.type == 'note_on':
                if msg.velocity > 0:  # ベロシティが0でない場合はノートオン
                    notes_on[msg.note] = current_time
                # ベロシティが0の場合はノートオフとみなす
                else:
                    if msg.note in notes_on:
                        start_time = notes_on.pop(msg.note)
                        note_data.append({
                            'note': msg.note,
                            'start_time': start_time,
                            'end_time': current_time,
                            'velocity': msg.velocity
                        })
            elif msg.type == 'note_off':
                if msg.note in notes_on:
                    start_time = notes_on.pop(msg.note)
                    note_data.append({
                        'note': msg.note,
                        'start_time': start_time,
                        'end_time': current_time,
                        'velocity': msg.velocity
                    })

    return note_data

# MIDIファイルの読み込み
mid = mido.MidiFile('c.mid')

# ノート情報の抽出
notes_info = extract_note_info(mid)

# ノート情報の表示
for note in notes_info:
    print(f"Note: {note['note']}, Start Time: {note['start_time']}, End Time: {note['end_time']}, Velocity: {note['velocity']}")

