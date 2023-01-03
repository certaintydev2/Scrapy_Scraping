from socket import gethostbyname,gaierror
from PyPDF2 import PdfReader
import requests
import io


pdf_name1 = []
pdf_text1 = []

for i, url in enumerate(pdf_file1):
    print("URL No. : " , i)
    print(url)
    response = requests.get(url=url, headers=headers, timeout=120)
    on_fly_mem_obj = io.BytesIO(response.content)
    try:      
        object = PdfReader(on_fly_mem_obj)
        NumPages = object.getNumPages()
    except : continue
    try:       
        for j in range(0, NumPages):
            PageObj = object.getPage(j)
            Text = PageObj.extractText()
            text2 = Text.split("\n")  
            search_words = ["Video Management System", " VMS ", "Video Surveillance", "Video surveillance", "Physical Security"]
            for itemIndex in range(len(text2)):
                 for word in search_words:
                        if word in text2[itemIndex]:
                            print(j)
                            print(text2[itemIndex])
                            pdf_name1.append(url)
                            pdf_text1.append(text2[itemIndex])
    except gaierror:
        print('getting error')