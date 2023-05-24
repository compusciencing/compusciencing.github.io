---
layout: post
title: "ARCS Lab Windows PC Setup"
tags: ["windows", "setup", "how to","installation"]
author: "Anjali Nuggehalli"

---

Here's how we set up a Windows PC to use with Unreal Engine 5 and a proper shell to use when connecting to the Pomona HPCs.

# AppInstaller and WinGet

AppInstaller and WinGet are already installed for new users - no need to worry about this step!

# PowerShell

PowerShell is already installed on your computer, but it’s the older version. When you search for PowerShell in your Windows search and copy in the command line, it should look like this:

![Older version of Powershell](/assets/2023-05-24-windows-setup/powershellOLD.png)

However, this is the older version of PowerShell. Copy in the new command line to get the updated version.

~~~bash
winget install --scope machine --id Microsoft.Powershell --source winget
~~~

It’ll look like this when you have it installed:


![Newer version of PowerShell](/assets/2023-05-24-windows-setup/powershellNEW.png)

# Windows Terminal

When I tried to install the Windows Terminal within this updated PowerShell, I got this note:


![Error Message in installing Windows Terminal](/assets/2023-05-24-windows-setup/errormessage.png)

To mitigate this, right click on the PowerShell icon and hit “Run as Administrator.” Then, copy in the following command.

~~~bash
winget install --id Microsoft.WindowsTerminal --source winget
~~~

# Visual Studio Code and Git

Download and install [Visual Studio Code using their provided installer](https://code.visualstudio.com/download).

Follow the same procedure for [installing git](https://gitforwindows.org/).

# Epic Games Laucher

You’ll see in Prof Clark’s instructions that it says to “Create a new email address” because he doesn’t want us to use our personal accounts. I’ll put the new email/password on the shared doc.
Once you’re all logged in, your Epic Games screen should look like this:


![Epic Games Launcher](/assets/2023-05-24-windows-setup/epicgames.png)

## Unreal Engine Installation and TwinMotion

Then hit "Install Engine" in the top right corner. We don’t want to install it using `C:` (it’ll take up too much storage), so hit “Browse” and then under the “Devices and Drives” tab within your File Explorer, select the `E:` disk. Right click, create a new folder called “Programs,” and select this folder to be your install location. Once you select it, you should see something like this: (It was `D:` on my computer, but Prof Clark mentioned that it’ll probably be `E:` on the other computer).


![Installing Unreal Engine](/assets/2023-05-24-windows-setup/unrealengine.png)

Repeat this same process for Twinmotion (The installation tab is also within Epic Games), which should be installed on the other drive. 

# MambaForge

For Mambaforge, you might get a notification that it could be harmful to your device. Just run it anyways!


