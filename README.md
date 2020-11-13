# JJ2

プログラムの採点スクリプト

# run

```
$ git clone https://github.com/ymmtr6/jj2_scoring.git
cd jj2_scoring
```

dockerの場合
```
$ docker run -it --rm -v `pwd`:/workspace ymmtr6/jj2 01/1-1.yml --pre --post
```

python3.7以上の場合
```
$ pip3 install -r requirements.txt
$ python3 run.py 05/5-2.yml --pre --post
```

# 事前準備

採点用のExcelファイル(401-2.xlsx, 403-4.xlsx)をプロジェクトルートに配置する。

# 採点方法

1. 課題番号のディレクトリを掘る (mkdir 05)
2. 課題番号のディレクトリで、先生から配られるpre/postを配置する (05/pre, 05/post)
3. ansX-X_X.txtの形式で回答ファイルを作る(05/ans5-1_1.txt, ...)
4. YAMLファイルを書く(05/5-1.yml)

```yml
# 課題番号
kadai: 5-1
# 確認するクラス名(拡張子は省く)
classname: SwitchExample2
# ログの個数(1, 2, 3, ...)
numbers:
- 1
- 2
# 部屋番号　401-402 or 403-404
rooms:
- 401
- 402
# 出力ファイル
output: output5-1.xlsx
# 課題Root
root: '05'
# 採点ファイルのテンプレート(401-1.xlsx or 403-4.xlsx)
book: 401-2.xlsx
```

5. 上記のdockerコマンドを実行する。(カレントディレクトリはプロジェクトルートで)
6. あとは入力値に答えていくだけ(赤塗りは正答例、黄色は出力、修飾なしは合致)
7. 採点が終了すると、採点ファイル、再提出指示ファイルが自動出力される。

## スクリプトの流れ

全体の流れは以下の通り。pre/postの計2回実行する。
  1. 未提出者の確認(miteishutu.txtを解析)
  2. Runtime Errorの確認(XXX.errを解析)
  3. Logファイルを確認し、同様の回答を集計する
  4. 正解と判断できない回答に対してok/ngで判断を求める
  5. 3,4を元に全員の採点を行う。
  6. 2,3,4,5をチェックステップ回数繰り返す。

チェックしなくて良いものはその時点で無視することに注意。

## ファイル構成
```
.
├── 01
│   ├── ans1-1_1.txt
│   ├── ans1-1_2.txt
│   ├── post
│   │   ├── 401
│   │   ├── 402
│   │   ├── 403
│   │   ├── 404
│   │   ├── bad_zipname.txt
│   │   ├── comment_401.txt
│   │   ├── comment_402.txt
│   │   ├── comment_403.txt
│   │   ├── comment_404.txt
│   │   ├── ls.txt
│   │   ├── lsPDF.txt
│   │   └── miteishutu.txt
│   ├── pre
│   │   ├── 401
│   │   │   ├── HelloWorld1.err
│   │   │   ├── HelloWorld1.log
│   │   ├── 402
│   │   ├── 403
│   │   ├── 404
│   │   ├── bad_zipname.txt
│   │   ├── comment_401.txt
│   │   ├── comment_402.txt
│   │   ├── comment_403.txt
│   │   ├── comment_404.txt
│   │   ├── ls.txt
│   │   ├── lsPDF.txt
│   │   └── miteishutu.txt
├── 401-2.xlsx
├── README.md
├── jj2_assert.py
├── output.json
├── output.xlsx
├── re-output.xlsx
└── resubmit.xlsx
```

## 注意事項

* 採点ファイル、回答ファイルはネット上で公開しないこと。(守秘義務)
* Dockerhubにアップロードされているのは環境と最低限の動作スクリプトであり、学生の個人データは含まれていない。
* 採点する必要がない場合は自動採点となり、問い合わせない。(例 preの段階でOK、複数のチェックのうちどれかがNGなど)

## LICENCE

MIT LICENCE
