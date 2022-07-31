import re
from bs4 import BeautifulSoup
from Qalam.automate import Automate
# import requests

def SetInfo(info, count):
    newline = []
    with open("Qalam/info.txt", 'r') as f:
        for line in f.readlines():
            if info in line:
                newline.append(re.sub('\d+',str(count),line))
            else:
                newline.append(line)
    with open("Qalam/info.txt", 'w') as f:
        for line in newline:
            f.writelines(line)

def GetInfo(info):
    with open("Qalam/info.txt", 'r') as f:
        for line in f.readlines():
            if info in line:
                return int(re.search(r'\d+', line).group())

def PCResults():
    with Automate() as auto:
        soup = BeautifulSoup(auto.GetPCResultsPage(), 'html.parser')
        resultRow = soup.find_all('tr', class_="table-parent-row show_child_row")
        newCount = len(resultRow)
        oldCount = GetInfo('SemesterCount:')
        if oldCount < newCount:
            SetInfo('SemesterCount:', oldCount+1)
            for row in resultRow:
                term = row.td.a
                _, _, _, gpa, cgpa = row.find_all('td', class_="uk-text-center")
                term, gpa, cgpa = ' '.join(term.text.split()), ' '.join(gpa.text.split()), ' '.join(cgpa.text.split())
            return term, gpa, cgpa
    
    def ACResults():
        _
