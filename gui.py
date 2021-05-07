# imports

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile, StringVar, Button
from functions import display_logo, display_textbox, extract_images

root = tk.Tk()

root.geometry('+%d+%d' % (1250, 10))

header = Frame(root, width=800, height=300, bg="white")
header.grid(columnspan=3, rowspan=2, row=0)

# main content area - text and image extraction
main_content = Frame(root, width=800, height=250, bg="#20bebe")
main_content.grid(columnspan=3, rowspan=2, row=2)


# logo
# logo = Image.open('logo.png')
# logo = ImageTk.PhotoImage(logo)
# logo_label = tk.Label(image=logo)
# logo_label.image = logo
# logo_label.grid(column=1, row=0)

# instructions

# instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
# instructions.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', filetype=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()
        # page_content = page_content.encode('cp1252')
        page_content = page_content.replace('\u2122', "'")

        # show text box on row w col 0
        display_textbox(page_content, 2, 0, root)

        # text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        # text_box.insert(1.0, page_content)
        #  text_box.tag_configure("center", justify="center")
        #  text_box.tag_add("center", 1.0, 'end')
        #  text_box.grid(column=1, row=3)

        browse_text.set("Browse")


display_logo('logo.png', 0, 0)

# broserbbuttom

browse_text = StringVar()
browse_btn = Button(root, textvariable="browse_text", command=lambda:open_file(), font=("Raleway", 10), bg="white")
browse_text.set("Browse")
browse_btn.grid(column=2, row=1, sticky=NE, padx=50)
# browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway", bg="#20bebe",
#                       fg="white", height=2, width=15)
# browse_text.set("Browse")
# browse_btn.grid(column=1, row=2)

# canvas = tk.Canvas(root, width=600, height=250)
# canvas.grid(columnspan=3)

root.mainloop()
