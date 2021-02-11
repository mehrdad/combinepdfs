import os
from PyPDF2 import PdfFileMerger

blank_file = '../blank.pdf'
source_dir = os.getcwd()

merger = PdfFileMerger()

for item in os.listdir(source_dir):
    if item.endswith('pdf'):
        merger.append(item)
        merger.append(blank_file)

merger.write('./Output/combined.pdf')       
merger.close()