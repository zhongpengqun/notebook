CSRF


- 202 vs 200

CORS跨域
    - 以避开浏览器的同源策略（英语：same-origin policy），是 JSONP 模式的现代版，与 JSONP 不同，CORS 除了 GET 请求方法以外也支援其他的 HTTP 请求
    - 什么是域：当一个请求url的协议、域名、端口三者之间任意一个与当前页面url不同即为不同的域

POST方法的参数形式
    - GET方法是否也有这些形式？
    - multipart/form-data：既可以上传文件等二进制数据，也可以上传表单键值对，只是最后会转化为一条信息；
    - x-www-form-urlencoded：
        - 只能上传键值对，并且键值对都是间隔分开的。等价于application/x-www-from-urlencoded,会将表单内的数据转换为键值对，比如,name=java&age = 23
    - binary
        - 相当于Content-Type:application/octet-stream,从字面意思得知，只可以上传二进制数据，通常用来上传文件，由于没有键值，所以，一次只能上传一个文件
    - raw
        - 可以上传任意格式的文本，可以上传text、json、xml、html等
    - form-data
        - 等价于http请求中的multipart/form-data,它会将表单的数据处理为一条消息，以标签为单元，用分隔符分开。既可以上传键值对，也可以上传文件。当上传的字段是文件时，会有Content-Type来表名文件类型；content-disposition，用来说明字段的一些信息；由于有boundary隔离，所以multipart/form-data既可以上传文件，也可以上传键值对，它采用了键值对的方式，所以可以上传多个文件。
    - 哪些形式可以上传文件？

- python request.post中data和json参数的区别？
如：requests.post(url, data={key: value}, json={key: value}, args)
    - https://www.datasciencebyexample.com/2023/03/12/using-json-or-data-parameter-in-requests-post/
        - `Using the json parameter is the preferred way to send JSON data in a POST request because it’s more concise and Pythonic. It also automatically sets the Content-Type header to application/json, which is the recommended way to send JSON data in an HTTP POST request`
        - `The data parameter is an alternative way to send JSON data in a POST request using the requests library`
            - `The data parameter expects a byte string, which is why we convert the JSON string to a byte string using json.dumps().`

JSON Schema (json-schema) 本身是一段 JSON 格式的数据，如下例所示
```
{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name":  { "type": "string" },
        "email": { "type": "string" },
        "age": {
            "type": "number",
            "minimum": 0,
            "exclusiveMinimum": false
        },
        "telephone": {
            "type": "string",
            "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"
        }
    },
    "required": ["name", "email"],
    "additionalProperties": false
}
```
下面就是一个符合上面 Schema 的 JSON 数据：
```
{
    "name": "C语言中文网",
    "email": "2758010091@qq.com",
    "age": 18
}
```
    - schema如何表示比如{"xx": [{"a": "b"}，{"11":"22"}]} 这种？
    - "additionalProperties": false,
        - `json串只能出现schema定义的属性`
    - 在线转schema辅助工具：https://www.lddgo.net/string/generate-json-schema
    