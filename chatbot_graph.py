#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py


from question_classifier import *
from question_parser import *
from answer_search import *

'''问答类'''
class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是小倪医药智能助理，希望可以帮到您。如果没答上来，可联系https://nynCoder.github.io/。祝您身体棒棒！'
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers and "谢谢" not in sent:
            return answer
        elif "谢谢" in sent:
            return "不客气哒，有问题随时找我哦！"
        else:
            return '\n'.join(final_answers)

if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('用户:')
        answer = handler.chat_main(question)
        print('小倪:', answer)

