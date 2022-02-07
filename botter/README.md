# 機械学習を使った仮想通貨自動売買ボットの試し

## 依存

MacOSでTA-Libのインストール結構えぐいけど、これで一応解決した。

```sh
$ brew install ta-lib
$ export TA_INCLUDE_PATH="$(brew --prefix ta-lib)/include"
$ export TA_LIBRARY_PATH="$(brew --prefix ta-lib)/lib"
$ poetry add TA-Lib
```