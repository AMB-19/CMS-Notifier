import os
import re
from bs4 import BeautifulSoup
from Qalam.automate import Automate
# import requests

def SetInfo(info, count):
    newlines = []
    with open("Qalam/info.txt", 'r') as f:
        for line in f.readlines():
            if info in line:
                newlines.append(re.sub('\d+',str(count), line.strip()))
            else:
                newlines.append(line.strip())
    with open("Qalam/info.txt", 'w') as f:
        # for line in newlines:
        f.writelines(newlines)

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
        oldCount = GetInfo('FinalResultCount')
        if oldCount < newCount:
            SetInfo('FinalResultCount', newCount)
            for row in resultRow:
                term = row.td.a
                _, _, _, gpa, cgpa = row.find_all('td', class_="uk-text-center")
                term, gpa, cgpa = ' '.join(term.text.split()), ' '.join(gpa.text.split()), ' '.join(cgpa.text.split())
            return term, gpa, cgpa
    
def ACResults():
    return

def SemesterInvoice():
    with Automate() as auto:
        soup = BeautifulSoup(auto.GetInvoicesPage(), 'html.parser')
        invoiceTable = soup.find('table', class_="uk-table uk-table-nowrap table_check")
        invoiceRow = invoiceTable.find('tbody').find_all('tr')
        newCount = len(invoiceRow)
        oldCount = GetInfo('InvoiceCount')
        if oldCount < newCount:
            SetInfo('InvoiceCount', newCount)
            for invoiceList in invoiceRow:
                term, amount = invoiceList.find_all('td')[3:8:4]
                term, amount = ' '.join(term.text.split()), ' '.join(amount.text.split())
                return term, amount
