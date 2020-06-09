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
