# coco_trial
COCO: A platform for Comparing Continuous Optimizers in a Black-Box Setting¶

# Benchmark

We use [COCO (COmparing Continuous Optimisers)](https://coco.gforge.inria.fr/) to test the performance of Limited-GP.

#### installation of COCO

The following commands install python modules `cocoex` and `cocopp`:

```console
$ git clone https://github.com/numbbo/coco.git
$ cd coco
$ pip install numpy scipy tqdm matplotlib
$ python do.py run-python
$ python do.py install-postprocessing
```

### test

```console
$ python solver run.py
```

Results will be outputted to directory `exdata/`.

#### drawing graph

```console
$ python -m cocopp -o results exdata/*
```

## Memo
関数の次元数$D$は$D=2$と$D=3$でそれぞれ実験しました。探索回数は$10×D$としました。　　　
横軸がlog(探索回数/次元数)を表し、縦軸がすべての関数に対する平均精度を表します（※正確には、このグラフはempirical cumulative distribution function [3]と呼ばれるもの）。グラフ上の×印は探索の終了点を表し、それより後の部分は、結果描画時に補完された値（詳細は参考文献）。   
”best 2009”は各関数ごとに2009年のコンペティションで提出された手法のうち最も良い結果が得られたものを選んだ場合の学習曲線を表す。実際にはブラックボックス関数であるため手法をあらかじめ選ぶということはできず、ある種の性能上界として参考までに載せています。

## Reference
[1] [Eric Brochu, Vlad M. Cora, and Nando de Freitas. A tutorial on Bayesian optimization of expensive cost functions, with application to active user modeling and hierarchical reinforcement learning. pre-print, 2010. arXiv:1012.2599.](https://arxiv.org/abs/1012.2599)

[2] [Hansen, N.: The CMA Evolution Strategy: A tutorial.](https://arxiv.org/abs/1604.00772)

[3] [N. Hansen, A. Auger, D. Brockhoff, D. Tušar, T. Tušar (2016). COCO: Performance Assessment. ArXiv e-prints, arXiv:1605.03560.](https://arxiv.org/abs/1603.08785)

[4] [Posìk, P. Huyer, W. & Pal, L. A comparison of global search algorithms for continuous black box optimization. Evol. Comput. 20, 509–541 (2012).](https://www.mitpressjournals.org/doi/pdf/10.1162/EVCO_a_00084)

## related work
limited-gp: https://github.com/pfnet-research/limited-gp
