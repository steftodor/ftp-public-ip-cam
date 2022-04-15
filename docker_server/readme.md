


```
docker run -d \
  --name=camera-ftpfeed \
  -e camera_snap_url= \
  -e capture_interval= \
  -e ftp_url= \
  -e ftp_user= \
  -e ftp_pass= \
  -e ftp_path= \
  --restart unless-stopped \
  steftodor/ftp-public-ip-cam

```
