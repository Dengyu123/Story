from urllib.request import urlopen
from bs4 import BeautifulSoup
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import sys
import re

if len(sys.argv)<2:
	print ("python ",sys.argv[0],"< PDF_file | PDF_url >")
	print ("Function: Get the pdf words")
	print (" Author : Yuki Deng")
	print (" Time   : 9.19 2016")
	exit(1)
def readPDF(pdfFile):
	rsrcmgr = PDFResourceManager()
	retstr = StringIO()
	laparams = LAParams()
	device = TextConverter(rsrcmgr,retstr,laparams=laparams)

	process_pdf(rsrcmgr,device,pdfFile)
	device.close()

	content = retstr.getvalue()
	retstr.close()
	return content

pdfFile=""
if re.search(r"http",sys.argv[1]):
	pdfFile = urlopen(sys.argv[1])
else:
	pdfFile = open(sys.argv[1],'rb')
outputString = readPDF(pdfFile)
print (outputString)
pdfFile.close()
