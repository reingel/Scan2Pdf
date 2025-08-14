import os
import sys
from BookScanSplit import *


mode = 'photo' # 'text' or 'photo'
input_folder = '/Users/reingel/Downloads/split_scanned_book/원본/'
imgout_folder = '/Users/reingel/Downloads/split_scanned_book/image/'
debug_folder = '/Users/reingel/Downloads/split_scanned_book/debug/'

bss = BookScanSplit('text', input_folder, imgout_folder)
bss.clear_output_folders()
bss.split()

print('All done.')
