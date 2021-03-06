# STEP week7

---

## 宿題1　matrix.c
> 行列積のループ順序としては6種類の組合せがある。この6種類を実行速度が速いと思う方から順に並べてください。実際に実験してその予想が正しいかどうか確かめてください。
* i-j-k, i-k-j, j-i-k, j-k-i, k-i-j, k-j-i


> * 注:この宿題はC/C++、JavaまたはGoでやってください(理由は宿題2を参照)

まず、上の6通りのループ順序に対して、アクセスが連続ではないものは`c[i * n + j] += a[i * n + k] * b[k * n + j];`の3つのうち何個あるかを調べた。

| i - j - k | i - k - j | j - i - k | j - k - i | k - i - j | k - j - i |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 0 | 1 | 2 | 0 | 2 |

よって、実行速度は

i - k - j, k - i - j < i - j - k, j - i - k < j - k - i, k - j - i

のようになると予想した。

### 実行結果
```
$ ./matrix 1000
average time: 9.308862 sec
$ ./matrix 1000
average time: 3.536111 sec
$ ./matrix 1000
average time: 5.388316 sec
$ ./matrix 1000
average time: 13.103453 sec
$ ./matrix 1000
average time: 3.770486 sec
$ ./matrix 1000
average time: 10.369421 sec
```
得られた実行結果を表にまとめると

| i - j - k | i - k - j | j - i - k | j - k - i | k - i - j | k - j - i |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 9.308862 sec | 3.536111 sec | 5.388316 sec | 13.103453 sec | 3.770486 sec | 10.369421 sec |


## 宿題2
> C/C++/Java/Goで行列積を書くと、i-k-j ループのほうが i-j-k ループよりもずっと速かった。でも、実はPythonで書くと、ループ順序を入れ替えても速度差はほとんどない。ここまでの説明をふまえて、その理由を考えてください。

Pythonはインタプリタ言語であるので、プログラムの構造を構文木として表現し、構文木をたどりながらプログラムを実行(=評価)する。そのため、配列の要素がメモリ上で隣にあるとは限らず、キャッシュされない可能性が大きいから。


## 宿題3
> これまでの7回の授業で学んできたことを総合して、TSP Challenge のプログラムを最適化して、Challenge 6(都市数=2048)のベストスコア更新とChallenge 7(都市数 = 8192)のベストスコアを目指してください！

### 方針
* Challenge6：「greedyと2-optを用いて最短経路を求める」というのをスタートする点を変えて繰り返し求める。
* Challenge7：引数で与えられたスタートするような経路で、greedyと2-optを用いて最短経路を求める。

また、前回のコードで誤っていたところがあったため、それを修正した。(前回のコード 79行目)

### 実行結果
* コンパイル：`g++ -O3 -o solver solver.cpp common.cpp -std=c++11`
* 実行：`./solver (入力ファイル) (出力ファイル) (スタートする点)`

```
$ ./solver input_6.csv output_6.csv 0
min_total_dist: 41894.2
$ ./solver input_7.csv output_7.csv 0
min_total_dist: 84190.7
```
### コメント
PythonからC++に変えると実行時間がとても短くなりました。前回のときは、同じアルゴリズムだとChallenge6も時間がかかりすぎて最後まで実行できなかったので、改めてCやC++のコンパイラ言語の実行速度の速さが分かりました。

今までほとんどC++でコードを書いたことがなかったので、PythonからC++にコードを書き直すのに予想より時間がかかってしまい、アルゴリズムはあまり変えられませんでしたが、時間があるときにまた考えてみようと思います。

また、前回のコードレビューで教えていただいた、`入れ替える2つの辺をランダムに選んで、1000回前と比べて1％しか短くならなかったというのを終了条件にするとよい`という方法も実装してみたのですが、もとのアルゴリズムより実行結果が向上しなかったため、N^Nの組み合わせ全部を試す方法のままにしました。
