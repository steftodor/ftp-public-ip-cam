


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

```
---
version: "2.1"
services:
  camera-ftpfeed:
    image: steftodor/ftp-public-ip-cam
    container_name: camera-ftpfeed
    environment:
      - camera_snap_url=
      - capture_interval=
      - ftp_url=
      - ftp_user=
      - ftp_pass=
      - ftp_path=
    restart: unless-stopped

```
