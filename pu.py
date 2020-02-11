import os
import shutil
src=input("enter the source")
dst=input("enter the destination")
shutil.rmtree(dst)
os.mkdir(dst)
shutil.rmtree(dst)
shutil.copytree(src,dst)
