# CSC 196P - Proof of Concept - Project 1: RFID

This project is to demonstrate one's ability to utilize technologies and the
cloud (via [Firebase](https://firebase.google.com/)).

I will be using Radio Frequency Identification (RFID) as a means to demonstrate
my understanding of both the technology and how to make some kind service/tool
with the cloud.

- [CSC 196P - Proof of Concept - Project 1: RFID](#csc-196p---proof-of-concept---project-1-rfid)
  - [Assets](#assets)
    - [Hardware](#hardware)
    - [Software](#software)
  - [Implementations](#implementations)
    - [Python](#python)
  - [Resources](#resources)

## The Course [CSC 196P: Cloud and Mobile Computing Pragmatics](https://catalog.csus.edu/search/?search=CSC+196P)

Prerequisite(s): [CSC 134: Database Management Systems](https://catalog.csus.edu/search/?P=CSC%20134), [CSC 138: Computer Networking Fundamentals](https://catalog.csus.edu/search/?P=CSC%20138), and [CSC 139: Operating System Principles](https://catalog.csus.edu/search/?P=CSC%20139)

Introduction to cloud computing. Cloud services. Deployment options. The installation,
configuration, and deployment of a cloud infrastructure based upon industrial standards.
Step-by-step cloud setup as well as the development of scripts for automated deployment.
The installation, building, deployment, testing, and provisioning of a multi-tier
cloud based mobile application as a cloud service.

## Assets

### Hardware

1. [Raspberry Pi 4 Model B (8 GB)](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)
   1. Update: `sudo apt update`
   2. Upgrade: `sudo apt full-upgrade`
2. [ELEGOO UNO R3 Project Most Complete Starter Kit with Tutorial Compatible with Arduino IDE (63 Items)](https://www.amazon.com/gp/product/B01CZTLHGE/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
   1. [RC522 Reader Module with key fob and Card](https://www.amazon.com/SunFounder-Mifare-Reader-Arduino-Raspberry/dp/B07KGBJ9VG)
   2. [Breadboard](https://www.amazon.com/BB830-Solderless-Plug-BreadBoard-tie-Points/dp/B0040Z4QN8/ref=sr_1_1?crid=RA8UZ60586KY&dib=eyJ2IjoiMSJ9.iQcZZ-eAyQqEzQo4dHwB32MKalyzq4GZaioeVOzl7FJR0t6rDtX-aVJZudcf06LDI59FSTAdFAhLYDKOrMYKQ9myWkpLrDWU2HmKNkX0bJ8.P97ZdzIGA00xynAeSRNYlgWSAy39nUhXqaU-VnmzAYM&dib_tag=se&keywords=BB830+Breadboard&qid=1711091655&refinements=p_72%3A1248921011&rnid=1248919011&s=industrial&sprefix=bb830+breadboard%2Caps%2C255&sr=1-1)
3. [CanaKit Raspberry Pi GPIO Breakout Board Bundle](https://www.canakit.com/raspberry-pi-gpio-breakout-bundle.html)
   1. 40-Pin T-Shaped (Assembled) Breakout Board and Ribbon Cable
4. [ELECROW Small Monitor 10.1 Inch Mini Monitor](https://www.amazon.com/gp/product/B076GZVCP2/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
5. [Raspberry Pi Keyboard and Hub](https://www.raspberrypi.com/products/raspberry-pi-keyboard-and-hub/)
6. [Raspberry Pi Mouse](https://www.raspberrypi.com/products/raspberry-pi-mouse/)

### Software

[Setup TigerVNC server (Windows)](https://github.com/TigerVNC/tigervnc/wiki/Setup-TigerVNC-server-%28Windows%29)

## Implementations

### Python

1. `pip install -r requirements.txt`

## Resources

- [circuitbasics: HOW TO USE RFID CARDS WITH A RASPBERRY PI Posted by Harry Mafukidze](https://www.circuitbasics.com/what-is-an-rfid-reader-writer/)
- [components101: RC522 RFID Module Pin Configuration](https://components101.com/wireless/rc522-rfid-module)
- [Connect To Firebase In Python](https://www.youtube.com/watch?v=M1JjK9DXC6U&ab_channel=TheAssembly)
- [Firebase - Back to the Basics](https://www.youtube.com/watch?v=q5J5ho7YUhA&ab_channel=Fireship)
- [Firebase Quickstart by Jeff Delaney](https://fireship.io/lessons/firebase-quickstart/)
- [lastminuteengineers: What is RFID? How It Works? Interface RC522 RFID Module with Arduino](https://lastminuteengineers.com/how-rfid-works-rc522-arduino-tutorial/)
- [pimylifeup: How to Set Up a Raspberry Pi RFID RC522 Chip](https://pimylifeup.com/raspberry-pi-rfid-rc522/)
- [Raspberry Pi documentation: Raspberry Pi hardware - GPIO and the 40-pin header](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
- [raspberrypi-spy: RC522 RFID Tag Reading with the Raspberry Pi](https://www.raspberrypi-spy.co.uk/2018/02/rc522-rfid-tag-read-raspberry-pi/)
- [Robotix: An introduction to a RFID](https://www.robotix.in/tutorial/auto/RFID/)
