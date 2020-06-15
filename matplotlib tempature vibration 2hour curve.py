
import matplotlib.pyplot as plt
import random

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

plt.figure(figsize=(20,8),dpi=80)

plt.xlabel('Time(min)')
plt.ylabel('Temperature (C)')
plt.title('Temperature change during 10:00-11:00AM')

plt.plot(x,y)

# adjust x-axis linspace 步长和刻度
_xtick_labels = ["10h{}min".format(i) for i in range(60)]
_xtick_labels += ["11h{}min".format(i) for i in range(60)]
plt.xticks(list(x)[::5],_xtick_labels[::5],rotation =45)

plt.show()

##plt.xlim((-1,2))
##plt.ylim((-1,3))

##plt.xlabel('I am x')
##plt.ylabel('I am y')
##plt.title('Temperature change during the daytime')

## 调整大小
##plt.figure(figsize=(20,8),dpi=80)


##轴刻度
##plt.xticks(range((2,25,5))
##plt.yticks(range(min(y),max(y)+2,2))

##new_ticks = np.linspace(-1,2,5)
##print(new_ticks)
##plt.xticks(new_ticks)
##plt.yticks([-2,-1.8,-1,1.22,3],
            ##['really bad','bad',r'$noraml\ \delta$','good','excellent'])

##随机选取整数
## y = [random.randint(20,35) for i in range(120)]

# adjust x-axis linspace 步长和刻度
##_xtick_labels = ["10h{}min".format(i) for i in range(60)]
##_xtick_labels += ["11h{}min".format(i) for i in range(60)]
##plt.xticks(list(x)[::3],_xtick_labels[::3],rotation =45)

##gca"get current axis'
##ax = plt.gca()
##ax.spines['right'].set_color('none')
##ax.spines['top'].set_color('none')
##ax.xaxis.set_ticks_position('bottom')
##ax.yaxis.set_ticks_position('left')
##ax.spines['bottom'].set_position(('data',0)) #outward, axes
##ax.spines['left'].set_position(('data',0))





