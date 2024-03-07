# 如何赋值  https://www.jianshu.com/p/a9de5f4ec3f7
# makefile的变量有如下四种赋值方式
#  ?  简单赋值 ( := )     zhong: 获得到第一次赋的值
#  ?  递归赋值 ( = )      zhong: 获取到最终值
# ok   条件赋值 ( ?= )
# ok    追加赋值 ( += )

boy := I am a boy
girl := $(boy)?
boy := Maybe

qa :
    @echo "girl : $(girl)"
    @echo "boy : $(boy)"

.PHONY : qa
