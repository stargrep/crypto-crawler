# Crypto-Crawler
> Python 3.7, Flask, simple-model, BeautifulSoup, MySql

## Overview

#### 这份源代码只作为学习交易信号和交易系统知识用途, 未经回测不要用来执行交易

### Class 1
```

学习project结构, 基本文件如下
- design.md         (设计文档)
- LICENCE           (授权)
- .gitignore        (可忽略文件列表)
- README.md         (读我)
- requirement.txt   (pip 安装文件)
- setup.py          (build python project)
- crypto_crawler    (源代码)
    - __init__.py
    - ... 
- tests             (测试代码)


运行步骤
0. 确定运行的folder
$ pwd
${your system dir}/crypto-crawler

1. 设置virtual environment
$ python -m venv env
这行命令将会创建 env/ 包含这个env中引入的包

2. 使用 env
$ source env/bin/activate

$ pip list
Package        Version
-------------- -------
pip            20.1.1
setuptools     41.2.0
证明在此env下的 pip 是新生成的。

$ pip install -r requirement.txt
$ pip list
Package        Version
-------------- -------
click          7.1.2
Flask          1.1.2
itsdangerous   1.1.0
Jinja2         2.11.2
MarkupSafe     1.1.1
pip            20.1.1
setuptools     41.2.0
Werkzeug       1.0.1

按照 requirement.txt 安装了 Flask

3. build project
$ python setup.py sdist
生成 sdist/ 里面会有当前版本(v0.2)的tar.gz文件

$ ls dist
crypto_crawler-0.2.tar.gz

4. pip 安装
$ pip install dist/crypto_crawler-0.2.tar.gz

5. pip list 查看crypto_crawler安装
$ pip list
Package        Version
-------------- -------
click          7.1.2
crypto-crawler 0.2
Flask          1.1.2
itsdangerous   1.1.0
Jinja2         2.11.2
MarkupSafe     1.1.1
pip            20.1.1
setuptools     41.2.0
Werkzeug       1.0.1
(env) 

新添加了crypto-crawler包

6. 运行crypto-cralwer包，会执行 crypto_crawler/__main__.py
$ python -m crypto_crawler
hello,  https://coinmarketcap.com/currencies/bitcoin/markets
(env) 

7. 运行测试
右键点击 tests/ 执行 "Run 'Unittest in tests'"

```

### Class 2
Sqlite
https://www.sqlitetutorial.net/sqlite-data-types/
https://sqlite.org/cli.html

```
1. Update requirement.txt

2. data model definition and unit tests
common.py

3. sqlite 
https://pythonexamples.org/python-sqlite3-insert-multiple-rows-to-table/
https://www.sqlitetutorial.net/sqlite-date/
$ sqlite3 test
sqlite> .tables
sqlite> .schema tablename
sqlite> .headers ON

4. run sql_utils tests

```

### Class 3
```
0. declar the dunder names
1. Update common and test
2. Updae write many for crypto prices
3. update time str for crypto

4. strategy 2 ways
5. how to report with ploting 
6. notification
7. next?
(1) alarm trading chances
(2) daily reporting
(3) auto-trading
(4) back-testing
(5) other strategy
so many...

```