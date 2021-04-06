import pyttsx3
import PyPDF2
book = open('oops.pdf', 'rb')
pdfreader=PyPDF2.PdfFileReader(book)
pages=pdfreader.numPages
print(pages)
speaker = pyttsx3.init()
page=pdfreader.getPage(9)
text=page.extractText()
print(text)
speaker.say(text)
speaker.runAndWait()
