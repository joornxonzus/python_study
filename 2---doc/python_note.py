python_note
=====================================================
第0章 前言
=====================================================
编程世界的主流思想
	结构化编程
		c fortran 功能 子功能
	面向对象开发	
		兰布达验算
		LISP，ERLang
		尾递归，栈
		防御式编程
	ER实体关系
		关系数据库
		选择
		投影
		笛卡尔
	面向对象编程
		集成封装多态
解释型脚本语言的特点
	解释型和编译型
	运行时和动态类型
	强类型和弱类型
	开发效率
	通用性强
	内置方便的数据容器
	容易扩展和嵌入
编程语言类型
	嵌入式
		c/c++
		Python/ERlang/lua
	网络应用
		java/.net
		python/Erlang/Perl/ASP/Shell/Lua
	网络界面
		flex AS/Java Applet
		HTML/JS/lisp
	APP
		Android/Object-c
		Html5/Lua
方法论
	笛卡尔方法论
		拆分
		排序
		处理
		归并
	软件工程过程方法论
		软件生命周期
		RUP同意软件过程管理
		敏捷开发
	项目管理
		计划
		组织
		执行
		控制
现实世界的变化
	多任务 图界面 多线程 跨平台 网络分布式 多语言
程序员的境界
	线性级
	逻辑级
	架构级
	工程级
程序员的陋习
	自我
	封闭
	惯性
	沟通障碍
	一叶障目
	乐观估计工作量
	拒绝变化
	拒绝重构
=====================================================
第一章 环境，安装
=====================================================
Windows上python开发
	python运行环境的安装和配置
	交互式开发环境
		查看模块 查找python module
		python的帮助文档
	Setuptools
	wingide
	自省的便利
	两个模块os sys
python idle的基本使用
	安装
	python的shell分类
		黑色的
		白色的idle
	常用的idle
	查看上一条命令快捷键
		alt+n
		alt+p
	运算命令
		print(5+4)
		print("this is a py\n"*8)
远程的Linux的连接方式
	ssh root@223.4.19.237
=====================================================
第一章 基础语法
=====================================================
	基本概念
		常量
			常量无名
			不需修饰
		数
			整数
				100
				0xff
			长整数
			浮点数
				1.23e9
				-9.01
			复数
		字符串
			''
			""
			""" """ 多行字符串常用
			\n \t \r
			r''
			r""
			5+8 计算
			'5'+'8' 字符串
			字符串中出现单引号和双引号
			print('let\'s go') 转义
			print("let's go") 引号交叉
			print('c:\now') 问题
			print(r'c:\now') 原生字符串
			print(r'c:\now\') 语法错误，原生末尾不能加\
		布尔型
			True
			False
			and,or,not 运算得出
		空值
			None
		变量
			python没有变量只有值，把变量贴在值上
			使用前需要赋值
			变量名不以数字开头
			变量名=变量值
			typr()
		常量
			大写
			PI=1.1415926
			9/3=3.0
			10/3=3.333
			10//3=3
			10%3=1
		变量
		数据类型
		逻辑行与物理行
		缩进
	运算符和表达式
	逻辑控制
		分支
			if 逻辑 :
				程序
			else :
				程序
		循环
			which 逻辑 :
				程序
	函数
	面向对象
	异常处理
	模块和包
	输入输出和文件的操作
		# -*- coding: utf-8 -*-
		print()
		str=input()
		编码
		py默认是Unicode
		print('中文q')
		ord('A')
		ord('中')
		chr(66)
		'\u4e2d\u6587'
		byte类型的
		x=b'ABC' (一个字符对应多个字节)
		'ABC'.encode('ascii')
		'中文'.encode('utf-8')
		s = 'Python-中文'
		print(s)
		b = s.encode('utf-8')
		print(b)
		print(b.decode('utf-8'))
	格式化
		'Hi, %s, you have $%d.' % ('Michael', 1000000)
		'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)

	常见的容器
		list 列表
		len 长度
		tuple () 元组(不可修改)
		list [] 列表(可修改)	
		

















