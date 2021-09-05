import PyPDF2

# PDF portable document file
pdfFileObj = open("/Users/apple/Downloads/QQ下载/朱玲-316202060760-尹辉平.pdf", mode="rb")
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)
pageText = pageObj.extractText()
print(pageText)
