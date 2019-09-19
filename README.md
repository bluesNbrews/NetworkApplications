![NetworkApplications1](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/networkApplications.png)

![NetworkApplications2](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/network.png)

# Network Application - Projects from the Udemy Course Python 3 Network Programming

> 5 total projects

## Creator (taught by Milhai Catalin Teodosiu)

👤 **Steven Williams**

* Github: [@bluesNbrews](https://github.com/bluesNbrews)

* Twitter: [@wsm9671](https://twitter.com/wsm9671)

## Recommended Environment / Setup

> 3 Arista virtual switches

You will need to create an account (https://eos.arista.com/user-manager/?action=login). Once you have an account, go to the bottom of the page and click "Software Downloads" under the Support heading. Scroll down and expand vEOS-lab->4.20. Click on  vEOS-lab-4.20.14M.vmdk to download. You will also need to expand vEOS-lab->aboot and click on Aboot-veos-8.0.0.iso to download.

> Virtual Box - Version 6.0.10 (a new release should be fine)

Download here: https://www.virtualbox.org/wiki/Downloads. You will need to setup the vmdk and iso files.

> Python 3.6.5 - See packages below (recommend using virtual environment)

![NetworkApplications3](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/)

## Project 1 - Switch Configuration via Secure Shell (SSH)

The objective of this project is to automate commands on one or more switches using Python. 

There are 3 files that can be used for configuration - username(s)/password(s), commands, and Internet Protocol (IP) addresses. The program will first check that the files are valid and that the IP addresses can be reached via ping.

![NetworkApplications4](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/)

If the checks pass, then the program will run the commands below on all 3 Arista switches (must be running in Virtual Box). The ouput from the switches will need to be cleaned up for better readability, this is an arbitrary example to show the functionality. 

![NetworkApplications5](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/)

![NetworkApplications6](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/)

## Show your support

Give a ⭐️ if this project helped you!
