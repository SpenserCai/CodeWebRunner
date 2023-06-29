<!--
 * @Author: SpenserCai
 * @Date: 2023-06-29 10:27:02
 * @version: 
 * @LastEditors: SpenserCai
 * @LastEditTime: 2023-06-29 17:19:59
 * @Description: file content
-->
# OpenCvWebRunner

以WebApi的方式运行OpenCv的图像处理算法

## 用法请求/api/run接口

### 请求参数

```json
{
  "argv": {
    "a": 1,
    "b": 2
  },
  "code": "ab=a+b\naxb=a*b\nreturn {\"sub\":ab,\"x\":axb}"
}
```

### 返回结果

```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "sub": 3,
    "x": 2
  }
}
```