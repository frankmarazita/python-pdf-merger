import os
import PyPDF2

def merge(files, file_name):

    pdf_writer = PyPDF2.PdfFileWriter()

    for f in files:
        file_object = open(f, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(file_object)

        for i in range(pdf_reader.numPages):
            page_object = pdf_reader.getPage(i)
            pdf_writer.addPage(page_object)

    pdf_file = open(file_name + '.pdf', 'wb')
    pdf_writer.write(pdf_file)
    pdf_file.close()
