# STEP week6

---

### 宿題　malloc.c
> Linked list の実装が終わった状態の `simple_malloc.c` を改良してメモリ使用率と速度を向上させる
* First fit を Best fit, Worst fit などに変更してみて、その比較を行う

### アルゴリズム
Best fit / Worst fit :

「十分な大きさの空き容量のうち、最も大きいもの / 最も小さいもの」の Linked list の位置を保存し、更新しながら、Linked list すべてを見に行く。Linked list すべてを見終わったあとに保存してある Linked list の位置が求めたい空き領域となる。


### 実行結果
例)
* Best Fit
```
$ make
cc -o malloc_challenge.bin main.c malloc.c simple_malloc.c -Wall -O3 -g -lm
$ make run
./malloc_challenge.bin
Challenge 1: simple malloc => my malloc
Time: 13 ms => 1517 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 6 ms => 654 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 132 ms => 799 ms
Utilization: 8% => 50%
==================================
Challenge 4: simple malloc => my malloc
Time: 40531 ms => 9101 ms
Utilization: 15% => 71%
==================================
Challenge 5: simple malloc => my malloc
Time: 30876 ms => 5866 ms
Utilization: 15% => 74%
==================================
```
* Worst Fit
```
$ make
cc -o malloc_challenge.bin main.c malloc.c simple_malloc.c -Wall -O3 -g -lm
$ make run
./malloc_challenge.bin
Challenge 1: simple malloc => my malloc
Time: 9 ms => 1602 ms
Utilization: 70% => 70%
==================================
Challenge 2: simple malloc => my malloc
Time: 9 ms => 720 ms
Utilization: 40% => 40%
==================================
Challenge 3: simple malloc => my malloc
Time: 128 ms => 115658 ms
Utilization: 8% => 4%
==================================
Challenge 4: simple malloc => my malloc
Time: 40211 ms => 1087573 ms
Utilization: 15% => 7%
==================================
Challenge 5: simple malloc => my malloc
Time: 32096 ms => 962711 ms
Utilization: 15% => 7%
==================================
```

### コメント
実行結果から分かるように、Best Fit にすることで challenge3 〜 challenge5 のメモリ使用率と速度を向上することができました。
逆に、Worst Fit にするとメモリ使用率と速度は悪化してしまいました。
