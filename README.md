# 概要

ランダムデータ生成
pandasを使えばある程度楽に解決できると思うが
ライブラリのインストールをしたくないので、自力でやってみる(pandas版も作るかも)

# 設計

## クラス設計

- Client => client.py
- IDData
- Statuses => status.py
- Status => status.py
- Value => value.py
- Order => order.py
- Sequence => sequence.py
    - 数列は複数のクラスを作る可能性があるため1つのファイルで管理
- Random => random.py
    - randomもある程度複雑なことをしたいため、1つのファイルで管理


### Client

- 保持データ
    - 辞書 + リスト => メインデータ
        - データを追加する時、それぞれのvalueが同じ大きさか毎回測定
        - 値はsequenceに、Order, Dimension, Statusを入れる(入れるというよりは乗算？) => 重み × 基幹数列
    - index_key(idデータ) => これを一番最初に入れる
    - カラム名を入れる。(dimensionの種類ごとに分けるかどうか・カラム名は普通の文字列リスト)
    - statuses
    - order
        - 順番・日付など

#### 処理順

- メインデータ作成・最初は空っぽ

イメージは下記の感じ
a, bはカラム名

```python
a = {'a':['data1', 'data2'], 'b':['data3', 'data4']}
```

- idを入れる。この時メインデータに入れても意味はないのでindex_keyとしてクラス内に保持
- statusesからstutasを網羅させて入れる。

イメージは下記の感じ
例えば
ステータスでカラムaに対して、apple, not apple
ステータスでカラムbに対して、banana, not banana
がある時

```python
a = {'a'['apple', 'appple', 'not apple', 'not apple'], 'b':['banana', 'not banana', 'banana', 'not banana']}
```

のように網羅させてデータを作る
(重みを定義したいので、apple, not appleはvalueで取得できるようにstatusを変えつつ、全てのクラスに対してvalueが存在するように継承を利用するか？)

- Orderを入れる。サイズを調べる。サイズによって上記のレコードを倍しなければならない。
例えばサイズが4であれば上記のaを同じデータを4つ並べなければならない。
(order_columnは定義しておいた方がいいか？)
(そもそもcolumnは文字列ではなく、columnクラスにした方がいいか？)

- 順序データに従って数列を展開

1. Orderのカラムを取得(数字idのやつ)
2. Orderのデータを1行目から取得
3. Statusデータも1行目から取得。
4. 数列を作っておく。
5. 数列の数字の数字id番目×ステータスの重み => 結果
6. 結果を1行目に入れる

### Statuses


- statuses


```python
a = {'a':['apple', 'not apple'], 'b':['banana', 'not banana']}
```




###  Status

- column
- name
- value