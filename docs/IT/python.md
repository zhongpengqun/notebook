- modules
    - getopt
    - getpass
    - syslog
    - Fabric

- python中有对应c中make的项目build工具吗？

- asyncio

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

- iterator
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
