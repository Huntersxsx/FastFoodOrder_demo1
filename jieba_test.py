import jieba


def jieba_part(str='怎么修改邮箱的个性签名？'):
    result = jieba.cut(str, cut_all=False)
    print(' '.join(result))


if __name__ == '__main__':
    jieba_part()
