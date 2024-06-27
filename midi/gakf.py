import mido
from mido import MidiFile, MidiTrack, Message
import numpy as np
import music21

music21.configure.run()
n = music21.note.Note("D#3")
n.duration.type = 'half'
n.show()

class MusicComposer:
    def __init__(self, tempo=120):
        # インスタンス作成時に呼び出される初期化メソッド
        self.tempo = tempo
        self.mid = MidiFile()
        self.track = MidiTrack()
        self.mid.tracks.append(self.track)
        self.track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(tempo)))

    def add_note(self, note, duration, velocity=64):
        # MIDIトラックにノートを追加するメソッド
        note_on = Message('note_on', note=note, velocity=velocity, time=0)
        note_off = Message('note_off', note=note, velocity=velocity, time=self.duration_to_ticks(duration))
        self.track.append(note_on)
        self.track.append(note_off)
        
    def duration_to_ticks(self, duration):
        # 4分音符を1とする場合のdurationからMIDI ticksへの変換
        ticks_per_beat = self.mid.ticks_per_beat
        return int(ticks_per_beat * duration)

    def save_midi(self, filename):
        # MIDIファイルとして保存するメソッド
        self.mid.save(filename)

    def generate_scale(self, key, scale_type='major'):
        # 指定されたキーとスケールの音階を生成するメソッド
        scale = music21.scale.MajorScale(key) if scale_type == 'major' else music21.scale.MinorScale(key)
        notes = [pitch.midi for pitch in scale.getPitches()]
        return notes

    def create_simple_melody(self, key='C', scale_type='major'):
        # 指定されたキーとスケールに基づいてシンプルなメロディを生成するメソッド
        scale_notes = self.generate_scale(key, scale_type)
        melody = np.random.choice(scale_notes, size=8)
        for note in melody:
            self.add_note(note, duration=0.5)  # 8分音符でメロディを生成

# 使用例
composer = MusicComposer(tempo=120)  # MusicComposerクラスのインスタンスを作成
composer.create_simple_melody(key='C', scale_type='major')  # シンプルなメロディを生成
composer.save_midi('simple_melody.mid')  # MIDIファイルとして保存
