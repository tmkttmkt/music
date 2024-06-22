from sinse import *
"""
必要なライブラリはpyaudioとscipy、もしかしたらsubprocessとnumpy
音量は音符に複数の波を重ねて増すことができるし、トラック全体の音量を変更できるが合計値1を超えると音割れする
全体の音量 = トラック1の音量倍率*(音符で足した波1の音量+音符で足した波2の音量...)+トラック2の音量倍率*(音符で足した波1の音量+音符で足した波2の音量...)...
sinseの中でもPlayerだけコピーしたからこれ理解出来たら頭よさそうなライブラリかけると思う
"""

k=kyok(44100,file_name="rei")
#必須引数 サンプリング周波数(基本44100)、指定引数 second:秒数、file_name:出力するファイル名(.wavとかつけない)

onp1=k.create_onp(1)
#音符生成関数 必須引数 (秒数)

onp1.sin(f("A3"),0.1)
#音符に波を入れる関数:正弦波 必須引数 (周波数,音量)
"""
関数f()は音の名前(文字列)入れたら周波数を返してくれる
小文字でもok
"""
onp1.reset()
#音符の波をリセットする関数

onp1.nok(f("A3"),0.1)
#音符に波を入れる関数:ノコギリ波 必須引数 (周波数,音量)

onp2=k.create_onp(2)

onp2.tan(f("A3"),0.1)
#音符に波を入れる関数:矩形波(四角形) 必須引数 (周波数,音量)

k.play([onp1,onp2])
#音符リストを再生する関数 必須引数 k.create_onp()で生成した音符のリスト

k.write([onp1,onp2],file_name="koremo")
#音符リストをwavにする関数 必須引数 k.create_onp()で生成した音符のリスト 指定引数 file_name:出力するファイル名(.wavとかつけない)なければ前に入れたファイル名になる、それもなければ"output.wav"になる

base=k.create_track(0,[onp1,onp2,onp2])
#トラックを生成する関数 必須引数(再生を開始する秒数、k.create_onp()で生成した音符のリスト)
base.volume(1.1)
#トラック全体の音量を調整する関数 必須引数 音量(1だと変わらない)

merody=k.create_track(0.5,[onp1,onp2,onp2])

k.play_waves([base,merody])
#トラックを再生する関数 必須引数 k.create_onp()で生成した音符のリスト

k.write_waves([base,merody],file_name="aremo")
#トラックを再生する関数 必須引数 k.create_onp()で生成した音符のリスト 指定引数 file_name:出力するファイル名(.wavとかつけない)なければ前に入れたファイル名になる、それもなければ"output.wav"になる

k.run()
#事前に出力したwavファイルを再生する関数