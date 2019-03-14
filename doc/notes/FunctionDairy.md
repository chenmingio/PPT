## 背景

* 最大程度自动化项目采购日常工作
* 工作环境是公司电脑（不能随便运行程序）+ 大量MS Excel报表 + 一些MS Word和PPT
* 大量精力被浪费在从各方（项目经理、设计、物流、质量、供应商端等）收集简单信息，汇总在几张excel报告里。


## 功能

### 模块1 - 内部文件

* 自动生成Project大文件夹
* 文件夹的子文件夹、文件夹内的excel根据一张meta-information表格生成
* 生成后也可以额外增加一批
* 各张excel内引用的数据互相关联，只需且只能在一处输入

### 模块2 - 报价

* 上传表格，自动生成项目，提醒入选的供应商报价。
* 供应商在web端固定的格式上报价和更新报价。
* 汇总报价，简单计算，生成比价表。
* 自动按模板生成合同（HTML/MD)

### 模块3 - 会议

* 供应商在web端上传excel/ppt/pdf格式的技术文件
* 供应商修改技术文件
* 客户的设计和质量审核技术文件，批复，同意。
* 生成签字版本的技术文件

## 如何实现

#### 模块1 - 内部文件

excel + VBA

#### 模块2 - 报价

Python + Sql + HTML ...

#### 模块3 - 会议

Github? 

## 思考与疑问

### 关于编程本身

* 编程一方面就是回答这个问题：陈铭这个家伙在组织中扮演的是何种机械功能？
* 能否借鉴/借用git/github

### 未来的功能

* 利用web端的可供性，改变目前的“报价/更新”的模式
* 合并其他部门的功能