from sinse import *
import markovify
import re
import glob

def extract_pitch_from_file(content):
    # 正規表現パターン
    pattern = re.compile(r'(\d*[A-Ga-g]#?\d*)')
    # 正規表現にマッチするすべての部分文字列を抽出
    pitches = re.findall(pattern, content)

    return pitches
def pl(melody_pitches,bpm):
    k=kyok()
    print(melody_pitches)
    list=[]
    for melody in melody_pitches:
        print(melody[0])
        o=k.create_onp((4/int(melody[0]))*(60/bpm))
        o.sin(f(melody[1:]),1)
        list.append(o)
    k.play(list)

#onファイルに入ってるtxtのパスを全部取得
file_paths = glob.glob('on/na.txt')
print(file_paths)
txt=[]
#パスを全部開いて内容をリストにしてマルコフモデルに突っ込む
for pas in file_paths:
    with open(pas,"r",encoding="utf-8") as file:
        txt_e=file.read()
        txt.append(txt_e)
text_model = markovify.Text(txt)

#確率変遷を表示
print(text_model.chain.model)
#文章生成したものを正規表現(一定の文字列規則)に当てはまるもののリストにする
tt=extract_pitch_from_file(text_model.make_sentence())
#生成した文章から音楽を生成
pl(tt,60)


"""
##指示##
有名な曲のメロディーを一つ教えてください

##例##
4A4 4B4 8C5 8B4

##出力##
音の長さ(何拍子か)
音の長さ音の種類(アルファベットで)
音の高さで表記してください

例
4A4 4B4 8C5 8B4

"""
