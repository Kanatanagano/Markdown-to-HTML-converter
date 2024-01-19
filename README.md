# Markdown-to-HTML-converter

## デモ
<img width="700" alt="markdown" src="https://github.com/Kanatanagano/Markdown-to-HTML-converter/assets/112442087/1e7e094f-fdd6-4775-b61d-8006d96a99a3">


## 概要

このプログラムは、任意のMarkdownファイルをHTMLファイルに変換するものです。通常、ウェブサーバーにはUbuntuなどのLinuxディストリビューション
が使われることが多いため、このプログラムはLinuxディストリビューション上で動かすことを想定しています。これにより、このようなREADMEのような
Markdownファイルを書くだけで、簡単にHTMLファイルを生成して提供することができます。

Markdownファイルを読み取るために、'r'モードのファイル権限を使用してファイルディスクリプタを作成し、その内容を別のライブラリであるpython-markdown
に渡してHTMLの内容を取得しました。HTMLの内容を取得した後、この内容を書き込んだ新しいファイルを作成するためにさらにシステムコールを行い、これはCLI
引数で指定された出力ファイルに書き込まれます。

私はこれをUbuntu上のVirtualBoxを使用して開発し、UbuntuのAPTパッケージマネージャを使用してVSCode、Python、およびpipをインストールしました。


## 使い方
1. シェルを通して
python3 main.py markdown inputfile outputfile をコマンドを実行することにより行うことができます。


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
