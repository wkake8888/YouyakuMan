import os
import argparse
from argparse import RawTextHelpFormatter

from src.TestLoader import TestLoader
from src.ModelLoader import ModelLoader
from src.Summarizer import SummarizerIO
from src.Translator import TranslatorY
from src.LangFactory import LangFactory
import pandas as pd

body_list = []
sum_list = []
text_file = open('test_text.txt', "r")
for line in text_file.readlines():
    l = line
    s1 = l.find('body') + 8
    e1 = l.find("'}")

    s2 = l.find('body', s1) + 8
    e2 = l.find("'}", s2)
    t2 = l[s2: e2]
    body_list.append(t2)


os.chdir('./')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description="""
    Intro:   This is an one-touch extractive summarization machine.
             using BertSum as summatization model, extract top N important sentences.

    Note:    Since Bert only takes 512 length as inputs, this summarizer crop articles >512 length.
             If --super_long option is used, summarizer automatically parse to numbers of 512 length
             inputs and summarize per inputs. Number of extraction might slightly altered with --super_long used.

    Example: youyakuman.py -txt_file YOUR_FILE -n 3
    """)

    parser.add_argument("-n", default=3, type=int,
                        help='Numbers of extraction summaries')
    parser.add_argument("-lang", default='en', type=str,
                        help='If language of article isn\'t Englisth, will automatically translate by google')
    parser.add_argument("--super_long", action='store_true',
                        help='If length of article >512, this option is needed')

    args = parser.parse_args()

#    if args.super_long:
#        sys.stdout.write('\n<Warning: Number of extractions might slightly altered since with --super_long option>\n')

    # Language initiator
    lf = LangFactory(args.lang)
    translator = None if args.lang in lf.support_lang else TranslatorY()

    model = ModelLoader(lf.toolkit.cp, lf.toolkit.opt, lf.toolkit.bert_model)
    sum_list = []
    for i in range(len(body_list)):
        data = TestLoader(body_list[i], args.super_long, args.lang, translator).data
        summarizer = SummarizerIO(data, model, args.n, translator)

