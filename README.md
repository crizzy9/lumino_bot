
# Lumino Bot
Inspired from Master Pi by Hiwonder

[Master Pi Instructions Drive](https://drive.google.com/drive/folders/19wOOF4T_N37y_SSklHbo7DnL76_P_NWb?usp=drive_link)

[Master Pi Image Drive](https://drive.google.com/drive/folders/1HFL5PVNSByu93iu684BVlrJzYYIZY8RH?usp=drive_link)

## Installation

```sh
chmod +x ./install
./install
```

## Adjusting servos

Make minor adjustments to a servo using Read and Save Deviation mechanism
[Deviation Adjustments](https://drive.google.com/drive/folders/17HpnMlfOHrpZfOgUnjLjHC9Nm85yQIAx)

## Using Wifi

[Wifi instructions](https://drive.google.com/drive/folders/1sNx4BD5YbgNLipkGx8u_dNLvZyD7gXnA)

```sh
ls -la /etc/systemd/system
ls -la /lib/systemd/system
```

## Running the App

```sh
cd lumino_bot
chmod +x runapp.py
./runapp.py arm
cd lumino_bot

// to run qt5 gui
sudo lumino_car/Arm.py
// or
chmod +x runapp.py
python3 runapp.py arm


// if doesnt work set dtparam=i2c_arm=on in /boot/config.txt
vim /boot/config.txt
dtparam=i2c_arm=on
```
