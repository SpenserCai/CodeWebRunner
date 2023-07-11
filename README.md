<!--
 * @Author: SpenserCai
 * @Date: 2023-06-29 10:27:02
 * @version: 
 * @LastEditors: SpenserCai
 * @LastEditTime: 2023-07-11 10:52:00
 * @Description: file content
-->
# CodeCvWebRunner

以WebApi的方式运行Python代码，这将是AiMediaService的一部分，为了实现一个可以整合ai能力PaaS化开发落地应用的平台

# 部署

## 首次运行
```bash
bash run.sh
```
上述代码会自动创建虚拟环境并安装依赖

## 安装ai能力包

在本项目相同的虚拟环境下安装ai能力包

## 运行

```bash
bash run.sh
```
此时运行本服务即可实现ai能力的调用，注意编写代码是import对应的ai能力包


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
