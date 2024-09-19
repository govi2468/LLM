# import PyPDF2
# import os
# pdfFileObject = open(r"data\b[A-Za-zA-Za-z]+\W+FAQ+\b.pdf", 'rb')
# pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
# print(" No. Of Pages :", pdfReader.numPages)
# pageObject = pdfReader.getPage(0)
# print(pageObject.extractText())
# def extract_text_from_pdf(folder_path):
#     with open(folder_path)
#
# def read_dir(folder_path):
#     for file_name in os.listdir(folder_path):
#         # file_path = os.path.join(folder,file_name)
#         text = extract_text_from_pdf(file_name)
#         return file_name
import os
import PyPDF2
import openai
# from pdf_file_directory import directory
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def process_pdfs_in_directory(directory):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            results.append(text)
    return results


def split_into_sections(text):
    # Example: split by paragraphs
    sections = text.split(r'\n\n')
    return sections

# import re
# import spacy
# # Disable the parser and NER to speed up the pipeline
# nlp = spacy.load("en_core_web_lg", disable=["parser", "ner"])
# # Load a pre-trained NLP model
# # nlp = spacy.load("en_core_web_lg")
#
# def extract_information(section):
#     doc = nlp(section)
#     # Custom logic to extract information using regex or NLP entities
#     equipment_name = "..."
#     domain = "..."
#     model_numbers = re.findall(r'\b[A-Z0-9-]+\b', section)
#     manufacturer = "..."
#
#     return {
#         'equipment_name': equipment_name,
#         'domain': domain,
#         'model_numbers': model_numbers,
#         'manufacturer': manufacturer
#     }
# #
#
