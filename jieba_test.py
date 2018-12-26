import jieba


def jieba_part(str='你知道邮箱怎么发送和删除邮件吗？'):
    result = jieba.cut(str, cut_all=False)
    print(' '.join(result))


if __name__ == '__main__':
    jieba_part()
