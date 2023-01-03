# importing required modules
from pathlib import Path
import pandas as pd
import PyPDF2
import re


pdfFileObj = open('../file_path', 'rb')        ## no return o/p for Video Surveillance

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
  
# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a total page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText()) 

# creating a total page object
NumPages = pdfReader.getNumPages()
for i in range(0, NumPages):
    PageObj = pdfReader.getPage(i)
    Text = PageObj.extractText().split("\n")

    # # first level of searching
    search_words = [' Total Camera Count ', ' Camera total ', "Due Date",  "Target Date",  "Completion Date",  "Closing Date",  "Proposal Date",
        "Submission Date",  "Bid Date",  "Close Date",  "Deadline",  "Response  Date", "End Date" ]


    for line in Text:
        for item in search_words:
            if item in line:
                print("####", item)
                print("@@@@", line)
 
pdfFileObj.close()

