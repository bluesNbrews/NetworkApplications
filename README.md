![NetworkApplications1](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/networkApplications.png)

![NetworkApplications2](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/network.png)

# Network Applications

> 1 completed project, 1 pending

## Author

👤 **Steven Williams**

* Github: [@bluesNbrews](https://github.com/bluesNbrews)

* Twitter: [@wsm9671](https://twitter.com/wsm9671)

## Recommended Environment / Setup

> 3 Arista virtual switches

You will need to create an account (https://eos.arista.com/user-manager/?action=login) with Arista. Once you have an account and log in, go to the bottom of the page and click "Software Downloads" under the Support heading. Scroll down and expand vEOS-lab -> 4.20. Click on  vEOS-lab-4.20.14M.vmdk to download. You will also need to expand vEOS-lab -> aboot and click on Aboot-veos-8.0.0.iso to download.

> Virtual Box - Version 6.0.10 (a newer release should work fine)

Download here: https://www.virtualbox.org/wiki/Downloads. You will need to setup the vmdk and iso files. There is some configuration involved to be able to network with your host PC.

> Python 3.6.5 - See packages below (recommend using virtual environment)

![NetworkApplications3](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/reqModules.png)

## Project 1 - Switch Configuration via Secure Shell (SSH)

The objective of this project is to automate commands on one or more switches using Python. 

There are 3 files that can be used for configuration - username(s)/password(s), commands, and Internet Protocol (IP) addresses. The program will first check that the files are valid and that the IP addresses can be reached via ping.

![NetworkApplications4](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/checks.png)

If the checks pass, then the program will run the commands below on all 3 Arista switches (must be running in Virtual Box). The ouput from the switches will need to be cleaned up for better readability, this is an arbitrary example to show the functionality. 

![NetworkApplications5](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/cmd.png)

![NetworkApplications6](https://github.com/bluesNbrews/NetworkApplications/blob/master/img/commandOutput.png)

## Show your support

Give a ⭐️ if this project helped you!
