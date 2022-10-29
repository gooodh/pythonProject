from PyPDF2 import PdfReader

reader = PdfReader("paycheck-83550757-01.09.2022.pdf")
page = reader.pages[0]

parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    y = tm[5]
    if y > 40 and y < 700:
        parts.append(text)


page.extract_text(visitor_text=visitor_body)
text_body = "".join(parts)

print(text_body)