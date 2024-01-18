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
