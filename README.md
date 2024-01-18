# Markdown-to-HTML-converter

## デモ
<img width="700" alt="markdown" src="https://github.com/Kanatanagano/Markdown-to-HTML-converter/assets/112442087/1e7e094f-fdd6-4775-b61d-8006d96a99a3">


## 概要
マークダウンファイルをHTMLファイルに変換するプログラムです。


## 使い方
1. シェルを通して
python3 main.py markdown inputfile outputfile をコマンドを実行することにより行うことができます。

## 前提条件
このスクリプトを実行するには、下記ソフトウェアを事前にインストールしておく必要があります。

インストールされていない場合は、[インストール](#インストール)/[使用方法](#使用方法)/[使用例](#使用例)で記載されているコマンドが実行できませんので

必ずインストールしてから進めてください。

### Git
Gitがインストールされていない場合は、下記手順でインストールしてください。

1. ターミナルを起動する。<br>使用するOSによりターミナルの名称が異なりますので注意してください。<br>(例. Windows:コマンドプロンプト,mac:ターミナル)

2. Gitがインストールされているか確認する。<br>`git version 2.34.1` のように表示された場合は、Gitがインストールされています。<br>以降の手順はスキップしてください。<br>**また、ターミナルは引き続き使用しますので開いたままにしてください!**
```
git --version
```

3. システムを更新する
```
sudo apt-get update
```

4. Gitをインストールする
```
sudo apt install git
```

5. Gitがインストールされたことを確認する。<br>`git version 2.34.1` のように表示されていれば、Gitのインストールは完了です!
```
git --version
```

### Python 3.x
[Python](https://www.python.org/downloads/)の公式サイトからあなたのPCのOSに合わせて、ダウンロードしてください。

ダウンロードしたファイルを使用してインストールできます。

Pythonがインストールされているかは、下記コマンドで確認することができます。

`Python 3.10.12`のように表示されていれば、Pythonはインストールされています。

```
python3 --version
```

### pip
pipは、Python用のパッケージマネージャで、パッケージのインストールと管理を行うことができます。

[pipのインストールガイド](https://pip.pypa.io/en/stable/installation/)に従って、pipをインストールしてください。

aptを使用してpipをインストールする場合は、下記手順でインストールしてください。

1. pipがインストールされているか確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示された場合は、pipがインストールされています。<br>以降の手順はスキップしてください。
```
pip3 --version
```

2. システムを更新する
```
sudo apt-get update
```

3. pipをインストールする
```
sudo apt install python3-pip
```

4. pipがインストールされたことを確認する。<br>`pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)` のように表示されていれば、pipのインストールは完了です!
```
pip3 --version
```

### markdown

markdownは、MarkdownをHTMLへ変換する機能を提供しているPythonのパッケージです。

pipを使用して、下記手順でインストールしてください。

[pip](#pip)は、あらかじめインストールしておいてください。

また、markdownについて詳しく知りたい場合は、[markdownのプロジェクトの説明](https://pypi.org/project/Markdown/)を確認してください。

1. markdownがインストールされているか確認する。<br>Name/Version/Summaryなどが表示された場合は、markdownがインストールされています。<br>以降の手順はスキップしてください。
```
pip3 show markdown
```

2. markdownをインストールする
```
pip3 install markdown
```

3. markdownがインストールされたことを確認する。<br>Name/Version/Summaryなどが表示されていれば、markdownのインストールは完了です!
```
pip3 show markdown
```
## インストール
### クローン
このスクリプトをあなたのPCで実行するために、クローンします。

クローンとは、このスクリプトの実行に必要なファイル(リポジトリのコンテンツ)をあなたのPCのローカル環境へコピーすることです。

下記手順でクローンしてください。

1. リポジトリをクローンする
```
git clone https://github.com/Kanatanagano/Markdown-to-HTML-converter.git
```

2. クローンしたリポジトリへ移動する
```
cd yourdir
```

## 使用方法
1. Markdownファイル(.md)を用意する
2. スクリプトを実行する
3. 生成されたファイル(.html)を確認する

## 使用例

1. Markdownファイル(.md)を用意する。<br>インプットとなるファイルを作成してください。<br>ファイルは、Markdown形式で記述しておく必要があります。<br>今回は、動作確認をしたいので、クローンした際にコピーされたsample.mdというファイルを使用します。
2. スクリプトを実行する。<br>スクリプトを利用する際は、ターミナルに[コマンドの入力例](#コマンドの入力例)のようなコマンドを入力します。<br>今回は、[コマンドの入力使用例](#コマンドの入力使用例)のようにコマンドを入力しました。
3. 生成されたファイルを確認する。<br>index.htmlというHTMLファイルが生成されていました。

### 手順2の補足
#### コマンドの入力例
```
python3 file-converter.py markdown [inputfile] [outputfile]
```
| コマンド | 内容 |
| ------- | ------- |
| `[inputfile]`| 手順1.で用意したファイルのパスを入力します。<br>パスには、用意したファイルの名前まで含めてください。 |
| `[outputfile]`| スクリプトを利用することで、生成されるファイルのパスを入力します。<br>パスには、生成されるファイルの名前まで含めてください。 |

#### コマンドの入力使用例
```
python3 file-converter.py markdown ../python_practice/sample.md ../python_practice/index.html
```

## 使用技術
| カテゴリ    | 技術スタック   |
|------------|--------------|
| 開発言語    | Python       |
| インフラ    |              |
|            | Ubuntu       |
|            | VirtualBox   |
| その他      |              |
|            | Git          |
|            | Github       |

## 参考文献
### 公式ドキュメント
- [Python](https://docs.python.org/ja/3/)
### 参考にしたサイト
- [Python_Download](https://www.python.org/downloads/)
- [pipのインストールガイド](https://pip.pypa.io/en/stable/installation/)
- [markdownのプロジェクトの説明](https://pypi.org/project/Markdown/)
- [Markdown記法一覧](https://qiita.com/oreo/items/82183bfbaac69971917f#:~:text=Markdown%EF%BC%88%E3%83%9E%E3%83%BC%E3%82%AF%E3%83%80%E3%82%A6%E3%83%B3%EF%BC%89%E3%81%AF%E3%80%81,%E3%82%82%E9%96%8B%E7%99%BA%E3%81%95%E3%82%8C%E3%81%A6%E3%81%84%E3%82%8B%E3%80%82)
- [HTML の基本](https://developer.mozilla.org/ja/docs/Learn/Getting_started_with_the_web/HTML_basics)
