from site import venv
#4requerimets python 3.8
import sys
import subprocess
import pkg_resources

required = {'art', 'argparse', 'opencv-python', 'tqdm', 'colorama'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
#end of requeriments

from art import *
import glob  
import os  
import argparse  
import cv2  
import concurrent.futures  
import time 
from tqdm import tqdm  
from colorama import Fore, Back, Style, Cursor, init
init()  
cv2.__file__  

start = time.perf_counter()  

parser = argparse.ArgumentParser()
parser.add_argument('--folder', required=True, help='Path to Folder image')
parser.add_argument('--percent', type=int, required=False, help='percent Resize 5 - 100%. Default 50', nargs='?', default=50, const=50)
parser.add_argument('--dfolder', required=True, help='path destin folder')
parser.add_argument('--quality', type=int, required=False, help='quality JPEG 40-95. Default 70', default=70, nargs='?', const=70)
args = vars(parser.parse_args())  

dfolder = str(args['dfolder'])  

folder = str(args['folder'] + '/')  

quality = str(args['quality']  )  

ext = ['png', 'jpg', 'jpeg']  

newfldr = os.makedirs(dfolder, exist_ok=True) 

newfldr  

files = []  

[files.extend(glob.glob(folder + '*.' + e)) for e in ext]  

file_count = len(files)  

percent = str(args['percent'])  

scale_percent = args['percent']  

tprint('RFP')  
print(f'{Fore.LIGHTYELLOW_EX}Resize Folder Pics V1.13.07.2022 By {Fore.LIGHTBLUE_EX} GOZARCK {Fore.RESET}')

print \
    (f'Resize image at {Fore.LIGHTGREEN_EX}{percent} % {Fore.RESET}from {Fore.LIGHTGREEN_EX}{folder}{Fore.RESET} Save in {Fore.LIGHTGREEN_EX}{dfolder}{Fore.RESET} quality at {Fore.LIGHTGREEN_EX}{quality}%{Fore.RESET}')
#pbar = tqdm(ncols=100, total=file_count, ascii="░▒█"  )
pbar = tqdm(ncols=100, total=file_count  )  
def imres(files):  

    image = cv2.imread(files, cv2.IMREAD_UNCHANGED)  

    head_tail = os.path.split(files)  
    
    width = int(image.shape[1] * scale_percent / 100)  
    height = int(image.shape[0] * scale_percent / 100)  
    dim = (width, height)

    resizedPercent = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  

    img_path = os.path.join \
        (dfolder + '/' + str(head_tail[1]))  

    cv2.imwrite(img_path, resizedPercent, [cv2.IMWRITE_JPEG_QUALITY, int(quality)])  

    File_Size = os.path.getsize(files)  
    File_Size_MB = round(File_Size / 1024 / 1024, 2)  
    print_file_size = str(files + str(File_Size_MB) + ' Mb')  
    pbar.set_description(f'Resizing...{head_tail[1]}'  )  
    pbar.update(  )  



def main():  
    while True:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor  :  
                executor.map(imres, files  )
                break
        except ValueError:
            print(f'{Fore.LIGHTYELLOW_EX}upsss something is wrong....')



if __name__ == '__main__':  
    main()
    pbar.close(  )  
finish = time.perf_counter()
print(f'Finished in {Fore.LIGHTYELLOW_EX}{round(finish - start, 2)} {Fore.RESET}seconds')
print(f'{Fore.LIGHTBLACK_EX}Made in python3.8-64-pycharm-cx-Freeze(compiled in windows) ')
