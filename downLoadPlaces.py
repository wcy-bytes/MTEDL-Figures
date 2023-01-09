import wget
import tempfile
import os

url = 'http://pages.cs.wisc.edu/~huangrui/imagenet_ood_dataset/Places.tar.gz'

# 获取文件名
file_name = wget.filename_from_url(url)
print(file_name)

# 下载文件，使用默认文件名,结果返回文件名
file_name = wget.download(url)