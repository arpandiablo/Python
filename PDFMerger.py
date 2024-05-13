from pypdf import PdfWriter

merger = PdfWriter()

for pdf in ["Test Folder/1.pdf", "Test Folder/2.pdf", "Test Folder/3.pdf"]:
    merger.append(pdf)

merger.write("Test Folder/merged-pdf.pdf")
merger.close()
print("Merge Operation Completed")