```
# python -m pyflowchart service.py -f 田块的灌溉决策算法.运行算法逻辑 -o static/flow.html;gunicorn -b 0.0.0.0:8000 app:app
Saved HTML to static/flow.html
[2025-01-20 19:03:57 +0800] [9] [INFO] Starting gunicorn 21.2.0
[2025-01-20 19:03:57 +0800] [9] [INFO] Listening at: http://0.0.0.0:8000 (9)
[2025-01-20 19:03:57 +0800] [9] [INFO] Using worker: sync
[2025-01-20 19:03:57 +0800] [10] [INFO] Booting worker with pid: 10
/usr/local/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.20) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
/usr/local/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py:868: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
[2025-01-20 19:08:04 +0800] [9] [INFO] Handling signal: winch


[2025-01-20 19:09:15 +0800] [9] [CRITICAL] WORKER TIMEOUT (pid:10)
[2025-01-20 19:09:15 +0800] [10] [INFO] Worker exiting (pid: 10)
[2025-01-20 19:09:15 +0800] [9] [ERROR] Worker (pid:10) exited with code 1
[2025-01-20 19:09:15 +0800] [9] [ERROR] Worker (pid:10) exited with code 1.
[2025-01-20 19:09:15 +0800] [14] [INFO] Booting worker with pid: 14
/usr/local/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.20) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
/usr/local/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py:868: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
[2025-01-20 19:10:03 +0800] [9] [CRITICAL] WORKER TIMEOUT (pid:14)
[2025-01-20 19:10:03 +0800] [14] [INFO] Worker exiting (pid: 14)
[2025-01-20 19:10:04 +0800] [9] [ERROR] Worker (pid:14) exited with code 1
[2025-01-20 19:10:04 +0800] [9] [ERROR] Worker (pid:14) exited with code 1.
[2025-01-20 19:10:04 +0800] [18] [INFO] Booting worker with pid: 18
/usr/local/lib/python3.9/site-packages/requests/__init__.py:102: RequestsDependencyWarning: urllib3 (1.26.20) or chardet (5.2.0)/charset_normalizer (2.0.12) doesn't match a supported version!
  warnings.warn("urllib3 ({}) or chardet ({})/charset_normalizer ({}) doesn't match a supported "
/usr/local/lib/python3.9/site-packages/flask_sqlalchemy/__init__.py:868: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
```
用Python脚本请求，找到了原因
```
C:\Users\zlzk>python
Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> requests.get('http://10.109.2.246:8000/user/login')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "E:\python10\lib\site-packages\requests\api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
  File "E:\python10\lib\site-packages\requests\api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "E:\python10\lib\site-packages\requests\sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "E:\python10\lib\site-packages\requests\sessions.py", line 724, in send
    history = [resp for resp in gen]
  File "E:\python10\lib\site-packages\requests\sessions.py", line 724, in <listcomp>
    history = [resp for resp in gen]
  File "E:\python10\lib\site-packages\requests\sessions.py", line 191, in resolve_redirects
    raise TooManyRedirects(
requests.exceptions.TooManyRedirects: Exceeded 30 redirects.
```
