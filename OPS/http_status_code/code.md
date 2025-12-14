| 2XX | 成功 |
| --- | --- |
| 200 | OK                      | 请求成功（GET/POST 等请求的默认成功响应）。
| 201 | Created                 | 请求成功且服务器创建了新资源（如 POST 新增数据、文件上传成功）。
| 202 | Accepted                | 请求已接收，但处理未完成（如异步任务提交）。
| 204 | No Content              | 请求成功，但响应体为空（如 DELETE 删除数据）。


| 3XX | 重定向 |
| --- | --- |
| 301 | Moved Permanently       | 资源永久移动到新地址（浏览器会缓存新地址，后续直接访问新地址）。
| 302 | Found                   | 资源临时移动到新地址（浏览器不缓存，每次请求仍会先访问原地址）。
| 304 | Not Modified            | 资源未修改（客户端缓存仍有效，直接使用本地缓存，无需重新下载）。核心：基于 If-Modified-Since/If-None-Match 缓存机制，减少带宽消耗。
| 307 | Temporary Redirect      | 临时重定向（严格保持原请求方法，如 POST 不会转为 GET，比 302 更规范）。
| 308 | Permanent Redirect      | 永久重定向（严格保持原请求方法，比 301 更规范）。


| 4XX | 客户端错误 |
| --- | --- |
| 400 | Bad Request             | 请求参数错误、格式非法（如 JSON 语法错误、表单字段缺失）。
| 401 | Unauthorized            | 未授权（需要登录或 Token 无效，服务器未识别用户身份）。
| 403 | Forbidden               | 禁止访问（用户已认证，但无权限操作资源，如普通用户访问管理员接口）。
| 404 | Not Found               | 资源不存在（URL 错误、页面被删除，最常见的错误码）。
| 405 | Method Not Allowed      | 请求方法不支持（如服务器只允许 GET，客户端用了 POST）。
| 406 | Not Acceptable          | 请求的资源不支持客户端指定的 Accept 头（如请求 JSON 格式，但服务器只返回 XML）。
| 408 | Request Timeout         | 请求超时（客户端等待服务器响应时间超过了服务器设置的超时时间）。
| 415 | Unsupported Media Type  | 请求的媒体类型不被服务器支持（如上传文件时指定了不支持的文件类型）。
| 429 | Too Many Requests       | 客户端请求次数超过了服务器限制（如 API 调用频率超过了配额）。


| 5XX | 服务器错误 |
| --- | --- |
| 500 | Internal Server Error   | 服务器内部错误（如代码逻辑错误、数据库连接失败等）。
| 501 | Not Implemented         | 服务器不支持请求的功能（如请求了服务器不支持的 HTTP 方法）。
| 502 | Bad Gateway             | 网关错误（如反向代理返回了错误的响应）。
| 503 | Service Unavailable     | 服务不可用（如服务器正在维护、过载等）。
| 504 | Gateway Timeout         | 网关超时（如反向代理等待服务器响应超时）。
