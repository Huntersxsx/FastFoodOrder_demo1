import jieba


def jieba_part(str='我想要一杯可乐'):
    result = jieba.cut(str, cut_all=False)
    print(' '.join(result))


if __name__ == '__main__':
    jieba_part(str='我想要一杯可乐')
    jieba_part(str='我想点一杯可乐')
    jieba_part(str='我还要一杯可乐')
    jieba_part(str='来个甜筒')
    #jieba.suggest_freq(('要', '点'), True)
    #jieba.suggest_freq(('点', '份'), True)
    #jieba.suggest_freq(('来', '份'), True)
    jieba_part(str='再来两个汉堡吧')
    jieba_part(str='我想要来份鸡翅')
    jieba_part(str='我要点餐')
    jieba_part(str='我想要买杯可乐')
    jieba_part(str='我想要点杯可乐')
    jieba_part(str='我想要点个汉堡')
    jieba_part(str='我想要点份鸡翅')
