from pymagnitude import Magnitude, MagnitudeUtils

# ダウンロード
# デフォルトのダウンロード先: `~/.magnitude/`
# vectors = Magnitude(MagnitudeUtils.download_model("chive-1.1-mc90-aunit", remote_path="https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/"))

# リモートでのロード
# 下記例は300MBのベクトル、検証環境で1分弱
vectors = Magnitude(
    "https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.2-mc15.magnitude")

# リモートでのストリーム
# ローカルにファイルをダウンロードせず、ベクトルをすばやく取得
# vectors = Magnitude("https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.1-mc90-aunit.magnitude", stream=True)

print(vectors.similarity("はり", "張り"))
print(vectors.similarity("痛み", "痛い"))
print(vectors.similarity("腹", "お腹"))
print(vectors.similarity("腹", "腹"))
print(vectors.similarity("妊娠中", "妊娠"))
print(vectors.similarity("妊娠初期", "妊娠"))
print(vectors.similarity("妊娠", "痛み"))
print(vectors.similarity("ぶつけた", "ぶつける"))
print(vectors.similarity("頭", "こぶ"))
print(vectors.similarity("打った", "ぶつけた"))
