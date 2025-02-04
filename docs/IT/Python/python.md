- modules
    - getopt
    - getpass
    - syslog
    - Fabric

- python中有对应c中make的项目build工具吗？

- asyncio
  - https://www.ruanyifeng.com/blog/2019/11/python-asyncio.html
    - 为什么有了threading和multiprocessing还需要asyncio？
    - thread的锁，代码示例
    - JavaScript的async/await，什么场景需要用到？
    - asyncio是单线程的，只是多个task轮流使用该线程的cpu时间
      - asyc/asyncio allows concurrency within a single thread
    - 最好的example

- def __invert__(self):
print(7 .__invert__()) # -8
  - 7后必须加空格
  - 
  >>> ~a
  __invert__ called on Test(True)
  False


```python
>>> a=[]
>>> b=a
>>> b.append(1)
>>> b
[1]
>>> a
[1]
```


- Environment
    - pylintrc


- pip与LD_LIBRARY_PATH


- python3 -m ensurepip
    - ensurepip
        - 该调用会在当前未安装 pip 的情况下安装 pip ，如已安装则无事发生

- Pyenv
    - https://github.com/pyenv/pyenv/wiki#suggested-build-environment

- re module
    - \t
    - 
    ```
    >>>re.findall('.{3}aaa.{1}', "\nxxxaaaxxaaaffff")
    ['xxxaaax']
    ```

- PYTHONPATH
```
Pythonpath is an environment variable that is used to specify the location of Python libraries. It is typically used by developers to ensure that their code can find the required Python libraries when it is run.
```

- pip3 升级
    - https://www.jianshu.com/p/34235f5d484a
        - pip3 install --upgrade pip

- How to upgrade to Python 3.8 on Ubuntu 18.04 LTS
  - https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-8-on-ubuntu-18-04-lts/
    - sudo add-apt-repository ppa:deadsnakes/ppa
    - sudo apt-get update
    - sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
    - sudo update-alternatives --config python3
      - 

```
>>> x=re.search("clients3_linux_amd64_(?P<version>.*).tar.bz2", "clients3_linux_amd64_2022-01-01.tar.bz2")
>>> x['version']

what doese `?P` mean ?
```

- b'' 的意思？比如 b'2023.06.09'
    - 意思在2和3中不同



#### py2
- Classic python low level libs

- test-driven


#### py3
- Why python2 is deprecated ? And what's the advantage of python3 ?
  - Many data science libs has stop supporting for py2, like numpy.
  - Type hinting
  - pathlib module
  - Type hinting
    - type-hinting is just a note of code ?
      - Yes, but still can enforce checking by use module https://github.com/RussBaz/enforce
  - glob module
  - format string
  - divison
  - Strict ordering
  - Unicode for NLP
  - More reable useage in ML modules, like numpy
    - `Matrix multiplication with @`
  - Preserving order of dictionaries and **kwargs
  - Iterable
  - pickle module
  - super() function
    - please explain how to use super() by yourself.
  - Future-proof APIs with keyword-only arguments
    - 这个挺实用的
  - Built-in breakpoint()

  - references:
    - https://github.com/arogozhnikov/python3_with_pleasure
    - https://www.toptal.com/python/python-3-is-it-worth-the-switch
    - https://snarky.ca/why-python-3-exists/


- Underscores in Python

- How to upgrade python, e.g. upgrade python3.6 on your machine to python3.9
  - https://www.itsupportwale.com/blog/how-to-upgrade-to-python-3-10-on-ubuntu-18-04-and-20-04-lts/

- Class in Class ?

- 给hint type做强制，实现强类型。。

- 当可以用py2和py3实现时，是否有lint tool来限制只能用py3的语法呢？也就是避免使用py2

- `with open(` 的几种模式:
```
The opening modes are exactly the same as those for the C standard library function fopen().
The BSD fopen manpage defines them as follows:
 The argument mode points to a string beginning with one of the following
 sequences (Additional characters may follow these sequences.):

 ``r''   Open text file for reading.  The stream is positioned at the
         beginning of the file.

 ``r+''  Open for reading and writing.  The stream is positioned at the
         beginning of the file.

 ``w''   Truncate file to zero length or create text file for writing.
         The stream is positioned at the beginning of the file.

 ``w+''  Open for reading and writing.  The file is created if it does not
         exist, otherwise it is truncated.  The stream is positioned at
         the beginning of the file.

 ``a''   Open for writing.  The file is created if it does not exist.  The
         stream is positioned at the end of the file.  Subsequent writes
         to the file will always end up at the then current end of file,
         irrespective of any intervening fseek(3) or similar.

 ``a+''  Open for reading and writing.  The file is created if it does not
         exist.  The stream is positioned at the end of the file.  Subse-
         quent writes to the file will always end up at the then current
         end of file, irrespective of any intervening fseek(3) or similar.
```

如何把 python3.9 build成一个单独的binary在linux下运行，有可能吗？

- python -c 中 tab 怎么写？




### PyInstaller
- .spec file
```python
# 该 moccasin/__main__.py 会被pyinstaller生成为一个可执行文件
configuration = Analysis(['moccasin/__main__.py'],    
#pathex = ['D:\\Company\\project\\untitled', 'D:\\Company']
#意思是项目需要从什么地方导入自定义库
#from mypath.util import module1  # 从D:\\Company\\project\\untitled找到mypath文件夹下面的util下面的module1
                         pathex = ['.', 'lib/python/', 'bin/'],
                         binaries = [(libsbml_lib_path(), '.')],  # 动态库
#项目需要用到什么数据，比如图片，视频等。里面格式为tuple，第一个参数是文件路径，第二个是打包后所在的路径。
#下面的代码意思就是，把image下面的所有以png结尾的文件打包到exe所在目录下的data/image目录下。把pdf目录下的#test.pdf文件打包到exe所在目录的data/pdf目录下
                         datas=[
                          ('image/*.png','data/image'),                        
                          ('pdf/test.pdf','data/pdf')
                         ],
                         hiddenimports = [],
                         hookspath = [],
                         runtime_hooks = [],
                         excludes = [],
                         win_no_prefer_redirects = False,
                         win_private_assemblies = False,
                         cipher = None,   # 加密密钥（一般无加密需求，可不设置）
                        )

application_pyz    = PYZ(configuration.pure,
                         configuration.zipped_data,
                         cipher = None,
                        )

executable         = EXE(application_pyz,
                         configuration.scripts,
                         configuration.binaries,
                         configuration.zipfiles,
                         configuration.datas,
                         name = 'moccasin',
                         debug = False,
                         strip = False,
                         upx = True,
                         runtime_tmpdir = None,
                         console = False,
                        )

app             = BUNDLE(executable,
                         name = 'MOCCASIN.app',
                         icon = 'dev/icon/moccasin.icns',
                         bundle_identifier = None,
                         info_plist = {'NSHighResolutionCapable': 'True'},
                        )
```

```python
subprocess.check_output(cmd, shell=True, text=True)
```

```python
>>> 'http://xx.com'.lstrip('xhttfffff://p')
'.com'
```
```shell
pytest tox.ini lint
```

- Python
    - python 3
    - logging
    - urllib urlparse
    -         "message": "Dangerous default value {} as argument",
    - super 放在不同的位置会怎样？
    - when staticmethod, when classmethod ?
    - collections
    - array & list
      - https://medium.com/backticks-tildes/list-vs-array-python-data-type-40ac4f294551
    - lambda, filter


- module from so file ?
```python
>>> import _tkinter
>>>
>>> _tkinter
<module '_tkinter' from '/usr/local/python-3.10.6-with-openssl-3.0.5/lib/python3.10/lib-dynload/_tkinter.cpython-310-x86_64-linux-gnu.so'>
>>>
```


- 参数 `--onefile`

- LD_LIBRARY_PATH=$(PY_LD_PATH) virtualenv/bin/pip3.9 install -r requirements.txt;


```
$ pyinstaller xxx-yyy.spec
The 'enum34' package is an obsolete backport of a standard library package and is incompatible with PyInstaller. Please `pip uninstall enum34` then try again.


```
```
857 INFO: UPX is not available.

```

- pyinstaller specific python version


- upx
  - upx=True
    - UPX is a free utility available for most operating systems. UPX compresses executable files and libraries, making them smaller, sometimes much smaller. UPX is available for most operating systems and can compress a large number of executable file formats

- raise_for_status()
  - 

- tenacity
  - stop_after_attempt
    - 重试次数

- python io module
  - Python io - BytesIO, StringIO
    - https://www.digitalocean.com/community/tutorials/python-io-bytesio-stringio
  - io.BytesIO
    - `Python io module allows us to manage the file-related input and output operations`
    - 
    ```
     io.BytesIO()
     .seek(0)
    ```
      - Python: are seek(0) and open() essentially doing the same thing?
        - https://stackoverflow.com/questions/40143525/python-are-seek0-and-open-essentially-doing-the-same-thing
    - 用于在内存中读写二进制数据,它的作用类似于文件对象，但是数据并不是存储在磁盘上，而是存储在内存中的字节串。你可以像文件对象一样对其进行读写、查找和截断等操作。通常用来操作二进制数据，如图片、音频、视频等。也可以用于测试或者临时存储数据
      - https://blog.csdn.net/qq_41604569/article/details/129835209
        - bytes转换成字符串
        - 输出的为什么是b开头的
  - io.StringIO

#### pytest
- Is it possible that a function be mocked globally ?

- conftest.py

- TDD (Test Driven Development)

- pytest's fixture


#### PyInstaller
- .spec file
```python
# 该 moccasin/__main__.py 会被pyinstaller生成为一个可执行文件
configuration = Analysis(['moccasin/__main__.py'],    
#pathex = ['D:\\Company\\project\\untitled', 'D:\\Company']
#意思是项目需要从什么地方导入自定义库
#from mypath.util import module1  # 从D:\\Company\\project\\untitled找到mypath文件夹下面的util下面的module1
                         pathex = ['.', 'lib/python/', 'bin/'],
                         binaries = [(libsbml_lib_path(), '.')],  # 动态库
#项目需要用到什么数据，比如图片，视频等。里面格式为tuple，第一个参数是文件路径，第二个是打包后所在的路径。
#下面的代码意思就是，把image下面的所有以png结尾的文件打包到exe所在目录下的data/image目录下。把pdf目录下的#test.pdf文件打包到exe所在目录的data/pdf目录下
                         datas=[
                          ('image/*.png','data/image'),                        
                          ('pdf/test.pdf','data/pdf')
                         ],
                         hiddenimports = [],
                         hookspath = [],
                         runtime_hooks = [],
                         excludes = [],
                         win_no_prefer_redirects = False,
                         win_private_assemblies = False,
                         cipher = None,   # 加密密钥（一般无加密需求，可不设置）
                        )

application_pyz    = PYZ(configuration.pure,
                         configuration.zipped_data,
                         cipher = None,
                        )

executable         = EXE(application_pyz,
                         configuration.scripts,
                         configuration.binaries,
                         configuration.zipfiles,
                         configuration.datas,
                         name = 'moccasin',
                         debug = False,
                         strip = False,
                         upx = True,
                         runtime_tmpdir = None,
                         console = False,
                        )

app             = BUNDLE(executable,
                         name = 'MOCCASIN.app',
                         icon = 'dev/icon/moccasin.icns',
                         bundle_identifier = None,
                         info_plist = {'NSHighResolutionCapable': 'True'},
                        )
```

```python
subprocess.check_output(cmd, shell=True, text=True)
```

```python
>>> 'http://xx.com'.lstrip('xhttfffff://p')
'.com'
```
```shell
pytest tox.ini lint
```

- Python
    - python 3
    - logging
    - urllib urlparse
    -         "message": "Dangerous default value {} as argument",
    - super 放在不同的位置会怎样？
    - when staticmethod, when classmethod ?
    - collections
    - array & list
      - https://medium.com/backticks-tildes/list-vs-array-python-data-type-40ac4f294551
        - `The main difference between these two data types is the operation you can perform on them. Arrays are specially optimised for arithmetic computations so if you’re going to perform similar operations you should consider using an array instead of a list.`
        - `Also lists are containers for elements having differing data types but arrays are used as containers for elements of the same data type.`
      - `Note: Python does not have built-in support for Arrays, but Python Lists can be used instead`
    - lambda, filter


- module from so file ?
```python
>>> import _tkinter
>>>
>>> _tkinter
<module '_tkinter' from '/usr/local/python-3.10.6-with-openssl-3.0.5/lib/python3.10/lib-dynload/_tkinter.cpython-310-x86_64-linux-gnu.so'>
>>>
```


- 参数 `--onefile`

- LD_LIBRARY_PATH=$(PY_LD_PATH) virtualenv/bin/pip3.9 install -r requirements.txt;


```
$ pyinstaller xxx-yyy.spec
The 'enum34' package is an obsolete backport of a standard library package and is incompatible with PyInstaller. Please `pip uninstall enum34` then try again.


```
```
857 INFO: UPX is not available.

```

- pyinstaller specific python version


- upx
  - upx=True
    - UPX is a free utility available for most operating systems. UPX compresses executable files and libraries, making them smaller, sometimes much smaller. UPX is available for most operating systems and can compress a large number of executable file formats


#### argparse
- from fabric.api import lcd

https://zhuanlan.zhihu.com/p/395173906?utm_id=0

- metavar

- action='append'

- 能否有多个parser ？




### Django doc notes
```
https://www.django-rest-framework.org/api-guide/serializers/

Expanding the usefulness of the serializers is something that we would like to address. However, it's not a trivial problem, and it will take some serious design work
扩展序列化程序的有用性是我们想要解决的问题。然而，这不是一个微不足道的问题，它需要一些认真的设计工作
```

- django serializer & drf serializer
- what should a serializer be ? i mean how to design a suitable serializer ?


- django signal post_save 如何获取到changed的field？
    - Identify the changed fields in django post_save signal
    - 可以在pre_save的signal中设置一个varible来保存old值


```
/usr/local/lib/python3.6/dist-packages/django/db/models/fields/__init__.py:1369: RuntimeWarning: DateTimeField Release.created received a naive datetime (2020-05-03 00:00:00) while time zone support is active.


```

- Django: Query using contains each value in a list
  - https://stackoverflow.com/questions/4824759/django-query-using-contains-each-value-in-a-list

- migration file, elidable=True

- Squashing migrations
    - xx

- queryset 
    - https://www.oschina.net/translate/django-querysets?print
        - queryset是有cache的，因此 `for x in A.objects.filter()`只会运行一次select，但是result会都塞在memory中.
            - iterator可以防止大cache，但是会增加查询次数

- Q函数
  - 作用：对对象进行复杂查询，并支持&（and）,|（or），~（not）操作符。
  - Example: search_obj=Asset.objects.filter(Q(hostname__icontains=keyword)|Q(ip=keyword))
- F函数
  - 避免竞争
  - Reporter.objects.all().update(stories_filed=F('stories_filed') + 1)
- from django.core.cache import caches

- from_db
    - Official doc: https://docs.djangoproject.com/en/4.1/ref/models/instances/#customizing-model-loading
    - 该方法什么时候被调用？每次query是都会被调用吗？

- update_fields
    - for better performance
        - https://dev.to/sankalpjonna/save-your-django-models-using-updatefields-for-better-performance-50ig

    ```
    >>> record = Record.objects.get(id=1)
    >>> record.name = "new record name"
    >>> record.save(update_fields=['name'])

    UPDATE "record" SET "name"='new record name' WHERE  "record"."id" = 1;
    ```

- django 的 signal 什么时候用比较好？

- mute_signals
    - Disable the list of selected signals when calling the factory, and reactivate them upon leaving.


- from django.core.management.base import BaseCommand

- viewsets
    - GenericViewSet
        - GenericViewSet 的 filter_class
        - e.g
        ```
        class XxxViewSet(viewsets.GenericViewSet):
            serializer_class = XxxSerializer
            filter_fields = ('query_option_1',)
            filter_backeds = (DjangoFilterBackend,)
            filter_class = SomeFilter

            def list(self, request):
                name = request.query_params['query_option_1']
                serializer = self.get_serializer({'xx': 'xx'})
                return Response(serializer.data)
        ```

- filterset
    - `strict = True` `strict=True`
    - filter_fields, filter_backeds, filter_class
    - filterset 非 model的，怎么弄


- get_object

- get_queryset

- basename
    - 

#### Software lifecycle
- product & release
- release
    - refers: https://en.wikipedia.org/wiki/Software_release_life_cycle
    - alpha & beta & RC & GA release
        - RC
    - milestone release



#### jekyll
```shell
docker run -it  --rm jekyll/jekyll:3.5 bash

bundle exec jekyll serve

# gem sources -a http://gems.ruby-china.org
Error fetching http://gems.ruby-china.org:
        no such name (http://gems.ruby-china.org/specs.4.8.gz)



install ruby in ubuntu18.04 container by source code
https://tool.4xseo.com/article/501208.html
```


```shell
# kubectl get pods
The connection to the server localhost:8080 was refused - did you specify the right host or port?

[resolve] https://blog.csdn.net/a506681571/article/details/86086005

systemctl start etcd
systemctl start docker
systemctl start kube-apiserver
systemctl start kube-controller-manager
systemctl start kube-scheduler
systemctl start kubelet
systemctl start kube-proxy
----------------

```shell
# minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Stopped
kubeconfig: Configured

- 如何查看 apiserver 的 log ?
```

  - Django
      - Develop django project by docker.
      - safe url
      - url endswith '/' & not endswith
      - Path Parameters
      - setup project from legacy database
      - ALLOWED_HOSTS
        - HTTP Host header attacks
  - Django-rest-framework
      - 2种url参数的区别，为什么要这样？


- http header Range bytes=0-1023
  - 

```
>>> os.path.sep
'/'

# os.path.dirname() method in Python is used to get the directory name from the specified path.
>>> os.path.dirname('/tmp/xx.txt')
'/tmp'
```

- metavar="SERVER-NAME"
```
  -S SERVER-NAME        Execute against the named server (default "default"),
                        add http(s) to designate protocol
```


```
a.py
abc = None

b.py
abc = 1

c.py
from 
```

```
Reloading modules in Python2.x
reload(module)

For above 2. x and <=Python3.3
import imp
imp.reload(module)

Reloading modules for >=Python3.4 and above
import importlib
importlib.reload(module)
```

- ipynb

- tiktoken

- langchain

- gpt-3.5-turbo

- next(iter(
  - 在Python 中,列表(List)是可迭代对象(Iterable),但并不是迭代器(Iterator)。但可以使用内置函数 iter() 将列表转换为迭代器。
    - 可迭代对象必须实现__iter__, 迭代器必须实现__iter__和__next__
  - 文件是迭代器，所以可以直接使用next()，而不需要转换成迭代器
  - 迭代器与列表相比，迭代器是延迟计算(惰性求值：azy evaluation)，更节省内存
    - 比如列表含有中一千万个整数，需要占超过400M的内存，而迭代器只需要几十个字节的空间。因为它并没有把所有元素装载到内存中，而是等到调用 next 方法时候才返回该元素（按需调用 call by need 的方式
    - 本质上 python的for 语句循环就是不断地调用迭代器的next方法）
    - 使用 for 循环或 next() 函数进行遍历
    - 使用 send() 方法向生成器发送值，使用 close() 方法关闭生成器
    - 使用生成器实现并发
      - 异步生成器和 async/await

  - generator
    - 生成器是一种特殊的迭代器，通过yield 关键字来创建，它可以延迟执行，并逐个生成值。
    - 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值。并在下一次执行 next() 方法时从当前位置继续运行。
    - yield 表达式和语句仅在定义 generator 函数时使用，并且仅被用于生成器函数的函数体内部。 在函数定义中使用 yield 就足以使得该定义创建的是生成器函数而非普通函数。

- @pytest.fixture()
  - https://blog.csdn.net/qq_42610167/article/details/119818358

- APITestCase
  - rest_framework.test.APIClient

- @retry(stop=stop_after_attempt(2), reraise=True)
  - reraise=True
    - https://github.com/jd/tenacity#error-handling
```
from tenacity import retry, stop_after_attempt
#@retry(reraise=True, stop=stop_after_attempt(3))
@retry(stop=stop_after_attempt(3))
def raise_my_exception():
    raise Exception("Fail")

try:
    raise_my_exception()
except Exception as e:
    # timed out retrying
    print(e)
```

- python mock a function raise an Exception
  - https://stackoverflow.com/questions/28305406/mocking-a-function-to-raise-an-exception-to-test-an-except-block

- __import__

- sys.modules
@receiver(package_updated, dispatch_uid="hello")
def hello(**kwargs):
  - https://docs.djangoproject.com/en/4.2/topics/signals/#preventing-duplicate-signals
    - A unique identifier for a signal receiver in cases where duplicate signals may be sent.
  
- 使用VS Code调试Python程序
  - https://www.youtube.com/watch?v=0peiVKd37wI
  - https://blog.csdn.net/Kefenggewu_/article/details/124158946

- pdb;pdb.set_trace()
  - GDB是GNU项目中的一个强大的调试工具，它可以用于调试多种程序语言，如C、C++、汇编等语言。在程序出现问题的时候，通过GDB可以帮助我们定位并解决这些问题。在Python中，通常使用CPython来解释执行Python代码，因此GDB也可以用来调试Python程序
  
- os.path.sep
  - 该os下的分隔符

django.db models.Manager


- pip3 install ghapi, 也会install一个fastcore，在shell中可以 import fastcore

#### Celery
  - xxx.delay(x, on_demand=True)

- encoding="u8"
  - the following are all valid aliases: 'U8', 'UTF', 'utf8'

- fastcore

- from django.utils.translation import gettext_lazy as _




- 被 @staticmethod 装饰的函数，调用的时候也要用self.xxx吗？
  - 从我的经验来看，是的，但是有点出乎意料
    - 其实2种调用方法都可以，比如 Time.sec_minutes(10,5),t.sec_minutes(t.sec,5)

- 单引号与双引号的区别，有区别吗？
  - x

```
The magic methods __and__, __or__ and __invert__ are used to override the operators a & b, a | b and ~a respectively.
```
- from concurrent.futures import ThreadPoolExecutor

```
$ python3 -m ensurepip --upgrade
/home/vincent-zhong/osstpmgt/.venv/bin/python3: No module named ensurepip

--------
ModuleNotFoundError: No module named 'apt_pkg'
solution:
  - https://oldtang.com/6102.html
    - 2 works

```

```
$ python3 -m venv .venv
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/vincent-zhong/osstpmgt/.venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']

--- 如何确定 ensurepip 是否是 available 的？

```

```
$ python3 -m venv .venv
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/vincent-zhong/osstpmgt/.venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip'

----------
sudo apt-get install python3-venv 安装了 python3-venv，但还是显示下面这个

$ sudo apt-get install python3-venv
[sudo] password for vincent-zhong: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
python3-venv is already the newest version (3.6.7-1~18.04).
0 upgraded, 0 newly installed, 0 to remove and 122 not upgraded.

------------
Solution:
  - https://stackoverflow.com/questions/66869411/error-command-im-ensurepip-upgrade-default-pip-returned-non-z
  - $ sudo apt-get install python3.8-venv

```

```
scrapy 安装报错 This package requires Rust >=1.48.0.
  - https://www.cnblogs.com/MrHSR/p/16718353.html
```


```
File "/home/vincent-zhong/osstpmgt/.venv/lib/python3.8/site-packages/setuptools/installer.py", line 103, in _fetch_build_egg_no_warn
        raise DistutilsError(str(e)) from e
    distutils.errors.DistutilsError: Command '['/home/vincent-zhong/osstpmgt/.venv/bin/python3.8', '-m', 'pip', '--disable-pip-version-check', 'wheel', '--no-deps', '-w', '/tmp/tmp72qs0tbh', '--quiet', 'cffi>=1.4.1']' returned non-zero exit status 1.
    
    ----------------------------------------
Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-d2bj5_ju/pynacl/

-----
solution:
  - pip3 install --upgrade pip
```

```
Failed to build mysqlclient psycopg2 pykerberos python-ldap
ERROR: Could not build wheels for mysqlclient, psycopg2, pykerberos, python-ldap, which is required to install pyproject.toml-based projects

--------

```

```
$ pip3 install yaml
Defaulting to user installation because normal site-packages is not writeable
ERROR: Could not find a version that satisfies the requirement yaml (from versions: none)
ERROR: No matching distribution found for yaml

----
pip3.8 install yaml
```

- Split a Python list into fixed-size chunks

- @pytest.mark.parametrize

- def notice(self) -> "str":
  - xx
  - 双引号有必要吗？

- from typing import ClassVar, Final
  - type hints
  - ClassVar
    - 类变量
    - 适用场景
  - Final
    - 告知类型检查器某名称不能再次赋值或在子类中重写的特殊类型构造器

- __subclasses__
  - 函数获取类的所有子类

- from types import MappingProxyType
  - 在Python3.3开始
  - 不可变字典

- from dataclasses import dataclass, field, fields
  - dataclass
    - 被dataclass装饰的类，根据类中定义的name，unit_price。。。会自动生成一个__init__方法
  - @dataclass(frozen=True)
  - @dataclass
    - it's to replace `namedtuple` in python2
      - namedtuple: https://blog.csdn.net/qq_30159015/article/details/80356226
- 
```
myVar: Union[int, str] = "Hello"
myVar = 5

mylist: List[Union[int, str]] = [1,2,3]
mylist = ["a", "b"]
```

- from tastypie.authentication import ApiKeyAuthentication, MultiAuthentication
  - ApiKeyAuthentication
  - MultiAuthentication
  - from rest_framework.authentication import BaseAuthentication
    - 

- defaultdict(lambda: 0)
  - 如果key不存在，则不会报错，且key对应的value是0
  - defaultdict(lambda: defaultdict)

- threading.Semaphore(MAX_THREADS)
  - why named 'semaphore'

- from queue import Queue
  - 适用场景
    - A synchronized queue class
    - queue 模块实现了多生产者、多消费者队列。这特别适用于消息必须安全地在多线程间交换的线程编程。模块中的 Queue 类实现了所有所需的锁定语义
  - queue.put(1）
    - 
    - The method put() will block if the queue has reached its maximum capacity or executed in blocking mode.
      - 默认有block=True,阻塞时间由timeout确定

- np.cumsum(
  - https://blog.csdn.net/weixin_49346755/article/details/124139184
```
import numpy as np
a = np.array([1, 2, 3, 4, 5])
result = np.cumsum(a)
print(result)
```

- pandas.DataFrame
  - DataFrame 既有行索引，也有列索引


- sys.path.append
  - `sys.path 返回的是一个列表,当我们要添加自己的搜索目录时,可以通过列表的 append() 方法,这种方法导入的路径会在 Python 程序退出后失效`

- 使用 pd.isna() 判断常规缺失值 NaN（np.nan）和 None
pd.isna(np.nan)  # 返回 True， NaN 被判断为缺失值
pd.isna(None)    # 返回 True， None 被判断为缺失值
pd.isna('')      # 返回 False，空字符不被判断为缺失值
pd.isna('\n')    # 返回 False，换行符不被判断为缺失值
pd.isna('\t')    # 返回 False，制表符不被判断为缺失值
  - 我：为什么不直接 if not xxx 呢？可能是因为：
```
>>> if np.nan:
...     print(1)
...
1
```

- data = df.at[0, 'a']
  - 作用：获取某个位置的值，例如，获取第0行，第a列的值，即：index=0，columns='a'

- np.radians 将角度转换为弧度

- strftime('%j')
  - 使用 strftime(‘%j’) 进行转换会返回用零填充的 3 位总天数
  - 2023/04/01的总天数: 091

- pd.concat()函数可以沿着指定的轴将多个dataframe或者series拼接到一起，这一点和另一个常用的pd.merge()函数不同，pd.merge()函数只能实现两个表的拼接

- pd.api.types.is_datetime64_any_dtype 函数的返回值是一个布尔值，如果变量的数据类型是datetime64[ns]，则返回True，否则返回False

- np.percentile(
```
>>> xxx=np.array([1,2,3,4,5,6,7,8,9])
>>> print(np.percentile(xxx,1))
1.08
>>> print(np.percentile(xxx,60))
5.8
```
```
# 示例
a = [1, 2, 10, 100] # or 'a = np.array([1, 2, 10, 100])' or 'a = range(10)'
np.percentile(a, 1) # 1.03 => 1 + (2-1)/(100/3) = 1.03
np.percentile(a, 100/3+1) # 2.240000000000002 => 2 + (10-2)/(100/3) = 2.24
```

- yy = df.sub(value).abs().idxmin()
  - sub() 方法用指定的值减去 DataFrame 中的每个值
  - abs() 方法返回 DataFrame 且其中每个值都是绝对值
  - 各column上最小值的横index

- .apply(

- np.concatenate
  - concatenate 一词在英文中是级联的意思，我们可以简单地理解为连接，拼接, 可以合并一维，也可以合并多维
```
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.concatenate((a, b))
>>> [1 2 3 4 5 6]
```

- np.full
  - 返回一个给定大小和类型并且以指定数字全部填充的新数组

- np.linspace
  - 它用于在指定的区间内创建等间隔的数值
  -  np.linspace(0, 10, 10) 这会生成一个包含从0到10的10个等间隔数值的一维数组
    - np.linspace(kc_ini, kc_mid, dev_period.size)

- df.drop(columns=['P'])
  - `最后，记得将修改后的DataFrame赋值给一个变量，或使用inplace=True参数来直接修改原始的DataFrame`


lines = f.readlines()

            ^^^^^^^^^^^^^

UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 1812: illegal multibyte sequence

lines = f.readlines()

            ^^^^^^^^^^^^^

  File "<frozen codecs>", line 322, in decode

UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb7 in position 1550: invalid start byte

    with open(text_file_path, 'rb') as f:

        lines = f.readlines()

        last_lines = lines[-2:]

        print("----------------")

        print('\n'.join([x.decode('utf8') for x in last_lines]))

        print("----------------")

 t1.join()

#将t线程设置成阻塞状态，直到t线程执行完后才能进入下一线程---------------- 

.astype(---------------- 

用于将 Series 或 DataFrame 中的数据转换为指定的数据类型---------------- 

Return the cumulative sum of the elements along a given axis---------------- 

numpy.cumsum---------------- 

errors='coerce' 遇到不能转换的就会设置为NAN---------------- 

sep='\s+'---------------- 

\s+ 意思就是至少有一个空白字符存在---------------- 

skiprows=11 跳过前面10行---------------- 

wth_data.drop(wth_data.index[0], inplace=True)  # 删除第一行---------------- 

A unique index is an index that contains non-duplicate labels. In such an index there cannot be two or more identical labels.---------------- 

Monotonic Index

Monotonicity is a mathematical property that indicates a given function maintains a non-increasing or non-decreasing order throughout its domain---------------- 

Monotonic Index

Monotonicity is a mathematical property that indicates a given function maintains a non-increasing or non-decreasing order throughout its domain---------------- 

unique_index = pd.Index(list('abc'))

unique_index.get_loc('b')

1---------------- 

>>> monotonic_index = pd.Index(list('abbc'))

>>> monotonic_index.get_loc('b')

slice(1, 3, None)---------------- 

>>> non_monotonic_index = pd.Index(list('abcb'))

>>> non_monotonic_index.get_loc('b')

array([False,  True, False,  True])---------------- 

# 使用 iloc 获取特定行和列的数据

# 获取第二行（索引为1）的所有列数据

row_1 = df.iloc[1, :]---------------- 

.iloc[行：列]---------------- 

data.iloc[:,[0]] #取第0列所有行，多取几列格式为 data.iloc[:,[0,1]]---------------- 

data.loc[:,['A']] #取'A'列所有行，多取几列格式为 data.loc[:,['A','B']]---------------- 

'{:12.7f}'.format(14.12345678123)   >>> '  14.1234568'---------------- 

'{:012.7f}'.format(14.12345678123)    >>> '0014.1234568'---------------- 

{:>12s}   it is used to add space around the element your printing;> - Add space to left side; < - Add space to right side  ---------------- 

>>> int('30.000')

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: invalid literal for int() with base 10: '30.000'---------------- 

>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数

[1, 4, 9, 16, 25]


- @property
  - https://www.liaoxuefeng.com/wiki/1016959663602400/1017502538658208
    - 可以让调用者写出简短的代码，同时保证对参数进行必要的检查
    - 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性
    - 练习, 给一个Screen对象加上width和height属性，以及一个只读属性resolution
```
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
```
---------------- 

od = OrderedDict()

od['a'] = 1

od['b'] = 2

od['c'] = 3

od['d'] = 4



for key, value in od.items():

    print(key, value)---------------- 

datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")---------------- 

>>> from collections import Counter

>>> Counter([11,22,22])

Counter({22: 2, 11: 1})---------------- 

获取上上级目录

print(os.path.abspath(os.path.join(os.getcwd(), "../..")))---------------- 

>>> 1/3

0.3333333333333333

>>> 1//3

0---------------- 

selected = random.choices(population, k=3)---------------- 

re.sub() 的详细用法，该函数主要用于替换字符串中的匹配项---------------- 

        xx = re.findall(r'[\u4e00-\u9fff]|[≥℃≤＞＜]|\d|[a-zA-Z]+', col)

---------------- 

>>> '大风_大于等于1天'.strip('_大于等于1天')

'风'---------------- 

>>> '大风_大于天天天天天天天天天天天天天天天天等于1天'.strip('_大于等于1天')

'风'---------------- 

Tuples are ordered collections of elements, which are immutable (meaning they can't be changed once created). Sets, on the other hand, are unordered collections of unique elements---------------- 

>>> _tuple=(1,2,1)

>>> _tuple

(1, 2, 1)---------------- 

>>> s

'{$.precipitation_6}\t{$.wind_6}\t{$.tmax_6}/{$.tmin_6}'

>>> re.findall("{\$\.(.*?)}", s, re.DOTALL)

['precipitation_6', 'wind_6', 'tmax_6', 'tmin_6']---------------- 

>>> re.findall("{\$\.(.*?)}", s)

['precipitation_6', 'wind_6', 'tmax_6', 'tmin_6']---------------- 

python正则表达式 （.*?）与（.*）的区别  https://blog.csdn.net/m0_37962192/article/details/103768541---------------- 

（.*?）是非贪婪的，即匹配最少数量的就够了---------------- 

                days_condition = re.findall(f'_(大于等于|小于等于|大于|小于){days_count}d', cc)[0]

---------------- 

dict.setdefault(key, default)---------------- 

print(re.findall(r"预[计|报].*[\?日]+.*?,", ss))

---------------- 

['预计4月?日-?日日均温稳定在12℃以上且无降雨,', '预计4月?日-?日有持续降水,', '预计4月?日-?日有持续低温阴雨天气,'---------------- 

xx = re.findall(r"预[计|报].*?[\?日]+.*?,", ss)

---------------- 

_extrame_weather---------------- 

exec 函数没有返回值，它只是在指定的命名空间中执行代码---------------- 

code_str = "a = 10"
   exec(code_str)

   # 在不同的命名空间中访问变量
   print(a)     # 报错，因为 a 只在执行的命名空间中有效
   print(locals())  # 输出结果为 {'a': 10}

g = {'x': 1, 'y': 2}

l = {}

exec('''

global x,z

x=100

z=200

m=300

''', g, l)

print(g)  # {'x': 100, 'y': 2,'z':200,......}

print(l)  # {'m': 300}---------------- 

>>> set({1,2})==set({2,1}) 

True---------------- 

tuple(元组)、set(集合)---------------- 

>>> type({}) 

<class 'dict'>

- if manage_strategy_dict is not None: 是否等效于 if not manage_strategy_dict:
  - 不一样

```
from retry import retry
 
@retry()
def make_trouble():
    print ('retryxing...')
    raise
 
if __name__ == '__main__':
    make_trouble()
 
# 输出: 一直重试，直到运行成功
retryxing...
retryxing...
retryxing...
retryxing...
retryxing...
retryxing...
```

```
    def extract_render_vars(line):
        _vars = re.findall("{\$(.*?)}", line)
        return _vars
```