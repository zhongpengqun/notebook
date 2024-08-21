# 为什么需要Flask-SQLAlchemy，而不直接使用SQLAlchemy?Flask-SQLAlchemy解决了哪些问题？
`It simplifies using SQLAlchemy with Flask by setting up common objects and patterns for using those objects, such as a session tied to each web request, models, and engines.`
    - `a session tied to each web request` 与每个web请求关联的会话
`Flask-SQLAlchemy does not change how SQLAlchemy works or is used. `

- 个人理解
    - 针对web做了相应的方便，比如 `db.get_or_404(User, id)`

# 报错
```
用SQLAlchemy的时候: Can't reconnect until invalid transaction is rolled back

- https://groups.google.com/g/sqlalchemy/c/moAjxnVEy3U
    - `To solve this problem, you should open a new db session at the beginning of the web request, and close the session at the end of the request.`
```
