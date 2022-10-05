
      ______                                   __                                   
     /      \                                 /  |                                  
    /$$$$$$  |  _______   ______   __    __  _$$ |_                                 
    $$ \__$$/  /       | /      \ /  |  /  |/ $$   |                                
    $$      \ /$$$$$$$/ /$$$$$$  |$$ |  $$ |$$$$$$/                                 
     $$$$$$  |$$ |      $$ |  $$ |$$ |  $$ |  $$ | __                               
    /  \__$$ |$$ \_____ $$ \__$$ |$$ \__$$ |  $$ |/  |                              
    $$    $$/ $$       |$$    $$/ $$    $$/   $$  $$/                               
     $$$$$$/   $$$$$$$/  $$$$$$/   $$$$$$/     $$$$/                                
                                               
     _______             __                                                         
    /       \           /  |                                                        
    $$$$$$$  |  ______  $$ |____   __    __   ______    ______    ______    ______  
    $$ |  $$ | /      \ $$      \ /  |  /  | /      \  /      \  /      \  /      \ 
    $$ |  $$ |/$$$$$$  |$$$$$$$  |$$ |  $$ |/$$$$$$  |/$$$$$$  |/$$$$$$  |/$$$$$$  |
    $$ |  $$ |$$    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |$$ |  $$/ 
    $$ |__$$ |$$$$$$$$/ $$ |__$$ |$$ \__$$ |$$ \__$$ |$$ \__$$ |$$$$$$$$/ $$ |      
    $$    $$/ $$       |$$    $$/ $$    $$/ $$    $$ |$$    $$ |$$       |$$ |      
    $$$$$$$/   $$$$$$$/ $$$$$$$/   $$$$$$/   $$$$$$$ | $$$$$$$ | $$$$$$$/ $$/       
                                            /  \__$$ |/  \__$$ |                    
                                            $$    $$/ $$    $$/                     
                                             $$$$$$/   $$$$$$/
                                             
## Purpose
"Scout" is an extendable basic debugger that was designed for use in those cases that there is no built-in debugger / gdb-stub in the debugee process / firmware. The debugger is intended to be used by security researchers in various scenarios, such as:
1. Collecting information on the address space of the debuggee - recon phase and exploit development
2. Exploring functionality of the original executable by accessing and executing selected code snippets
3. Adding and testing new functionality using custom debugger instructions

We have successfully used "Scout" as a debugger in a Linux Kernel setup, and in several embedded firmware research projects, and so we believe that it's extendable API could prove handy for other security researchers in their research projects.

## Read The Docs
https://scout-debugger.readthedocs.io/

### Supported Architectures
* x86 - Intel 32 bit
* x64 - Intel 64 bit
* ARM 32 bit - Little & Big endian (Including Thumb mode)
* AARCH64 - Arm 64 bit - Little & Big endian
* MIPS 32 bit - Little & Big endian (Without Mips16 mode)

##### Future Architectures
* MIPS 16 bit - Little & Big endian
* MIPS 64 bit - Little & Big endian
* ...

### Supported Operating Systems
* Linux - User-mode (PC Mode)
* Linux - Kernel-mode (PC Mode)
* Any Posix-like operating system (Embedded Mode)

## Folder Structure
* **docs:** Documentation files that generated the read-the-docs that was linked above
* **examples:**
  * **embedded_scout** - Use case example for an "Embedded Mode" compilation
  * **kernel_scout** - Use case example for a Linux "Kernel Mode" compilation
* **src**
  * **scout** - Source code for the debugger (core of the server side)
  * **utils** - Python compilation scripts and network API for the client/server
* **tests:** A simple exploit_me.c for checking PIC compiled binaries

## Installation
* Installing the python package: ```python3 setup.py install```
* Dedicated compilers: A list of compilers per-architecture is found on ```compilers.txt```

## Credits
This projects combines together design and compilation tricks that I learned from many fellow researchers during the years.

## Links
Scout was developed and used in our following research projects:
* [Check Point Research - RCE over the FAX protocol](https://research.checkpoint.com/sending-fax-back-to-the-dark-ages)
* [Check Point Research - Say Cheese - Ransomware-ing A DSLR Camera](https://research.checkpoint.com/say-cheese-ransomware-ing-a-dslr-camera)
* [Check Point Research - Don't be Silly - It's Only a Lightbulb](https://research.checkpoint.com/2020/dont-be-silly-its-only-a-lightbulb/)
* [Check Point Research - Would you like some RCE with your Guacamole?](https://research.checkpoint.com/2020/apache-guacamole-rce/)
* [Check Point Research - Linux Kernel MMap vulnerabilities](https://research.checkpoint.com/mmap-vulnerabilities-linux-kernel)

## Maintenance
Scout was developed during my years at Check Point Research, hence the original repository is: https://github.com/CheckPointSW/Scout.
As I fully intened on keeping on maintaining and developing this repository, I forked the repository so to be positioned under my personal Github user.


## Contact
Eyal Itkin

[@EyalItkin](https://twitter.com/EyalItkin)