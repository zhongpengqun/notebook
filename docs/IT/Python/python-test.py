from html2image import Html2Image
hti = Html2Image()
with open('d:/mm.html', 'r', encoding='UTF-8') as f:
    hti.screenshot(f.read(), save_as='out.png')