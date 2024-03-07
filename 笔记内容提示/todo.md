>>>re.findall('.{3}aaa.{1}', "\nxxxaaaxxaaaffff")
['xxxaaax']

↑所以如果我想搜索python，只会显示一条，但是实际上有2条
    - 换一种思路，先replace，然后在findall就可以解决了

todo:
- console output是否可以在remote机器的terminal上output出来?

