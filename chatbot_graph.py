#!/usr/bin/env python3
# coding: utf-8

from question_classifier import *
from question_parser import *
from answer_search import *


class ChatBotGraph:

    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionParser()
        self.searcher = AnswerSearcher()

    def chat_kg_main(self, sent):
        answer = 'no answer'

        # 问题分类
        res_classify = self.classifier.classify(sent)
        if not res_classify:
            return 'wrong class'

        # 问题解析
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


if __name__ == '__main__':
    handler = ChatBotGraph()
    while 1:
        question = input('Q:')
        USE_KG = True
        if USE_KG:
            answer = handler.chat_kg_main(question)
        else:
            answer = handler.chat_interface_main(question)
        print('A:', answer)

