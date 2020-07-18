#-*- coding: UTF-8 -*-
# @Time    : 2020/3/1 14:43
# @File    : run.py.py
# @Software: PyCharm

#python run.py 127.0.0.1:1234

import sys
import web
from chatbot_graph import ChatBotGraph
render = web.template.render('templates/')

urls = ('/', 'index','/add','add')
app = web.application(urls, globals())

handler= ChatBotGraph()
print("create question object finish! ")

# 主页显示类
class index:
    def GET(self):
        return render.index()

    def POST(self):
        text=web.input()
        print(text)
        raise web.seeother('/')

# 处理问题类
class add:
    # get方式处理问题
    def GET(self):
        pass

    # post方式处理问题
    def POST(self):
        def enablePrint():
            sys.stdout = sys.__stdout__
        enablePrint()
        while 1:
            text=web.input()
            # 简单的过滤掉无效post请求
            if text['id']=="bei":
                question=text['q']
                print("received question:",question)
                print("now get answer!")
                answer=dealquestion(question)
                print("得到的答案是：",answer)
                if len(str(answer).strip())==0:
                    answer="我也不知道呢！"
                # print("return answer!")
                return answer
            else:
                pass


# 处理问题的方法
def dealquestion(question):
    # 查询知识图谱
    answer = handler.chat_main(question)
    return answer

if __name__=="__main__":
    web.internalerror = web.debugerror

    app.run()