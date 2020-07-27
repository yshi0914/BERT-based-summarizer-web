"""Views for the base app"""
# python manage.py runserver
from summarizer import Summarizer
from sumbert import summarize

import numpy as np

import pickle
from html import unescape
from html import escape

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def getReply(request):
    question_cnt=request.GET.get("content")
    print("Start processing...")
    result = process(unescape(question_cnt))
    return HttpResponse(result)


def process(text_input):
    model = Summarizer()
    # Minimum length that the sentences must be
    # It can be optimized by modify sentenct_handler
    result = model(text_input, min_length=60)
    full = ''.join(result)    
    innerHtmlResult = '<div style="border-style: solid;">'+ summarize(full)
    innerHtmlResult += '</div>'
    return innerHtmlResult.replace('\n', '<br/>')
