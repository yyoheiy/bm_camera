from ftplib import FTP
from pprint import pprint


from dateutil.relativedelta import relativedelta

from datetime import datetime

ftp=FTP("hachimantai.sakura.ne.jp")
ftp.login("hachimantai","aputuh4urv")
ftp.cwd("www/camera_bm")
#ftp.cwd("www/ftp_test")
#ftp.delete("video18-02-14_18-49-38-42.mkv")
#ftpFile = ftp.nlst()
items=ftp.mlsd()

today=datetime.now()
pday=today-relativedelta(months=3) #3months before



date=int(pday.strftime("%Y%m%d%H%M%S"))

for file,opt in items:
    filedate=int(opt["modify"])
    if filedate<date:
        if len(file)>3:
            ftp.delete(file)
            print(file+" deleted")
        

ftp.quit()
