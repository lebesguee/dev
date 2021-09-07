from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

#split pdfs documents by page
input_pdf = PdfFileReader("test.pdf")
output = PdfFileWriter()
output.addPage(input_pdf.getPage(0)) # page parameter
with open("first_page.pdf", "wb") as output_stream:
    output.write(output_stream)

#merge pdfs documents by page
pdf_file1 = PdfFileReader("file1.pdf")
pdf_file2 = PdfFileReader("file2.pdf")
output = PdfFileMerger()
output.append(pdf_file1)
output.append(pdf_file2)

with open("merged.pdf", "wb") as output_stream:
    output.write(output_stream)