"""
@author: lvhanyi
"""

import pandas as pd
import jieba


# 加载停用词列表（假设停用词列表存储在一个文本文件中，每行一个停用词）
def load_stopwords(stopwords_file):
    with open(stopwords_file, 'r', encoding='utf-8') as f:
        stopwords = f.read().splitlines()
    return stopwords


# 删除停用词并进行分词
def process_text(text, stopwords):
    if isinstance(text, str):  # 检查是否为字符串类型
        words = jieba.lcut(text)
        filtered_words = [word for word in words if word not in stopwords]
        return ' '.join(filtered_words)
    else:
        # 如果不是字符串，可以选择返回原始值、空字符串或其他处理方式
        # 这里我们返回空字符串表示不对非字符串类型进行分词
        return ''


# 主函数
def main(excel_file, content_column, stopwords_file, output_file):
    df = pd.read_excel(excel_file)
    stopwords = load_stopwords(stopwords_file) # 加载停用词
    df[content_column] = df[content_column].apply(lambda x: process_text(x, stopwords)) # 处理每一行的内容
    df.to_excel(output_file, index=False) # 将结果保存到新的Excel文件


if __name__ == "__main__":
    job_file = "C:\\Users\\LENOVO\\WPSDrive\\569704374\\WPS云盘\\数据挖掘\\JobDataMining\\data\\jobdata_preprocessed.xlsx"
    job_column = '工作简介'
    job_stopwords = "C:\\Users\\LENOVO\\WPSDrive\\569704374\\WPS云盘\\数据挖掘\\JobDataMining\\data\\cutwords\\stopwords_for_jobs.txt"
    job_output = "C:\\Users\\LENOVO\\WPSDrive\\569704374\\WPS云盘\\数据挖掘\\JobDataMining\\data\\cutwords\\jobdata_req_cut.xlsx"

    # zhihu_file = "C:\\Users\\LENOVO\\WPSDrive\\569704374\\WPS云盘\\数据挖掘\\JobDataMining\\data\\attitudes_zhihu_raw.xlsx"
    # zhihu_column = 'content'
    # zhihu_stopwords = "C:\\Users\\LENOVO\\WPSDrive\\569704374\\WPS云盘\\数据挖掘\\JobDataMining\\data\\cutwords\\stopwords.txt"
    # zhihu_output = 'job_output' 

    main(job_file, job_column, job_stopwords, job_output)
    # main(zhihu_file, zhihu_column, zhihu_stopwords, zhihu_output)