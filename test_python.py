'''
Created on Aug 4, 2020

@author: tim
'''

if __name__ == '__main__':
    # 這邊是一些基本資料型態的例子
    # 我們在檢查型態的時候，通常可以用'type'這個函式
    
    # 整數int
    print(type(1)) # output: <class 'int'>
    
    # 浮點數float

    print(type(1.0)) # output: <class 'float'>
    
    # 布林值bool

    print(type(True)) # ouptut: <class 'bool'>
    
    # 字串 str
    #===========================================================================
    # 'c' # 一個字母在其他語言可能有另一個字元型態，在python則為str
    # 'hello'
    # 'hi, how are u'
    # "double quote" # 單引號跟雙引號都可以表示str，但不能一單一雙
    # "you're good" # 在雙引號字串裡的單引號會被視為字串內容的一部分
    # '' # 空字串
    # 'I am a "bad" guy' # 反之亦然
    # 'you\'re are good' # 如果在單引號裡還想使用單引號當成字串內容，需要跳脫(\)
    # '\n' # 特殊字串: \n = 換行
    # '\t' # 特殊字串: \t = tab
    #===========================================================================
    
    # 如果想在字串印出跳脫字元\，需要使用多一個\來阻止跳脫發生
    #'hello \\n\\n' # => 'hello \n\n'
    
    print(type('1')) # output: <class 'str'>
    
    #'''
    #以下list, tuple, dict, set屬於collection，可以裝載多筆資料，這邊只有一些例子
    #之後介紹個細節的用法
    #'''
    
    #===========================================================================
    # # 列表 list
    # [1, 2, 3]
    # [1, '2', True] # 可以同時擁有不同類型的資料
    # [1]
    # [] # 空列表
    # list() # 空列表
    #===========================================================================
    
    print(type([1, 2])) # output: <class 'list'>
    
    #===========================================================================
    # # tuple
    # (1, 2)
    # (1,) # 如果想要使用只有一筆資料的tuple，需要這樣寫
    #===========================================================================
    
    print(type((1, 2))) # output: <class 'tuple'>
    
    #===========================================================================
    # # 字典 dict
    # {1: 'hi'}
    # {'key': 'value'}
    # {} # 空字典
    # dict() # 空字典
    #===========================================================================
    
    print(type({})) # output: <class 'dict'>
    a = {1:'dddd','1': 455555}
    print(a['1'])
    
    #===========================================================================
    # # 集合 set
    # set() # 空的set，值得注意的是{}是空的dict不是set
    # {1}
    # {1, 2, 3}
    # set([1, 2, 3]) # 宣告set的時候，是從list轉換過來
    #===========================================================================
    
    print(type({1, 2, 3})) # output: <class 'set'>
    a=[1, 2, 3]
    print(a[1]) 