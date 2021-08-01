from tqdm import tqdm 

from time import sleep 

  

  

for i in tqdm(range(0, 100), ncols = 90,

               desc ="Tunggu su"):

    sleep(.1)
