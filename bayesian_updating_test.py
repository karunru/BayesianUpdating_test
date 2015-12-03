import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

n = 100 #試行回数
i = 0 #コインの種類
pi = np.array([0.1,0.4,0.5]) #含有率π
theta = np.array([0.8,0.6,0.3]) #表の出る確率θ
pri_prob = np.array([pi]) #１番最初の事前確率
plot_data = np.array([pri_prob]) #プロットするためのデータ

#コインの表の出る確率によって系列を作成
X = np.random.choice(["H","T"],size=n,p=[theta[i],1-theta[i]])
print(X)

#事後確率の計算
def bayes_post(pri_prob,x):
	if x == "H":
		numerator = pri_prob * theta
	elif x == "T":
		numerator = pri_prob * (1 - theta)
	else:
		pass
	post_prob = numerator / numerator.sum();
	return post_prob

#データの数だけベイズ更新
for x in X:
	pri_prob = bayes_post(pri_prob,x)
	plot_data = np.append(plot_data,pri_prob)

print(pri_prob.T) #求められた事後確率を表示

#プロット
plot_data = plot_data.reshape(n+1,3)
plt.plot(plot_data)
plt.show()
