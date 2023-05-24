---
layout: post
title: "5.24_NOTES_AnjaliN"
tags: ["list", "of", "tags"]
author: "Anjali Nuggehalli"
---

# Installation/Setting up Machine
## AppInstaller and WinGet
AppInstaller and WinGet are already installed for new users - no need to worry about this step!

## PowerShell
PowerShell is already installed on your computer, but it’s the older version. When you search for PowerShell in your Windows search and copy in the command line, it should look like this:

![Older version of Powershell](/assets/2023-05-24-windows-setup/powershellOLD.png)

However, this is the older version of PowerShell. Copy in the new command line to get the updated version. It’ll look like this:


![Newer version of PowerShell](/assets/2023-05-24-windows-setup/powershellNEW.png)

## Windows Terminal
When I tried to install the Windows Terminal within this updated PowerShell, I got this note:


![Error Message in installing Windows Terminal](/assets/2023-05-24-windows-setup/errormessage.png)

To mitigate this, right click on the PowerShell icon and hit “Run as Administrator.” Then, copy in the same command line as before but delete “scope machine.” Not sure why, but it should work after this.

## Visual Studio Code and Git
Installing Visual Studio Code is pretty simple. Download it directly from the App Store rather than copying in any command line because Prof. Clark said we get more features this way. For installing Git, I just pressed next on everything - pretty straightforward.

## Epic Games Laucher
You’ll see in Prof Clark’s instructions that it says to “Create a new email address” because he doesn’t want us to use our personal accounts. I’ll put the new email/password on the shared doc and also stick it here for you to use:
### Login Details
Email: arcslabpomona@gmail.cmo
Password: chirpchirp47!
If you need to enter DOB for whatever reason, use 08/23/2004 (I used my birthday:). The display name is Anjali Nuggehalli. Once you’re all logged in, your Epic Games screen should look like this:


![Epic Games Launcher](/assets/2023-05-24-windows-setup/epicgames.png)

### Unreal Engine Installation and TwinMotion
Then hit "Install Engine" in the top right corner. We don’t want to install it using C: (it’ll take up too much storage), so hit “Browse” and then under the “Devices and Drives” tab within your File Explorer, select the E: disk. Right click, create a new folder called “Programs,” and select this folder to be your install location. Once you select it, you should see something like this: (It was D: on my computer, but Prof Clark mentioned that it’ll probably be E: for you).


![Installing Unreal Engine](/assets/2023-05-24-windows-setup/unrealengine.png)

Repeat this same process for Twinmotion (The installation tab is also within Epic Games). 

## MambaForge
For Mambaforge, you might get a notification that it could be harmful to your device. Just run it anyways!


