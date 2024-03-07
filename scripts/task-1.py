# coding: utf-8
import re

def repleace_word_by_pronunciation(to_be_handle, pronunciation_text):
    # xx = re.findall('[a-zA-Z]+\(?[\u4e00-\u9fff]*\)?__[a-zA-Z|\u4e00-\u9fff]+__', pronunciation_text)
    xx = re.findall('[a-zA-Z]+\(?[\u4e00-\u9fff]*\)?__\S+__', pronunciation_text)
    # print(xx)
    # print(len(xx))

    result = {}
    for x in xx:
        result.update({re.findall('[a-zA-Z]+', x)[0]: x})

    # print(result)

    # for k, v in result.items():
    #     k = " {} ".format(k)
    #     v = " {} ".format(v)
    #     to_be_handle = to_be_handle.replace(k, v)

    for _syb in [' ', '\n', ',']:
        for k, v in result.items():
            k = " {}{}".format(k, _syb)
            v = " {}{}".format(v, _syb)
            to_be_handle = to_be_handle.replace(k, v)

    print(to_be_handle)


def map_cn_en(cn, en):
    ens = en.split(".")
    cns = cn.split("。")

    print(len(ens))
    print(len(cns))
    assert len(ens) == len(cns)

    for i in range(len(ens)):
        print(ens[i])
        print("<br>")
        print("<br>")
        print(cns[i])
        print("<hr>")

pronunciation_text = """DaJiangDaJiang Helping DaJiang move house, DaJiang squatted() on the ground and cried while sorting(排序) out a pile__派欧(4声)__ of old books DaJiang What DaJiang opened was a notebook, which recorded daily expenses, one by one, as clear as a one-dollar breakfast and three-dollar lunch DaJiang Later, DaJiang told me a story about him and his father DaJiang DaJiang's home is in a village in the countryside of Xuzhou.
In his memory, his father has been working part-time near Xuzhou Railway Station, and it is rare to return home once DaJiang When DaJiang was admitted(承认)__啊(2)得咪剃的__ to a university in Xi'an, his father took out a bag of money from the bank, counted(数) each one with saliva(唾液), and counted(数) them again and again DaJiang When he was a freshman, DaJiang was addicted(上瘾) to online games and often spent the whole night in the Internet cafes outside the school DaJiang Although he felt a little wasted, the classmates around him were similar, either playing football, watching movies, or playing games online.
, DaJiang is relieved(松了一口气)__瑞利误的__ DaJiang After returning home from the summer vacation(假期), DaJiang stayed in the village for a few days and felt very bored(无聊)__勃(4)的__, so he suggested to his father nervously(紧张地) that he wanted to go to his place to play for a few days At least there is an Internet cafe there!
Father actually agreed for the first time DaJiang From a distance, DaJiang saw his father waiting__微ting(4声)__ at the exit of the train station DaJiang After a year of baptism(洗礼)__吧普剃震__ in college, DaJiang felt for the first time that his father was so dazzling(眼花缭乱的) in the crowd - the clothes were tattered(破烂的)__它特的__ and too large to fit He reminded his father that the clothes were too old Father said that the one who worked hard was not sitting in the office, so why did he wear so new clothes?
He said again, that's too big Father said again, the clothes are bigger, so you can stretch()__死倔(4趣)__ your hands and feet when you work, otherwise, as soon as you stretch()__死倔(4趣)__ out your hands, the clothes will be torn() DaJiang2003 What DaJiang did not expect was that in 2003, his father, who had a monthly income of more than 4,000 yuan, lived in the attic(阁楼)__阿替克__ of a private house with only six or seven square meters DaJiang In addition(除了)__啊(2声)滴迅__ to an iron-framed()__福累木的__ bed, there is also a wooden shelf(架子上) for the washbasin(脸盆).
On the enamel(搪瓷)__以那(1声)谋(4声)__ basin(盆地)__玩(新余)sin__ with many broken enamels__以那(1)谋(4)四__, there is an old towel(毛巾)__套沃__ that can't be seen.
.
.
DaJiang always thought that his father lived in the city.
It's a very comfortable day, I didn't expect it to be so hard DaJiang Father took DaJiang back to his residence()__蜕(新余)Z等死__, and said, "You sit, I'm going to do some work " Then he went downstairs and walked away DaJiang DaJiang couldn't sit down, so he quietly(安静地)__快特利__ closed the door and went downstairs, Following behind his father, he wanted to see what his father did DaJiang After a round of twists and turns, DaJiang followed his father to the Xuzhou cold storage DaJiang There were more than a dozen__搭震__ people who were similar to his father, some pushing carts()__卡(4)自__, some carrying poles(波兰人)__剖(4)自__, DaJiang saw his father push out his own from the doorman.
Trolley(电车)__缺利__ At this moment, a large truck entered__恩(新余)特的__ the compound(复合)__康胖得(4声)__, and my father and everyone followed behind the truck and went in DaJiang A few minutes later, DaJiang saw his father.
He hunched(弯腰驼背) over a large cardboard box, walked a few steps, paused(停顿了一下)__破自的__, wiped()__外铺特__ the sweat on his forehead with a towel(毛巾)__套沃__ tied() around his wrist(手腕)__瑞斯特(w不发音)__, and walked a few steps forward, putting the cardboard box on his back.
On the trolley(电车)__缺利__, then ran to the big truck, and after a few seconds, hunched(弯腰驼背) over another cardboard box DaJiang After repeating this for seven times, my father pushed the car towards the icehouse, hunched(弯腰驼背) over his waist(腰)__为四特__, his legs clenched(握紧)__可烂趣的__ tightly(紧密)__胎特利__, and DaJiang could even see the blue veins() on his father's legs from a few dozen__搭震__ meters away DaJiang It turns out that my father earned(赢得了)__摁的__ hard-earned(赢得了)__摁的__ money!
DaJiang is melancholy(忧郁的) He asked the doorman, how much money can he make when he moves the goods?
The doorman told him that it was fifty cents a box DaJiang DaJiang calculated(计算) in his heart that his father shipped seven boxes at a time, earning() three yuan and fifty cents DaJiang DaJiang went home that afternoon He no longer thought about surfing(冲浪)__奢fing__ the Internet, and his father's blue-veined(有纹理的) legs were always shaking() in front of his eyes He didn't even think about it, how much his father's sweat was wasted in the Internet cafe DaJiangDaJiang When DaJiang returned to school, his father took out a thick(厚)__色(广东话)克__ wad(使成一团) of money from the bank, counted(数) it and handed it over to DaJiang DaJiang DaJiang counted(数) it and said, "This semester(学期)__谁(sei)吗四特__ is short, two thousand is enough "Speaking, split half and leave it to my father DaJiang On this day, DaJiang is determined to be a good son and a good student But this kind of thought quickly became a thing of the past.
When those old playmates went to the Internet cafe again, when he saw the game pattern__趴疼(4声)__ of Warcraft intentionally or not, he could not help but feel restless in his heart Finally, He walked into the Internet cafe again K During the National Day, the roommates organized to go to karaoke, go to the bar, and even go to the sauna(桑拿)__嗦那__ The 2,000 yuan brought(带来了)__补落特__ from home will be gone by the end of October DaJiang DaJiang called her mother and said that she had given birth some time ago.
I fell ill, and the money I brought(带来了)__补落特__ was spent DaJiang On the afternoon of the third day, Xi'an suddenly cooled(冷却) down.
DaJiang, who was playing cards with his classmates in the dormitory(宿舍)__多密趣__, received a call saying that someone was looking for him at the school gate DaJiang DaJiang ran to the school gate and saw her father Father in his fifties(五十多岁), like a seven-year-old A ten-year-old old man, old and tired, with a bed of cotton wool() on his back DaJiang DaJiang took his father into the campus() and asked him in a low voice: "Why are you here, I left an account for my mother, you just put the money into that card You have run so far, carrying this thing on your back, Hard work and waste of money " His father smiled at him flatteringly()__福拉特ringly__, and said, "Listen to your mother, you were sick some time ago, how are you now, are you okay?
Eat well, take care of yourself, you don't have to worry about living expenses, as long as you can eat Good health, good grades in school, no matter how much living expenses, your father can afford it It's getting cold, this is the batting(击球) your mother made for you with the cotton she planted DaJiang " DaJiang murmured()__默默的__, "It's.
.
.
well.
.
.
"On the way to the teaching building, my father said, "I'm relieved(松了一口气)__瑞利误的__ to see that you are fine.
I'll go back after giving you the living expenses It won't affect you DaJiang " DaJiang took the money from his father, I wanted to bring my father to live in the hostel(旅馆) of the school, but my father said again, "Winter vacation(假期) in two months?
I brought(带来了)__补落特__ you 3,000 yuan this time.
You just got sick, so you need to eat better and take care of yourself.
Only when you are strong can you have the energy to study hard DaJiang " Father stopped, "Go back!
"DaJiang knew his father's temper(脾气), so he didn't say anything anymore He was not far away, when he turned around, he found his father still standing there and waved()__为误的__ to him He remembered that when he was in high school, every time his father sent him to the school in the county(县) seat, It's all this scene(场景)__性(新余)__, tears overflowing(满溢的) my eyes DaJiang The shriveled(枯萎)__学(1)沃的__ purse(钱包) finally swelled() up, and the monster that he had not seen for a week was calling DaJiang again DaJiang After dinner, DaJiang went to the Internet cafe outside the school DaJiang After five hours of fierce(激烈的)__肺叶四__ fighting, DaJiang was going back to the dormitory(宿舍)__多密趣__ As usual, he I came to a big banyan tree outside the school again, and climbed the wall from there to enter the school The moment he climbed over the wall, his heart suddenly ached(痛)__诶克的__!
The dim() streetlights shone(照)__西像(快连)__ on his father.
He was leaning()__李(1声)宁__ against the corner of the wall, with a ragged(衣衫褴褛的) cardboard box under him.
At this moment, he was wrapping and wrapping the cotton-padded() clothes on his body.
Scarf(围巾)__死嘎(4)付__, wrapped tightly(紧密)__胎特利__ around father's head DaJiang DaJiang said this, he couldn't help crying again DaJiang After crying for a while, DaJiang continued(继续): "Later my mother told me that my dad heard that I was ill and wanted to see me desperately(拼命)__折(新余)四泼略特利__.
I couldn't buy a seat ticket, and I was reluctant(不情愿的)__瑞拉客tan特__ to buy a sleeper, so I came to Xi'an after standing for more than 20 hours In order to save money for accommodation(住宿)__啊康摸dei迅__, I squatted() in the corner of our school all night.
.
.
I cried on the phone, I pretended not to know until my mother told me Because I knew my father's stubbornness(固执)__死搭born逆四__, I was Even if you wake him up, he'll stick(坚持)__死剃克__ around there I quietly(安静地)__快特利__ went back to the dormitory(宿舍)__多密趣__, but my heart was still in pain.
Thinking of his action of wrapping his clothes, I felt distressed()__底四倔(4声)四特__ I deleted all the accounts related to the game overnight(在一夜之间) Since then, I have never been in an Internet cafe again, and I have never wasted a penny again That is, from that day on, I prepared this ledger(分类帐) and started to make up for the schoolwork(家庭作业) that I had lost in the past.
"I used to think that his life was bad and he didn't enjoy the blessings of life After that incident(事件), I realized that it was not that he had no blessings, but that he was used to giving all the enjoyment to his son.
.
.
He has been from the age of seventeen.
Started to work in that freezer, until last spring DaJiang " DaJiang couldn't go on anymore DaJiangDaJiang I know that DaJiang's father passed away last spring, leaving DaJiang with a deposit(存款)__得(3声)泼这__ of 370,000 yuan DaJiang DaJiang's father is the epitome()__以批特密__ of many poor fathers, deep and selfless() love Fortunately, his children saw the father in the corner, and I know that there are many children who can't think of and can't see the love in the corner"""



to_be_handle = """帮DaJiang搬家，在整理一堆旧书籍的时候，DaJiang蹲在地上呜呜大哭起来
Helping DaJiang move house, DaJiang squatted on the ground and cried while sorting out a pile of old books


DaJiang打开的是一个笔记本，上面记着日常开支，一笔一笔，清晰到一块钱的早餐，三块钱的午餐
What DaJiang opened was a notebook, which recorded daily expenses, one by one, as clear as a one-dollar breakfast and three-dollar lunch


稍后，DaJiang给我讲了关于他和父亲的一段往事
Later, DaJiang told me a story about him and his father


DaJiang的家在徐州乡下的一个村子里，在他的记忆里，父亲一直在徐州火车站附近打短工，难得回家一次
DaJiang's home is in a village in the countryside of Xuzhou. In his memory, his father has been working part-time near Xuzhou Railway Station, and it is rare to return home once


DaJiang考上西安的一所大学时，父亲从银行取出一包钱，一张一张沾着口水数，数了一次又一次
When DaJiang was admitted to a university in Xi'an, his father took out a bag of money from the bank, counted each one with saliva, and counted them again and again 


大一的时候，DaJiang迷上了网络游戏，经常整晚耗在校外的网吧里
When he was a freshman, DaJiang was addicted to online games and often spent the whole night in the Internet cafes outside the school 


他虽然感觉到有些虚度光阴，但身边的同学们都差不多，不是打球，就是看电影，或者上网打游戏，DaJiang也就释然了
 Although he felt a little wasted, the classmates around him were similar, either playing football, watching movies, or playing games online. , DaJiang is relieved 


暑假回家，DaJiang在村里待了几天，感觉特别无聊，就忐忑地对父亲提出，想去他那里玩几天
After returning home from the summer vacation, DaJiang stayed in the village for a few days and felt very bored, so he suggested to his father nervously that he wanted to go to his place to play for a few days 


至少那里有网吧！父亲竟然破天荒地答应了
 At least there is an Internet cafe there! Father actually agreed for the first time 


远远地，DaJiang就看到父亲等在火车站的出口
From a distance, DaJiang saw his father waiting at the exit of the train station


经过一年大学生活的洗礼，DaJiang第一次感觉父亲在人群中是那么扎眼——衣服破旧，还宽大得有些不合身
After a year of baptism in college, DaJiang felt for the first time that his father was so dazzling in the crowd - the clothes were tattered and too large to fit 


他提醒父亲，衣服太旧了
He reminded his father that the clothes were too old 


父亲说，出力干活的，又不是坐办公室，穿那么新干吗？他又说，那也太大了啊
 Father said that the one who worked hard was not sitting in the office, so why did he wear so new clothes? He said again, that's too big 


父亲又说，衣服大点，干活才能伸展开手脚，不然，一伸手，衣服就撕破了
 Father said again, the clothes are bigger, so you can stretch your hands and feet when you work, otherwise, as soon as you stretch out your hands, the clothes will be torn


让DaJiang没有想到的是，在2003年，月入就有四千多元的父亲，竟然住在一栋民房的阁楼里，只有六七平方米
What DaJiang did not expect was that in 2003, his father, who had a monthly income of more than 4,000 yuan, lived in the attic of a private house with only six or seven square meters 


除了一张铁架床之外，还有个放洗脸盆的木架子，那个多处掉瓷的搪瓷盆上，搭着一条看不出本色的旧毛巾……DaJiang一直以为，父亲在城里过的是很舒服的日子，没想到竟是这样清苦
In addition to an iron-framed bed, there is also a wooden shelf for the washbasin. On the enamel basin with many broken enamels, there is an old towel that can't be seen... DaJiang always thought that his father lived in the city. It's a very comfortable day, I didn't expect it to be so hard 


父亲把DaJiang带回住处，就说：“你坐着，我要去忙活了
Father took DaJiang back to his residence, and said, "You sit, I'm going to do some work


”说着，就咚咚咚下楼走了
" Then he went downstairs and walked away


DaJiang坐不下去，就悄悄地关上门，下楼，跟在父亲身后，他想看看父亲是做什么的
 DaJiang couldn't sit down, so he quietly closed the door and went downstairs, Following behind his father, he wanted to see what his father did


七弯八拐，DaJiang跟随父亲来到了徐州冷库
After a round of twists and turns, DaJiang followed his father to the Xuzhou cold storage 


那儿聚集着十多个跟父亲差不多的人，有的推着推车，有的拿着扁担，DaJiang看到父亲从门卫那里推出了自己的手推车
 There were more than a dozen people who were similar to his father, some pushing carts, some carrying poles, DaJiang saw his father push out his own from the doorman. Trolley


正在这时，一辆大货车进入大院，父亲和大伙一起，跟在车后拥了进去
At this moment, a large truck entered the compound, and my father and everyone followed behind the truck and went in


几分钟后，DaJiang看到了父亲，他弓着腰扛着大大的纸箱，走几步，停一下，用系在手腕处的毛巾擦额头的汗，再前行几步，把背上的纸箱放到手推车上，接着又奔向大货车，几秒钟后，又弓着腰扛来一个纸箱
A few minutes later, DaJiang saw his father. He hunched over a large cardboard box, walked a few steps, paused, wiped the sweat on his forehead with a towel tied around his wrist, and walked a few steps forward, putting the cardboard box on his back. On the trolley, then ran to the big truck, and after a few seconds, hunched over another cardboard box 


如此反复七次之后，父亲推着那辆车向冰库走去，弓着腰，双腿蹬得紧紧的，几十米外的DaJiang甚至看得到父亲腿上的青筋
After repeating this for seven times, my father pushed the car towards the icehouse, hunched over his waist, his legs clenched tightly, and DaJiang could even see the blue veins on his father's legs from a few dozen meters away


原来父亲赚的是血汗钱！DaJiang惆怅不已
It turns out that my father earned hard-earned money! DaJiang is melancholy 


他向门卫打听，搬一次货，能有多少钱？门卫告诉他，五毛钱一箱
 He asked the doorman, how much money can he make when he moves the goods? The doorman told him that it was fifty cents a box


DaJiang在心里算了一下，父亲一次运了七箱，赚三块五毛钱
DaJiang calculated in his heart that his father shipped seven boxes at a time, earning three yuan and fifty cents


DaJiang当天下午就回了家
DaJiang went home that afternoon 


他不再想着上网了，他的眼前总是晃动着父亲暴着青筋的腿
 He no longer thought about surfing the Internet, and his father's blue-veined legs were always shaking in front of his eyes


他还算了算，自己在网吧浪费了多少父亲的汗水
 He didn't even think about it, how much his father's sweat was wasted in the Internet cafe


DaJiang返校的时候，父亲又从银行里取出厚厚的一沓钱，数了又数，交给DaJiang
When DaJiang returned to school, his father took out a thick wad of money from the bank, counted it and handed it over to DaJiang


DaJiang数了一下，说，“这学期时间短，有两千就够了
DaJiang counted it and said, "This semester is short, two thousand is enough


”说着，分出一半，留给父亲
 "Speaking, split half and leave it to my father 


这一天，DaJiang下决心做个好儿子，做个好学生
 On this day, DaJiang is determined to be a good son and a good student


但他的这种想法，很快成为过眼云烟
But this kind of thought quickly became a thing of the past.


当那些旧日的玩伴又吆喝着去网吧，当他有意无意地看到魔兽游戏图案，他内心里总是忍不住躁动
When those old playmates went to the Internet cafe again, when he saw the game pattern of Warcraft intentionally or not, he could not help but feel restless in his heart


终于，他又一次走进了网吧
Finally, He walked into the Internet cafe again 


国庆节的时候，室友们组织去K歌，去酒吧，还去洗了桑拿
During the National Day, the roommates organized to go to karaoke, go to the bar, and even go to the sauna


从家里带来的两千块钱，到十月底就没有了
The 2,000 yuan brought from home will be gone by the end of October


DaJiang给妈妈打电话，说前段时间生了一场病，带来的钱花完了
DaJiang called her mother and said that she had given birth some time ago. I fell ill, and the money I brought was spent 


第三天下午，西安突然降温，正在宿舍里和同学打牌的DaJiang接到电话，说校门口有人找他
On the afternoon of the third day, Xi'an suddenly cooled down. DaJiang, who was playing cards with his classmates in the dormitory, received a call saying that someone was looking for him at the school gate


DaJiang跑到校门口，看到了父亲
DaJiang ran to the school gate and saw her father


五十多岁的父亲，像个七十岁的老人，老态龙钟，一脸的疲惫，身上背着一床棉絮
Father in his fifties, like a seven-year-old A ten-year-old old man, old and tired, with a bed of cotton wool on his back


DaJiang把父亲带入校园里，才小声问他：“你怎么来了，我给妈留了账号，你把钱打入那个卡上就行了
DaJiang took his father into the campus and asked him in a low voice: "Why are you here, I left an account for my mother, you just put the money into that card 


你跑这么远，还背着这个东西，又辛苦，又浪费钱
 You have run so far, carrying this thing on your back, Hard work and waste of money 


”
" 


父亲讨好地对他笑着，说：“听你妈说，你前段时间病了，现在怎么样了，好了没？要吃好点，照顾好自己，你不用担心生活费，只要你能吃出好身体，学出好成绩，就是再多的生活费，你爸也掏得起
His father smiled at him flatteringly, and said, "Listen to your mother, you were sick some time ago, how are you now, are you okay? Eat well, take care of yourself, you don't have to worry about living expenses, as long as you can eat Good health, good grades in school, no matter how much living expenses, your father can afford it


天冷了，这是你妈妈用自己种的棉花给你做的棉胎
It's getting cold, this is the batting your mother made for you with the cotton she planted 


”DaJiang嗫嚅着说：“已经……好了……”在通往教学楼的路上，父亲说：“看到你好好的，我也就放心了，把生活费给你，我就回去
" DaJiang murmured, "It's... well..."On the way to the teaching building, my father said, "I'm relieved to see that you are fine. I'll go back after giving you the living expenses 


不影响你
 It won't affect you


”DaJiang接过父亲递过来的钱，正想说带父亲到学校的招待所住，父亲又说了，“再有两个月就放寒假了吧？我这次给你带了三千块，你刚生病，要吃好点，把身子养壮点，才能有精力上好学
" DaJiang took the money from his father, I wanted to bring my father to live in the hostel of the school, but my father said again, "Winter vacation in two months? I brought you 3,000 yuan this time. You just got sick, so you need to eat better and take care of yourself. Only when you are strong can you have the energy to study hard


”父亲止住脚步，“你回去吧！”DaJiang知道父亲的脾气，就不再说什么
" Father stopped, "Go back!"DaJiang knew his father's temper, so he didn't say anything anymore


他走出不远，回头的时候，发现父亲还站在原地，朝他挥手
He was not far away, when he turned around, he found his father still standing there and waved to him


他想起读高中的时候，每次父亲送他去县城的学校，都是这个场景，泪就溢满了眼睛
He remembered that when he was in high school, every time his father sent him to the school in the county seat, It's all this scene, tears overflowing my eyes


干瘪的钱包终于鼓了起来，一周不见的魔兽又在呼唤DaJiang
The shriveled purse finally swelled up, and the monster that he had not seen for a week was calling DaJiang again


晚饭过后，DaJiang又去了校外的网吧
After dinner, DaJiang went to the Internet cafe outside the school


五个小时的凶猛厮杀之后，DaJiang要回宿舍了
After five hours of fierce fighting, DaJiang was going back to the dormitory


和往常一样，他又来到了校外的一棵大榕树下，从那儿翻墙进校
As usual, he I came to a big banyan tree outside the school again, and climbed the wall from there to enter the school


就在他翻上墙头的那一刻，他的心一下子疼了起来！昏黄的路灯，照着他的父亲，他偎在那个墙角，身下垫着不知从哪里拣来的破纸箱
The moment he climbed over the wall, his heart suddenly ached! The dim streetlights shone on his father. He was leaning against the corner of the wall, with a ragged cardboard box under him.


此刻，他正把身上的棉衣裹了又裹，而自己高中时围过的围巾，紧紧地缠在父亲头上
At this moment, he was wrapping and wrapping the cotton-padded clothes on his body. Scarf, wrapped tightly around father's head


DaJiang说到这里，又忍不住放声大哭起来
DaJiang said this, he couldn't help crying again 


哭了好一会儿，DaJiang又接着说：“后来我妈告诉我说，我爸听说我病了，就不顾一切地要来看我，买不到座位票，又舍不得买卧铺，站了二十多个小时来到西安
 After crying for a while, DaJiang continued: "Later my mother told me that my dad heard that I was ill and wanted to see me desperately. I couldn't buy a seat ticket, and I was reluctant to buy a sleeper, so I came to Xi'an after standing for more than 20 hours


为了省下住宿的钱，在我们学校的墙角下蹲了一夜……我在电话这头就哭，在妈妈告诉我之前，我一直装作不知道
In order to save money for accommodation, I squatted in the corner of our school all night...I cried on the phone, I pretended not to know until my mother told me


因为我知道父亲的固执，我那时就是叫醒他，他也会坚持着在那里
Because I knew my father's stubbornness, I was Even if you wake him up, he'll stick around there


我悄悄回了宿舍，可我的心里却一直疼着，想到他裹紧衣服的动作，我就心疼
I quietly went back to the dormitory, but my heart was still in pain. Thinking of his action of wrapping his clothes, I felt distressed 


我连夜把所有的关于游戏的账号全部删掉了
 I deleted all the accounts related to the game overnight 


从那以后，我再也没有进过网吧，再也不浪费一分钱
Since then, I have never been in an Internet cafe again, and I have never wasted a penny again


也就是从那一天起，我准备了这个记账本，开始把以前落下的学业一点点补回来
 That is, from that day on, I prepared this ledger and started to make up for the schoolwork that I had lost in the past.


”“我以前一直以为是他命不好，没有享受生活的福气
”"I used to think that his life was bad and he didn't enjoy the blessings of life 


经过那件事情，我才知道，不是他没有福，而是他习惯了把一切享受给予他儿子……他从十七岁开始在那个冰库做事，一直做到去年春天
 After that incident, I realized that it was not that he had no blessings, but that he was used to giving all the enjoyment to his son... He has been from the age of seventeen. Started to work in that freezer, until last spring 


”DaJiang说不下去了
" DaJiang couldn't go on anymore


我知道，DaJiang的父亲于去年春天去世了，给DaJiang留下了三十七万元的存款
I know that DaJiang's father passed away last spring, leaving DaJiang with a deposit of 370,000 yuan


DaJiang的父亲是许多贫困父亲的缩影，深沉而又无私的爱
DaJiang's father is the epitome of many poor fathers, deep and selfless love


所幸的是，他的孩子看到了墙角的父亲，而我知道，还有很多孩子想不到，也看不到墙角里的爱
Fortunately, his children saw the father in the corner, and I know that there are many children who can't think of and can't see the love in the corner
"""


to_be_handle_2 = """In receiving the distinction with which your free Academy has so generously honoured me, my gratitude has been profound, particularly when I consider the extent to which this recompense has surpassed my personal merits


尊敬的国王和皇后陛下，尊敬的王室成员，女士们，先生们：秉承自由精神的贵学院慷慨授予我这份殊荣，我自认我的成就远远配不上它的分量，所以更是由衷地心怀感激


<hr>
 Every man, and for stronger reasons, every artist, wants to be recognized


所有人都渴望得到认可，艺术家就更为如此


<hr>
 So do I


我也是一样


<hr>
 But I have not been able to learn of your decision without comparing its repercussions to what I really am


只有当我将你们的决定所产生的影响与真实的我进行比较之后，我才真正理解你们何以作了这样一个决定


<hr>
 A man almost young, rich only in his doubts and with his work still in progress, accustomed to living in the solitude of work or in the retreats of friendship: how would he not feel a kind of panic at hearing the decree that transports him all of a sudden, alone and reduced to himself, to the centre of a glaring light? And with what feelings could he accept this honour at a time when other writers in Europe, among them the very greatest, are condemned to silence, and even at a time when the country of his birth is going through unending misery?I felt that shock and inner turmoil


一个尚且年轻的人，除了疑惑一无所有，他的作品尚未成型，并且习惯于在工作中孤独地生活，对各种示好也退避三舍，对于这样一个离群索居的人来说，突然被逮到，并抛置于这耀眼的聚光灯下，又怎么能不感到一种恐慌呢？当欧洲其他的作家，哪怕是其中最伟大的一些作家，都被迫保持沉默，当他的故土，正遭受着无止境的苦难，他将以怎样的心情来接受这份荣誉呢？我就经历了这种内心的惶恐与不安


<hr>
 In order to regain peace I have had, in short, to come to terms with a too generous fortune


为了重新获得平静，我只能接受这份命运慷慨的馈赠


<hr>
 And since I cannot live up to it by merely resting on my achievement, I have found nothing to support me but what has supported me through all my life, even in the most contrary circumstances: the idea that I have of my art and of the role of the writer


既然我的成就无法与这份奖项匹配，我便只能倚赖那份支撑着我人生的信念，即便在最艰难的境况下也未曾抛却我的那份信念：那就是我对我的艺术以及对作家这一角色的看法


<hr>
 Let me only tell you, in a spirit of gratitude and friendship, as simply as I can, what this idea is


让我怀着感激和友好的心情，对大家尽可能简短地表达一下这个想法


<hr>
For myself, I cannot live without my art


于我而言，没有艺术，我便无法存活


<hr>
 But I have never placed it above everything


但我从没有把这份艺术置于一切之上，


<hr>
 If, on the other hand, I need it, it is because it cannot be separated from my fellow men, and it allows me to live, such as I am, on one level with them

相反，它之所以对我而言不可或缺，正是因为它与所有人紧紧相连，并且允许像我这样的一个人能和大家一样生活下去




<hr>
 It is a means of stirring the greatest number of people by offering them a privileged picture of common joys and sufferings


艺术在我看来并不是一场孤独的狂欢, 艺术是一种手段，它以其特有的方式呈现了人类共同的苦难与欢乐，从而感动了大多数的人


<hr>
 It obliges the artist not to keep himself apart; it subjects him to the most humble and the most universal truth


所以它迫使艺术家不再自我孤立，使其屈从于一种最为质朴、最为普世的真理


<hr>
 And often he who has chosen the fate of the artist because he felt himself to be different soon realizes that he can maintain neither his art nor his difference unless he admits that he is like the others


而通常情况下，那个自认与众不同而选择艺术生涯的人很快就会发现，只有承认自己与众生的共性，他的艺术和他的独特才能从中得到滋养


<hr>
 The artist forges himself to the others, midway between the beauty he cannot do without and the community he cannot tear himself away from


正是在这种自身与他者不断的往来中、在与他不可搁置的美以及不可抽离的群体的交往之中，艺术家得到了自我锤炼


<hr>
 That is why true artists scorn nothing: they are obliged to understand rather than to judge


这也是为什么真正的艺术家不会蔑视任何东西；他们要求自己必须理解一切，而不是评判一切


<hr>
 And if they have to take sides in this world, they can perhaps side only with that society in which, according to Nietzsche’s great words, not the judge but the creator will rule, whether he be a worker or an intellectual


如果他们必须在这个世界上选择一个阵营，那他们或许只能属于尼采的伟大言论中所构建的那种社会：一个由创造者而不是评判者来统治的社会，无论这里的创造者是劳动人民还是知识分子


<hr>
By the same token, the writer’s role is not free from difficult duties


同样地，作家这一角色也被赋予了艰难的职责


<hr>
 By definition he cannot put himself today in the service of those who make history; he is at the service of those who suffer it


身为作家，在如今这个年代，他不该为制造历史的人服务，他应该为承受历史的人服务


<hr>
 Otherwise, he will be alone and deprived of his art


 否则，他将被孤立，也将失去他的艺术


<hr>
 Not all the armies of tyranny with their millions of men will free him from his isolation, even and particularly if he falls into step with them


一个作家，若是与独裁者为伍，那么即便独裁者有千军万马与之同行，他也依然无法摆脱那种孤独


<hr>
 But the silence of an unknown prisoner, abandoned to humiliations at the other end of the world, is enough to draw the writer out of his exile, at least whenever, in the midst of the privileges of freedom, he manages not to forget that silence, and to transmit it in order to make it resound by means of his art


但世界另一头，一个被遗弃在屈辱中的无名之囚，他的沉默却足以一次又一次将作家从这种孤独的流放中拯救出来，只要他在享有自由权利的同时，始终不忘这种沉默，并以艺术的方式来使这种沉默发出声响


<hr>
None of us is great enough for such a task


我们中任何人都没有伟大到足以承担这一使命


<hr>
 But in all circumstances of life, in obscurity or temporary fame, cast in the irons of tyranny or for a time free to express himself, the writer can win the heart of a living community that will justify him, on the one condition that he will accept to the limit of his abilities the two tasks that constitute the greatness of his craft: the service of truth and the service of liberty


但是在他一生的境遇中，无论是门庭冷落还是扬名一时，无论是被压制于暴政的桎梏之下还是拥有一时的言论自由，作家只有忠心耿耿竭尽所能地为真理和自由服务，他的职业才能因此变得伟大，他才能得到民众发自肺腑的正名


<hr>
 Because his task is to unite the greatest possible number of people, his art must not compromise with lies and servitude which, wherever they rule, breed solitude


作家的使命，就是团结尽可能多的人，这个使命不应屈服于谎言和奴役，因为在谎言和奴役统治的土地上，处处囚禁着孤独的灵魂


<hr>
 Whatever our personal weaknesses may be, the nobility of our craft will always be rooted in two commitments, difficult to maintain: the refusal to lie about what one knows and the resistance to oppression


无论我们作为个人有着怎样的弱点，我们职业的高贵却永远扎根在两个并不容易坚守的承诺里：对于知晓的事，绝无谎言；对于任何压迫，反抗到底


<hr>
For more than twenty years of an insane history, hopelessly lost like all the men of my generation in the convulsions of time, I have been supported by one thing: by the hidden feeling that to write today was an honour because this activity was a commitment – and a commitment not only to write


在二十多年的荒诞历程中，孤立无援的我和同代人一样，迷失在时代的跌宕变迁中， 仅靠内心隐隐的一种感觉支撑着：在当今这个世界，写作是一种光荣，因为这一行为肩负使命，并迫使你不仅仅去写作


<hr>
 Specifically, in view of my powers and my state of being, it was a commitment to bear, together with all those who were living through the same history, the misery and the hope we shared


它尤其迫使我按我自己的方式，以我的一己之力，与所有和我一样经历过那段历史的人一起去承担起我们共有的那种痛苦与希冀


<hr>
 These men, who were born at the beginning of the First World War, who were twenty when Hitler came to power and the first revolutionary trials were beginning, who were then confronted as a completion of their education with the Spanish Civil War, the Second World War, the world of concentration camps, a Europe of torture and prisons – these men must today rear their sons and create their works in a world threatened by nuclear destruction


这些人，出生于第一次世界大战之初；希特勒政权建立和最初的革命浪潮掀起时，他们又正值二十多岁, 接着，像是要使他们的经历更加完整，他们又经历了西班牙内战、第二次世界大战，他们经历了那个满目疮痍、遍地集中营和牢狱的欧洲，而如今，正是他们这些人，又要在毁灭性核武器的威胁下，抚育他们的下一代，完成他们的使命



<hr>
 Nobody, I think, can ask them to be optimists

我想，没有任何人有权利要求他们乐观



<hr>
 And I even think that we should understand – without ceasing to fight it – the error of those who in an excess of despair have asserted their right to dishonour and have rushed into the nihilism of the era


我甚至主张，在与他们不断斗争的同时，我们应该理解他们的所作所为：他们只是因为与日俱增的绝望，而做出了耻辱之举，并且堕入了这个时代所盛行的虚无主义


<hr>
 But the fact remains that most of us, in my country and in Europe, have refused this nihilism and have engaged upon a quest for legitimacy


但是，不论是在我们国家，还是在整个欧洲，我们中的大多数，仍然拒绝虚无主义，仍在寻找一种正义


<hr>
 They have had to forge for themselves an art of living in times of catastrophe in order to be born a second time and to fight openly against the instinct of death at work in our history


我们需要锻造一种在多事之秋生活的艺术，为的是能够涅槃重生，然后坦然地与那历史进程中的死亡本能作斗争


<hr>
Each generation doubtless feels called upon to reform the world


或许，每代人都自信肩负着重塑世界的使命


<hr>
 Mine knows that it will not reform it, but its task is perhaps even greater


然而，我们这代人却知道，我们对此无能为力


<hr>
 It consists in preventing the world from destroying itself

但是，我们这代人的使命或许更伟大，因为我们的使命是：不让这个世界分崩离析



<hr>
 Heir to a corrupt history, in which are mingled fallen revolutions, technology gone mad, dead gods, and worn-out ideologies, where mediocre powers can destroy all yet no longer know how to convince, where intelligence has debased itself to become the servant of hatred and oppression, this generation starting from its own negations has had to re-establish, both within and without, a little of that which constitutes the dignity of life and death

我们继承的，是一段残破的历史，它混杂着革命的失败、走火入魔的科技、已经死去的诸神和穷途末路的意识形态，纵使在这样的时代，任何平庸的势力都能让这个世界毁于一旦，但这种平庸的势力只有否定的力量，在理智自甘堕落成仇恨与压迫的奴隶时，这种否定的力量并不能教会我们这代人在内心和外部世界重新修建起一点点能够给予生命和死亡以尊严的东西



<hr>
 In a world threatened by disintegration, in which our grand inquisitors run the risk of establishing forever the kingdom of death, it knows that it should, in an insane race against the clock, restore among the nations a peace that is not servitude, reconcile anew labour and culture, and remake with all men the Ark of the Covenant


在这样一个每时每刻都有可能崩塌的世界面前，我们伟大的裁判官们建立的恐怕永远是死亡的国度，而我们这代人知道，我们应该在与时间疯狂赛跑的同时，在不同民族之间，建立起一种不屈从于任何奴役的和平，重新调和工作与文化的关系，并与全世界所有人携起手来，构建一种联盟


<hr>
 It is not certain that this generation will ever be able to accomplish this immense task, but already it is rising everywhere in the world to the double challenge of truth and liberty and, if necessary, knows how to die for it without hate


没有人能够确定我们这代人是否能完成这项浩大的任务，但是，我们确定的是，他们已经遍布在全世界各个角落，为真理和自由而战，并时刻准备着为之赴死，无怨无悔


<hr>
 Wherever it is found, it deserves to be saluted and encouraged, particularly where it is sacrificing itself


正是这些人，值得我们尊敬和鼓励，无论在何时何地——尤其是在他们牺牲的地方


<hr>
 In any event, certain of your complete approval, it is to this generation that I should like to pass on the honour that you have just given me


总之，我想把你们刚刚授予我的荣耀转献给他们，相信你们也会感同身受


<hr>
At the same time, after having outlined the nobility of the writer’s craft, I should have put him in his proper place


与此同时，在说了作家职业的高尚之后，我想要还原作家的真实模样，除了和他的战友们一起共享的身份之外，他没有其他身份


<hr>
 He has no other claims but those which he shares with his comrades in arms: vulnerable but obstinate, unjust but impassioned for justice, doing his work without shame or pride in view of everybody, not ceasing to be divided between sorrow and beauty, and devoted finally to drawing from his double existence the creations that he obstinately tries to erect in the destructive movement of history


他既脆弱又固执；他无法永远保持公正，却又热切追寻着公正；在所有人的视线中，他默默构建着自己的作品，既不以之为耻，也不引以为傲，他永无止息地在痛苦与美好中被撕扯，最终是为了从他这双重的存在中，提炼出他固执地想要在历史的废墟中创建起来的东西


<hr>
 Who after all this can expect from him complete solutions and high morals? Truth is mysterious, elusive, always to be conquered


这么说完，谁还能期待他给出现成的答案和完美的道德信条呢？真理是神秘的、难以捕捉的，总是有待征服的


<hr>
 Liberty is dangerous, as hard to live with as it is elating


自由固然是令人振奋的，但实践起来也同样是危险的、艰难的


<hr>
 We must march toward these two goals, painfully but resolutely, certain in advance of our failings on so long a road


我们必须走向这两个目标，艰苦卓绝、征途漫漫，却坚定不移、矢志不渝


<hr>
 What writer would from now on in good conscience dare set himself up as a preacher of virtue? For myself, I must state once more that I am not of this kind


由此，哪个有着自知之明的作家还敢自诩为美德的传道者？至于我，我必须再说一次，这完全不是我的身份


<hr>
 I have never been able to renounce the light, the pleasure of being, and the freedom in which I grew up


我从来未能放弃生命中的光和幸福，不能放弃自由的生活，这些东西自小就伴随着我成长


<hr>
 But although this nostalgia explains many of my errors and my faults, it has doubtless helped me toward a better understanding of my craft


这种怀旧之情虽然也让我犯了不少错误，却无疑也帮助我更好地理解了我的职业，

<hr>

It is helping me still to support unquestioningly all those silent men who sustain the life made for them in the world only through memory of the return of brief and free happiness


帮助我毫不犹豫地站在那些沉默的人身边，那些人，除了从回忆中追索那一点点短暂而自由的幸福，在这个世上便无以为继


<hr>
Thus reduced to what I really am, to my limits and debts as well as to my difficult creed, I feel freer, in concluding, to comment upon the extent and the generosity of the honour you have just bestowed upon me, freer also to tell you that I would receive it as an homage rendered to all those who, sharing in the same fight, have not received any privilege, but have on the contrary known misery and persecution


现在，我向大家还原了真实的我，你们知道了我的浅薄有限，知道了我得益于他人，也知道了我艰难的信仰，作为结束，我终于能更自如地表达诸位授予我这份荣誉的广博与慷慨，也能更自如地对你们说，我接受这份荣誉，并要把它视作为一种致敬，向所有和我一样经历了战斗，却没有获得任何殊荣，只是饱经了苦难与迫害的人致敬


<hr>
 It remains for me to thank you from the bottom of my heart and to make before you publicly, as a personal sign of my gratitude, the same and ancient promise of faithfulness which every true artist repeats to himself in silence every day


最后，我要发自肺腑地对诸位表示感谢，并公开地，以感恩的心，向你们作出一个古老的承诺，任何一个真正的艺术家每天都会在静默中向自己作出的古老的承诺，那便是——忠诚


<hr>"""

pronunciation_text_2 = """In receiving the distinction with which your free Academy has so generously(慷慨地) honoured()__啊呢的__ me, my gratitude(感激之情)__葛入啊剃臭(新余)的__ has been profound, particularly__婆踢Q勒利__ when I consider the extent to which this recompense(报应) has surpassed(超过了) my personal merits(优点)__咪瑞自__.
Every man, and for stronger reasons, every artist, wants to be recognized.
So do I.
But I have not been able to learn of your decision without comparing its repercussions(影响)__瑞泼咔迅四__ to what I really am.
A man almost young, rich only in his doubts and with his work still in progress, accustomed(习惯了)__啊customed__ to living in the solitude(孤独)__梭(新余话)了臭（新余话）的__ of work or in the retreats(撤退)__瑞催自__ of friendship: how would he not feel a kind of panic at hearing the decree(法令)__底克瑞__ that transports him all of a sudden, alone and reduced to himself, to the centre of a glaring(明显的)__葛辣润__ light?
And with what feelings could he accept this honour at a time when other writers in Europe, among them the very greatest, are condemned(谴责)__肯den(4)的__ to silence, and even at a time when the country of his birth is going through unending(无休止的) misery?
I felt that shock(冲击) and inner turmoil(动荡)__特墨oil__.
In order to regain(恢复)__蕊gay摁__ peace I have had, in short, to come to terms with a too generous(慷慨的) fortune(《财富》杂志)__for群(新余)__.
And since I cannot live up to it by merely(仅仅是)__密二利__ resting on my achievement, I have found nothing to support me but what has supported me through all my life, even in the most contrary(相反)__肯缺瑞__ circumstances(): the idea that I have of my art and of the role of the writer.
Let me only tell you, in a spirit of gratitude(感激之情)__葛入啊剃臭(新余)的__ and friendship, as simply as I can, what this idea is.
For myself, I cannot live without my art.
But I have never placed it above everything.
If, on the other hand, I need it, it is because it cannot be separated from my fellow men, and it allows me to live, such as I am, on one level with them.
It is a means of stirring(激动人心的)__死的润__ the greatest number of people by offering them a privileged(享有特权的)__普瑞沃利巨的__ picture of common joys and sufferings(痛苦).
It obliges(要求)__啊波来(1声)撅四__ the artist not to keep himself apart; it subjects him to the most humble() and the most universal truth.
And often he who has chosen the fate(命运)__废特__ of the artist because he felt himself to be different soon realizes that he can maintain__命(一声)藤(4声)__ neither his art nor his difference unless he admits() that he is like the others.
The artist forges(伪造)__for(1声)撅四__ himself to the others, midway(中途) between the beauty he cannot do without and the community he cannot tear himself away from.
That is why true artists scorn() nothing: they are obliged()__鹅波赖聚的__ to understand rather than to judge.
And if they have to take sides in this world, they can perhaps side only with that society in which, according to Nietzsches great words, not the judge but the creator__可瑞A特__ will rule, whether he be a worker or an intellectual()__因特le克却__.
By the same token, the writers role is not free from difficult duties.
By definition__折(新余)飞(新余)你(新余)迅__ he cannot put himself today in the service of those who make history; he is at the service of those who suffer it.
Otherwise, he will be alone and deprived(被剥夺了) of his art.
Not all the armies of tyranny()__踢热你__ with their millions of men will free him from his isolation__癌搜勒(新余)迅__, even and particularly__婆踢Q勒利__ if he falls into step with them.
But the silence of an unknown prisoner__铺瑞争呢__, abandoned to humiliations(耻辱) at the other end of the world, is enough to draw the writer out of his exile(流亡)__e`克赛欧__, at least whenever, in the midst()__密自特__ of the privileges__(普洛V二)倔(4)四__ of freedom, he manages not to forget that silence, and to transmit(传输) it in order to make it resound() by means of his art.
None of us is great enough for such a task.
But in all circumstances() of life, in obscurity() or temporary(临时)__ten(1)破瑞二利__ fame()__废木__, cast in the irons(熨斗)__爱摁四__ of tyranny()__踢热你__ or for a time free to express himself, the writer can win the heart of a living community that will justify(证明)__撅四踢five__ him, on the one condition that he will accept to the limit of his abilities the two tasks that constitute() the greatness of his craft: the service of truth and the service of liberty(自由)__粒波剃__.
Because his task is to unite the greatest possible number of people, his art must not compromise(妥协) with lies and servitude(奴役)__奢为tude__ which, wherever they rule, breed(品种)__补瑞的__ solitude(孤独)__梭(新余话)了臭（新余话）的__.
Whatever our personal weaknesses may be, the nobility()__no biu了剃__ of our craft will always be rooted in two commitments(承诺), difficult to maintain__命(一声)藤(4声)__: the refusal(拒绝)__refu走__ to lie about what one knows and the resistance(电阻)__瑞z四ten四__ to oppression().
For more than twenty years of an insane history, hopelessly lost like all the men of my generation in the convulsions(抽搐)__肯窝选四__ of time, I have been supported by one thing: by the hidden feeling that to write today was an honour because this activity was a commitment__可密特ment__ and a commitment__可密特ment__ not only to write.
Specifically(具体地说)__死pe色(新余)飞(新余)可利__, in view of my powers and my state of being, it was a commitment__可密特ment__ to bear, together with all those who were living through the same history, the misery and the hope we shared.
These men, who were born at the beginning of the First World War, who were twenty when Hitler came to power and the first revolutionary() trials(试用)__try呕四__ were beginning, who were then confronted() as a completion of their education with the Spanish Civil War, the Second World War, the world of concentration()__康渗催迅__ camps, a Europe of torture()__拖却__ and prisons__普瑞震自__ these men must today rear(后)__瑞二__ their sons and create their works in a world threatened() by nuclear destruction().
Nobody, I think, can ask them to be optimists(乐观主义者)__哦铺剃密四自__.
And I even think that we should understand without ceasing(停止)__C-sing__ to fight it the error of those who in an excess(多余的) of despair(绝望) have asserted(断言)__鹅奢剃的__ their right to dishonour and have rushed into the nihilism of the era()__亿弱啊__.
But the fact remains that most of us, in my country and in Europe, have refused this nihilism and have engaged(订婚了) upon a quest(追求) for legitimacy(合法性)__里巨剃马see__.
They have had to forge()__for巨__ for themselves an art of living in times of catastrophe(灾难)__可他色特废__ in order to be born a second time and to fight openly against the instinct(本能)__因死停(新余)克特__ of death at work in our history.
Each generation doubtless() feels called upon to reform the world.
Mine knows that it will not reform it, but its task is perhaps even greater.
It consists__肯see四自__ in preventing(防止) the world from destroying itself.
Heir()__医生检查口腔(4声)__ to a corrupt(腐败的)__可（撸啊）[快连]普特__ history, in which are mingled()__民(1)购的__ fallen revolutions, technology gone mad, dead gods, and worn(穿)__沃摁__-out ideologies, where mediocre()__咪地欧克__ powers can destroy all yet no longer know how to convince(说服)__肯问四__, where intelligence has debased(贬值) itself to become the servant(仆人)__奢问特__ of hatred() and oppression(), this generation starting from its own negations(否定) has had to re-establish, both within and without, a little of that which constitutes(构成) the dignity(尊严)__的哥逆剃__ of life and death.
In a world threatened() by disintegration(解体), in which our grand inquisitors(确)__赢亏着特四__ run the risk of establishing forever the kingdom of death, it knows that it should, in an insane race against the clock, restore among the nations a peace that is not servitude(奴役)__奢为tude__, reconcile()__蜕(新余)啃赛欧(4)__ anew(重新) labour()__勒bo(4声)__ and culture, and remake with all men the Ark of the Covenant(约)__咔沃嫩特__.
It is not certain that this generation will ever be able to accomplish(完成)__啊(2声)康普利絮__ this immense()__引men四__ task, but already it is rising everywhere in the world to the double challenge of truth and liberty(自由)__粒波剃__ and, if necessary, knows how to die for it without hate.
Wherever it is found, it deserves to be saluted(敬礼) and encouraged, particularly__婆踢Q勒利__ where it is sacrificing()__杀可瑞fine性(新余)__ itself.
In any event, certain of your complete approval(批准), it is to this generation that I should like to pass on the honour that you have just given me.
At the same time, after having outlined(概述了) the nobility()__no biu了剃__ of the writers craft, I should have put him in his proper__普咯破__ place.
He has no other claims(索赔)__可累木自__ but those which he shares with his comrades(同志们)__康木瑞自__ in arms: vulnerable but obstinate()__啊不四内特__, unjust but impassioned(慷慨激昂的) for justice, doing his work without shame or pride in view of everybody, not ceasing(停止)__C-sing__ to be divided(划分)__迪歪地的__ between sorrow and beauty, and devoted() finally to drawing(画)__拽(4声)硬__ from his double existence the creations that he obstinately() tries to erect(勃起的)__衣rect__ in the destructive() movement of history.
Who after all this can expect from him complete solutions and high morals(道德)?
Truth is mysterious(神秘的)__米四特(1)瑞饿死__, elusive(难以捉摸的)__以撸c误__, always to be conquered().
Liberty(自由)__粒波剃__ is dangerous, as hard to live with as it is elating(得意的)__鹅勒停(新余)__.
We must march toward these two goals, painfully(痛苦的) but resolutely(), certain in advance of our failings(失败) on so long a road.
What writer would from now on in good conscience dare(敢) set himself up as a preacher(牧师)__普瑞缺二__ of virtue(美德)__窝臭(新余话)__?
For myself, I must state once more that I am not of this kind.
I have never been able to renounce() the light, the pleasure of being, and the freedom in which I grew__古路__ up.
But although this nostalgia(怀旧之情)__谐音-那是他家啊__ explains many of my errors and my faults, it has doubtless() helped me toward a better understanding of my craft.
It is helping me still to support unquestioningly(毫无疑问地) all those silent men who sustain(维持)__杀肆tain__ the life made for them in the world only through memory of the return of brief and free happiness.
Thus reduced to what I really am, to my limits and debts as well as to my difficult creed(信条)__可瑞的__, I feel freer()__福瑞二__, in concluding(结论), to comment upon the extent and the generosity()__gene弱四剃__ of the honour you have just bestowed(赋予)__bes透的__ upon me, freer()__福瑞二__ also to tell you that I would receive it as an homage() rendered to all those who, sharing in the same fight, have not received any privilege__普入爱沃乐巨__, but have on the contrary(相反)__肯缺瑞__ known misery and persecution().
It remains for me to thank you from the bottom of my heart and to make before you publicly, as a personal sign of my gratitude(感激之情)__葛入啊剃臭(新余)的__, the same and ancient(古老的)__an神(新余)特__ promise of faithfulness() which every true artist repeats to himself in silence every day."""

# repleace_word_by_pronunciation(to_be_handle, pronunciation_text)

cn = """陈词滥调很便宜。我们都听过一些组织说，他们致力于“多样性”和“宽容”，但从未具体说明，因此我们的立场如下：
我们欢迎你。
我们欢迎任何性别认同或表达、种族、肤色、种族、年龄、体型、国籍、性取向、能力水平、神经类型、宗教、老年人身份、家庭结构、文化、亚文化、政治观点、教育水平、身份和自我认同的人。我们欢迎活动家、艺术家、博客作者、工匠、程序员、潜在的程序员、设计师、企业家、文档作者、记者、系统管理员、教师、普通人、非凡的人，以及介于两者之间的每一个人。
我们欢迎你。你可以戴婴儿吊带、头巾、基帕、皮革、XXXL t恤、五角星、政治徽章、彩虹、念珠、纹身或我们只能梦想的东西。你可以随身携带一把吉他、一根手杖或一台15岁的笔记本电脑。保守主义或自由主义、自由主义或社会主义-我们相信，所有观点和信仰的人都有可能走到一起，相互学习。我们相信广泛的个人和集体经验以及所有人固有的尊严。我们相信，当来自不同世界和不同世界观的人相互接近创造对话时，会发生惊人的事情。
我们对网络开发感到兴奋-从专业到业余，从大型项目到简单的应用程序，从堪萨斯州构思Django的那一天起就一直在做这项工作的程序员，到今天刚刚开始学习Django教程的新手。
我们认为残疾人的无障碍是一个优先事项，而不是事后考虑。我们认为神经多样性是一种特征，而不是一种缺陷。我们相信包容、欢迎和支持任何带着诚意和建设社区愿望来到我们这里的人。
Django社区有一些多样性倡议，但总可以有更多。我们通过我们的行为准则和应用该准则的团队来保护我们的多样性。我们还呼吁你，作为Django社区的一员，自豪地表示支持。慷慨、理解和尊重你的Djangonauts同伴。寻找新来者，帮助他们感觉自己属于自己。当有人有不同的观点时，以同理心倾听。如果你注意到事情可能会更好，就和别人谈谈。
我们有足够的经验知道，我们不会在第一次尝试时得到任何完美的结果。但我们有足够的希望、精力和理想主义去学习我们现在不知道的东西。我们可能无法满足所有人，但我们肯定可以努力避免排斥任何人。我们承诺，如果我们弄错了，当你向我们指出错误时，我们会认真、尊重地倾听你的意见，我们会尽最大努力弥补我们的错误。
我们认为我们的技术经验很重要，但我们认为社区经验更重要。我们知道当组织说一件事做另一件事，或者他们什么都不说的时候会出什么问题。我们相信，保持Django软件基金会的透明性与保持我们的服务器稳定同样重要。
我们使用Django web框架，我们邀请每个人为Django核心代码、DjangoPackages生态系统和社区做出贡献。
来和我们一起建立网络。"""

# en = """Platitudes are cheap. We've all heard organizations say they're committed to "diversity" and "tolerance" without ever getting specific, so here's our stance on it:
#
# We welcome you.
#
# We welcome people of any gender identity or expression, race, skin color, ethnicity, age, size, nationality, sexual orientation, ability level, neurotype, religion, elder status, family structure, culture, subculture, political opinion, education level, identity, and self-identification. We welcome activists, artists, bloggers, crafters, coders, wannabe-coders, designers, entrepreneurs, documentation writers, journalists, sysadmins, teachers, ordinary people, extraordinary people, and everyone in between.
#
# We welcome you. You may wear a baby sling, hijab, a kippah, leather, an XXXL t-shirt, a pentacle, a political badge, a rainbow, a rosary, tattoos, or something we can only dream of. You may carry a guitar or walking cane or a 15 year old laptop. Conservative or liberal, libertarian or socialist — we believe it's possible for people of all viewpoints and persuasions to come together and learn from each other. We believe in the broad spectrum of individual and collective experience and in the inherent dignity of all people. We believe that amazing things happen when people from different worlds and world-views approach each other to create a conversation.
#
# We get excited about web development — from professional to amateur, from giant projects to simple apps, from the coder who's been doing this since the day Django was conceived in Kansas to the newbie who just started studying the Django tutorial today.
#
# We think accessibility for people with disabilities is a priority, not an afterthought. We think neurodiversity is a feature, not a bug. We believe in being inclusive, welcoming, and supportive of anyone who comes to us with good faith and the desire to build a community.
#
# There are a few diversity initiatives in the Django community, but there can always be more. We protect our diversity through our Code of Conduct and the team that applies it. We also call on you, as a member of the Django community, to proudly show your support. Be generous, understanding and respectful to your fellow Djangonauts. Seek out newcomers and help them feel like they belong. Listen with empathy when someone has a different perspective. Talk to someone if you notice that something could be better.
#
# We have enough experience to know that we won't get any of this perfect on the first try. But we have enough hope, energy, and idealism to want to learn things we don't know now. We may not be able to satisfy everyone, but we can certainly work to avoid excluding anyone. And we promise that if we get it wrong, we'll listen carefully and respectfully to you when you point it out to us, and we'll do our best to make good on our mistakes.
#
# We think our technical experience is important, but we think our community experience is more important. We know what goes wrong when organizations say one thing and do another, or when they refuse to say anything at all. We believe that keeping the Django Software Foundation transparent is just as important as keeping our servers stable.
#
# We work with the Django web framework, and we invite everyone to contribute, to the core Django code, the ecosystem of Django packages, and the community.
#
# Come build the web with us."""

en = """Platitudes() are cheap.
We've all heard organizations say they're committed to "diversity" and "tolerance(宽容)" without ever getting specific__死pe色(新余)飞(新余)扣__, so here's our stance(的立场)__屎蛋四__ on it: We welcome you.
We welcome people of any gender identity__癌灯(新余)特利__ or expression, race, skin color, ethnicity(种族), age, size, nationality, sexual orientation(), ability level, neurotype(neurotype)__妞肉type__, religion, elder status, family structure, culture, subculture, political(政治)__坡粒剃扣__ opinion, education level, identity__癌灯(新余)特利__, and self-identification(识别).
We welcome activists, artists, bloggers, crafters, coders, wannabe-coders, designers, entrepreneurs(企业家), documentation writers, journalists, sysadmins, teachers, ordinary people, extraordinary(非凡的) people, and everyone in between.
We welcome you.
You may wear a baby sling()__死令__, hijab(头巾), a kippah(kippah), leather(皮革)__追(新余)的__, an XXXL t-shirt, a pentacle(五角星形)__pen它扣__, a political(政治)__坡粒剃扣__ badge(徽章)__霸巨__, a rainbow, a rosary(念珠), tattoos, or something we can only dream of.
You may carry a guitar or walking cane(甘蔗)__K摁__ or a 15 year old laptop.
Conservative(保守的) or liberal()__粒波(4声)肉__, libertarian(自由意志主义) or socialist we believe it's possible for people of all viewpoints and persuasions(两人) to come together and learn from each other.
We believe in the broad spectrum() of individual__银地微就呕__ and collective experience and in the inherent(固有的)__赢he-rent__ dignity(尊严)__的哥逆剃__ of all people.
We believe that amazing things happen when people from different worlds and world-views approach(方法)__啊铺(4声)肉去误__ each other to create a conversation.
We get excited about web development from professional to amateur(业余)__啊骂特__, from giant__倦按特__ projects to simple apps, from the coder who's been doing this since the day Django was conceived(构思)__肯see误的__ in Kansas() to the newbie(新手)__牛(新余)毕__ who just started studying the Django tutorial today.
We think accessibility for people with disabilities is a priority__排哦(入爱)利__, not an afterthought.
We think neurodiversity(神经的多样性)__妞肉diversity__ is a feature__飞(新余)却__, not a bug.
We believe in being inclusive, welcoming, and supportive(支持) of anyone who comes to us with good faith__废四__ and the desire to build a community.
There are a few diversity initiatives in the Django community, but there can always be more.
We protect our diversity through our Code of Conduct and the team that applies it.
We also call on you, as a member of the Django community, to proudly show your support.
Be generous(慷慨的), understanding and respectful to your fellow Djangonauts().
Seek out newcomers and help them feel like they belong.
Listen with empathy(同理心) when someone has a different perspective(的角度来看)__泼四趴克剃误__.
Talk to someone if you notice that something could be better.
We have enough experience to know that we won't get any of this perfect on the first try.
But we have enough hope, energy, and idealism to want to learn things we don't know now.
We may not be able to satisfy everyone, but we can certainly work to avoid excluding anyone.
And we promise that if we get it wrong, we'll listen carefully and respectfully to you when you point it out to us, and we'll do our best to make good on our mistakes.
We think our technical experience is important, but we think our community experience is more important.
We know what goes wrong when organizations say one thing and do another, or when they refuse to say anything at all.
We believe that keeping the Django Software Foundation__方得(新余)迅__ transparent__犬四趴软(4声)特__ is just as important as keeping our servers stable.
We work with the Django web framework, and we invite__引外特__ everyone to contribute, to the core Django code, the ecosystem of Django packages, and the community.
Come build the web with us."""

cn = """一个幽灵，共产主义的幽灵，在欧洲游荡。为了对这个幽灵进行神圣的围剿，旧欧洲的一切势力，教皇和沙皇、梅特涅和基佐、法国的激进派和德国的警察，都联合起来了。

　　有哪一个反对党不被它的当政的敌人骂为共产党呢？又有哪一个反对党不拿共产主义这个罪名去回敬更进步的反对党人和自己的反动敌人呢？

　　从这一事实中可以得出两个结论：

　　共产主义已经被欧洲的一切势力公认为一种势力；

　　现在是共产党人向全世界公开说明自己的观点、自己的目的、自己的意图并且拿党自己的宣言来反驳关于共产主义幽灵的神话的时候了。

　　为了这个目的，各国共产党人集会于伦敦，拟定了如下的宣言，用英文、法文、德文、意大利文、弗拉芒文和丹麦文公布于世。"""

en = """A spectre is haunting Europe — the spectre of communism. All the powers of old Europe have entered into a holy alliance to exorcise this spectre: Pope and Tsar, Metternich and Guizot, French Radicals and German police-spies.

Where is the party in opposition that has not been decried as communistic by its opponents in power? Where is the opposition that has not hurled back the branding reproach of communism, against the more advanced opposition parties, as well as against its reactionary adversaries?

Two things result from this fact:

I, Communism is already acknowledged by all European powers to be itself a power,

II, It is high time that Communists should openly, in the face of the whole world, publish their views, their aims, their tendencies, and meet this nursery tale of the Spectre of Communism with a manifesto of the party itself.

To this end, Communists of various nationalities have assembled in London and sketched the following manifesto, to be published in the English, French, German, Italian, Flemish and Danish languages."""

# repleace_word_by_pronunciation(to_be_handle_2, pronunciation_text_2)

cn = """至今一切社会的历史都是阶级斗争的历史。

　　自由民和奴隶、贵族和平民、领主和农奴、行会师傅和帮工，一句话，压迫者和被压迫者，始终处于相互对立的地位，进行不断的、有时隐蔽有时公开的斗争，而每一次斗争的结局都是整个社会受到革命改造或者斗争的各阶级同归于尽。

　　在过去的各个历史时代，我们几乎到处都可以看到社会完全划分为各个不同的等级，看到社会地位分成多种多样的层次。在古罗马，有贵族、骑士、平民、奴隶，在中世纪，有封建主、臣仆、行会师傅、帮工、农奴，而且几乎在每一个阶级内部又有一些特殊的阶层。

　　从封建社会的灭亡中产生出来的现代资产阶级社会并没有消灭阶级对立。它只是用新的阶级、新的压迫条件、新的斗争形式代替了旧的。

　　但是，我们的时代，资产阶级时代，却有一个特点：它使阶级对立简单化了。整个社会日益分裂为两大敌对的阵营，分裂为两大相互直接对立的阶级：资产阶级和无产阶级。

　　从中世纪的农奴中产生了初期城市的城关市民；从这个市民等级中发展出最初的资产阶级分子。

　　美洲的发现、绕过非洲的航行，给新兴的资产阶级开辟了新天地。东印度和中国的市场、美洲的殖民化、对殖民地的贸易、交换手段和一般商品的增加，使商业、航海业和工业空前高涨，因而使正在崩溃的封建社会内部的革命因素迅速发展。

　　以前那种封建的或行会的工业经营方式已经不能满足随着新市场的出现而增加的需求了。工场手工业代替了这种经营方式。行会师傅被工业的中间等级排挤掉了；各种行业组织之间的分工随着各个作坊内部的分工的出现而消失了。

　　但是，市场总是在扩大，需求总是在增加。甚至工场手工业也不再能满足需要了。于是，蒸汽和机器引起了工业生产的革命。现代大工业代替了工场手工业；工业中的百万富翁，一支一支产业大军的首领，现代资产者，代替了工业的中间等级。

　　大工业建立了由美洲的发现所准备好的世界市场。世界市场使商业、航海业和陆路交通得到了巨大的发展。这种发展又反过来促进了工业的扩展。同时，随着工业、商业、航海业和铁路的扩展，资产阶级也在同一程度上得到发展，增加自己的资本，把中世纪遗留下来的一切阶级排挤到后面去。

　　由此可见，现代资产阶级本身是一个长期发展过程的产物，是生产方式和交换方式的一系列变革的产物。

　　资产阶级的这种发展的每一个阶段，都伴随着相应的政治上的进展。它在封建主统治下是被压迫的等级，在公社里是武装的和自治的团体，在一些地方组成独立的城市共和国，在另一些地方组成君主国中的纳税的第三等级；后来，在工场手工业时期，它是等级君主国或专制君主国中同贵族抗衡的势力，而且是大君主国的主要基础；最后，从大工业和世界市场建立的时候起，它在现代的代议制国家里夺得了独占的政治统治。现代的国家政权不过是管理整个资产阶级的共同事务的委员会罢了。

　　资产阶级在历史上曾经起过非常革命的作用。

　　资产阶级在它已经取得了统治的地方把一切封建的、宗法的和田园般的关系都破坏了。它无情地斩断了把人们束缚于天然尊长的形形色色的封建羁绊，它使人和人之间除了赤裸裸的利害关系，除了冷酷无情的“现金交易”，就再也没有任何别的联系了。它把宗教虔诚、骑士热忱、小市民伤感这些情感的神圣发作，淹没在利己主义打算的冰水之中。它把人的尊严变成了交换价值，用一种没有良心的贸易自由代替了无数特许的和自力挣得的自由。总而言之，它用公开的、无耻的、直接的、露骨的剥削代替了由宗教幻想和政治幻想掩盖着的剥削。

　　资产阶级抹去了一切向来受人尊崇和令人敬畏的职业的神圣光环。它把医生、律师、教士、诗人和学者变成了它出钱招雇的雇佣劳动者。

　　资产阶级撕下了罩在家庭关系上的温情脉脉的面纱，把这种关系变成了纯粹的金钱关系。

　　资产阶级揭示了，在中世纪深受反动派称许的那种人力的野蛮使用，是以极端怠惰作为相应补充的。它第一个证明了，人的活动能够取得什么样的成就。它创造了完全不同于埃及金字塔、罗马水道和哥特式教堂的奇迹；它完成了完全不同于民族大迁徙和十字军征讨的远征。

　　资产阶级除非对生产工具，从而对生产关系，从而对全部社会关系不断地进行革命，否则就不能生存下去。反之，原封不动地保持旧的生产方式，却是过去的一切工业阶级生存的首要条件。生产的不断变革，一切社会状况不停的动荡，永远的不安定和变动，这就是资产阶级时代不同于过去一切时代的地方。一切固定的僵化的关系以及与之相适应的素被尊崇的观念和见解都被消除了，一切新形成的关系等不到固定下来就陈旧了。一切等级的和固定的东西都烟消云散了，一切神圣的东西都被亵渎了。人们终于不得不用冷静的眼光来看他们的生活地位、他们的相互关系。

　　不断扩大产品销路的需要，驱使资产阶级奔走于全球各地。它必须到处落户，到处开发，到处建立联系。

　　资产阶级，由于开拓了世界市场，使一切国家的生产和消费都成为世界性的了。使反动派大为惋惜的是，资产阶级挖掉了工业脚下的民族基础。古老的民族工业被消灭了，并且每天都还在被消灭。它们被新的工业排挤掉了，新的工业的建立已经成为一切文明民族的生命攸关的问题；这些工业所加工的，已经不是本地的原料，而是来自极其遥远的地区的原料；它们的产品不仅供本国消费，而且同时供世界各地消费。旧的、靠本国产品来满足的需要，被新的、要靠极其遥远的国家和地带的产品来满足的需要所代替了。过去那种地方的和民族的自给自足和闭关自守状态，被各民族的各方面的互相往来和各方面的互相依赖所代替了。物质的生产是如此，精神的生产也是如此。各民族的精神产品成了公共的财产。民族的片面性和局限性日益成为不可能，于是由许多种民族的和地方的文学形成了一种世界的文学。

　　资产阶级，由于一切生产工具的迅速改进，由于交通的极其便利，把一切民族甚至最野蛮的民族都卷到文明中来了。它的商品的低廉价格，是它用来摧毁一切万里长城、征服野蛮人最顽强的仇外心理的重炮。它迫使一切民族——如果它们不想灭亡的话——采用资产阶级的生产方式；它迫使它们在自己那里推行所谓的文明，即变成资产者。一句话，它按照自己的面貌为自己创造出一个世界。

　　资产阶级使农村屈服于城市的统治。它创立了巨大的城市，使城市人口比农村人口大大增加起来，因而使很大一部分居民脱离了农村生活的愚昧状态。正像它使农村从属于城市一样，它使未开化和半开化的国家从属于文明的国家，使农民的民族从属于资产阶级的民族，使东方从属于西方。

　　资产阶级日甚一日地消灭生产资料、财产和人口的分散状态。它使人口密集起来，使生产资料集中起来，使财产聚集在少数人的手里。由此必然产生的结果就是政治的集中。各自独立的、几乎只有同盟关系的、各有不同利益、不同法律、不同政府、不同关税的各个地区，现在已经结合为一个拥有统一的政府、统一的法律、统一的民族阶级利益和统一的关税的统一的民族。

　　资产阶级在它的不到一百年的阶级统治中所创造的生产力，比过去一切世代创造的全部生产力还要多，还要大。自然力的征服，机器的采用，化学在工业和农业中的应用，轮船的行驶，铁路的通行，电报的使用，整个整个大陆的开垦，河川的通航，仿佛用法术从地下呼唤出来的大量人口，——过去哪一个世纪料想到在社会劳动里蕴藏有这样的生产力呢？

　　由此可见，资产阶级赖以形成的生产资料和交换手段，是在封建社会里造成的。在这些生产资料和交换手段发展的一定阶段上，封建社会的生产和交换在其中进行的关系，封建的农业和工场手工业组织，一句话，封建的所有制关系，就不再适应已经发展的生产力了。这种关系已经在阻碍生产而不是促进生产了。它变成了束缚生产的桎梏。它必须被炸毁，它已经被炸毁了。

　　起而代之的是自由竞争以及与自由竞争相适应的社会制度和政治制度、资产阶级的经济统治和政治统治。

　　现在，我们眼前又进行着类似的运动。资产阶级的生产关系和交换关系，资产阶级的所有制关系，这个曾经仿佛用法术创造了如此庞大的生产资料和交换手段的现代资产阶级社会，现在像一个魔法师一样不能再支配自己用法术呼唤出来的魔鬼了。几十年来的工业和商业的历史，只不过是现代生产力反抗现代生产关系、反抗作为资产阶级及其统治的存在条件的所有制关系的历史。只要指出在周期性的重复中越来越危及整个资产阶级社会生存的商业危机就够了。在商业危机期间，总是不仅有很大一部分制成的产品被毁灭掉，而且有很大一部分已经造成的生产力被毁灭掉。在危机期间，发生一种在过去一切时代看来都好像是荒唐现象的社会瘟疫，即生产过剩的瘟疫。社会突然发现自己回到了一时的野蛮状态；仿佛是一次饥荒、一场普遍的毁灭性战争，使社会失去了全部生活资料；仿佛是工业和商业全被毁灭了，——这是什么缘故呢？因为社会上文明过度，生活资料太多，工业和商业太发达。社会所拥有的生产力已经不能再促进资产阶级文明和资产阶级所有制关系的发展；相反，生产力已经强大到这种关系所不能适应的地步，它已经受到这种关系的阻碍；而它一着手克服这种障碍，就使整个资产阶级社会陷入混乱，就使资产阶级所有制的存在受到威胁。资产阶级的关系已经太狭窄了，再容纳不了它本身所造成的财富了。——资产阶级用什么办法来克服这种危机呢？一方面不得不消灭大量生产力，另一方面夺取新的市场，更加彻底地利用旧的市场。这究竟是怎样的一种办法呢？这不过是资产阶级准备更全面更猛烈的危机的办法，不过是使防止危机的手段越来越少的办法。

　　资产阶级用来推翻封建制度的武器，现在却对准资产阶级自己了。

　　但是，资产阶级不仅锻造了置自身于死地的武器；它还产生了将要运用这种武器的人——现代的工人，即无产者。

　　随着资产阶级即资本的发展，无产阶级即现代工人阶级也在同一程度上得到发展；现代的工人只有当他们找到工作的时候才能生存，而且只有当他们的劳动增殖资本的时候才能找到工作。这些不得不把自己零星出卖的工人，像其他任何货物一样，也是一种商品，所以他们同样地受到竞争的一切变化、市场的一切波动的影响。

　　由于推广机器和分工，无产者的劳动已经失去了任何独立的性质，因而对工人也失去了任何吸引力。工人变成了机器的单纯的附属品，要求他做的只是极其简单、极其单调和极容易学会的操作。因此，花在工人身上的费用，几乎只限于维持工人生活和延续工人后代所必需的生活资料。但是，商品的价格，从而劳动的价格，是同它的生产费用相等的。因此，劳动越使人感到厌恶，工资也就越少。不仅如此，机器越推广，分工越细致，劳动量出就越增加，这或者是由于工作时间的延长，或者是由于在一定时间内所要求的劳动的增加，机器运转的加速，等等。

　　现代工业已经把家长式的师傅的小作坊变成了工业资本家的大工厂。挤在工厂里的工人群众就像士兵一样被组织起来。他们是产业军的普通士兵，受着各级军士和军官的层层监视。他们不仅仅是资产阶级的、资产阶级国家的奴隶，他们每日每时都受机器、受监工、首先是受各个经营工厂的资产者本人的奴役。这种专制制度越是公开地把营利宣布为自己的最终目的，它就越是可鄙、可恨和可恶。

　　手的操作所要求的技巧和气力越少，换句话说，现代工业越发达，男工也就越受到女工和童工的排挤。对工人阶级来说，性别和年龄的差别再没有什么社会意义了。他们都只是劳动工具，不过因为年龄和性别的不同而需要不同的费用罢了。

　　当厂主对工人的剥削告一段落，工人领到了用现钱支付的工资的时候，马上就有资产阶级中的另一部分人——房东、小店主、当铺老板等等向他们扑来。

　　以前的中间等级的下层，即小工业家、小商人和小食利者，手工业者和农民——所有这些阶级都降落到无产阶级的队伍里来了，有的是因为他们的小资本不足以经营大工业，经不起较大的资本家的竞争；有的是因为他们的手艺已经被新的生产方法弄得不值钱了。无产阶级就是这样从居民的所有阶级中得到补充的。

　　无产阶级经历了各个不同的发展阶段。它反对资产阶级的斗争是和它的存在同时开始的。

　　最初是单个的工人，然后是某一工厂的工人，然后是某一地方的某一劳动部门的工人，同直接剥削他们的单个资产者作斗争。他们不仅仅攻击资产阶级的生产关系，而且攻击生产工具本身；他们毁坏那些来竞争的外国商品，捣毁机器，烧毁工厂，力图恢复已经失去的中世纪工人的地位。

　　在这个阶段上，工人是分散在全国各地并为竞争所分裂的群众。工人的大规模集结，还不是他们自己联合的结果，而是资产阶级联合的结果，当时资产阶级为了达到自己的政治目的必须而且暂时还能够把整个无产阶级发动起来。因此，在这个阶段上，无产者不是同自己的敌人作斗争，而是同自己的敌人的敌人作斗争，即同专制君主制的残余、地主、非工业资产者和小资产者作斗争。因此，整个历史运动都集中在资产阶级手里；在这种条件下取得的每一个胜利都是资产阶级的胜利。

　　但是，随着工业的发展，无产阶级不仅人数增加了，而且它结合成更大的集体，它的力量日益增长，它越来越感觉到自己的力量。机器使劳动的差别越来越小，使工资几乎到处都降到同样低的水平，因而无产阶级内部的利益、生活状况也越来越趋于一致。资产者彼此间日益加剧的竞争以及由此引起的商业危机，使工人的工资越来越不稳定；机器的日益迅速的和继续不断的改良，使工人的整个生活地位越来越没有保障；单个工人和单个资产者之间的冲突越来越具有两个阶级的冲突的性质。工人开始成立反对资产者的同盟；他们联合起来保卫自己的工资。他们甚至建立了经常性的团体，以便为可能发生的反抗准备食品。有些地方，斗争爆发为起义。

　　工人有时也得到胜利，但这种胜利只是暂时的。他们斗争的真正成果并不是直接取得的成功，而是工人的越来越扩大的联合。这种联合由于大工业所造成的日益发达的交通工具而得到发展，这种交通工具把各地的工人彼此联系起来。只要有了这种联系，就能把许多性质相同的地方性的斗争汇合成全国性的斗争，汇合成阶级斗争。而一切阶级斗争都是政治斗争。中世纪的市民靠乡间小道需要几百年才能达到的联合，现代的无产者利用铁路只要几年就可以达到了。

　　无产者组织成为阶级，从而组织成为政党这件事，不断地由于工人的自相竞争而受到破坏。但是，这种组织总是重新产生，并且一次比一次更强大，更坚固，更有力。它利用资产阶级内部的分裂，迫使他们用法律形式承认工人的个别利益。英国的十小时工作日法案就是一个例子。

　　旧社会内部的所有冲突在许多方面都促进了无产阶级的发展。资产阶级处于不断的斗争中：最初反对贵族；后来反对同工业进步有利害冲突的那部分资产阶级；经常反对一切外国的资产阶级。在这一切斗争中，资产阶级都不得不向无产阶级呼吁，要求无产阶级援助，这样就把无产阶级卷进了政治运动。于是，资产阶级自己就把自己的教育因素即反对自身的武器给予了无产阶级。

　　其次，我们已经看到，工业的进步把统治阶级的整批成员抛到无产阶级队伍里去，或者至少也使他们的生活条件受到威胁。他们也给无产阶级带来了大量的教育因素。

　　最后，在阶级斗争接近决战的时期，统治阶级内部的、整个旧社会内部的瓦解过程，就达到非常强烈、非常尖锐的程度，甚至使得统治阶级中的一小部分人脱离统治阶级而归附于革命的阶级，即掌握着未来的阶级。所以，正像过去贵族中有一部分人转到资产阶级方面一样，现在资产阶级中也有一部分人，特别是已经提高到从理论上认识整个历史运动这一水平的一部分资产阶级思想家，转到无产阶级方面来了。

　　在当前同资产阶级对立的一切阶级中，只有无产阶级是真正革命的阶级。其余的阶级都随着大工业的发展而日趋没落和灭亡，无产阶级却是大工业本身的产物。

　　中间等级，即小工业家、小商人、手工业者、农民，他们同资产阶级作斗争，都是为了维护他们这种中间等级的生存，以免于灭亡。所以，他们不是革命的，而是保守的。不仅如此，他们甚至是反动的，因为他们力图使历史的车轮倒转。如果说他们是革命的，那是鉴于他们行将转入无产阶级的队伍，这样，他们就不是维护他们目前的利益，而是维护他们将来的利益，他们就离开自己原来的立场，而站到无产阶级的立场上来。

　　流氓无产阶级是旧社会最下层中消极的腐化的部分，他们在一些地方也被无产阶级革命卷到运动里来，但是，由于他们的整个生活状况，他们更甘心于被人收买，去干反动的勾当。

　　在无产阶级的生活条件中，旧社会的生活条件已经被消灭了。无产者是没有财产的；他们和妻子儿女的关系同资产阶级的家庭关系再没有任何共同之处了；现代的工业劳动，现代的资本压迫，无论在英国或法国，无论在美国或德国，都是一样的，都使无产者失去了任何民族性。法律、道德、宗教在他们看来全都是资产阶级偏见，隐藏在这些偏见后面的全都是资产阶级利益。

　　过去一切阶级在争得统治之后，总是使整个社会服从于它们发财致富的条件，企图以此来巩固它们已获得的生活地位。无产者只有废除自己的现存的占有方式，从而废除全部现存的占有方式，才能取得社会生产力。无产者没有什么自己的东西必须加以保护，他们必须摧毁至今保护和保障私有财产的一切。

　　过去的一切运动都是少数人的或者为少数人谋利益的运动。无产阶级的运动是绝大多数人的、为绝大多数人谋利益的独立的运动。无产阶级，现今社会的最下层，如果不炸毁构成官方社会的整个上层，就不能抬起头来，挺起胸来。

　　如果不就内容而就形式来说，无产阶级反对资产阶级的斗争首先是一国范围内的斗争。每一个国家的无产阶级当然首先应该打倒本国的资产阶级。

　　在叙述无产阶级发展的最一般的阶段的时候，我们循序探讨了现存社会内部或多或少隐蔽着的国内战争，直到这个战争爆发为公开的革命，无产阶级用暴力推翻资产阶级而建立自己的统治。

　　我们已经看到，至今的一切社会都是建立在压迫阶级和被压迫阶级的对立之上的。但是，为了有可能压迫一个阶级，就必须保证这个阶级至少有能够勉强维持它的奴隶般的生存的条件。农奴曾经在农奴制度下挣扎到公社成员的地位，小资产者曾经在封建专制制度的束缚下挣扎到资产者的地位。现代的工人却相反，他们并不是随着工业的进步而上升，而是越来越降到本阶级的生存条件以下。工人变成赤贫者，贫困比人口和财富增长得还要快。由此可以明显地看出，资产阶级再不能做社会的统治阶级了，再不能把自己阶级的生存条件当作支配一切的规律强加于社会了。资产阶级不能统治下去了，因为它甚至不能保证自己的奴隶维持奴隶的生活，因为它不得不让自己的奴隶落到不能养活它反而要它来养活的地步。社会再不能在它统治下生存下去了，就是说，它的生存不再同社会相容了。

　　资产阶级生存和统治的根本条件，是财富在私人手里的积累，是资本的形成和增殖；资本的条件是雇佣劳动。雇佣劳动完全是建立在工人的自相竞争之上的。资产阶级无意中造成而又无力抵抗的工业进步，使工人通过结社而达到的革命联合代替了他们由于竞争而造成的分散状态。于是，随着大工业的发展，资产阶级赖以生产和占有产品的基础本身也就从它的脚下被挖掉了。它首先生产的是它自身的掘墓人。资产阶级的灭亡和无产阶级的胜利是同样不可避免的。"""

en = """The history of all hitherto existing societies is the history of class
struggles.

Freeman and slave, patrician and plebeian, lord and serf, guild-master
and journeyman, in a word, oppressor and oppressed, stood in constant
opposition to one another, carried on an uninterrupted, now hidden, now
open fight, a fight that each time ended, either in a revolutionary
re-constitution of society at large, or in the common ruin of the
contending classes.

In the earlier epochs of history, we find almost everywhere a
complicated arrangement of society into various orders, a manifold
gradation of social rank. In ancient Rome we have patricians, knights,
plebeians, slaves; in the Middle Ages, feudal lords, vassals,
guild-masters, journeymen, apprentices, serfs; in almost all of these
classes, again, subordinate gradations.

The modern bourgeois society that has sprouted from the ruins of feudal
society has not done away with class antagonisms. It has but
established new classes, new conditions of oppression, new forms of
struggle in place of the old ones. Our epoch, the epoch of the
bourgeoisie, possesses, however, this distinctive feature: it has
simplified the class antagonisms. Society as a whole is more and more
splitting up into two great hostile camps, into two great classes,
directly facing each other: Bourgeoisie and Proletariat.

From the serfs of the Middle Ages sprang the chartered burghers of the
earliest towns. From these burgesses the first elements of the
bourgeoisie were developed.

The discovery of America, the rounding of the Cape, opened up fresh
ground for the rising bourgeoisie. The East-Indian and Chinese markets,
the colonisation of America, trade with the colonies, the increase in
the means of exchange and in commodities generally, gave to commerce,
to navigation, to industry, an impulse never before known, and thereby,
to the revolutionary element in the tottering feudal society, a rapid
development.

The feudal system of industry, under which industrial production was
monopolised by closed guilds, now no longer sufficed for the growing
wants of the new markets. The manufacturing system took its place. The
guild-masters were pushed on one side by the manufacturing middle
class; division of labour between the different corporate guilds
vanished in the face of division of labour in each single workshop.

Meantime the markets kept ever growing, the demand ever rising. Even
manufacture no longer sufficed. Thereupon, steam and machinery
revolutionised industrial production. The place of manufacture was
taken by the giant, Modern Industry, the place of the industrial middle
class, by industrial millionaires, the leaders of whole industrial
armies, the modern bourgeois.

Modern industry has established the world-market, for which the
discovery of America paved the way. This market has given an immense
development to commerce, to navigation, to communication by land. This
development has, in its time, reacted on the extension of industry; and
in proportion as industry, commerce, navigation, railways extended, in
the same proportion the bourgeoisie developed, increased its capital,
and pushed into the background every class handed down from the Middle
Ages.

We see, therefore, how the modern bourgeoisie is itself the product of
a long course of development, of a series of revolutions in the modes
of production and of exchange.

Each step in the development of the bourgeoisie was accompanied by a
corresponding political advance of that class. An oppressed class under
the sway of the feudal nobility, an armed and self-governing
association in the mediaeval commune; here independent urban republic
(as in Italy and Germany), there taxable “third estate” of the monarchy
(as in France), afterwards, in the period of manufacture proper,
serving either the semi-feudal or the absolute monarchy as a
counterpoise against the nobility, and, in fact, corner-stone of the
great monarchies in general, the bourgeoisie has at last, since the
establishment of Modern Industry and of the world-market, conquered for
itself, in the modern representative State, exclusive political sway.
The executive of the modern State is but a committee for managing the
common affairs of the whole bourgeoisie.

The bourgeoisie, historically, has played a most revolutionary part.

The bourgeoisie, wherever it has got the upper hand, has put an end to
all feudal, patriarchal, idyllic relations. It has pitilessly torn
asunder the motley feudal ties that bound man to his “natural
superiors,” and has left remaining no other nexus between man and man
than naked self-interest, than callous “cash payment.” It has drowned
the most heavenly ecstasies of religious fervour, of chivalrous
enthusiasm, of philistine sentimentalism, in the icy water of
egotistical calculation. It has resolved personal worth into exchange
value, and in place of the numberless and indefeasible chartered
freedoms, has set up that single, unconscionable freedom—Free Trade. In
one word, for exploitation, veiled by religious and political
illusions, naked, shameless, direct, brutal exploitation.

The bourgeoisie has stripped of its halo every occupation hitherto
honoured and looked up to with reverent awe. It has converted the
physician, the lawyer, the priest, the poet, the man of science, into
its paid wage labourers.

The bourgeoisie has torn away from the family its sentimental veil, and
has reduced the family relation to a mere money relation.

The bourgeoisie has disclosed how it came to pass that the brutal
display of vigour in the Middle Ages, which Reactionists so much
admire, found its fitting complement in the most slothful indolence. It
has been the first to show what man’s activity can bring about. It has
accomplished wonders far surpassing Egyptian pyramids, Roman aqueducts,
and Gothic cathedrals; it has conducted expeditions that put in the
shade all former Exoduses of nations and crusades.

The bourgeoisie cannot exist without constantly revolutionising the
instruments of production, and thereby the relations of production, and
with them the whole relations of society. Conservation of the old modes
of production in unaltered form, was, on the contrary, the first
condition of existence for all earlier industrial classes. Constant
revolutionising of production, uninterrupted disturbance of all social
conditions, everlasting uncertainty and agitation distinguish the
bourgeois epoch from all earlier ones. All fixed, fast-frozen
relations, with their train of ancient and venerable prejudices and
opinions, are swept away, all new-formed ones become antiquated before
they can ossify. All that is solid melts into air, all that is holy is
profaned, and man is at last compelled to face with sober senses, his
real conditions of life, and his relations with his kind.

The need of a constantly expanding market for its products chases the
bourgeoisie over the whole surface of the globe. It must nestle
everywhere, settle everywhere, establish connexions everywhere.

The bourgeoisie has through its exploitation of the world-market given
a cosmopolitan character to production and consumption in every
country. To the great chagrin of Reactionists, it has drawn from under
the feet of industry the national ground on which it stood. All
old-established national industries have been destroyed or are daily
being destroyed. They are dislodged by new industries, whose
introduction becomes a life and death question for all civilised
nations, by industries that no longer work up indigenous raw material,
but raw material drawn from the remotest zones; industries whose
products are consumed, not only at home, but in every quarter of the
globe. In place of the old wants, satisfied by the productions of the
country, we find new wants, requiring for their satisfaction the
products of distant lands and climes. In place of the old local and
national seclusion and self-sufficiency, we have intercourse in every
direction, universal inter-dependence of nations. And as in material,
so also in intellectual production. The intellectual creations of
individual nations become common property. National one-sidedness and
narrow-mindedness become more and more impossible, and from the
numerous national and local literatures, there arises a world
literature.

The bourgeoisie, by the rapid improvement of all instruments of
production, by the immensely facilitated means of communication, draws
all, even the most barbarian, nations into civilisation. The cheap
prices of its commodities are the heavy artillery with which it batters
down all Chinese walls, with which it forces the barbarians’ intensely
obstinate hatred of foreigners to capitulate. It compels all nations,
on pain of extinction, to adopt the bourgeois mode of production; it
compels them to introduce what it calls civilisation into their midst,
_i.e_., to become bourgeois themselves. In one word, it creates a world
after its own image.

The bourgeoisie has subjected the country to the rule of the towns. It
has created enormous cities, has greatly increased the urban population
as compared with the rural, and has thus rescued a considerable part of
the population from the idiocy of rural life. Just as it has made the
country dependent on the towns, so it has made barbarian and
semi-barbarian countries dependent on the civilised ones, nations of
peasants on nations of bourgeois, the East on the West.

The bourgeoisie keeps more and more doing away with the scattered state
of the population, of the means of production, and of property. It has
agglomerated production, and has concentrated property in a few hands.
The necessary consequence of this was political centralisation.
Independent, or but loosely connected provinces, with separate
interests, laws, governments and systems of taxation, became lumped
together into one nation, with one government, one code of laws, one
national class-interest, one frontier and one customs-tariff. The
bourgeoisie, during its rule of scarce one hundred years, has created
more massive and more colossal productive forces than have all
preceding generations together. Subjection of Nature’s forces to man,
machinery, application of chemistry to industry and agriculture,
steam-navigation, railways, electric telegraphs, clearing of whole
continents for cultivation, canalisation of rivers, whole populations
conjured out of the ground—what earlier century had even a presentiment
that such productive forces slumbered in the lap of social labour?

We see then: the means of production and of exchange, on whose
foundation the bourgeoisie built itself up, were generated in feudal
society. At a certain stage in the development of these means of
production and of exchange, the conditions under which feudal society
produced and exchanged, the feudal organisation of agriculture and
manufacturing industry, in one word, the feudal relations of property
became no longer compatible with the already developed productive
forces; they became so many fetters. They had to be burst asunder; they
were burst asunder.

Into their place stepped free competition, accompanied by a social and
political constitution adapted to it, and by the economical and
political sway of the bourgeois class.

A similar movement is going on before our own eyes. Modern bourgeois
society with its relations of production, of exchange and of property,
a society that has conjured up such gigantic means of production and of
exchange, is like the sorcerer, who is no longer able to control the
powers of the nether world whom he has called up by his spells. For
many a decade past the history of industry and commerce is but the
history of the revolt of modern productive forces against modern
conditions of production, against the property relations that are the
conditions for the existence of the bourgeoisie and of its rule. It is
enough to mention the commercial crises that by their periodical return
put on its trial, each time more threateningly, the existence of the
entire bourgeois society. In these crises a great part not only of the
existing products, but also of the previously created productive
forces, are periodically destroyed. In these crises there breaks out an
epidemic that, in all earlier epochs, would have seemed an
absurdity—the epidemic of over-production. Society suddenly finds
itself put back into a state of momentary barbarism; it appears as if a
famine, a universal war of devastation had cut off the supply of every
means of subsistence; industry and commerce seem to be destroyed; and
why? Because there is too much civilisation, too much means of
subsistence, too much industry, too much commerce. The productive
forces at the disposal of society no longer tend to further the
development of the conditions of bourgeois property; on the contrary,
they have become too powerful for these conditions, by which they are
fettered, and so soon as they overcome these fetters, they bring
disorder into the whole of bourgeois society, endanger the existence of
bourgeois property. The conditions of bourgeois society are too narrow
to comprise the wealth created by them. And how does the bourgeoisie
get over these crises? On the one hand inforced destruction of a mass
of productive forces; on the other, by the conquest of new markets, and
by the more thorough exploitation of the old ones. That is to say, by
paving the way for more extensive and more destructive crises, and by
diminishing the means whereby crises are prevented.

The weapons with which the bourgeoisie felled feudalism to the ground
are now turned against the bourgeoisie itself.

But not only has the bourgeoisie forged the weapons that bring death to
itself; it has also called into existence the men who are to wield
those weapons—the modern working class—the proletarians.

In proportion as the bourgeoisie, _ie_, capital, is developed, in the
same proportion is the proletariat, the modern working class,
developed—a class of labourers, who live only so long as they find
work, and who find work only so long as their labour increases capital.
These labourers, who must sell themselves piece-meal, are a commodity,
like every other article of commerce, and are consequently exposed to
all the vicissitudes of competition, to all the fluctuations of the
market.

Owing to the extensive use of machinery and to division of labour, the
work of the proletarians has lost all individual character, and
consequently, all charm for the workman. He becomes an appendage of the
machine, and it is only the most simple, most monotonous, and most
easily acquired knack, that is required of him. Hence, the cost of
production of a workman is restricted, almost entirely, to the means of
subsistence that he requires for his maintenance, and for the
propagation of his race. But the price of a commodity, and therefore
also of labour, is equal to its cost of production. In proportion
therefore, as the repulsiveness of the work increases, the wage
decreases. Nay more, in proportion as the use of machinery and division
of labour increases, in the same proportion the burden of toil also
increases, whether by prolongation of the working hours, by increase of
the work exacted in a given time or by increased speed of the
machinery, etc.

Modern industry has converted the little workshop of the patriarchal
master into the great factory of the industrial capitalist. Masses of
labourers, crowded into the factory, are organised like soldiers. As
privates of the industrial army they are placed under the command of a
perfect hierarchy of officers and sergeants. Not only are they slaves
of the bourgeois class, and of the bourgeois State; they are daily and
hourly enslaved by the machine, by the over-looker, and, above all, by
the individual bourgeois manufacturer himself. The more openly this
despotism proclaims gain to be its end and aim, the more petty, the
more hateful and the more embittering it is.

The less the skill and exertion of strength implied in manual labour,
in other words, the more modern industry becomes developed, the more is
the labour of men superseded by that of women. Differences of age and
sex have no longer any distinctive social validity for the working
class. All are instruments of labour, more or less expensive to use,
according to their age and sex.

No sooner is the exploitation of the labourer by the manufacturer, so
far at an end, that he receives his wages in cash, than he is set upon
by the other portions of the bourgeoisie, the landlord, the shopkeeper,
the pawnbroker, etc.

The lower strata of the middle class—the small tradespeople,
shopkeepers, retired tradesmen generally, the handicraftsmen and
peasants—all these sink gradually into the proletariat, partly because
their diminutive capital does not suffice for the scale on which Modern
Industry is carried on, and is swamped in the competition with the
large capitalists, partly because their specialized skill is rendered
worthless by the new methods of production. Thus the proletariat is
recruited from all classes of the population.

The proletariat goes through various stages of development. With its
birth begins its struggle with the bourgeoisie. At first the contest is
carried on by individual labourers, then by the workpeople of a
factory, then by the operatives of one trade, in one locality, against
the individual bourgeois who directly exploits them. They direct their
attacks not against the bourgeois conditions of production, but against
the instruments of production themselves; they destroy imported wares
that compete with their labour, they smash to pieces machinery, they
set factories ablaze, they seek to restore by force the vanished status
of the workman of the Middle Ages.

At this stage the labourers still form an incoherent mass scattered
over the whole country, and broken up by their mutual competition. If
anywhere they unite to form more compact bodies, this is not yet the
consequence of their own active union, but of the union of the
bourgeoisie, which class, in order to attain its own political ends, is
compelled to set the whole proletariat in motion, and is moreover yet,
for a time, able to do so. At this stage, therefore, the proletarians
do not fight their enemies, but the enemies of their enemies, the
remnants of absolute monarchy, the landowners, the non-industrial
bourgeois, the petty bourgeoisie. Thus the whole historical movement is
concentrated in the hands of the bourgeoisie; every victory so obtained
is a victory for the bourgeoisie.

But with the development of industry the proletariat not only increases
in number; it becomes concentrated in greater masses, its strength
grows, and it feels that strength more. The various interests and
conditions of life within the ranks of the proletariat are more and
more equalised, in proportion as machinery obliterates all distinctions
of labour, and nearly everywhere reduces wages to the same low level.
The growing competition among the bourgeois, and the resulting
commercial crises, make the wages of the workers ever more fluctuating.
The unceasing improvement of machinery, ever more rapidly developing,
makes their livelihood more and more precarious; the collisions between
individual workmen and individual bourgeois take more and more the
character of collisions between two classes. Thereupon the workers
begin to form combinations (Trades Unions) against the bourgeois; they
club together in order to keep up the rate of wages; they found
permanent associations in order to make provision beforehand for these
occasional revolts. Here and there the contest breaks out into riots.

Now and then the workers are victorious, but only for a time. The real
fruit of their battles lies, not in the immediate result, but in the
ever-expanding union of the workers. This union is helped on by the
improved means of communication that are created by modern industry and
that place the workers of different localities in contact with one
another. It was just this contact that was needed to centralise the
numerous local struggles, all of the same character, into one national
struggle between classes. But every class struggle is a political
struggle. And that union, to attain which the burghers of the Middle
Ages, with their miserable highways, required centuries, the modern
proletarians, thanks to railways, achieve in a few years.

This organisation of the proletarians into a class, and consequently
into a political party, is continually being upset again by the
competition between the workers themselves. But it ever rises up again,
stronger, firmer, mightier. It compels legislative recognition of
particular interests of the workers, by taking advantage of the
divisions among the bourgeoisie itself. Thus the ten-hours’ bill in
England was carried.

Altogether collisions between the classes of the old society further,
in many ways, the course of development of the proletariat. The
bourgeoisie finds itself involved in a constant battle. At first with
the aristocracy; later on, with those portions of the bourgeoisie
itself, whose interests have become antagonistic to the progress of
industry; at all times, with the bourgeoisie of foreign countries. In
all these battles it sees itself compelled to appeal to the
proletariat, to ask for its help, and thus, to drag it into the
political arena. The bourgeoisie itself, therefore, supplies the
proletariat with its own instruments of political and general
education, in other words, it furnishes the proletariat with weapons
for fighting the bourgeoisie.

Further, as we have already seen, entire sections of the ruling classes
are, by the advance of industry, precipitated into the proletariat, or
are at least threatened in their conditions of existence. These also
supply the proletariat with fresh elements of enlightenment and
progress.

Finally, in times when the class struggle nears the decisive hour, the
process of dissolution going on within the ruling class, in fact within
the whole range of society, assumes such a violent, glaring character,
that a small section of the ruling class cuts itself adrift, and joins
the revolutionary class, the class that holds the future in its hands.
Just as, therefore, at an earlier period, a section of the nobility
went over to the bourgeoisie, so now a portion of the bourgeoisie goes
over to the proletariat, and in particular, a portion of the bourgeois
ideologists, who have raised themselves to the level of comprehending
theoretically the historical movement as a whole.

Of all the classes that stand face to face with the bourgeoisie today,
the proletariat alone is a really revolutionary class. The other
classes decay and finally disappear in the face of Modern Industry; the
proletariat is its special and essential product. The lower middle
class, the small manufacturer, the shopkeeper, the artisan, the
peasant, all these fight against the bourgeoisie, to save from
extinction their existence as fractions of the middle class. They are
therefore not revolutionary, but conservative. Nay more, they are
reactionary, for they try to roll back the wheel of history. If by
chance they are revolutionary, they are so only in view of their
impending transfer into the proletariat, they thus defend not their
present, but their future interests, they desert their own standpoint
to place themselves at that of the proletariat.

The “dangerous class,” the social scum, that passively rotting mass
thrown off by the lowest layers of old society, may, here and there, be
swept into the movement by a proletarian revolution; its conditions of
life, however, prepare it far more for the part of a bribed tool of
reactionary intrigue.

In the conditions of the proletariat, those of old society at large are
already virtually swamped. The proletarian is without property; his
relation to his wife and children has no longer anything in common with
the bourgeois family-relations; modern industrial labour, modern
subjection to capital, the same in England as in France, in America as
in Germany, has stripped him of every trace of national character. Law,
morality, religion, are to him so many bourgeois prejudices, behind
which lurk in ambush just as many bourgeois interests.

All the preceding classes that got the upper hand, sought to fortify
their already acquired status by subjecting society at large to their
conditions of appropriation. The proletarians cannot become masters of
the productive forces of society, except by abolishing their own
previous mode of appropriation, and thereby also every other previous
mode of appropriation. They have nothing of their own to secure and to
fortify; their mission is to destroy all previous securities for, and
insurances of, individual property.

All previous historical movements were movements of minorities, or in
the interests of minorities. The proletarian movement is the
self-conscious, independent movement of the immense majority, in the
interests of the immense majority. The proletariat, the lowest stratum
of our present society, cannot stir, cannot raise itself up, without
the whole superincumbent strata of official society being sprung into
the air.

Though not in substance, yet in form, the struggle of the proletariat
with the bourgeoisie is at first a national struggle. The proletariat
of each country must, of course, first of all settle matters with its
own bourgeoisie.

In depicting the most general phases of the development of the
proletariat, we traced the more or less veiled civil war, raging within
existing society, up to the point where that war breaks out into open
revolution, and where the violent overthrow of the bourgeoisie lays the
foundation for the sway of the proletariat.

Hitherto, every form of society has been based, as we have already
seen, on the antagonism of oppressing and oppressed classes. But in
order to oppress a class, certain conditions must be assured to it
under which it can, at least, continue its slavish existence. The serf,
in the period of serfdom, raised himself to membership in the commune,
just as the petty bourgeois, under the yoke of feudal absolutism,
managed to develop into a bourgeois. The modern laborer, on the
contrary, instead of rising with the progress of industry, sinks deeper
and deeper below the conditions of existence of his own class. He
becomes a pauper, and pauperism develops more rapidly than population
and wealth. And here it becomes evident, that the bourgeoisie is unfit
any longer to be the ruling class in society, and to impose its
conditions of existence upon society as an over-riding law. It is unfit
to rule because it is incompetent to assure an existence to its slave
within his slavery, because it cannot help letting him sink into such a
state, that it has to feed him, instead of being fed by him. Society
can no longer live under this bourgeoisie, in other words, its
existence is no longer compatible with society.

The essential condition for the existence, and for the sway of the
bourgeois class, is the formation and augmentation of capital; the
condition for capital is wage-labour. Wage-labour rests exclusively on
competition between the laborers. The advance of industry, whose
involuntary promoter is the bourgeoisie, replaces the isolation of the
labourers, due to competition, by their revolutionary combination, due
to association. The development of Modern Industry, therefore, cuts
from under its feet the very foundation on which the bourgeoisie
produces and appropriates products. What the bourgeoisie, therefore,
produces, above all, is its own grave-diggers. Its fall and the victory
of the proletariat are equally inevitable."""

map_cn_en(cn, en)





