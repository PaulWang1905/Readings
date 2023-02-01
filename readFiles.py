# -*- coding: UTF-8 -*-
# This module is used to read the files in the folder
# and return a list of entries
# entries are defined as class entry. See makeLD.py for details
from pathlib import Path
import re

class Entry():
    # class for the entries of Readings
    # read_date: date of reading
    # title: title of the paper
    # link: link of the paper
    # authors: authors of the paper
    # comments: comments on the paper
    # date: date of the paper
    # tags: tags of the paper
    def __init__(self, text: str):
        self.text = text
        self.read_date = None
        self.title = None
        self.link = None
        self.authors = None
        self.comments = None
        self.date = None
        #self.tags = None
    def extract(self):
        
        read_date = re.compile(r'(\d{4}-\d{2}-\d{2})')
        match = read_date.search(self.text)
        if match:
            self.read_date = match.group(1)
        
        title_pattern = re.compile(r'\[\*\*(.*)\*\*\]')
        match = title_pattern.search(self.text)
        if match:
            self.title = match.group(1)
        
        link_pattern = re.compile(r'\((.*)\)')
        match = link_pattern.search(self.text)
        if match:
            self.link = match.group(1)
        
        authors_pattern = re.compile(r'\*([^*]+)\*\.')
        match = authors_pattern.search(self.text)
        if match:
            self.authors = match.group(1)
        
        date_pattern = re.compile(r'(\d{4}-\d{2})\.')
        match = date_pattern.search(self.text)
        if match:
            self.date = match.group(1)

        comments_pattern = re.compile(r'\>(.*)')
        match = comments_pattern.search(self.text)
        if match:
            self.comments = match.group(1)

listOfEntries = []

def readFiles(self):
    files= str()
    for p in Path(self).glob('*.md'):
        file= f"{p.read_text()}\n"
        files += file
    return files

def readEntries(self):
    files = readFiles(self)
    # use re to remove lines that maches the pattern: one # + space + any characters + \n
    files = re.sub(r'^# .*?\n', '', files, flags=re.MULTILINE)
    # split the files into entries
    entries = files.split('## ')[1:]
    for entry in entries:
        entry = Entry(entry)
        entry.extract()
        listOfEntries.append(entry)
    return listOfEntries    
if __name__ == "__main__":
    print('This is a module. Please run makeLD.py, to test, run test_readFiles.py')

