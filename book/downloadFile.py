import requests
import os

#
def download(url, file_path):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0"
    }
    print("download from url:" + url + ", to path:" + file_path)
    r = requests.get(url=url, headers=headers)

    with open(file_path, "wb") as f:
        f.write(r.content)
        f.flush()


if __name__ == '__main__':
    url_pre = "https://pages.cs.wisc.edu/~remzi/OSTEP/Chinese/"
    file_path_pre = "/Users/viskaz/Documents/Pycharm-workSpace/Operating-Systems-Three-Easy-Pieces-NOTES/book/"
    for j in range (0, 6):
        for i in range(0, 10):
            suffix = str(j) + str(i) + ".pdf"
            url = url_pre + suffix
            download(url, file_path_pre +suffix)
