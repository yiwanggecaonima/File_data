from tqdm import tqdm
import time

for i in tqdm(range(10000)):
    time.sleep(0.01)

from tqdm import tqdm
import time

pbar = tqdm(["a","b","c","d"])
for char in pbar:
    time.sleep(0.5)
    pbar.set_description("processing {}".format(char))

with tqdm(total=100) as pbar:
    for i in range(20):
        time.sleep(0.2)
        pbar.update(5)
