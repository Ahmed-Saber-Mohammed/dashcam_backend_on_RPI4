# dashcam_backend_on_RPI4

##here is how to setup ngrok

uname -m
upon your Pi's architecture choose the right ngrok binary

wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar -xvzf ngrok-v3-stable-linux-arm64.tgz
sudo mv ngrok /usr/local/bin


ngrok config add-authtoken YOUR_NGROK_TOKEN

ngrok http 5000

http://<your_public_ip_(forward)>:5000/detection_videos
