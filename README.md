
# 概要
発車メロディボタンで発車メロディを流すやつ

# 初期設定
- Python3, Pygame, PySerialをインストールする
- udevでデバイスファイルを割り当てる。 `sudo cp udev_rules/* /etc/udev/rules.d/`

# 音源配置
- sounds/announce.wav にアナウンスを配置
- bells/ にwavでベルを配置
