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
print(vectors.most_similar("痛み", topn=5))
print(vectors.most_similar("頭痛", topn=5))
print(vectors.most_similar("赤ちゃん", topn=5))
print(vectors.most_similar("薬", topn=5))
print(vectors.most_similar("処方", topn=5))
print(vectors.most_similar("痛い", topn=5))
print(vectors.most_similar("5月", topn=5))
print(vectors.most_similar("若い時", topn=5))
print(vectors.most_similar("歩く", topn=5))
print(vectors.most_similar("診断", topn=5))
print(vectors.most_similar("病気", topn=5))
print(vectors.most_similar("大丈夫", topn=5))
print(vectors.most_similar("続く", topn=5))
