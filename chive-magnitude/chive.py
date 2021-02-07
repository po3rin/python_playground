from pymagnitude import Magnitude, MagnitudeUtils

# ダウンロード
# デフォルトのダウンロード先: `~/.magnitude/`
# vectors = Magnitude(MagnitudeUtils.download_model("chive-1.1-mc90-aunit", remote_path="https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/"))

# リモートでのロード
# 下記例は300MBのベクトル、検証環境で1分弱
vectors = Magnitude(
    "https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.1-mc90-aunit.magnitude")

# リモートでのストリーム
# ローカルにファイルをダウンロードせず、ベクトルをすばやく取得
# vectors = Magnitude("https://sudachi.s3-ap-northeast-1.amazonaws.com/chive/chive-1.1-mc90-aunit.magnitude", stream=True)
print(vectors.most_similar("痛み", topn=5))
print(vectors.most_similar("頭痛", topn=5))
print(vectors.most_similar("赤ちゃん", topn=5))
print(vectors.most_similar("薬", topn=5))
print(vectors.most_similar("処方", topn=5))
