# STEP week4

---

### 宿題　wikipedia.py
> Wikipedia のリンク構造を使って、"Google" から "渋谷" を(最短で)たどる方法を探す

##### アルゴリズム
まず、キューを用いた幅優先探索(BFS)を行うことで最短経路があるかどうかを調べた。また、BFSで探索中に、スタートの点から各頂点までの最短距離も記録しておく。その後、記録しておいた各点の最短距離を用いてトレースバックすることにより、最短経路を求めた。

##### 実行方法
以下のようなディレクトリ構成にする。
```
step_wikipedia-graph
├── data
│   ├── links.txt
│   └── pages.txt
└── Wikipedia.py
```
実行するときは、引数に「始点となるページ名」「終点となるページ名」の2つを引数に与える。

例) `$ python3 wikipedia.py Google 渋谷`

##### 実行結果
```
$ python3 wikipedia.py Google 渋谷
最短経路が見つかりました
Google から 渋谷 への最短経路 :
Google → スターバックス → 渋谷
```

また、以下を実行することで、得られた結果は正しそうであることが確認できた。
* `cat data/pages.txt | grep Google` →　`457783	Google`
* `cat data/pages.txt | grep スターバックス` →　`22188	スターバックス`
* `cat data/pages.txt | grep 渋谷` →　`22557	渋谷`


```
$ cat data/links.txt | grep 22557 | grep 22188
22188	22557

$ cat data/links.txt | grep 22188 | grep 457783
22188	457783
457783	22188
```
　
