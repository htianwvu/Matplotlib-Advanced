
import matplotlib.pyplot as plt


a = ["Star Wars","The Empire\n Strikes Back","The Godfather","Raiders of \nthe Lost Ark","The Shawshank\n Redemption",
     "Pulp Fiction","Return of\n the Jedi","Back to the Future","The Godfather\n Part II","Ikiru","Fight Club","GoodFellas",
     "Rear Window","City Lights","The Dark Knight","Alien","Casablanca","The Silence of\n the Lambs","Seven Samurai","The Shining"]
b = [1977,1980,1972,1981,1993,1994,1983,1985,1974,1952,1999,1991,1954,1931,2008,1979,1942,1991,1954,1980]

plt.figure(figsize=(20,8),dpi=80)

plt.barh(range(len(a)),b,height=0.2)

plt.yticks(range(len(a)),a)
plt.grid(alpha=0.4)

plt.xlim((1950,2000))

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





