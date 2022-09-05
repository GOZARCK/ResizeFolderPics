# ResizeFolderPics


Resize all the images in the folder and save it.
------------
This script resize all pics in folder with cv2 multithread
this is super faster🚀.
the pics are ready resized for shared to  the web.

###### base requerimets

- python3.8
- cv2
- argparse
- art
- colorama
- tqdm

<sub>  made it with pycharm-comunity and using his venv. </sub> 


How to use?
-----------
Is very easy.

--folder "folder contain files to resize"

--dfolder "Destin folder"

--percent "Resize percent"

--quality "Quality of pics(jpeg)"


example:
cmd windows
```

python main --folder pic --percent 50 --dfolder pics_resized --quality 40
```
or in linux
```sh
./venv/bin/python main --folder pic --percent 50 --dfolder pics_resized --quality 40
```

windows
-------
<h7>Run the script main  with python3.8<br>
or <br>
Compile the script with cx-freeze(using the setup code)
</h7>

Linux
-------------
----run in bash-----

For create bash in linux first says this is a bash with the line below

#!/bin/bash

now the code

./venv/bin/python main

chmod +x main

chmod 777 main 

the extension .py u can delete bc is not necesary


run this script bash.

./ResizeFolderPics.sh

List to do
-----------
- [x] Public my code

