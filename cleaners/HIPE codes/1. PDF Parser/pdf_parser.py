# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 20:25:08 2021

@author: LukaszMalucha
"""


from pathlib import Path
import datetime
import json
import shutil



import pandas as pd
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import csv



# Time and date
CURRENT_DATE = datetime.datetime.now().strftime("%Y-%m-%d")
TIME_NOW = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# Folder Paths
PDFS = list(Path(Path.cwd(),  "PDFS").glob('*.pdf'))
EXTRACTED_PATH = Path(Path.cwd(),  "EXTRACTED_FILES")


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr,  codec='utf-8', laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    maxpages = 0
    caching = True
    pagenos=set()


    for i, page in enumerate(PDFPage.get_pages(fp, pagenos, maxpages=maxpages,caching=caching, check_extractable=False)):
        print(i)
        if i > 33 and  i < 62:
            interpreter.process_page(page)


    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text




def extract_pdf_page(filename, input_file, brand, output_folder):
    
  
    # Paths for creating folder and file
    pdf_folder = Path(EXTRACTED_PATH, brand, input_file)
    pdf_folder.mkdir(parents=True, exist_ok=True) 
   
    pages = []
    
    text = convert_pdf_to_txt(filename)
    if len(text) < 10:
        error_folder = Path(EXTRACTED_PATH, "ERRORS")
        error_folder.mkdir(parents=True, exist_ok=True)  
        shutil.copy(str(filename), str(error_folder))
        shutil.rmtree(pdf_folder)
       
    
    else:        
        pages.append(text)         
        text_file_path = Path(output_folder, "page-1.csv")  
        with open(text_file_path, 'w', encoding="utf-8-sig") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(pages)
            
            
            
            
def pdf_extractor():
    """Extractor compiler with report creation"""    
    # Create directory if doesn't exist already
    EXTRACTED_PATH.mkdir(parents=True, exist_ok=True)    
    
    
    for i, document in enumerate(PDFS):
        print("PDF # " + str(i + 1))
        
        output_file_folder = Path(EXTRACTED_PATH, "HIPE")
        output_file_folder.mkdir(parents=True, exist_ok=True) 
        output_file_folder_pages = Path(EXTRACTED_PATH, "HIPE", "pages")
        output_file_folder_pages.mkdir(parents=True, exist_ok=True) 
        
        try:
            shutil.copy(str(document), str(output_file_folder))    
            extract_pdf_page(document, "2016", "codes", output_file_folder_pages)
              
            document.unlink()

        except Exception as e:            

            pass   


        
  
# Execute    
pdf_extractor()   


            
