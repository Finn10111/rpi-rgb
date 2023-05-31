# rpi-rgb

Very basic prototype of application for Raspberry Pi and Neopixel / ws281x LED strips. More to There's more to come.

## Installation

Note: Please have in mind a lot of paths are hardcoded at the moment (webserver path for example).

Please have in mind that you need to connect an external power supply if you want to use a lot of LEDs. Each LED uses up to 60mA, my Pi Zero has a 2A power supply and everything works fine with 24 LEDs.

First, if possible, disable sound on your Pi to gain more performance:

    echo "blacklist snd_bcm2835" > /etc/modprobe.d/snd-blacklist.conf
    sed -i 's/dtparam=audio=on/#dtparam=audio=on/' config.txt
    reboot

Clone this repository, install dependencies and set up environment:

    git clone https://gitea.pimux.de/finn/rpi-rgb.git /var/www/vhosts/rgb.local
    apt-get install apache2 libapache2-mod-wsgi-py3 python3-virtualenv python3-pip
    cd /var/www/vhosts/rgb.local
    virtualenv .
    . bin/activate
    pip install -r requirements.txt
    cp apache-rgb.conf /etc/apache2/sites-available
    a2ensite apache-rgb
    systemctl reload apache2

Then connect your Neopixel LEDs to the Pi.

    VCC -> Pin 2 5V
    GND -> Ground (e.g. pin 6, 9, 14...)
    DATA -> GPIO18 (pin 12)

Copy rgb.py to `/usr/local/bin` so the systemd service can use it. Then setup system file:

    cp rgb.py /usr/local/bin
    cp rgb.service /etc/systemd/system/
    systemctl daemon-reload
    systemctl enable rgb
    systemctl start rgb

Now put your Pi's IP address in any web browser and enjoy.
