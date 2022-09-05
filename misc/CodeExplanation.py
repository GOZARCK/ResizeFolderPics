from site import venv


#PYTHONPATH=/venv/bin

# convert image by percentage for web
#
'''
I had to install python 3.8 for compatibility with other programs like cv2
using cv2 install it in the venv and in the native
nuitka to compile correctly you need to install the libs on the pc and on the venv
it worked very well
python -m nuitka --onefile --enable-plugin=numpy --windows-icon-from-ico=resize.ico main.py
python -m pyinstaller --onefile
then switch to cx-freeze need setup.py(see setup.py for compile in windows)

this version is MT (multiheading)---great!!
'''
from art import *
import glob  # process folders and file extensions
import os  # create folders and others things
import argparse  # create arguments
import cv2  # computational vision 2
import concurrent.futures  # multithread
import time  # time of procesing
from tqdm import tqdm  # progressbar
from colorama import Fore, Back, Style, Cursor, init # color in text
init()  # for  colorama
cv2.__file__  # for  cv2
#colorama and art makes this fun...tqdm also!

start = time.perf_counter()  # start time
'''
*******************************
argparser add arguments*
easy to understand ************
*********************************************************************************************************
*  argument       in  is needed         yes or no?                     show help                         *
*'--quality',     type=int,          required=False,         help='quality JPEG 40-95. Default 70'       *
*                                                                                                        *
* default value       need for default value                              need for default value         *
*default=70,                 nargs='?'                                        const=70                   *
*********************************************************************************************************
for defalult parameters need to add this args  default=70, nargs='?', const=70
percent and quality now is by default
if u want to change the params do it!
'''
# start args
parser = argparse.ArgumentParser()
parser.add_argument('--folder', required=True, help='Path to Folder image')
parser.add_argument('--percent', type=int, required=False, help='percent Resize 5 - 100%. Default 50', nargs='?', default=50, const=50)
parser.add_argument('--dfolder', required=True, help='path destin folder')
parser.add_argument('--quality', type=int, required=False, help='quality JPEG 40-95. Default 70', default=70, nargs='?', const=70)
args = vars(parser.parse_args())  # para que funcione los argumentos
# end args

# convert args in vars
# error in path with special chars
dfolder = str(args['dfolder'])  # destin folder
folder = str(args['folder'] + '/')  # source folder

quality = str(args['quality']  )  # jpeg quality, convert to int for acept the code(no error)

ext = ['png', 'jpg', 'jpeg']  # extension detect

newfldr = os.makedirs(dfolder, exist_ok=True)  # create destination folder 

newfldr  # creating

files = []  # colect all the files in source folder

[files.extend(glob.glob(folder + '*.' + e)) for e in ext]  # trick  collects files names with extension from ext

file_count = len(files)  # total files from source folder

percent = str(args['percent'])  # convert arg in var

scale_percent = args['percent']  # percent use that var

tprint('RFP2W'  )  # This is import art
print(f'{Fore.LIGHTYELLOW_EX}Resize Folder 2 Web V1.13.07.2022 By {Fore.LIGHTBLUE_EX} GOZARCK {Fore.RESET}')
# print('Escala las todas imagenes para poder subirlas a la web ')
print \
    (f'Escalar las imagenes al {Fore.LIGHTGREEN_EX}{percent} % {Fore.RESET}de la carpeta {Fore.LIGHTGREEN_EX}{folder}{Fore.RESET} guardar en {Fore.LIGHTGREEN_EX}{dfolder}{Fore.RESET} calidad al {Fore.LIGHTGREEN_EX}{quality}%{Fore.RESET}')

# progress bar
pbar = tqdm(ncols=100, total=file_count, ascii="░▒█"  )  # progress bar funtion with this line and pbar.update() to the end in def like loop.
def imres(files):  # create this  def . this replace  "for" because this handle  multi threading

    image = cv2.imread(files, cv2.IMREAD_UNCHANGED)  # read image

    head_tail = os.path.split(files)  # split path and u get only filname and extension
    # formula resize percent
    width = int(image.shape[1] * scale_percent / 100)  # width value reading from  image 
    height = int(image.shape[0] * scale_percent / 100)  # height value reading from image
    dim = (width, height)

    resizedPercent = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  # do resize

    img_path = os.path.join \
        (dfolder + '/' + str(head_tail[1]))  # creating de destin folder with the same name like file source

    cv2.imwrite(img_path, resizedPercent, [cv2.IMWRITE_JPEG_QUALITY, int(quality)])  # save the file - resized - with quality jpeg 70

    File_Size = os.path.getsize(files)  # size of file
    File_Size_MB = round(File_Size / 1024 / 1024, 2)  # convert to megabytes
    print_file_size = str(files + str(File_Size_MB) + ' Mb')  # show in console
    pbar.set_description(f'Escalando...{head_tail[1]}'  )  # show resized file
    pbar.update(  )  # progress



def main():  # def main need is created for call def resize (to get no errors)
    while True:
        try:
            with concurrent.futures.ThreadPoolExecutor() as executor  :  # Creating executor
                executor.map(imres, files  )# This call  defimres and this works like a  loop in at for instruciton
                break
        except ValueError:
            print(f'{Fore.LIGHTYELLOW_EX}upsss algo salio mal....')#if something goes wrong



if __name__ == '__main__':  # Now run main(this run all the code)
    main()
    pbar.close(  )  # close progress bar (to get no errors)
finish = time.perf_counter()
print(f'Finished in {Fore.LIGHTYELLOW_EX}{round(finish - start, 2)} {Fore.RESET}seconds')
print(f'{Fore.LIGHTBLACK_EX}Made in python3.8-64-pycharm-cx-Freeze(compiled) ')
