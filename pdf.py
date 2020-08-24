import PyPDF2
# import sys
#
#
# inputs = sys.argv[1:]
#
#
# def pdf_combiner(pdf_list):
# 	mergered = PyPDF2.PdfFileMerger()
# 	for pdf in pdf_list:
# 		print(pdf)
# 		mergered.append(pdf)
# 	mergered.write('combined.pdf')
#
#
# pdf_combiner(inputs)

template = PyPDF2.PdfFileReader(open('combined.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page = template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked.pdf', 'wb') as file:
		output.write(file)
