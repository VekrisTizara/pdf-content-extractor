import glob

def find_pdf():
    list_pdfs = []
    for file in glob.glob('**/*.pdf', recursive=True):
        list_pdfs.append(file)
    return list_pdfs

print(find_pdf())
