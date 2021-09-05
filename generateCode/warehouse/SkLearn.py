def train_test_split():
    info = """\"\"\"
Splitting data into 70% training and 30% test data:

stratify=y获得内置的分层支持。 
举个栗子：
整个数据集有1000行，result列的数据也是1000个，而且分两类：0和1，其中0有300个，1有700个，即数据分类的比例为3：7。

那么现在把整个数据split，因为test_size = 0.2，所以训练集分到800个数据，测试集分到200个数据。

重点来了
那么由于stratify = result，则训练集和测试集中的数据分类比例将与result一致，也是3：7，结果就是在训练集中，有240个0和560个1；测试集中有60个0和140个1。

random_state打乱数据
\"\"\"
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=1, stratify=y)
    """.lower()
    return info


def standardScaler():
    info = """\"\"\
特征标准化
调用StandardScaler的fit方法对训练数据的每个特征维度估计参数μ（样本均值）
和σ（标准差）进行估算。
再调用transform方法，利用估计的参数μ和σ标准化训练数据。
在标准化测试数据集时，要注意使用相同的缩放参数以确保训练数据集与
测试数据集的数值具有可比性。
\"\"\"
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# 估算
sc.fit(X_train)
# 转换数据
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
    """.lower()
    return info


def perceptron():
    info = """
    \"\"\"
感知机模型(缺点:感知器算法从不收敛于不完全线性可分离的数据集)
ta0是学习速率,速率过大,容易错过最优的点,
速率过小,导致迭代次数的增加(可以把学习速率看上步长)
\"\"\"
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score
ppn = Perceptron(eta0=0.1, random_state=1)
# 训练模型
ppn.fit(X_train_std, y_train)
# 预测
y_pred = ppn.predict(X_test_std)
# 分类错误的数量
print('Misclassified examples: %d' % (y_test != y_pred).sum())
# 预测的正确率
print('Accuracy: %.3f' % accuracy_score(y_test, y_pred))
# 预测的正确率
print('Accuracy: %.3f' % ppn.score(X_test_std, y_test))
    """
    return info
def logisticRegression():
    info="""
    \"\"\"
逻辑回归
lbfgs算法(最小化损失函数)
ovr:一对多(多分类)
C:正则化参数λ太小容易产生过拟合，太大容易产生欠拟合。因为C是λ的倒数
所以C越大容易过拟合，越小越容易欠拟合
\"\"\"
lr = LogisticRegression(C=100.0, random_state=1, solver='lbfgs', multi_class='ovr')
# 训练数据
lr.fit(X_train_std, y_train)
\"\"\"
预测样本属于某个特定类的概率(如果标签有1 2 3类,则预测该样本分别是1 2 3类的概率)
    1类的概率      2类的概率       3类的概率
[[3.81527885e-09 1.44792866e-01 8.55207131e-01]]
通过结果一眼可以看出,属于第3类(0.85的概率)
\"\"\"
print(lr.predict_proba(X_test_std[0, :]))
\"\"\"
预测数据
预测三组数据,结果为[2 0 0]
说明第一组是第三类(2),第二组和第三组是第一类(0)
\"\"\"
print(lr.predict(X_test_std[:3, :]))
# 只预测一行数据
print(lr.predict(X_test_std[0, :].reshape(1, -1)))
    """.lower()
    return info