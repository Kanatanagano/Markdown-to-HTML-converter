# Markdown-to-HTML-converter

## 概要

このプログラムは、任意のMarkdownファイルをHTMLファイルに変換するものです。通常、ウェブサーバーにはUbuntuなどのLinuxディストリビューション
が使われることが多いため、このプログラムはLinuxディストリビューション上で動かすことを想定しています。これにより、READMEのようなMarkdown
ファイルを書くだけで、簡単にHTMLファイルを生成して提供することができます。

Markdownファイルを読み取るために、'r'モードのファイル権限を使用してファイルディスクリプタを作成し、その内容を別のライブラリであるpython-markdown
に渡してHTMLの内容を取得しました。HTMLの内容を取得した後、この内容を書き込んだ新しいファイルを作成するためにさらにシステムコールを行い、これはCLI
引数で指定された出力ファイルに書き込まれます。

私はこれをUbuntu上のVirtualBoxを使用して開発し、UbuntuのAPTパッケージマネージャを使用してVSCode、Python、およびpipをインストールしました。

## デモ
<img width="700" alt="markdown" src="https://github.com/Kanatanagano/Markdown-to-HTML-converter/assets/112442087/1e7e094f-fdd6-4775-b61d-8006d96a99a3">



## 使い方
1. シェルを通して
python3 main.py markdown inputfile outputfile をコマンドを実行することにより行うことができます。


## 使用方法
1. Markdownファイル(.md)を用意する
2. スクリプトを実行する
3. 生成されたファイル(.html)を確認する




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

