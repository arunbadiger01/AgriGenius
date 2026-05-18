import markdown
from xhtml2pdf import pisa

with open('fertilizer_presentation.md', 'r', encoding='utf-8') as f:
    text = f.read()

html = markdown.markdown(text)
html = f"<html><head><style>body {{ font-family: Helvetica, sans-serif; font-size: 14px; padding: 20px; }} h1 {{ color: #2c3e50; font-size: 24px; }} h2 {{ color: #34495e; font-size: 20px; border-bottom: 1px solid #ddd; padding-bottom: 5px; }} h3 {{ color: #2980b9; font-size: 16px; }} h4 {{ color: #16a085; font-size: 14px; }} ul {{ margin-bottom: 15px; }} li {{ margin-bottom: 5px; }}</style></head><body>{html}</body></html>"

with open('fertilizer_presentation.pdf', 'wb') as f:
    pisa.CreatePDF(html, dest=f)

print("PDF created successfully!")
