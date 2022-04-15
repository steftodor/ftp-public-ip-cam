var cam_url;
function updateImage() {
    newImage = new Image();
    var new_img_url = cam_url + "?" + new Date().getTime();
    console.log("Fetching image: " + new_img_url);
    newImage.src = new_img_url;
    document.getElementById("img-camera").src = newImage.src;

}
function getCamera(cam_url) {
    this.cam_url = cam_url;
    console.log("Camera URL set: " + cam_url);
    setTimeout(updateImage, 1000);
    setInterval(updateImage, 5000);
}