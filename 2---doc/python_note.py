python_note
=====================================================
第一章 环境，安装
=====================================================
shell的基本使用
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
=====================================================
第一章 基础语法
=====================================================
	输入输出
		# -*- coding: utf-8 -*-
		print()
		str=input()
	字符串
		5+8 计算
		'5'+'8' 字符串
		字符串中出现单引号和双引号
		print('let\'s go') 转义
		print("let's go") 引号交叉
		print('c:\now') 问题
		print(r'c:\now') 原生字符串
		print(r'c:\now\') 语法错误，原生末尾不能加\
	数据类型
		整数
			100
			0xff
		浮点数
			1.23e9
			-9.01
		字符串
			''
			""
			""" """ 多行字符串常用
			\n \t \r
			r''
			r""
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
		常量
			大写
			PI=1.1415926
			9/3=3.0
			10/3=3.333
			10//3=3
			10%3=1
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
	分支
		if 逻辑 :
			程序
		else :
			程序
	循环
		which 逻辑 :
			程序
	
		
		
		

















