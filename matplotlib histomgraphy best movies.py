
import matplotlib.pyplot as plt


a = [98,58,23,43,89,52,24,34,81,49,16,29,
     74,36,17,26,67,34,18,25,68,29,29,20,
     24,45,21,36,21,49,20,43,21,53,27,49,
     30,60,28,52,34,68,34,64,41,73,42,73,
     53,64,45,21,14,27,40,58,76,81,93,84,
     70,57,45,43,34,29,36,51,65,72,81,93,
     98,21,23,31,30,35,40,37,40,42,39,42,
     46,42,34,45,54,53,37,49,60,67,40,57,
     74,23,14,56,78,27,20,67,89,34,30,73,
     83,43,32,85,98,50,36,101,123,63,46,125,
     98,58,23,43,89,52,24,34,81,49,16,29,
     74,36,17,26,67,34,18,25,68,29,29,20,
     24,45,21,36,21,49,20,43,21,53,27,49,
     30,60,28,52,34,68,34,64,41,73,42,73,
     53,64,45,21,14,27,40,58,76,81,93,84,
     70,57,45,43,34,29,36,51,65,72,81,93,
     98,21,23,31,30,35,40,37,40,42,39,42,
     46,42,34,45,54,53,37,49,60,67,40,57,
     74,23,14,56,78,27,20,67,89,34,30,73,
     83,43,32,85,98,50,36,101,123,63,46,125]   

plt.figure(figsize=(20,8),dpi=80)
#calculate the group number
d = 3

num_bins = (max(a)-min(a))//d

# setup interval

plt.xticks(range(min(a),max(a)+d,d),rotation=45)

#plt.hist(a,num_bins)

# frequency distribution
plt.hist(a,num_bins,density = 1)


plt.grid(alpha=0.4)



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





