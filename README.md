Descartes' Daemon
=================

[![GitHub issues](https://img.shields.io/github/issues/JacobJWalker/DescartesDaemon.svg)](https://github.com/JacobJWalker/VubuntuBox/issues)

### Technical Description
Descartes' Daemon is an emulated imaging solution for organizations who have a need to have many systems setup with identical software, but run on top of many different types of hardware. It accomplishes this goal by having a modified lightweight form of Ubuntu which runs VirtualBox which in turn runs the main (guest) operating system, thus in essence Descartes' Daemon acts as middleware between the hardware and the guest operating system - or, as our motto says, "the ultimate hardware abstraction layer".

### Simple Explaination
Virtual machines are essentially simulated hardware that you can run an operating system (guest) in, making the guest blissfully unaware that it is not, in fact, running directly on hardware (bare metal/host). 

![Diagram showing how a VM is set up](https://ryantrotz.com/wp-content/uploads/2011/11/guest-os-virtualization.png)

While this works well, traditional methods of running a virtual machine require you to load an interface or otherwise interact with the host operating system in order to do certain functions with the guest opersating system such as mount a USB drive, or even treating the guest as a lesser and something not to primarily do functions in. 

![A screenshot of Virtualbox](http://screenshots.en.sftcdn.net/en/scrn/58000/58734/oracle-vm-virtualbox-6.jpg)
>A screenshot of Virtualbox, a virtual machine management software


Descartes' Daemon's goal is to make that layer between the hardware and the guest as thin/invisable as possible. We want the users to not even notice that the machine is not really running whatever guest operating system it displays, but rather runs on top of Linux!

![A screenshot of Windows Vista](http://img06.deviantart.net/0761/i/2009/029/0/f/windows_vista_default_login_11_by_raulwindows.jpg)
>A screenshot of what Vista would look like inside of Descartes' Daemon. Notice how it looks like it's running on the hardware!

# Goals
- Zero/One touch install
- Stable base
- Easy to use virtual machine management
- As little overhead as possible (speed is key!)
- No obstruction of hardware to guest

### How-To Make a Descartes' Daemon CD ###

1. [Download Ubuntu Server 14.04.02 i386 ISO](http://old-releases.ubuntu.com/releases/trusty/)

2. Extract Ubuntu Server ISO into a folder, we have our folder named DescartesDaemon_Files

3. Copy DescartesDaemon modified files into the extracted  Ubuntu Server ISO folder and overwrite all files

4. Make a new ISO by running 
            
         $ mkisofs -r -V "DescartesDaemon" -cache-inodes -J -l -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o "Disk_Images/DescartesDaemon.iso" "DescartesDaemon_Files/"

5. Boot from the ISO or use a Virtual Machine to test it

##### Credits
Brought to you by the [Descartes' Daemon development team](https://github.com/JacobJWalker/DescartesDaemon/graphs/contributors).
