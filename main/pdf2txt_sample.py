from pdfminer.pdfinterp import PDFPageInterpreter,PDFResourceManager
from pdfminer.converter import TextConverter,PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
from pdfminer.pdfpage import PDFPage

# 获取pdf文档
fp = open('exam.pdf','rb')

# 创建一个与文档相关的解释器
parser = PDFParser(fp)

# pdf文档的对象，与解释器连接起来
doc = PDFDocument(parser=parser)
parser.set_document(doc=doc)

# 如果是加密pdf，则输入密码
# doc._initialize_password()

# 创建pdf资源管理器
resource = PDFResourceManager()

# 参数分析器
laparam=LAParams()

# 创建一个聚合器
device = PDFPageAggregator(resource,laparams=laparam)

# 创建pdf页面解释器
interpreter = PDFPageInterpreter(resource,device)

# 获取页面的集合
for page in PDFPage.get_pages(fp):
    # 使用页面解释器来读取
    interpreter.process_page(page)
    
    # 使用聚合器来获取内容
    layout = device.get_result()
    for out in layout:
        if hasattr(out,'get_text'):
            print(out.get_text())
            
            # 写入txt文件
            fw = open('exam.txt','a')
            fw.write(out.get_text())
————————————————
版权声明：本文为CSDN博主「Erika1203」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_43257951/java/article/details/84258861