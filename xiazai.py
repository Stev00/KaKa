
import wget

def wget_download(url):
    file=wget.download(url)

if __name__ == '__main__':
    a=input('url:')
    wget_download(a)