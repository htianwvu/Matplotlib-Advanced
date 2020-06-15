
import matplotlib.pyplot as plt


a = ["ape plant","dekelok","spiderman","war wolf"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

x_14 = list(range(len(a)))
x_15 = [i+0.2 for i in x_14]
x_16 = [i+0.2*2 for i in x_14]

bar_width = 0.2
plt.figure(figsize=(20,8),dpi=80)

plt.bar(x_14,b_14,width=bar_width,label="Sept 14")
plt.bar(x_15,b_15,width=bar_width,label="Sept 15")
plt.bar(x_16,b_16,width=bar_width,label="Sept 16")

plt.legend()

plt.xticks(x_15,a,rotation=45)

plt.show()



##plt.xlim((-1,2))
##plt.ylim((-1,3))

##plt.plot(x,y1,label='me', color='r',linestyle='--', linewidth=5,alpha=0.7)

##plt.xlabel('I am x', fontsize=16)
##plt.ylabel('I am y',fontsize=16)
##plt.title('Temperature change during the daytime',fontsize=18)

## 调整图大小
##plt.figure(figsize=(20,8),dpi=80)

##文字太长，断开
##"The Shawshank\n Redemption"

##轴刻度
##plt.xticks(range((2,25,5))
##plt.yticks(range(min(y),max(y)+2,2))

##new_ticks = np.linspace(-1,2,5)
##print(new_ticks)
##plt.xticks(new_ticks)
##plt.yticks([-2,-1.8,-1,1.22,3],
            ##['really bad','bad',r'$noraml\ \delta$','good','excellent'])

##网格
##plt.grid(alpha=0.4)

##图例
plt.legend(handles=[l1,l2],labels=['aaa','bbb'],loc='best')

##文字轴的输入：
##plt.bar(range(len(a)),b)
##plt.xticks(range(len(a)),a,rotation=45)


##gca"get current axis'
##ax = plt.gca()
##ax.spines['right'].set_color('none')
##ax.spines['top'].set_color('none')
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
##ax.spines['bottom'].set_position(('data',0)) #outward, axes
##ax.spines['left'].set_position(('data',0))





