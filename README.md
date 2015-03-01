VubuntuBox
============

[![GitHub issues](https://img.shields.io/github/issues/JacobJWalker/VubuntuBox.svg)](https://github.com/JacobJWalker/VubuntuBox/issues)

VubuntuBox is an emulated imaging solution for organizations who have a need to have many systems setup with identical software, but run on top of many different types of hardware. It accomplishes this goal by having a modified lightweight form of Ubuntu which runs VirtualBox which in turn runs the main (guest) operating system, thus in essence VubuntuBox acts as middleware between the hardware and the guest operating system - or, as our motto says, "the ultimate hardware abstraction layer".

Brought to you by the [Vubuntu development team](http://vubuntubox.org/wiki/index.php?title=VubuntuBox_Development_Team).

### How-To Make a VubuntuBox CD ###

1. Download Lubuntu Alternative Installer ISO

2. Extract Lubuntu ISO into a folder, we have our folder named VubuntuBox_Files

3. Copy VubuntuBox modified files into the extracted Lubuntu ISO folder and overwrite all files

4.Make a new ISO by running 
            
    $ mkisofs -r -V "VubuntuBox" -cache-inodes -J -l -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table -o "Disk_Images/VubuntuBox.iso" "VubuntuBox_Files/"

5. Boot from the ISO or use a Virtual Machine to test it

### Documentation ###
For further documentation, you can go to [our website](http://www.vubuntuBox.org)
