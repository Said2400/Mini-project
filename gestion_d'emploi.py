import tkinter as tk
from PIL import Image, ImageTk
import fitz 


pdf_paths = ["DEV101.pdf", "DEV102.pdf", "AEFGT102.pdf", "AA101.pdf", "EIT101.pdf",
              "TDB102.pdf", "ID101.pdf", "GC102.pdf","GE101.pdf", "GE102.pdf", 
              "M101.pdf", "MA101.pdf", "AEFGT101.pdf","EB101.pdf", "EB102.pdf", 
              "EIT101.pdf", "EMI101.pdf", "GC101.pdf","RVA102.pdf", "RVA101.pdf", 
              "TDB101.pdf", "TREMOA101.pdf", ]


page_images = []


root = tk.Tk()
root.title("PDF Viewer")


page_label = tk.Label(root)
page_label.pack(pady=10)

def show_pdf(pdf_path):
    global page_images
    pdf_document = fitz.open(pdf_path)


    images = []
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        image = page.get_pixmap()
        image_tk = ImageTk.PhotoImage(Image.frombytes("RGB", (image.width, image.height), image.samples))
        images.append(image_tk)

    page_images = images


    show_page(page_number=0)

def show_page(page_number):

    image_tk = page_images[page_number]


    page_label.configure(image=image_tk)
    page_label.image = image_tk  


buttons = []
for i, pdf_path in enumerate(pdf_paths):
    button = tk.Button(root, text=pdf_path.split(".pdf")[0], command=lambda path=pdf_path: show_pdf(path))
    button.pack(pady=5)
    buttons.append(button)


root.geometry("900x600")


root.mainloop()





