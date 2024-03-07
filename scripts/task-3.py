# coding: utf-8
import re

cn_origin = """至今一切社会的历史都是阶级斗争的历史
自由民和奴隶、贵族和平民、领主和农奴、行会师傅和帮工，一句话，压迫者和被压迫者，始终处于相互对立的地位，进行不断的、有时隐蔽有时公开的斗争，而每一次斗争的结局都是整个社会受到革命改造或者斗争的各阶级同归于尽
在过去的各个历史时代，我们几乎到处都可以看到社会完全划分为各个不同的等级，看到社会地位分成多种多样的层次
在古罗马，有贵族、骑士、平民、奴隶，在中世纪，有封建主、臣仆、行会师傅、帮工、农奴，而且几乎在每一个阶级内部又有一些特殊的阶层
从封建社会的灭亡中产生出来的现代资产阶级社会并没有消灭阶级对立
它只是用新的阶级、新的压迫条件、新的斗争形式代替了旧的
但是，我们的时代，资产阶级时代，却有一个特点：它使阶级对立简单化了
整个社会日益分裂为两大敌对的阵营，分裂为两大相互直接对立的阶级：资产阶级和无产阶级
从中世纪的农奴中产生了初期城市的城关市民；从这个市民等级中发展出最初的资产阶级分子
美洲的发现、绕过非洲的航行，给新兴的资产阶级开辟了新天地
东印度和中国的市场、美洲的殖民化、对殖民地的贸易、交换手段和一般商品的增加，使商业、航海业和工业空前高涨，因而使正在崩溃的封建社会内部的革命因素迅速发展
以前那种封建的或行会的工业经营方式已经不能满足随着新市场的出现而增加的需求了
工场手工业代替了这种经营方式
行会师傅被工业的中间等级排挤掉了；各种行业组织之间的分工随着各个作坊内部的分工的出现而消失了
但是，市场总是在扩大，需求总是在增加
甚至工场手工业也不再能满足需要了
于是，蒸汽和机器引起了工业生产的革命
现代大工业代替了工场手工业；工业中的百万富翁，一支一支产业大军的首领，现代资产者，代替了工业的中间等级
大工业建立了由美洲的发现所准备好的世界市场
世界市场使商业、航海业和陆路交通得到了巨大的发展
这种发展又反过来促进了工业的扩展
同时，随着工业、商业、航海业和铁路的扩展，资产阶级也在同一程度上得到发展，增加自己的资本，把中世纪遗留下来的一切阶级排挤到后面去
由此可见，现代资产阶级本身是一个长期发展过程的产物，是生产方式和交换方式的一系列变革的产物
资产阶级的这种发展的每一个阶段，都伴随着相应的政治上的进展
它在封建主统治下是被压迫的等级，在公社里是武装的和自治的团体，在一些地方组成独立的城市共和国，在另一些地方组成君主国中的纳税的第三等级；后来，在工场手工业时期，它是等级君主国或专制君主国中同贵族抗衡的势力，而且是大君主国的主要基础；最后，从大工业和世界市场建立的时候起，它在现代的代议制国家里夺得了独占的政治统治
现代的国家政权不过是管理整个资产阶级的共同事务的委员会罢了
资产阶级在历史上曾经起过非常革命的作用
资产阶级在它已经取得了统治的地方把一切封建的、宗法的和田园般的关系都破坏了
它无情地斩断了把人们束缚于天然尊长的形形色色的封建羁绊，它使人和人之间除了赤裸裸的利害关系，除了冷酷无情的“现金交易”，就再也没有任何别的联系了
它把宗教虔诚、骑士热忱、小市民伤感这些情感的神圣发作，淹没在利己主义打算的冰水之中
它把人的尊严变成了交换价值，用一种没有良心的贸易自由代替了无数特许的和自力挣得的自由
总而言之，它用公开的、无耻的、直接的、露骨的剥削代替了由宗教幻想和政治幻想掩盖着的剥削
资产阶级抹去了一切向来受人尊崇和令人敬畏的职业的神圣光环
它把医生、律师、教士、诗人和学者变成了它出钱招雇的雇佣劳动者
资产阶级撕下了罩在家庭关系上的温情脉脉的面纱，把这种关系变成了纯粹的金钱关系
资产阶级揭示了，在中世纪深受反动派称许的那种人力的野蛮使用，是以极端怠惰作为相应补充的
它第一个证明了，人的活动能够取得什么样的成就
它创造了完全不同于埃及金字塔、罗马水道和哥特式教堂的奇迹；它完成了完全不同于民族大迁徙和十字军征讨的远征
资产阶级除非对生产工具，从而对生产关系，从而对全部社会关系不断地进行革命，否则就不能生存下去
反之，原封不动地保持旧的生产方式，却是过去的一切工业阶级生存的首要条件
生产的不断变革，一切社会状况不停的动荡，永远的不安定和变动，这就是资产阶级时代不同于过去一切时代的地方
一切固定的僵化的关系以及与之相适应的素被尊崇的观念和见解都被消除了，一切新形成的关系等不到固定下来就陈旧了
一切等级的和固定的东西都烟消云散了，一切神圣的东西都被亵渎了
人们终于不得不用冷静的眼光来看他们的生活地位、他们的相互关系
不断扩大产品销路的需要，驱使资产阶级奔走于全球各地
它必须到处落户，到处开发，到处建立联系
资产阶级，由于开拓了世界市场，使一切国家的生产和消费都成为世界性的了
使反动派大为惋惜的是，资产阶级挖掉了工业脚下的民族基础
古老的民族工业被消灭了，并且每天都还在被消灭
它们被新的工业排挤掉了，新的工业的建立已经成为一切文明民族的生命攸关的问题；这些工业所加工的，已经不是本地的原料，而是来自极其遥远的地区的原料；它们的产品不仅供本国消费，而且同时供世界各地消费
旧的、靠本国产品来满足的需要，被新的、要靠极其遥远的国家和地带的产品来满足的需要所代替了
过去那种地方的和民族的自给自足和闭关自守状态，被各民族的各方面的互相往来和各方面的互相依赖所代替了
物质的生产是如此，精神的生产也是如此
各民族的精神产品成了公共的财产
民族的片面性和局限性日益成为不可能，于是由许多种民族的和地方的文学形成了一种世界的文学
资产阶级，由于一切生产工具的迅速改进，由于交通的极其便利，把一切民族甚至最野蛮的民族都卷到文明中来了
它的商品的低廉价格，是它用来摧毁一切万里长城、征服野蛮人最顽强的仇外心理的重炮
它迫使一切民族——如果它们不想灭亡的话——采用资产阶级的生产方式；它迫使它们在自己那里推行所谓的文明，即变成资产者
一句话，它按照自己的面貌为自己创造出一个世界
资产阶级使农村屈服于城市的统治
它创立了巨大的城市，使城市人口比农村人口大大增加起来，因而使很大一部分居民脱离了农村生活的愚昧状态
正像它使农村从属于城市一样，它使未开化和半开化的国家从属于文明的国家，使农民的民族从属于资产阶级的民族，使东方从属于西方
资产阶级日甚一日地消灭生产资料、财产和人口的分散状态
它使人口密集起来，使生产资料集中起来，使财产聚集在少数人的手里
由此必然产生的结果就是政治的集中
各自独立的、几乎只有同盟关系的、各有不同利益、不同法律、不同政府、不同关税的各个地区，现在已经结合为一个拥有统一的政府、统一的法律、统一的民族阶级利益和统一的关税的统一的民族
资产阶级在它的不到一百年的阶级统治中所创造的生产力，比过去一切世代创造的全部生产力还要多，还要大
自然力的征服，机器的采用，化学在工业和农业中的应用，轮船的行驶，铁路的通行，电报的使用，整个整个大陆的开垦，河川的通航，仿佛用法术从地下呼唤出来的大量人口，——过去哪一个世纪料想到在社会劳动里蕴藏有这样的生产力呢？由此可见，资产阶级赖以形成的生产资料和交换手段，是在封建社会里造成的
在这些生产资料和交换手段发展的一定阶段上，封建社会的生产和交换在其中进行的关系，封建的农业和工场手工业组织，一句话，封建的所有制关系，就不再适应已经发展的生产力了
这种关系已经在阻碍生产而不是促进生产了，它变成了束缚生产的桎梏
它必须被炸毁，它已经被炸毁了
起而代之的是自由竞争以及与自由竞争相适应的社会制度和政治制度、资产阶级的经济统治和政治统治
现在，我们眼前又进行着类似的运动
资产阶级的生产关系和交换关系，资产阶级的所有制关系，这个曾经仿佛用法术创造了如此庞大的生产资料和交换手段的现代资产阶级社会，现在像一个魔法师一样不能再支配自己用法术呼唤出来的魔鬼了
几十年来的工业和商业的历史，只不过是现代生产力反抗现代生产关系、反抗作为资产阶级及其统治的存在条件的所有制关系的历史
只要指出在周期性的重复中越来越危及整个资产阶级社会生存的商业危机就够了
在商业危机期间，总是不仅有很大一部分制成的产品被毁灭掉，而且有很大一部分已经造成的生产力被毁灭掉
在危机期间，发生一种在过去一切时代看来都好像是荒唐现象的社会瘟疫，即生产过剩的瘟疫
社会突然发现自己回到了一时的野蛮状态；仿佛是一次饥荒、一场普遍的毁灭性战争，使社会失去了全部生活资料；仿佛是工业和商业全被毁灭了，——这是什么缘故呢？因为社会上文明过度，生活资料太多，工业和商业太发达
社会所拥有的生产力已经不能再促进资产阶级文明和资产阶级所有制关系的发展；相反，生产力已经强大到这种关系所不能适应的地步，它已经受到这种关系的阻碍；而它一着手克服这种障碍，就使整个资产阶级社会陷入混乱，就使资产阶级所有制的存在受到威胁
资产阶级的关系已经太狭窄了，再容纳不了它本身所造成的财富了
——资产阶级用什么办法来克服这种危机呢？一方面不得不消灭大量生产力，另一方面夺取新的市场，更加彻底地利用旧的市场
这究竟是怎样的一种办法呢？这不过是资产阶级准备更全面更猛烈的危机的办法，不过是使防止危机的手段越来越少的办法
资产阶级用来推翻封建制度的武器，现在却对准资产阶级自己了
但是，资产阶级不仅锻造了置自身于死地的武器；它还产生了将要运用这种武器的人——现代的工人，即无产者
随着资产阶级即资本的发展，无产阶级即现代工人阶级也在同一程度上得到发展；现代的工人只有当他们找到工作的时候才能生存，而且只有当他们的劳动增殖资本的时候才能找到工作
这些不得不把自己零星出卖的工人，像其他任何货物一样，也是一种商品，所以他们同样地受到竞争的一切变化、市场的一切波动的影响
由于推广机器和分工，无产者的劳动已经失去了任何独立的性质，因而对工人也失去了任何吸引力
工人变成了机器的单纯的附属品，要求他做的只是极其简单、极其单调和极容易学会的操作
因此，花在工人身上的费用，几乎只限于维持工人生活和延续工人后代所必需的生活资料
但是，商品的价格，从而劳动的价格，是同它的生产费用相等的
因此，劳动越使人感到厌恶，工资也就越少
不仅如此，机器越推广，分工越细致，劳动量出就越增加，这或者是由于工作时间的延长，或者是由于在一定时间内所要求的劳动的增加，机器运转的加速，等等
现代工业已经把家长式的师傅的小作坊变成了工业资本家的大工厂
挤在工厂里的工人群众就像士兵一样被组织起来
他们是产业军的普通士兵，受着各级军士和军官的层层监视
他们不仅仅是资产阶级的、资产阶级国家的奴隶，他们每日每时都受机器、受监工、首先是受各个经营工厂的资产者本人的奴役
这种专制制度越是公开地把营利宣布为自己的最终目的，它就越是可鄙、可恨和可恶
手的操作所要求的技巧和气力越少，换句话说，现代工业越发达，男工也就越受到女工和童工的排挤
对工人阶级来说，性别和年龄的差别再没有什么社会意义了
他们都只是劳动工具，不过因为年龄和性别的不同而需要不同的费用罢了
当厂主对工人的剥削告一段落，工人领到了用现钱支付的工资的时候，马上就有资产阶级中的另一部分人——房东、小店主、当铺老板等等向他们扑来
以前的中间等级的下层，即小工业家、小商人和小食利者，手工业者和农民——所有这些阶级都降落到无产阶级的队伍里来了，有的是因为他们的小资本不足以经营大工业，经不起较大的资本家的竞争；有的是因为他们的手艺已经被新的生产方法弄得不值钱了
无产阶级就是这样从居民的所有阶级中得到补充的
无产阶级经历了各个不同的发展阶段
它反对资产阶级的斗争是和它的存在同时开始的
最初是单个的工人，然后是某一工厂的工人，然后是某一地方的某一劳动部门的工人，同直接剥削他们的单个资产者作斗争
他们不仅仅攻击资产阶级的生产关系，而且攻击生产工具本身；他们毁坏那些来竞争的外国商品，捣毁机器，烧毁工厂，力图恢复已经失去的中世纪工人的地位
在这个阶段上，工人是分散在全国各地并为竞争所分裂的群众
工人的大规模集结，还不是他们自己联合的结果，而是资产阶级联合的结果，当时资产阶级为了达到自己的政治目的必须而且暂时还能够把整个无产阶级发动起来
因此，在这个阶段上，无产者不是同自己的敌人作斗争，而是同自己的敌人的敌人作斗争，即同专制君主制的残余、地主、非工业资产者和小资产者作斗争
因此，整个历史运动都集中在资产阶级手里；在这种条件下取得的每一个胜利都是资产阶级的胜利
但是，随着工业的发展，无产阶级不仅人数增加了，而且它结合成更大的集体，它的力量日益增长，它越来越感觉到自己的力量
机器使劳动的差别越来越小，使工资几乎到处都降到同样低的水平，因而无产阶级内部的利益、生活状况也越来越趋于一致
资产者彼此间日益加剧的竞争以及由此引起的商业危机，使工人的工资越来越不稳定；
机器的日益迅速的和继续不断的改良，使工人的整个生活地位越来越没有保障；单个工人和单个资产者之间的冲突越来越具有两个阶级的冲突的性质
工人开始成立反对资产者的同盟；他们联合起来保卫自己的工资
他们甚至建立了经常性的团体，以便为可能发生的反抗准备食品
有些地方，斗争爆发为起义
工人有时也得到胜利，但这种胜利只是暂时的
他们斗争的真正成果并不是直接取得的成功，而是工人的越来越扩大的联合
这种联合由于大工业所造成的日益发达的交通工具而得到发展，这种交通工具把各地的工人彼此联系起来
只要有了这种联系，就能把许多性质相同的地方性的斗争汇合成全国性的斗争，汇合成阶级斗争
而一切阶级斗争都是政治斗争
中世纪的市民靠乡间小道需要几百年才能达到的联合，现代的无产者利用铁路只要几年就可以达到了
无产者组织成为阶级，从而组织成为政党这件事，不断地由于工人的自相竞争而受到破坏
但是，这种组织总是重新产生，并且一次比一次更强大，更坚固，更有力
它利用资产阶级内部的分裂，迫使他们用法律形式承认工人的个别利益
英国的十小时工作日法案就是一个例子
旧社会内部的所有冲突在许多方面都促进了无产阶级的发展
资产阶级处于不断的斗争中：
最初反对贵族；后来反对同工业进步有利害冲突的那部分资产阶级；经常反对一切外国的资产阶级
在这一切斗争中，资产阶级都不得不向无产阶级呼吁，要求无产阶级援助，这样就把无产阶级卷进了政治运动
于是，资产阶级自己就把自己的教育因素即反对自身的武器给予了无产阶级
其次，我们已经看到，工业的进步把统治阶级的整批成员抛到无产阶级队伍里去，或者至少也使他们的生活条件受到威胁
他们也给无产阶级带来了大量的教育因素
最后，在阶级斗争接近决战的时期，统治阶级内部的、整个旧社会内部的瓦解过程，就达到非常强烈、非常尖锐的程度，甚至使得统治阶级中的一小部分人脱离统治阶级而归附于革命的阶级，即掌握着未来的阶级
所以，正像过去贵族中有一部分人转到资产阶级方面一样，现在资产阶级中也有一部分人，特别是已经提高到从理论上认识整个历史运动这一水平的一部分资产阶级思想家，转到无产阶级方面来了
在当前同资产阶级对立的一切阶级中，只有无产阶级是真正革命的阶级
其余的阶级都随着大工业的发展而日趋没落和灭亡，无产阶级却是大工业本身的产物
中间等级，即小工业家、小商人、手工业者、农民，他们同资产阶级作斗争，都是为了维护他们这种中间等级的生存，以免于灭亡
所以，他们不是革命的，而是保守的
不仅如此，他们甚至是反动的，因为他们力图使历史的车轮倒转
如果说他们是革命的，那是鉴于他们行将转入无产阶级的队伍，这样，他们就不是维护他们目前的利益，而是维护他们将来的利益，他们就离开自己原来的立场，而站到无产阶级的立场上来
流氓无产阶级是旧社会最下层中消极的腐化的部分，他们在一些地方也被无产阶级革命卷到运动里来，但是，由于他们的整个生活状况，他们更甘心于被人收买，去干反动的勾当
在无产阶级的生活条件中，旧社会的生活条件已经被消灭了
无产者是没有财产的；他们和妻子儿女的关系同资产阶级的家庭关系再没有任何共同之处了；现代的工业劳动，现代的资本压迫，无论在英国或法国，无论在美国或德国，都是一样的，都使无产者失去了任何民族性
法律、道德、宗教在他们看来全都是资产阶级偏见，隐藏在这些偏见后面的全都是资产阶级利益
过去一切阶级在争得统治之后，总是使整个社会服从于它们发财致富的条件，企图以此来巩固它们已获得的生活地位
无产者只有废除自己的现存的占有方式，从而废除全部现存的占有方式，才能取得社会生产力
无产者没有什么自己的东西必须加以保护，他们必须摧毁至今保护和保障私有财产的一切
过去的一切运动都是少数人的或者为少数人谋利益的运动
无产阶级的运动是绝大多数人的、为绝大多数人谋利益的独立的运动
无产阶级，现今社会的最下层，如果不炸毁构成官方社会的整个上层，就不能抬起头来，挺起胸来
如果不就内容而就形式来说，无产阶级反对资产阶级的斗争首先是一国范围内的斗争
每一个国家的无产阶级当然首先应该打倒本国的资产阶级
在叙述无产阶级发展的最一般的阶段的时候，我们循序探讨了现存社会内部或多或少隐蔽着的国内战争，直到这个战争爆发为公开的革命，无产阶级用暴力推翻资产阶级而建立自己的统治
我们已经看到，至今的一切社会都是建立在压迫阶级和被压迫阶级的对立之上的
但是，为了有可能压迫一个阶级，就必须保证这个阶级至少有能够勉强维持它的奴隶般的生存的条件
农奴曾经在农奴制度下挣扎到公社成员的地位，小资产者曾经在封建专制制度的束缚下挣扎到资产者的地位
现代的工人却相反，他们并不是随着工业的进步而上升，而是越来越降到本阶级的生存条件以下
工人变成赤贫者，贫困比人口和财富增长得还要快
由此可以明显地看出，资产阶级再不能做社会的统治阶级了，再不能把自己阶级的生存条件当作支配一切的规律强加于社会了
资产阶级不能统治下去了，因为它甚至不能保证自己的奴隶维持奴隶的生活，因为它不得不让自己的奴隶落到不能养活它反而要它来养活的地步
社会再不能在它统治下生存下去了，就是说，它的生存不再同社会相容了
资产阶级生存和统治的根本条件，是财富在私人手里的积累，是资本的形成和增殖；资本的条件是雇佣劳动
雇佣劳动完全是建立在工人的自相竞争之上的
资产阶级无意中造成而又无力抵抗的工业进步，使工人通过结社而达到的革命联合代替了他们由于竞争而造成的分散状态
于是，随着大工业的发展，资产阶级赖以生产和占有产品的基础本身也就从它的脚下被挖掉了
它首先生产的是它自身的掘墓人
资产阶级的灭亡和无产阶级的胜利是同样不可避免的
"""

en_origin = """The history of all hitherto existing societies is the history of class struggles
Freeman and slave, patrician and plebeian, lord and serf, guild-master and journeyman, in a word, oppressor and oppressed, stood in constant opposition to one another, carried on an uninterrupted, now hidden, now open fight, a fight that each time ended, either in a revolutionary re-constitution of society at large, or in the common ruin of the contending classes
In the earlier epochs of history, we find almost everywhere a complicated arrangement of society into various orders, a manifold gradation of social rank
 In ancient Rome we have patricians, knights,plebeians, slaves; in the Middle Ages, feudal lords, vassals,guild-masters, journeymen, apprentices, serfs; in almost all of these classes, again, subordinate gradations
The modern bourgeois society that has sprouted from the ruins of feudal society has not done away with class antagonisms
 It has but established new classes, new conditions of oppression, new forms of struggle in place of the old ones
 Our epoch, the epoch of the bourgeoisie, possesses, however, this distinctive feature: it has simplified the class antagonisms
 Society as a whole is more and more splitting up into two great hostile camps, into two great classes,directly facing each other: Bourgeoisie and Proletariat
From the serfs of the Middle Ages sprang the chartered burghers of the earliest towns, from these burgesses the first elements of the bourgeoisie were developed
The discovery of America, the rounding of the Cape, opened up fresh ground for the rising bourgeoisie
 The East-Indian and Chinese markets,the colonisation of America, trade with the colonies, the increase in the means of exchange and in commodities generally, gave to commerce,to navigation, to industry, an impulse never before known, and thereby,to the revolutionary element in the tottering feudal society, a rapid development
The feudal system of industry, under which industrial production was monopolised by closed guilds, now no longer sufficed for the growing wants of the new markets
 The manufacturing system took its place
 The guild-masters were pushed on one side by the manufacturing middle class; division of labour between the different corporate guilds vanished in the face of division of labour in each single workshop
Meantime the markets kept ever growing, the demand ever rising
 Even manufacture no longer sufficed
 Thereupon, steam and machinery revolutionised industrial production
 The place of manufacture was taken by the giant, Modern Industry, the place of the industrial middle class, by industrial millionaires, the leaders of whole industrial armies, the modern bourgeois
Modern industry has established the world-market, for which the discovery of America paved the way
 This market has given an immense development to commerce, to navigation, to communication by land
 This development has, in its time, reacted on the extension of industry;
 andin proportion as industry, commerce, navigation, railways extended, in the same proportion the bourgeoisie developed, increased its capital,and pushed into the background every class handed down from the MiddleAges
We see, therefore, how the modern bourgeoisie is itself the product ofa long course of development, of a series of revolutions in the modes of production and of exchange
Each step in the development of the bourgeoisie was accompanied by a corresponding political advance of that class
 An oppressed class under the sway of the feudal nobility, an armed and self-governing association in the media eval commune; here independent urban republic(as in Italy and Germany), there taxable “third estate” of the monarchy(as in France), afterwards, in the period of manufacture proper,serving either the semi-feudal or the absolute monarchy as a counterpoise against the nobility, and, in fact, corner-stone of the great monarchies in general, the bourgeoisie has at last, since the establishment of Modern Industry and of the world-market, conquered for itself, in the modern representative State, exclusive political sway
The executive of the modern State is but a committee for managing the common affairs of the whole bourgeoisie
The bourgeoisie, historically, has played a most revolutionary part
The bourgeoisie, wherever it has got the upper hand, has put an end to all feudal, patriarchal, idyllic relations
 It has pitilessly torn as under the motley feudal ties that bound man to his “natural superiors,” and has left remaining no other nexus between man and manthan naked self-interest, than callous “cash payment
” It has drowned the most heavenly ecstasies of religious fervour, of chivalrous enthusiasm, of philistine sentimentalism, in the icy water of egotistical calculation
 It has resolved personal worth into exchange value, and in place of the numberless and indefeasible chartered freedoms, has set up that single, unconscionable freedom—Free Trade
 In one word, for exploitation, veiled by religious and political illusions, naked, shameless, direct, brutal exploitation
The bourgeoisie has stripped of its halo every occupation hither to honoured and looked up to with reverent awe
 It has converted the physician, the lawyer, the priest, the poet, the man of science, in to its paid wage labourers
The bourgeoisie has torn away from the family its sentimental veil, and has reduced the family relation to a mere money relation
The bourgeoisie has disclosed how it came to pass that the brutal display of vigour in the Middle Ages, which Reactionists so much admire, found its fitting complement in the most slothful indolence
 It has been the first to show what man’s activity can bring about
 It has accomplished wonders far surpassing Egyptian pyramids, Roman aqueducts,and Gothic cathedrals; it has conducted expeditions that put in the shade all former Exoduses of nations and crusades
The bourgeoisie cannot exist without constantly revolutionising the instruments of production, and thereby the relations of production, and with them the whole relations of society
 Conservation of the old modes of production in unaltered form, was, on the contrary, the first condition of existence for all earlier industrial classes
 Constant revolutionising of production, uninterrupted disturbance of all social conditions, everlasting uncertainty and agitation distinguish the bourgeois epoch from all earlier ones
 All fixed, fast-frozen relations, with their train of ancient and venerable prejudices and opinions, are swept away, all new-formed ones become antiquated before they can ossify
 All that is solid melts into air, all that is holy is profaned,
 and man is at last compelled to face with sober senses, his real conditions of life, and his relations with his kind
The need of a constantly expanding market for its products chases the bourgeoisie over the whole surface of the globe
 It must nestlee verywhere, settle everywhere, establish connexions everywhere
The bourgeoisie has through its exploitation of the world-market given a cosmopolitan character to production and consumption in every country
 To the great chagrin of Reactionists, it has drawn from under the feet of industry the national ground on which it stood
 All old-established national industries have been destroyed or are daily being destroyed
 They are dislodged by new industries, whose introduction becomes a life and death question for all civilised nations, by industries that no longer work up indigenous raw material,but raw material drawn from the remotest zones; industries whose products are consumed, not only at home, but in every quarter of the globe
 In place of the old wants, satisfied by the productions of the country, we find new wants, requiring for their satisfaction the products of distant lands and climes
 In place of the old local and national seclusion and self-sufficiency, we have intercourse in every direction, universal inter-dependence of nations
 And as in material,so also in intellectual production
 The intellectual creations of individual nations become common property
 National one-sidedness and narrow-mindedness become more and more impossible, and from the numerous national and local literatures, there arises a world literature
The bourgeoisie, by the rapid improvement of all instruments of production, by the immensely facilitated means of communication, draws all, even the most barbarian, nations into civilisation
 The cheap prices of its commodities are the heavy artillery with which it batters down all Chinese walls, with which it forces the barbarians’ intensely obstinate hatred of foreigners to capitulate
 It compels all nations,on pain of extinction, to adopt the bourgeois mode of production; it compels them to introduce what it calls civilisation into their midst,_ie_, to become bourgeois themselves
 In one word, it creates a world after its own image
The bourgeoisie has subjected the country to the rule of the towns
 It has created enormous cities, has greatly increased the urban population as compared with the rural, and has thus rescued a considerable part of the population from the idiocy of rural life
 Just as it has made the country dependent on the towns, so it has made barbarian and semi-barbarian countries dependent on the civilised ones, nations of peasants on nations of bourgeois, the East on the West
The bourgeoisie keeps more and more doing away with the scattered state of the population, of the means of production, and of property
 It has agglomerated production, and has concentrated property in a few hands
The necessary consequence of this was political centralisation
Independent, or but loosely connected provinces, with separate interests, laws, governments and systems of taxation, became lumped together into one nation, with one government, one code of laws, one national class-interest, one frontier and one customs-tariff
 The bourgeoisie, during its rule of scarce one hundred years, has created more massive and more colossal productive forces than have all preceding generations together
 Subjection of Nature’s forces to man,machinery, application of chemistry to industry and agriculture,steam-navigation, railways, electric telegraphs, clearing of who le continents for cultivation, canalisation of rivers, whole populations conjured out of the ground—what earlier century had even a presentiment that such productive forces slumbered in the lap of social labour?We see then: the means of production and of exchange, on whose foundation the bourgeoisie built itself up, were generated in feudal society
 At a certain stage in the development of these means of production and of exchange, the conditions under which feudal society produced and exchanged, the feudal organisation of agriculture and manufacturing industry, in one word, the feudal relations of property became no longer compatible with the already developed productive forces;
 they became so many fetters
 They had to be burst asunder; they were burst asunder
Into their place stepped free competition, accompanied by a social and political constitution adapted to it, and by the economical and political sway of the bourgeois class
A similar movement is going on before our own eyes
 Modern bourgeois society with its relations of production, of exchange and of property,a society that has conjured up such gigantic means of production and of exchange, is like the sorcerer, who is no longer able to control the powers of the nether world whom he has called up by his spells
 For many a decade past the history of industry and commerce is but the history of the revolt of modern productive forces against modern conditions of production, against the property relations that are the conditions for the existence of the bourgeoisie and of its rule
 It is enough to mention the commercial crises that by their periodical return put on its trial, each time more threateningly, the existence of the entire bourgeois society
 In these crises a great part not only of the existing products, but also of the previously created productive forces, are periodically destroyed
 In these crises there breaks out an epidemic that, in all earlier epochs, would have seemed an absurdity—the epidemic of over-production
 Society suddenly finds itself put back into a state of momentary barbarism; it appears as if a famine, a universal war of devastation had cut off the supply of every means of subsistence; industry and commerce seem to be destroyed; and why? Because there is too much civilisation, too much means of subsistence, too much industry, too much commerce
 The productive forces at the disposal of society no longer tend to further the development of the conditions of bourgeois property; on the contrary,they have become too powerful for these conditions, by which they are fettered, and so soon as they overcome these fetters, they bring disorder into the whole of bourgeois society, endanger the existence of bourgeois property
 The conditions of bourgeois society are too narrow to comprise the wealth created by them
 And how does the bourgeoisie get over these crises? On the one hand in forced destruction of a mass of productive forces; on the other, by the conquest of new markets, and by the more thorough exploitation of the old ones
 That is to say, by paving the way for more extensive and more destructive crises, and by diminishing the means whereby crises are prevented
The weapons with which the bourgeoisie felled feudalism to the ground are now turned against the bourgeoisie itself
But not only has the bourgeoisie forged the weapons that bring death to it self; it has also called into existence the men who are to wield those weapons—the modern working class—the proletarians
In proportion as the bourgeoisie, _ie_, capital, is developed, in the same proportion is the proletariat, the modern working class,developed—a class of labourers, who live only so long as they find work, and who find work only so long as their labour increases capital
These labourers, who must sell themselves piece-meal, are a commodity,like every other article of commerce, and are consequently exposed to all the vicissitudes of competition, to all the fluctuations of the market
Owing to the extensive use of machinery and to division of labour, the work of the proletarians has lost all individual character, and consequently, all charm for the workman
 He becomes an appendage of the machine, and it is only the most simple, most monotonous, and most easily acquired knack, that is required of him
 Hence, the cost of production of a workman is restricted, almost entirely, to the means of subsistence that he requires for his maintenance, and for the propagation of his race
 But the price of a commodity, and therefore also of labour, is equal to its cost of production
 In proportion therefore, as the repulsiveness of the work increases, the wage decreases
 Nay more, in proportion as the use of machinery and division of labour increases, in the same proportion the burden of toil also increases, whether by prolongation of the working hours, by increase of the work exacted in a given time or by increased speed of the machinery, etc
Modern industry has converted the little workshop of the patriarchal master into the great factory of the industrial capitalist
 Masses of labourers, crowded into the factory, are organised like soldiers
 As privates of the industrial army they are placed under the command of a perfect hierarchy of officers and sergeants
 Not only are they slaves of the bourgeois class, and of the bourgeois State; they are daily and hourly enslaved by the machine, by the over-looker, and, above all, by the individual bourgeois manufacturer himself
 The more openly this despotism proclaims gain to be its end and aim, the more petty, the more hateful and the more embittering it is
The less the skill and exertion of strength implied in manual labour,in other words, the more modern industry becomes developed, the more is the labour of men superseded by that of women
 Differences of age and sex have no longer any distinctive social validity for the working class
 All are instruments of labour, more or less expensive to use,according to their age and sex
No sooner is the exploitation of the labourer by the manufacturer, sofar at an end, that he receives his wages in cash, than he is set upon by the other portions of the bourgeoisie, the landlord, the shopkeeper,the pawnbroker, etc
The lower strata of the middle class—the small tradespeople,shopkeepers, retired tradesmen generally, the handicraftsmen and peasants—all these sink gradually into the proletariat, partly because their diminutive capital does not suffice for the scale on which ModernIndustry is carried on, and is swamped in the competition with the large capitalists, partly because their specialized skill is rendered worthless by the new methods of production
 Thus the proletariat is recruited from all classes of the population
The proletariat goes through various stages of development
 With its birth begins its struggle with the bourgeoisie
 At first the contest is carried on by individual labourers, then by the workpeople of a factory, then by the operatives of one trade, in one locality, against the individual bourgeois who directly exploits them
 They direct their attacks not against the bourgeois conditions of production, but against the instruments of production themselves; they destroy imported wares that compete with their labour, they smash to pieces machinery, they set factories ablaze, they seek to restore by force the vanished statusof the workman of the Middle Ages
At this stage the labourers still form an incoherent mass scattered over the whole country, and broken up by their mutual competition
 If anywhere they unite to form more compact bodies, this is not yet the consequence of their own active union, but of the union of the bourgeoisie, which class, in order to attain its own political ends, is compelled to set the whole proletariat in motion, and is moreover yet,for a time, able to do so
 At this stage, therefore, the proletarians do not fight their enemies, but the enemies of their enemies, the remnants of absolute monarchy, the landowners, the non-industrial bourgeois, the petty bourgeoisie
 Thus the whole historical movement is concentrated in the hands of the bourgeoisie; every victory so obtained is a victory for the bourgeoisie
But with the development of industry the proletariat not only increases in number; it becomes concentrated in greater masses, its strength grows, and it feels that strength more
 The various interests and conditions of life within the ranks of the proletariat are more and more equalised, in proportion as machinery obliterates all distinctions of labour, and nearly everywhere reduces wages to the same low level
The growing competition among the bourgeois, and the resulting commercial crises, make the wages of the workers ever more fluctuating
The unceasing improvement of machinery, ever more rapidly developing,makes their livelihood more and more precarious; the collisions between individual workmen and individual bourgeois take more and more the character of collisions between two classes
 Thereupon the workers begin to form combinations (Trades Unions) against the bourgeois; they club together in order to keep up the rate of wages;
 they found permanent associations in order to make provision beforehand for these occasional revolts
 Here and there the contest breaks out into riots
Now and then the workers are victorious, but only for a time
 The real fruit of their battles lies, not in the immediate result, but in the ever-expanding union of the workers
 This union is helped on by the improved means of communication that are created by modern industry and that place the workers of different localities in contact with one another
 It was just this contact that was needed to centralise the numerous local struggles, all of the same character, into one national struggle between classes
 But every class struggle is a political struggle
 And that union, to attain which the burghers of the MiddleAges, with their miserable highways, required centuries, the modern proletarians, thanks to railways, achieve in a few years
This organisation of the proletarians into a class, and consequently into a political party, is continually being upset again by the competition between the workers themselves
 But it ever rises up again,stronger, firmer, mightier
 It compels legislative recognition of particular interests of the workers, by taking advantage of the divisions among the bourgeoisie itself
 Thus the ten-hours’ bill inEngland was carried
Altogether collisions between the classes of the old society further,in many ways, the course of development of the proletariat
 The bourgeoisie finds itself involved in a constant battle
 At first with the aristocracy; later on, with those portions of the bourgeoisie itself, whose interests have become antagonistic to the progress of industry; at all times, with the bourgeoisie of foreign countries
 In all these battles it sees itself compelled to appeal to the proletariat, to ask for its help, and thus, to drag it into the political arena
 The bourgeoisie itself, therefore, supplies the proletariat with its own instruments of political and general education, in other words, it furnishes the proletariat with weapons for fighting the bourgeoisie
Further, as we have already seen, entire sections of the ruling classes are, by the advance of industry, precipitated into the proletariat, or are at least threatened in their conditions of existence
 These also supply the proletariat with fresh elements of enlightenment and progress
Finally, in times when the class struggle nears the decisive hour, the process of dissolution going on within the ruling class, in fact within the whole range of society, assumes such a violent, glaring character,that a small section of the ruling class cuts itself adrift, and joins the revolutionary class, the class that holds the future in its hands
Just as, therefore, at an earlier period, a section of the nobility went over to the bourgeoisie, so now a portion of the bourgeoisie goes over to the proletariat, and in particular, a portion of the bourgeois ideologists, who have raised themselves to the level of comprehending theoretically the historical movement as a whole
Of all the classes that stand face to face with the bourgeoisie today,the proletariat alone is a really revolutionary class
 The other classes decay and finally disappear in the face of Modern Industry; the proletariat is its special and essential product
 The lower middle class, the small manufacturer, the shopkeeper, the artisan, the peasant, all these fight against the bourgeoisie, to save from extinction their existence as fractions of the middle class
 They are therefore not revolutionary, but conservative
 Nay more, they are reactionary, for they try to roll back the wheel of history
 If by chance they are revolutionary, they are so only in view of their impending transfer into the proletariat, they thus defend not their present, but their future interests, they desert their own stand point to place themselves at that of the proletariat
The “dangerous class,” the social scum, that passively rotting mass thrown off by the lowest layers of old society, may, here and there, be swept into the movement by a proletarian revolution; its conditions of life, however, prepare it far more for the part of a bribed tool of reactionary intrigue
In the conditions of the proletariat, those of old society at large are already virtually swamped
 The proletarian is without property; his relation to his wife and children has no longer anything in common with the bourgeois family-relations; modern industrial labour, modern subjection to capital, the same in England as in France, in America asin Germany, has stripped him of every trace of national character
 Law,morality, religion, are to him so many bourgeois prejudices, behind which lurk in ambush just as many bourgeois interests
All the preceding classes that got the upper hand, sought to fortify their already acquired status by subjecting society at large to their conditions of appropriation
 The proletarians cannot become masters of the productive forces of society, except by abolishing their own previous mode of appropriation, and thereby also every other previous mode of appropriation
 They have nothing of their own to secure and to fortify; their mission is to destroy all previous securities for, and insurances of, individual property
All previous historical movements were movements of minorities, or in the interests of minorities
 The proletarian movement is the self-conscious, independent movement of the immense majority, in the interests of the immense majority
 The proletariat, the lowest stratum of our present society, cannot stir, cannot raise itself up, without the whole super incumbent strata of official society being sprung into the air
Though not in substance, yet in form, the struggle of the proletariat with the bourgeoisie is at first a national struggle
 The proletariat of each country must, of course, first of all settle matters with its own bourgeoisie
In depicting the most general phases of the development of the proletariat, we traced the more or less veiled civil war, raging within existing society, up to the point where that war breaks out into open revolution, and where the violent overthrow of the bourgeoisie lays the foundation for the sway of the proletariat
Hitherto, every form of society has been based, as we have already seen, on the antagonism of oppressing and oppressed classes
 But inorder to oppress a class, certain conditions must be assured to it under which it can, at least, continue its slavish existence
 The serf,in the period of serfdom, raised himself to membership in the commune,just as the petty bourgeois, under the yoke of feudal absolutism,managed to develop into a bourgeois
 The modern laborer, on the contrary, instead of rising with the progress of industry, sinks deeper and deeper below the conditions of existence of his own class
 He becomes a pauper, and pauperism develops more rapidly than population and wealth
 And here it becomes evident, that the bourgeoisie is unfit any longer to be the ruling class in society, and to impose its conditions of existence upon society as an over-riding law
 It is un fit to rule because it is incompetent to assure an existence to its slave within his slavery, because it cannot help letting him sink into such astate, that it has to feed him, instead of being fed by him
 Society can no longer live under this bourgeoisie, in other words, its existence is no longer compatible with society
The essential condition for the existence, and for the sway of the bourgeois class, is the formation and augmentation of capital; the condition for capital is wage-labour
 Wage-labour rests exclusively on competition between the laborers
 The advance of industry, whose involuntary promoter is the bourgeoisie, replaces the isolation of the labourers, due to competition, by their revolutionary combination, due to association
 The development of Modern Industry, therefore, cuts from under its feet the very foundation on which the bourgeoisie produces and appropriates products
 What the bourgeoisie, therefore,produces, above all, is its own grave-diggers
 Its fall and the victor yof the proletariat are equally inevitable
"""


en_origin = """Have Foucault and Blanchot ever met? For Foucault, the answer is no. For Blanchot, the answer is yes. Foucault and Blanchot met on the campus of the Sorbonne during the May storm of 1968. On those stormy days, discussions between strangers were not abrupt. Blanchot recognized the already famous Foucault and spoke to him a few words. However, Foucault did not know that the person speaking to him was his idol Blanchot. Despite his stellar reputation, Blanchot hardly made a public appearance after World War II. He was present only by means of writing. Apart from his writings, nothing is known about him. It was only during the May storm that he appeared in public for the only time in an anonymous capacity. Of course Foucault would not recognize him. Blanchot does not give interviews to reporters, does not reveal his photos, does not participate in academic conferences, and rarely even meets his friends (including his best friend Levinas). The way he communicates with friends is to write continuously letter. He lived a life of seclusion and isolation, and as he has repeatedly expressed in his books, he endowed silence, loneliness and distance with a unique value. Instead of talking to people face to face, Blanchot takes the Nietzschean way, talking passionately to himself, a loner talking to his shadow. He often asks and answers himself in the book, having "infinite conversations" with himself. Until his death in 2003, it was unclear whether the man known as France's most famous disappearance of the twentieth century was still alive.

In the sixties, Foucault read a great deal of Blanchot. Blanchot became one of Foucault's most obsessive authors. Foucault has repeatedly and unabashedly expressed his homage to Blanchot on various occasions. He once told his friends that when he was young, he dreamed of being Blanchot. He quoted Blanchot a lot in the text. Following Blanchot's style, the self-questioning and self-answering method he adopted in the back of "The Archeology of Knowledge" is an imitation and tribute to Blanchot. Blanchot, Bataille and Krosovsky, the three philosophers and writers at the same time, were also the three authors that Foucault was obsessed with in the 1950s and 1960s. It was they who decisively led Foucault to Nietzsche. "For me, Nietzsche, Bataille, Blanchot, Krosovsky are escapes from philosophy. Bataille's rage, Blanchot's tantalizing and annoying sweetness, Krosovsky's Spirals, these are all starting from philosophy, bringing philosophy into play and questioning, out of philosophy, and back into philosophy." They both break down the line between philosophy and non-philosophy - which is also Foucault's style . However, he did not associate with them. He only met Krosovsky on the recommendation of Roland Barthes and suggested a solid friendship. While Bataille died prematurely in 1962, Blanchot, a recluse, was never seen. For Foucault, too, he was willing to maintain the mystical cult of Blanchot. Perhaps, keeping a distance is the inner tacit understanding between them. Once, a friend invited Foucault to dinner with Blanchot, but Foucault politely declined: to know him and understand him only by reading his articles. The two deliberately did not meet. But, in Blanchot's words, they "both miss each other".

Foucault discovered Blanchot through Sartre's article, but he soon sided with Blanchot against Sartre. If we say that Sartre was the sun of French thought in the 1960s, the hidden Blanchot was the dark night of thought. But how did the mysterious Blanchot discover Foucault? After being recommended by a publishing friend, Blanchot saw the manuscript of Foucault's unpublished doctoral dissertation "History of Madness in the Classical Age" and greatly admired this unknown young man. After the book was published, Blanchot was the first to write an ebullient review of the book. After Foucault's death in 1984, Blanchot wrote Michel Foucault as I imagined it, a comprehensive assessment of all of Foucault's important writings, his entire academic career--which he apparently continued Read and follow Foucault. Why the imaginary Michel Foucault? Just because they never met. It was a distanced friendship that never met. What is friendship at distance? Blanchot explained it this way in his book Friendship:

We must greet them in a relationship of strangers, and they greet us in that relationship, and we are like strangers to each other. Friendship, a relationship without dependencies, without a storyline, into which the simplicity of all life enters, a friendship that does so through an acknowledgment of the common unknown, so that it does not allow us to talk about our friends, we can only communicate with They talk to each other, we can't use them as the topic of our conversation (article), even in the understanding activities, they always maintain an infinite distance to us, even if the relationship is better, this distance is a fundamental separation , on this basis, the separation becomes a connection. This separation is not a refusal to talk to the confidant (how tacky it is, if only to think about it), but the distance that exists between me and the man called a friend, a pure distance that measures the distance between us relationship, this isolation keeps me from ever having the power to use him, or to use my knowledge of him (even to praise him), however, this does not prevent communication, but in this difference , and sometimes in the silence of language we came together.

This is Blanchot's unique view of friendship. Since Aristotle, friendship has always been associated with sharing and coexistence. Friendship is about living together (Roland Barthes once devoted his one-year course at the Collège de France to this question: How to live together?). If there is no contact for a long time, the friendship will gradually die out. It is in sharing that friendship is endured and maintained: sharing good times together, enjoying each other's happiness and gospel together, and it is in this sharing that friendship is deepened. And Montaigne wasn't content to share the concept. For him, true friendship is not just sharing and mutual understanding, but a complete exchange of two souls. A true friend is exactly the same deep down, and there is no difference between the two souls combined. At this moment, there is no so-called gratitude, obligation and responsibility among friends. Because a good friend is like a person, a person is just an image of another person, and they achieve a complete overlap between them, that is, there is no distance at all. Montaigne said: "The friendship I want to talk about here is the superposition of two hearts. I have you, you have me, and they become one, and the bond that connects the two has disappeared and can no longer be identified. ." Therefore, "All that is between them, including will, thought, opinion, property, wife, children, honor, and life, is in common. They act in unison, and according to Aristotle's definition, they are one The soul occupies two bodies, so nothing can be given or received between them."

We see that Blanchot is a rejection of this long and deeply ingrained notion of friendship, who reverses the direction of the friendship discussion: that friendship is not infinitely close. On the contrary, friendship means not seeing each other, maintaining distance, deliberately maintaining distance and differences, and keeping silent among friends. Perhaps it is precisely because of this difference and silence that friendship is purer, and the friendship bond between friends does not become a bond, or, in other words, there is no bond between friends, and "separation becomes a connection".

And Foucault also has a special feeling for the relationship between silence and friendship. In an interview, he said:

Some silences carry intense hostility, while others imply deep friendship, reverence, and even love. I fondly remember when producer Daniel Schmidt visited me and we had only been talking for a few minutes before somehow suddenly there was nothing to say to each other. Next we stayed from three o'clock in the afternoon until midnight. We drank, smoked heavily, and had a hearty dinner. In a full ten hours, we did not speak for more than twenty minutes. From then on, a long friendship began between us. This is the first time I have had friendship with someone in silence.

Perhaps this is what happened between Blanchot and Foucault: not seeing each other, keeping a pure distance, without any pollution of the world, leaving the friend in a state of absolute freedom. At the same time, pay attention to each other, comment on each other, and communicate with each other in the way of writing and reading. There is no "personal friendship" in this kind of friendship. This is what Blanchot calls an "intellectual friendship." However, this kind of friendship is never spoken out easily. This kind of friendship needs to be maintained in a silent way. The words and declarations of this kind of friendship are not an affirmation of it, but a depletion of it. A friend can be claimed only when the friend is gone forever, only when the friend never hears the name friend. It was also when Foucault could never listen that Blanchot began to declare this friendship openly: yes, Foucault was his friend. "Friendship is a gift that is promised to Foucault behind you. It goes beyond strong emotions, beyond contemplation, beyond life-threatening... I firmly believe that no matter how embarrassing the situation may be, I remain faithful to this An intellectual friendship. Foucault's death grieves me, but it allows me to declare this friendship to him today."

Although Foucault can no longer declare this friendship to Blanchot—two friends, one has to go first, one cannot declare friendship openly to the other—but we can still imagine Foucault agreeing Blanchot's approach. For, after the death of Roland Barthes, what Foucault expressed about friendship in his memorial speech bears a striking resemblance to what Blanchot said. It was also after Barthes's death that Foucault declared this friendship. Foucault said that Roland Barthes "has gained social recognition for more than two decades of unremitting efforts, and has produced important research results of originality, which have spared me from my friendship with him... Allow me to disclose this this afternoon." The only friendship. This friendship is at least reticently similar to the death it hates." Likewise, friendship can only be revealed after death; friendship happens only in silence; friendship is not any pragmatic tool. Isn't that what Blanchot said to the late Foucault?

Blanchot ends his commemorative essay with a quote from Aristotle: "Friend, there is no friend in the world." Often, this is a curious oxymoron: how can one be called a friend? , how can you face a friend, but at the same time tell him that there are no friends in the world? But, in Blanchot, there is absolutely no paradox in this sentence: yes, Foucault is no longer a friend. So, now, I can call him my friend. This is a "no personal" friend, a silent friend, a pure "intellectual friendship"."""

cn_origin = """福柯和布朗肖见过一次吗？对于福柯来说，答案是否定的。对于布朗肖来说，答案则是肯定的。1968年五月风暴期间，福柯和布朗肖在索邦大学的校园内相遇了。在那个风起云涌的日子里，陌生人之间的讨论并不突兀。布朗肖认出了已经大名鼎鼎的福柯，并和他讲过几句话。但是，福柯并不知道同他讲话的这个人就是他的偶像布朗肖。尽管布朗肖名声显赫，但二战以后几乎从未抛头露面。他只通过写作的方式在场。除了他的著作，人们对他一无所知。只是在五月风暴期间，他才唯一一次以匿名者的身份出现在公开场合。福柯当然不会认出他来。布朗肖不接受记者采访，不暴露自己的照片，也不参加学术会议，甚至也极少同自己的朋友（包括最好的朋友列维纳斯）见面，他和朋友的交往方式就是不间断地写信。他过着隐居而隔绝的生活，就像他一再在他的书中所表达的那样，他赋予了沉默、孤独和距离以独特的价值。不和人面对面说话，布朗肖就采取尼采的方式，自己和自己热烈地谈话，一个孤独者和他的影子在说话。他常常在书中自问自答，自己和自己进行“无限的交谈”。到2003年他去世之前，人们并不清楚，这个被称为法国二十世纪最著名的失踪者，到底是否还在人世。

在六十年代，福柯读过布朗肖的大量著作。布朗肖成为福柯最迷恋的作者之一。福柯在各种不同的场合多次毫不掩饰地表达对布朗肖的敬意。他曾对他的朋友说，他年轻的时候，梦想成为布朗肖。他在文中大量引用布朗肖的话，仿照布朗肖的风格，他在《知识考古学》后面所采用的自问自答的方式就是对布朗肖的模仿和致敬。布朗肖、巴塔耶和克罗索夫斯基，这三个人同时是哲学家和作家，他们也是福柯五六十年代迷恋的三个作者。正是他们决定性地把福柯引向了尼采。“对我来说，尼采、巴塔耶、布朗肖、克罗索夫斯基是逃离哲学的途径。巴塔耶的狂暴，布朗肖既诱人又恼人的甜蜜，克罗索夫斯基的螺旋，这些都是从哲学出发，把哲学带入游戏和疑问，从哲学中出来，再回到哲学中去。”他们都打破了哲学和非哲学的界线——这也正是福柯的风格。不过，他和他们并不来往。他只是在罗兰·巴特的引荐下同克罗索夫斯基见面并建议了牢靠的友谊。而巴塔耶1962年就过早地去世，隐居者布朗肖则从不见人。对福柯来说，他也愿意保持着对布朗肖的神秘崇拜。或许，保持距离，正是他们之间的内在默契。有一次，一个朋友邀请福柯同布朗肖共进晚餐，被福柯婉言谢绝了：只通过读他的文章来认识他和理解他。两人刻意地不见面。但是，用布朗肖的说法，他们“都惦念着对方”。

福柯是通过萨特的文章发现布朗肖的，但是，他很快就站在布朗肖的一边来反对萨特。如果说，萨特是六十年代法国思想界的太阳，而隐匿的布朗肖则是思想界的暗夜。但神秘的布朗肖是如何发现福柯的？经过一个出版界朋友的推荐，布朗肖看到了福柯尚未出版的博士论文《古典时代疯狂史》的手稿，就对这个默默无闻的年轻人大为赞赏。在本书出版后，布朗肖最早为这本书写了热情洋溢的评论文章。福柯1984年去世之后，布朗肖写了《我想象中的米歇尔·福柯》，对福柯的所有重要著作，对他的整个学术生涯作了全面的评价——显然，他在持续地阅读和关注福柯。为什么是想象中的米歇尔·福柯？就是因为从未谋面。这是一种从未见面的保持距离的友谊。何谓保持距离的友谊？布朗肖在他出版的《友谊》一书中作了这样的解释：

我们必须以一种陌生人的关系迎接他们，他们也以这种关系迎接我们，我们之间相互形同路人。友谊，这种没有依靠、没有故事情节的关系，然而所有生命的朴实都进入其中，这种友谊以通过对共同未知的承认的方式进行，因此它不允许我们谈论我们的朋友，我们只能与他们对话，不能把他们作为我们谈话（文章）的话题，即使在理解活动之中，他们对我们言说也始终维持一种无限的距离，哪怕关系再为要好，这种距离是一种根本的分离，在这个基础上，那分离遂成为一种联系。这种分离不是拒绝交谈知心话语（这是多么俗气，哪怕只是想想），而就是存在于我和那个称为朋友的人之间的这种距离，一种纯净的距离，衡量着我们之间的关系，这种阻隔让我永远不会有权力去利用他，或者是利用我对他的认识（即便是去赞扬他），然而，这并不会阻止交流，而是在这种差异之中，有时是在语言的沉默中我们走到了一起。

这是布朗肖独特的友谊观。自亚里士多德以来，友谊总是同分享和共存联系起来。友谊就是要共同生活（罗兰·巴特曾经在法兰西学院的一年课程中专门讨论过这个问题：如何共同生活？）。如果长时间不来往，友谊就渐趋熄灭。友谊正是在共享中得以持久和维护：共同享受美好的时光，共同享受彼此之间的快乐和福音，正是在这种分享中，友谊得以深化。而蒙田还不满足于共享这个概念。对他来说，真正的友谊不仅是分享和相互理解，而是两个人灵魂的完全交流，真正的朋友其内心深处是一模一样的，两个灵魂复合在一起毫无差异。此刻，朋友之间不存在所谓的感激、义务和责任。因为好的朋友就如同一个人，一个人不过是另外一个人的影像，他们之间达成了彻底的重叠，也就是说，完全没有距离。蒙田说：“我这里要说的友谊，则是两颗心灵叠合，我中有你，你中有我，浑然成为一体，令二者联结起来的纽带已消隐其中，再也无从辨认。”因此，“他们间所有的一切，包括意志、思想、观点、财产、妻子、儿女、荣誉和生命，都是共同拥有的。他们行动一致，依据亚里士多德的定义，他们是一个灵魂占据两个躯体，所以他们之间不能给予或得到任何东西。”

我们看到，布朗肖是对这种漫长而根深蒂固的友谊观念的一个拒绝，他扭转了友谊讨论的方向：友谊不是无限地接近。相反，友谊就是不见面，就是保持距离，就是对距离和差异的刻意维护，就是朋友之间的沉默以对。或许，正是因为有这种差异和沉默，友谊才会更加纯净，朋友之间的友谊纽带不会成为羁绊，或者说，朋友之间不存在纽带，“分离遂成为一种联系”。

而福柯对沉默和友谊的关系也有一种特殊的感受，在一次访谈中，他说：

某些沉默带有强烈的敌意，另一些沉默却意味着深切的友谊、崇敬，甚至爱情。我深深地记得制片人丹尼尔·施密特造访我时的情景，我们才聊了几分钟，就不知怎地突然发现彼此间没有什么可说的了。接下来我们从下午三点钟一直待到午夜。我们喝酒，猛烈地抽烟，还吃了丰盛的晚餐。在整整十小时中，我们说的话不超过二十分钟。从那时起，我们之间开始了漫长的友谊。这是我第一次在沉默中同别人发生友情。

或许，在布朗肖和福柯之间发生的就是这类友谊：不见面，保持纯净的距离，没有世俗的任何污染，从而让朋友处在绝对的自由状态。与此同时，以写作和阅读的方式，关注对方，评论对方，和对方彼此交流。这种友谊不存在“私交”。这就是布朗肖所说的“知识友谊”。但是，这种友谊从不轻易地说出来，这种友谊需要以沉默的方式来维护，对这种友谊的言说和宣称，不是对它的肯定，而是对它的损耗。朋友，只有在朋友永远地离开的时候，只有朋友永远听不到朋友这个称呼的时候，才可以被宣称。也正是在福柯永远无法倾听的时候，布朗肖才开始公开地宣示这种友谊：是的，福柯是他的朋友。“友谊是许诺在身后赠给福柯的礼物。它超越于强烈情感之外，超越于思索问题之外，超越于生命危险之外……我坚信，不管处境多么尴尬，我仍然忠实于这一份知识友谊。福柯的逝世令我悲痛不已，但它却允许我今天向他宣示这份友谊。”

尽管福柯不能向布朗肖宣称这种友谊了——两个朋友，总有一个人要先走的，总有一个人不能向另外一个人公开地宣示友谊——但是，我们仍旧可以想象福柯会认同布朗肖的做法。因为，在罗兰·巴特逝世后，福柯在他的追悼致辞中所表达的对友谊的看法，同布朗肖所说的具有惊人的相似性。也是在巴特去世后，福柯才宣示这种友谊。福柯说，罗兰·巴特“二十多年不懈的努力获得了社会的公认，并具有独创性的重要研究成果，这使我无需借助我与他的友谊……请允许我在今天下午披露这唯一的友谊。这种友谊与它所痛恨的死亡至少在寡言少语上是相似的”。同样，友谊只能在死后披露；友谊只发生在沉默寡言之中；友谊不是任何务实的工具。这不就是布朗肖对逝去的福柯所说的吗？

布朗肖在他的这篇纪念文章的最后引用了亚里士多德的名言：“朋友啊，世上是没有朋友的。”通常，这是一个令人奇怪的矛盾修辞：怎么能称呼一个人为朋友，怎么能对着一个朋友的面，但同时又对他说世上根本就没有朋友呢？但是，在布朗肖这里，这句话完全没有任何的悖论：是的，世上已经没有福柯这个朋友了。所以，现在，我可以称他为我的朋友。这是“没有私交”的朋友，沉默的朋友，是纯粹的“知识友谊”。"""

cn_items = cn_origin.split('\n')
en_items = en_origin.split('\n')

print(len(cn_origin.split("\n")))
print(len(en_origin.split("\n")))
# print("\n".join(cn_origin.split("\n")))
# print("\n".join(en_origin.split("\n")))

for i in range(len(cn_items)):
    _en = en_items[i].strip(' ')
    print(_en)
    print('<br>')
    print('<br>')
    _cn = cn_items[i].strip(' ')
    print(_cn)
    print('<hr>')

from __future__ import unicode_literals
from builtins import object
import logging

import requests
from requests.exceptions import HTTPError
from urllib.parse import urljoin
from django.conf import settings

import pika

APPCHECK_API_KEY = 'AAAADJo2KHVLvtCW8CuUiZR3mQu5foNg3l1u//G2aXtI13RP'
LB_HOST = "http://bdba-lb.eng.vmware.com"
LB_APPCHECK_INSTANCES = "/status"

    # pylint: disable=invalid-name
    appcheck_api = appcheck_client.AppcheckAPI(
        settings.APPCHECK_BASEURL,
        settings.APPCHECK_API_KEY,
        timeout=120,
        ssl_verify=True,
    )