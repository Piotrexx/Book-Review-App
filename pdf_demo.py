from weasyprint import HTML

def generate_pdf(url, pdf_file):
    print("generating PDF...")
    HTML(url).write_pdf(pdf_file)

if __name__ == '__main__':
    url = 'https://www.google.com'
    pdf_file = 'demo_pego.pdf'
    generate_pdf(url, pdf_file)