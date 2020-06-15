
import matplotlib.pyplot as plt


y3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,19,21,22,22,22,23]
y10 =[26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x3= range(1,31,1)
x10=range(51,82,1)

plt.figure(figsize=(20,8),dpi=80)

plt.scatter(x3,y3)
plt.scatter(x10,y10)

_x = list(x3)+list(x10)
_xtick_labels = ["Mar,{}".format(i) for i in x3]
_xtick_labels += ["Oct,{}".format(i-50) for i in x10]
plt.xticks(_x[::2],_xtick_labels,rotation=45)

plt.xlabel('Date', fontsize=16)
plt.ylabel('Temperatures (C)',fontsize=16)
plt.title('Temperature change during Two Months',fontsize=18)

plt.legend(labels=['March','October'],loc='best',fontsize=18)

plt.show()



##plt.xlim((-1,2))
##plt.ylim((-1,3))

##plt.plot(x,y1,label='me', color='r',linestyle='--', linewidth=5,alpha=0.7)

##plt.xlabel('I am x', fontsize=16)
##plt.ylabel('I am y',fontsize=16)
##plt.title('Temperature change during the daytime',fontsize=18)

## 调整图大小
##plt.figure(figsize=(20,8),dpi=80)


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

##gca"get current axis'
##ax = plt.gca()
##ax.spines['right'].set_color('none')
##ax.spines['top'].set_color('none')
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
##ax.spines['bottom'].set_position(('data',0)) #outward, axes
##ax.spines['left'].set_position(('data',0))





