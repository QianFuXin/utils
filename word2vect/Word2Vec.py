# encoding:utf-8
import jieba.analyse
import multiprocessing
import re
import gensim
import jieba.analyse
from gensim.models import Word2Vec
import os
import logging
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
import random

# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.unicode_minus'] = False

# 设置日志级别 in (debug、info、warning、error、critical) 只显示级别以上的日志
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 启动paddle模式
jieba.enable_paddle()
# 加载停用词
stopwords = [i.strip() for i in open("data/stop-words.txt", encoding="utf-8", mode="r").readlines()]
# 加载个人词典 可以识别某些特定词
userDic = [i.strip() for i in open("data/userDic.txt", encoding="utf-8", mode="r").readlines()]
for i in userDic:
    jieba.suggest_freq(i, True)


# 文件预处理，把文件按照？！。；分割
# 目的：把文本分为n句话
def __preProcess__(textPath):
    lines = open(textPath, encoding="utf-8", mode="r").read().replace("\n", "")
    # 替换空白数据
    lines = re.sub(re.compile(r"\s+"), '', lines)
    # 按照符号分割
    lines = re.split("[？！。；]", lines)
    # 去除两端空白 例如'   ' 或者''
    lines = [i.strip() for i in lines]
    lines = [i for i in lines if i]
    return lines


# 分词
def __splitWord__(lines):
    allWords = []
    for id, value in enumerate(lines):
        logging.debug(f'已经完成{id + 1}条句子')
        # jieba分词后去除停用词
        lineWords = [i for i in jieba.lcut(value, use_paddle=True) if not i in stopwords]
        # 如果结果中包含着','或者'”''“' 则去除
        pattern = re.compile(r"[（）【】{}‘’~！@#￥%…&*-+=·—、；：/》《”，“`!^*()$-=_+'\";:\\|<>,.?]")
        lineWords = [re.sub(pattern, "", i) for i in lineWords]
        # 去除两端空白 例如'   ' 或者''
        lineWords = [i.strip() for i in lineWords]
        lineWords = [i for i in lineWords if i]
        # 如果分词后数组为空 不加入
        if not len(lineWords) == 0:
            allWords.append(lineWords)
    return allWords


# 保存模型的两种形式
def __savaModel__(model, modelName):
    # 如果文件夹不存在则创建
    if os.path.exists("model") and os.path.isdir("model"):
        pass
    else:
        os.mkdir("model")
    # 保存模型
    model.save(f"./model/gensim-model_{modelName}")
    # 保存word2vec（每个词对应的词向量值）
    model.wv.save_word2vec_format(f"./model/gensim-word2vec_{modelName}")


# 训练模型
def trainModel(textPath, modelName):
    # 数据预处理
    lines = __preProcess__(textPath)
    logging.debug(f'数据预处理完成,共{len(lines)}条句子')
    # 分词
    allWords = __splitWord__(lines)
    logging.debug('数据分词完成')
    """
   参数
   min_count 词频少于min_count次数的单词会被丢弃掉, 默认值为5。
   vector_size 向量的维度
   workers 多cpu
    """
    # 训练模型
    model = Word2Vec(allWords, workers=multiprocessing.cpu_count())
    logging.debug('训练模型处理完成')
    # 保存模型
    __savaModel__(model, modelName)
    logging.debug('保存模型处理完成')
    return model


# 加载模型
def loadModel(modelName, word2vec=False, binary=False):
    # 模型路径
    modelPath = os.path.join("model", modelName)
    # 模型的两种方式
    if word2vec:
        model = gensim.models.KeyedVectors.load_word2vec_format(modelPath, binary=binary)
    else:
        model = gensim.models.Word2Vec.load(modelPath)
    logging.debug('加载模型处理完成')
    return model


# 更新模型  只支持model模式
def updateModel(modelName, textPath, modelNewName):
    # 模型路径
    modelPath = os.path.join("model", modelName)
    # 加载旧模型
    model = gensim.models.Word2Vec.load(modelPath)
    # 数据预处理
    lines = __preProcess__(textPath)
    logging.debug('数据预处理完成')
    # 分词
    allWords = __splitWord__(lines)
    logging.debug('数据分词完成')
    model.build_vocab(allWords, update=True)
    # 训练
    model.train(allWords, total_examples=model.corpus_count, epochs=model.epochs)
    __savaModel__(model, modelNewName)
    return model


# 降维
def __reduce_dimensions__(model):
    num_dimensions = 2

    vectors = np.asarray(model.wv.vectors)
    labels = np.asarray(model.wv.index_to_key)

    # 使用 t-SNE降维
    tsne = TSNE(n_components=num_dimensions, random_state=0)
    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    return x_vals, y_vals, labels


# 画图
def __plot_with_matplotlib__(x_vals, y_vals, labels, pictureName):
    random.seed(0)

    plt.figure(figsize=(12, 12))
    plt.scatter(x_vals, y_vals)

    indices = list(range(len(labels)))
    selected_indices = random.sample(indices, 25)
    for i in selected_indices:
        plt.annotate(labels[i], (x_vals[i], y_vals[i]))
    # 保存svg
    plt.savefig(f"{pictureName}.svg", format="svg")
    plt.show()


# 模型可视化
def modelVisualization(model, pictureName):
    # 降维
    x_vals, y_vals, labels = __reduce_dimensions__(model)
    # 绘图
    __plot_with_matplotlib__(x_vals, y_vals, labels, pictureName)

trainModel("活着.txt","活着")