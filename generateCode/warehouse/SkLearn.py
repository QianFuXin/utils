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
    info = """
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


def svc():
    info = '''
# 线性SVC模型,C越大,分类要求越严格
svm = SVC(kernel='linear', C=1.0, random_state=1)
svm.fit(X_train_std, y_train)
# 非线性SVC模型
# gamma参数,高斯球的截止参数,gamma越大,范围越小,会一直收缩
svm = SVC(kernel='rbf', random_state=1, gamma=0.10, C=10.0)
svm.fit(X_train_std, y_train)
    '''.lower()
    return info


def sgd():
    info = '''
# 随机梯度下降算法分类器,针对于数据集较大的情况
ppn = SGDClassifier(loss='perceptron')
ppn.fit(X_train_std, y_train)
lr = SGDClassifier(loss='log')
lr.fit(X_train_std, y_train)
svm = SGDClassifier(loss='hinge')
svm.fit(X_train_std, y_train)
    '''.lower()
    return info


def dicisionTree():
    info = '''
# 评判标准为基尼杂质,最大深度为4,通过减少最大深度,来进行修剪枝叶
tree_model = DecisionTreeClassifier(criterion='gini',
                                    max_depth=4,
                                    random_state=1)
tree_model.fit(X_train, y_train)
tree_model.predict()
# 决策树详细信息可视化
tree.plot_tree(tree_model)
plt.show()
# 更详细的决策树信息可视化
dot_data = export_graphviz(tree_model,
                           filled=True,
                           rounded=True,
                           class_names=['Setosa',
                                        'Versicolor',
                                        'Virginica'],
                           feature_names=['petal length',
                                          'petal width'],
                           out_file=None)
graph = graph_from_dot_data(dot_data)
graph.write_png('tree.png')
    '''.lower()
    return info


def randomForest():
    info = '''
# 评判标准为基尼杂质
# 25个决策树组成的随机森林
# 使用两个核心
forest = RandomForestClassifier(criterion='gini',
                                n_estimators=25,
                                random_state=1,
                                n_jobs=2)
forest.fit(X_train, y_train)
forest.predict()
    '''.lower()
    return info


def knn():
    info = '''
    # k近邻 5个邻居  p = 2等于标准欧几里德度量标准
knn = KNeighborsClassifier(n_neighbors=5,
                           p=2,
                           metric='minkowski')
knn.fit(X_train_std, y_train)
knn.predict()
    '''.lower()
    return info


def nanProcess():
    info = '''
# 输出每类有多少个缺失值
print(df.isnull().sum())
# 输出值
print(df.values)
# 删除包含缺失值的行
print(df.dropna(axis=0))
# 删除包含缺失值的列
print(df.dropna(axis=1))
# 删除一行全是缺失值的行
print(df.dropna(how='all'))
# 删除一行有效值小于3个的行
print(df.dropna(thresh=4))
# 删除指定列出现缺失值的行
print(df.dropna(subset=['C']))

# 用列的均值去代替缺失值 mean可以替换为median、most_frequent（中位数和众数）
imr = SimpleImputer(missing_values=np.nan, strategy='mean')
# 从训练数据中学习参数
imr = imr.fit(df.values)
# 转换模型
imputed_data = imr.transform(df.values)
print(imputed_data)
# 用列的均值去代替缺失值
df.fillna(df.mean())
'''


def lableOrFeatureEncoder():
    info = '''
    df = pd.DataFrame([['green', 'M', 10.1, 'class2'],
                   ['red', 'L', 13.5, 'class1'],
                   ['blue', 'XL', 15.3, 'class2']])

df.columns = ['color', 'size', 'price', 'classlabel']
print(df)
size_mapping = {'XL': 3,
                'L': 2,
                'M': 1}
# 把字符串转数字,可以比较大小
df['size'] = df['size'].map(size_mapping)
print(df)

# 把字符串类型的标签转换为数字
# {标签1:值,标签2:值,}
class_mapping = {label: idx for idx, label in enumerate(np.unique(df['classlabel']))}
print(class_mapping)
# df['classlabel'] = df['classlabel'].map(class_mapping)
# print(df)
# sk自带的标签编码方法
class_le = LabelEncoder()
print(df['classlabel'].values)
# 把字符标签转化为数字标签
y = class_le.fit_transform(df['classlabel'].values)
print(y)
# 把数字标签转换为字符标签
print(class_le.inverse_transform(y))

# 独热编码，n个数据，n维，只有自己的那一维是1，其他全是0
X = df[['color', 'size', 'price']].values
color_ohe = OneHotEncoder()
print(color_ohe.fit_transform(X[:, 0].reshape(-1, 1)).toarray())

# 把one hot编码加入原始数据中
X = df[['color', 'size', 'price']].values
c_transf = ColumnTransformer([('onehot', OneHotEncoder(), [0]),
                              ('nothing', 'passthrough', [1, 2])])
print(c_transf.fit_transform(X).astype(float))

# 通过pandas实现热编码 只转换字符串列
pd.get_dummies(df[['price', 'color', 'size']])

# 删除第一个特征列
print(pd.get_dummies(df[['price', 'color', 'size']], drop_first=True))

# 删除ont hot编码的冗余列
color_ohe = OneHotEncoder(categories='auto', drop='first')
c_transf = ColumnTransformer([('onehot', color_ohe, [0]),
                              ('nothing', 'passthrough', [1, 2])])
print(c_transf.fit_transform(X).astype(float))
    '''
    return info


def scaler():
    info = '''# 最大最小归一化 数值范围[0 - 1]
mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
print(X_train_norm)
print(X_test_norm)

# 标准化缩放
stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)
ex = np.array([0, 1, 2, 3, 4, 5])

print('standardized:', (ex - ex.mean()) / ex.std())'''
    return info


# 特征选择
def featureChoose():
    info = '''
    ## 特征提取是压缩多个维度，特征选择是舍弃一些不重要的维度
    # SBS算法 使用特征选择去实现降维
class SBS():
    def __init__(self, estimator, k_features, scoring=accuracy_score,
                 test_size=0.25, random_state=1):
        self.scoring = scoring
        self.estimator = clone(estimator)
        self.k_features = k_features
        self.test_size = test_size
        self.random_state = random_state

    def fit(self, X, y):

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=self.test_size,
                                                            random_state=self.random_state)

        dim = X_train.shape[1]
        self.indices_ = tuple(range(dim))
        self.subsets_ = [self.indices_]
        score = self._calc_score(X_train, y_train,
                                 X_test, y_test, self.indices_)
        self.scores_ = [score]

        while dim > self.k_features:
            scores = []
            subsets = []

            for p in combinations(self.indices_, r=dim - 1):
                score = self._calc_score(X_train, y_train,
                                         X_test, y_test, p)
                scores.append(score)
                subsets.append(p)

            best = np.argmax(scores)
            self.indices_ = subsets[best]
            self.subsets_.append(self.indices_)
            dim -= 1

            self.scores_.append(scores[best])
        self.k_score_ = self.scores_[-1]

        return self

    def transform(self, X):
        return X[:, self.indices_]

    def _calc_score(self, X_train, y_train, X_test, y_test, indices):
        self.estimator.fit(X_train[:, indices], y_train)
        y_pred = self.estimator.predict(X_test[:, indices])
        score = self.scoring(y_test, y_pred)
        return score

knn = KNeighborsClassifier(n_neighbors=5)
# 查找特征
sbs = SBS(knn, k_features=1)
sbs.fit(X_train_std, y_train)

#对特征子集的性能进行绘图
k_feat = [len(k) for k in sbs.subsets_]

plt.plot(k_feat, sbs.scores_, marker='o')
plt.ylim([0.7, 1.02])
plt.ylabel('Accuracy')
plt.xlabel('Number of features')
plt.grid()
plt.tight_layout()
# plt.savefig('images/04_08.png', dpi=300)
plt.show()


# 用随机森林选择特征
feat_labels = df_wine.columns[1:]

forest = RandomForestClassifier(n_estimators=500,
                                random_state=1)

forest.fit(X_train, y_train)
importances = forest.feature_importances_

indices = np.argsort(importances)[::-1]

for f in range(X_train.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30,
                            feat_labels[indices[f]],
                            importances[indices[f]]))

plt.title('Feature Importance')
plt.bar(range(X_train.shape[1]),
        importances[indices],
        align='center')

plt.xticks(range(X_train.shape[1]),
           feat_labels[indices], rotation=90)
plt.xlim([-1, X_train.shape[1]])
plt.tight_layout()
# plt.savefig('images/04_09.png', dpi=300)
plt.show()

# 选择特征 只选择重要性大于0.1的特征
sfm = SelectFromModel(forest, threshold=0.1, prefit=True)
X_selected = sfm.transform(X_train)
print('Number of features that meet this threshold criterion:',
      X_selected.shape[1])

# Now, let's print the 3 features that met the threshold criterion for feature selection that we set earlier (note that this code snippet does not appear in the actual book but was added to this notebook later for illustrative purposes):


for f in range(X_selected.shape[1]):
    print("%2d) %-*s %f" % (f + 1, 30,
                            feat_labels[indices[f]],
                            importances[indices[f]]))
'''
    return info


def PCA():
    info = '''# 主成分分析（非监督学习）
# 只保留两个主成分分析
# 如果n_components=None 则不降维，返回所有排序后的主成分
pca = PCA(n_components=2)
X_train_pca = pca.fit_transform(X_train_std)
# 访问解释方差比
print(pca.explained_variance_ratio_)

# 通过SK实现LDA（监督学习） 两个主成
lda = LDA(n_components=2)
X_train_lda = lda.fit_transform(X_train_std, y_train)
X_test_lda = lda.transform(X_test_std)

# KPAC(解决非线性问题的降维)
X, y = make_moons(n_samples=100, random_state=123)
scikit_kpca = KernelPCA(n_components=2, kernel='rbf', gamma=15)
X_skernpca = scikit_kpca.fit_transform(X)'''
    return info
