import matplotlib.pyplot as plt
from scipy import stats
Hours =[2.5,5.1,3.2,8.5,3.5,1.5,9.2,5.5,8.3,2.7,7.7,5.9,4.5,3.3,1.1,8.9,2.5,1.9,6.1,7.4,2.7,4.8,3.8,6.9,7.8]
Scores =[21,47,27,75,30,20,88,60,81,25,85,62,41,42,17,95,30,24,67,69,30,54,35,76,86]
slope,intercept,r,p,std_err= stats.linregress(Hours,Scores)
def effeciency(Hours):
    return slope * Hours + intercept
eff1= effeciency(9.25)
print(eff1)
mymodel=list(map(effeciency,Hours))
plt.scatter(Hours,Scores)
plt.plot(Hours,mymodel)
plt.show()