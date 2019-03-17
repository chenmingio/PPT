# PPT开发日志

## MVP

### Quotations数据结构设计
name relation

#### 先做5个key：
collection = quotations
quotation = documents

研究document里面怎么再创建document

### 用shell输入到mongodb里
* 已经用robomongo搞定。[MongoDB Insert Document](https://www.tutorialspoint.com/mongodb/mongodb_insert_document.htm)
	* 注意mongodb支持的几个type [MongoDB Data Types - 16 Various Data Types in MongoDB - DataFlair](https://data-flair.training/blogs/mongodb-data-types/)
	* 以及输入中最后一个item不要加逗号

### 用python脚本文件读写mongodb里的cbd数据
[Tutorial — PyMongo 3.7.2 documentation](https://api.mongodb.com/python/current/tutorial.html)

所谓document，其实就是record。W3C的教程写的相当不错。
[Python MongoDB Insert Document](https://www.w3schools.com/python/python_mongodb_insert.asp)

插入record对象的要求：
`TypeError: document must be an instance of dict, bson.son.SON, bson.raw_bson.RawBSONDocument, or a type that inherits from collections.MutableMapping`

具体代码在mongopy.py里

### 在timelogger项目里实现user seesion control功能

done

### 使用bottle结合pymongo

done


### tpl的简单草稿

done
### 实现简单的read url（输入？得到对应的json table）

done

### 实现上传url

done

### 实现修改url

done
#### 修改页面的设计

done

### 从localhost部署到VPS上

done

剩下使用supervisor的任务

## 第一轮优化

添加报表页面

添加project info页面

## 第二轮优化






