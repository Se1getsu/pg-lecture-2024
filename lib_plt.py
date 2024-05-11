import numpy as np
import matplotlib.pyplot as plt

# x軸の値を生成
x = np.linspace(-2*np.pi, 2*np.pi, 100)

# y軸の値を生成（sin関数を適用）
y = np.sin(x)

# グラフを描画
plt.plot(x, y)
plt.title('Sin Graph')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
