# -*- coding: utf-8 -*-
"""

utilities for NLP text summarizer 

Created on Sun Jan 2 09:56:10 2022
@author: dkf

"""

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import re, math
from string import punctuation
from collections import defaultdict
from heapq import nlargest
from transformers import pipeline

class Summarizer():
    
    def __init__(self, method="Extract"):
        self.method = method
        self.punctuation = punctuation + ' \n'
        self.stopwords = None

        if self.method == "Extract":
            pass
        elif self.method == "Abstract":
            self.transformer_model = "sshleifer/distilbart-cnn-12-6"
            print(f"If you don't have the huggingface {self.transformer_model} model downloaded, this could be a while.")
        else:
            return f"{self.method} method not implemented"

        
    def summarize(self, file, output_len=250):
        self.file = file
        self.output_len = output_len

        if self.method == "Extract":
            return self._extract(self.file, self.output_len)
        elif self.method == "Abstract":
            return self._abstract(self.file, self.output_len)
        else:
            return f"{self.method} method still not implemented"
        
    def _extract(self, file, output_len):
        
        # get text from file
        f = open(file, mode='r')
        text = f.read()
        f.close()
        
        # tokenize
        doc = word_tokenize(text, language="english")
        sents = sent_tokenize(text, language="english")
        
        # get names of participants and build stopwords list
        self.stopwords = set(stopwords.words("english") + ['like', 'um', 'uh', 'yeah'])
        names = self._get_names(sents)
            ## would be good to distinguish in-text names from formatting-introduced names ##
        self.stopwords.update(set(names)) 
        
        # build word frequency table
        word_freq = self._build_word_freq_dict(doc)

        # build log inverse document->sentence table
        inverse_sent_freq = self._build_inverse_sent_freq(word_freq.keys(), sents)

        # build sentence token scores
        sentence_scores = self._build_sent_scores(sents, word_freq, inverse_sent_freq)

        select_length = int(len(sents)*0.5)
        # select_length is puts an upper bound on max length, irrelevant,
        # and it can be changed to len(sents) but variable name must be used in line below
        summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)

        word_count = 0
        final_summary = []
        for k in range(select_length):
            word_count += len(word_tokenize(summary[k]))
            if word_count > output_len:
                break
            final_summary.append(summary[k])

        # summary formatting for Markdown or for input to huggingface wrapper
        if self.method == "Extract":
            return '*' + ' \n\n *'.join(final_summary)
        else:
            return " ".join(final_summary)
    
    def _get_names(self, sents):
        # match coding pattern for header line.  the rube goldberg of regex in the house.
        name_pattern1 = "(.*):\s{15,}(.+?):(.+?)\s{40,}"
        name_pattern2 ="(.*)(\s)(.*)?:\s{15,}(.+?):(.+?)\s{40,}"
        names = []
        name_tokens = []
        for s in sents:
            if re.search(name_pattern1, s):
                wds = word_tokenize(s)
                if wds[1] == ":":
                    names.append(wds[0])
                    name_tokens.append(wds[0].lower())                    
            if re.search(name_pattern2, s):
                wds = word_tokenize(s)
                if wds[2] == ":":
                    nom = wds[0] + " " + wds[1]
                    names.append(nom)
                    name_tokens += [wds[0].lower(), wds[1].lower()]
        
        print(f"participant names scraped from transcript:\n{set(names)}")
        return name_tokens
    
    def _build_sent_scores(self, sents, word_freq, inv_freq):
        sentence_scores = defaultdict(lambda: 0)

        for s in sents:
            for word in word_tokenize(s):
                token = word.lower()
                if token in word_freq.keys():
                    sentence_scores[s] += word_freq[token]*inv_freq[token]
                    
        return sentence_scores
    
    def _build_word_freq_dict(self, doc):
        timestamp_pattern = "\S+\d:\d\S+"
        
        word_freq = defaultdict(lambda: 0)
        for word in doc:
            token = word.lower()
            if (not re.search(timestamp_pattern, token)):
                if (token not in self.punctuation):              
                    if (token not in self.stopwords): 
                        word_freq[token] += 1
        
        return word_freq
    
    def _build_inverse_sent_freq(self, words, sents):
        N = len(sents)
        inv_sent_freq = defaultdict(lambda: 0)
        
        for w in words:
            for s in sents:
                split_sent = word_tokenize(s)
                if w in split_sent:
                    inv_sent_freq[w] += 1
                    continue
                    
        for w in inv_sent_freq.keys():
            inv_sent_freq[w] = math.log(N / inv_sent_freq[w])

        return inv_sent_freq

    
    def _abstract(self, file, output_len=250):
        # transformer pipelines have a lot of exception handling issues,
        # must look up and hard-code max token length for chosen encoder at present time
        MAX_LEN = 1024

        # big safety margin because huggingface tokenize != nltk tokenizer
        MAX_LEN = int(0.6 * MAX_LEN)

        truncated = self._extract(file, MAX_LEN)

        # initialize HuggingFace summarization pipeline
        summarizer = pipeline("summarization", model=self.transformer_model)

        # summarize text using pipeline
        summarized = summarizer(truncated, min_length=75, max_length=output_len)
        summary = summarized[0]["summary_text"]

        return summary
    

