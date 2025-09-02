from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import textwrap

def text_to_pdf(text_content, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    
    # Split content into lines
    lines = text_content.split('\n')
    
    y_position = height - 50
    for line in lines:
        if y_position < 50:  # Start new page
            c.showPage()
            y_position = height - 50
            
        # Handle long lines
        if len(line) > 80:
            wrapped_lines = textwrap.wrap(line, width=80)
            for wrapped_line in wrapped_lines:
                c.drawString(50, y_position, wrapped_line)
                y_position -= 15
        else:
            c.drawString(50, y_position, line)
            y_position -= 15
    
    c.save()

with open('./data/earnings_report_content.txt', 'r') as f:
    content = f.read()

text_to_pdf(content, 'data/earnings_report.pdf')
