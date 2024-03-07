"""
A tool to extract words(Include Chinese and English) from given media like video or picture.
"""

import sys

COPYRIGHT = """
@author: zhongpengqun2022@gmail.com
@copyright:  2023, Not determined, But all rights reserved.
"""
import logging
import argparse
from PIL import Image
import pytesseract


PICTURE_POSTFIXS = ['mp3', 'jpg', 'jpeg', 'png']
VIDEO_POSTFIXS = ['mp4']

LOGGER = logging.getLogger("main")


def extract_words_from_picture(path):


    # If you don't have tesseract executable in your PATH, include the following:
    pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
    # Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    # Simple image to string
    print(pytesseract.image_to_string(Image.open('test.png')))

    # In order to bypass the image conversions of pytesseract, just use relative or absolute image path
    # NOTE: In this case you should provide tesseract supported images or tesseract will return error
    print(pytesseract.image_to_string('test.png'))

    # List of available languages
    print(pytesseract.get_languages(config=''))

    # French text image to string
    print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

    # Batch processing with a single file containing the list of multiple image file paths
    print(pytesseract.image_to_string('images.txt'))

    # Timeout/terminate the tesseract job after a period of time
    try:
        print(pytesseract.image_to_string('test.jpg', timeout=2)) # Timeout after 2 seconds
        print(pytesseract.image_to_string('test.jpg', timeout=0.5)) # Timeout after half a second
    except RuntimeError as timeout_error:
        # Tesseract processing is terminated
        pass

    # Get bounding box estimates
    print(pytesseract.image_to_boxes(Image.open('test.png')))

    # Get verbose data including boxes, confidences, line and page numbers
    print(pytesseract.image_to_data(Image.open('test.png')))

    # Get information about orientation and script detection
    print(pytesseract.image_to_osd(Image.open('test.png')))

    # Get a searchable PDF
    pdf = pytesseract.image_to_pdf_or_hocr('test.png', extension='pdf')
    with open('test.pdf', 'w+b') as f:
        f.write(pdf) # pdf type is bytes by default

    # Get HOCR output
    hocr = pytesseract.image_to_pdf_or_hocr('test.png', extension='hocr')

    # Get ALTO XML output
    xml = pytesseract.image_to_alto_xml('test.png')    
    return words


def extract_words_from_video(path):
    def split_video_as_pictures(path):
        
    return words


class Command():
    HELP = __doc__
    DEBUG = False

    parser = argparse.ArgumentParser(
                description=HELP,
                epilog=COPYRIGHT,
                usage=None,
            )

    parser.add_argument('--media-path', dest='media_path', required=True, help='Path of media')
    parser.add_argument('--result', dest='result', required=True, help='Where result saved')


    def execute(self):
        argv = sys.argv[1:]
        if not argv:
            argv = ['-h']
        args = self.parser.parse_args(argv)
        media_postfix = args.media_path.split('/')[-1].split('.')[-1]

        if media_postfix.lower() in PICTURE_POSTFIXS:
            pass
        elif media_postfix.lower() in VIDEO_POSTFIXS:
            pass
        else:
            LOGGER.error('Media format error!')
            sys.exit(1)

Command().execute()