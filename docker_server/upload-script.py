from datetime import datetime
import time
import requests
import ftplib
import sys
import os

camera_snap_url = os.environ['camera_snap_url']
capture_interval = int(os.environ['capture_interval'])

ftp_url = os.environ['ftp_url']
ftp_user = os.environ['ftp_user']
ftp_pass = os.environ['ftp_pass']
ftp_path = os.environ['ftp_path']


while(True):
    try:
        ### DOWNLOAD IMAGE FROM CAMERA
        sys.stderr.write(f"{datetime.now()} - Camera : Start Download\n")
        response = requests.get(camera_snap_url, timeout=10)
        if response.status_code == 200:
            with open('temp_capture','wb') as f:
                f.write(response.content)
            upload_src = "temp_capture"
            sys.stderr.write(f"{datetime.now()} - Camera : Download Complete\n")
        else:
            upload_src = "failed_capture.jpg"
            sys.stderr.write(f"{datetime.now()} - Camera : Download Failed\n")
    except:
        upload_src = "failed_capture.jpg"  
        sys.stderr.write("SOMETHING WENT WRONG\n")
    try:
        ### FTP Upload portion
        sys.stderr.write(f"{datetime.now()} - FTP : Start\n")
        session = ftplib.FTP(ftp_url,ftp_user,ftp_pass)    
        sys.stderr.write(f"{datetime.now()} - FTP : Connection established\n")
        with open(upload_src,'rb') as f:
            session.storbinary('STOR '+ftp_path, f)     # send the file
        sys.stderr.write(f"{datetime.now()} - FTP : Image uploaded\n")
        session.quit()
        sys.stderr.write(f"{datetime.now()} - FTP : Connection closed\n")
        time.sleep(capture_interval)
    except:
        sys.stderr.write("SOMETHING WENT WRONG\n")
