## a2g-wordsbook
---
a2g-wordsbook 是一个可以将来源于音频（通过 AWS Transcribe 转换为 JSON), TXT, PDF 的英文单词，与自己已经的词库相对，生成生词，可以以纯单词，单词加释义，或者有道单词本的 XML 格式输入。帮助用户可以快速通过先预览生词，再听音频，看文章，来使初次听力，阅读更加流畅。

## Press Release:
---

2020年6月28日，这个特殊的纪念日里面，Allen 为自己送上了一个礼物 a2g-wordsbook，是一个英语学习的系统。这个系统将帮助他可以更有效地学习他感兴趣的英文素材文章。同时提高他的英文听力与阅读能力，为未来洋参加国际会议，学习英文视频打下扎实基础。同时为未来他的孩子做同样的事情提供相应的能力。
Allen做为一个没有国际留学背景却有着跨国公司工作经验的人，工作英文中一直有一些瓶颈无法突破，但却很难找到有效的办法。他发现自己的孩子也有类似的问题。于是他想到做一个学习系统，可以方便地帮助他快速而且无障碍学习感兴趣的国际内容。
用户可以通过上传他们感兴趣的视频，文本，声音等多媒体素材。来得到相应的文本，并且建立自己的英文生词库。通过对比自己已经掌握的英文生词与素材文本比对，从而生成生词表。方便用户先对生词进行学习之后，无障碍地对文章进行阅读。或者听音视频。从而更享受视频与音频内容。
Allen 这个系统构建在 AWS 上，并且通过构建这一套系统开始了由一个售前、运维角色向一名开发者的转变，他构建了自己熟悉的开发、测试、运维环境，并且在开发过程中使用非常多的微服务与无服务器服务如（S3, Lambda，Transcribe等) 架构。使系统可以在低成本高效地运行。

## 使用说明
---
1. 安装本地依赖
	pip install -r requirements.txt
2. 配置主程序 a2g-wordsbook.py 中的常量，如下
```
	WORD_CONFIDENCE = 1 # AWS Transcribe 生成 JSON 文件中单词的置信度
	NEW_WORDS_FILENAME = "./words/new_words.txt" # 生词单词 TXT 文件默认路
	BASE_WORDS_FILENAME = "./words/base_words.txt" # 熟词本默认路径
	MEDIA_JSON_FILENAME = "./words/media-overview.json" # AWS Transcribe 生成 JSON 文件默认路径
	DICT_FILENAME = "./dict/star_sqldb.db" # 词典的默认路径，使用 sqlite3 数据库的话，要提前转换，转换办法是运行 stardict.py
	YOUDAO_XML_FILENAME = "./words/youdao_xml.xml" # 有道单词本输出路径
	YOUDAO_XML_TAGS = "a2g-wordsbook" # 有道单词本的生词分组名字
```
3. 主程序命令行参数
```

usage: a2g-wordsbook.py [-h] [-i 输入文件名]
                        [--parse-type {txt,transcribe_json,pdf}]
                        [-b 熟词库文件名] [--base-type {txt,ddb}]
                        [-o 输出生词文件名]
                        [--out-type {pure_words,trans_words,youdao_xml,ddb}]

Wordsbook process the words file based on known words and output new words file

参数说明:
  -h, --help            显示帮助信息并退出
  -i PARSE_FILE_NAME, --parse-file PARSE_FILE_NAME
                        要处理的学习文件
  --parse-type {txt,transcribe_json,pdf}
                        支持的文件类型选择，可以是 txt-纯文本，transcribe-AWS Transcribe 翻译生成 JSON, pdf-PDF文件
  -b BASE_FILE, --base-file BASE_FILE
                        自己的熟词库文件，格式是每行一个单词
  --base-type {txt,ddb}
                        熟词库文件类型，可以是txt-纯文本，或者是 DynamoDB (开发中)
  -o WORDS_OUT_FILE, --words-out WORDS_OUT_FILE
                        输出的文件名
  --out-type {pure_words,trans_words,youdao_xml,ddb}
                        输出的文件类型，可以选择 pure_words-单纯每行单词的 txt 文本文件, trans_words-带有翻译的文本文件,
                        youdao_xml-可被导入的有道单词本XML文件, ddb 加入到 DynamoDB 词库当中
