#插值方法
====================
- Liner
- Hermite
- Lagrange
- Newton

##Liner
可以简单的认为，给出了两个数字，这两个数字分别都带有一个代表权重的数字，算加权平均数后，计算我们想得到的权重对应的数字。
一般情况下，用点+斜率的方式表述，我们只需要计算：

_a0+a1x0 = y0_

_a0+a1x1 = y1_

找到对应的a0和a1取值，即可得到该直线上的任意一点。
编程方法中，我们会更多的使用该公式的变形——找到基函数。