### Software test

```shell
coverage run --branch --source=. --omit=*/tests*,*__init__* -m unittest discover
```

---------
https://www.bilibili.com/video/BV1LD4y1o79K/?spm_id_from=autoNext&vd_source=f209dde1a1d76e06b060a034f36bb756

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm

https://www.gutenberg.org/files/1998/1998-h/1998-h.htm#link2H_INTR

2022年09月21日10:49:03

- test --> side effect

- How coverage test a specific case ?

```python
>>> try:
...     assert 1==2
... except Exception as exc:
...     print(str(exc))
...

>>>
```

### Test
- 回归测试
