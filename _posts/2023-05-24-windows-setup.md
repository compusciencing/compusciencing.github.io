---
layout: post
title: "ARCS Lab Windows PC Setup"
tags: ["windows", "setup", "how to", "installation"]
author: "Anjali Nuggehalli"
---

Here are some instructions on how to set up a Windows PC for use in the ARCS lab. The campus is currently using Windows 10, and the lab machines are on the campus-wide system. You should have permission to install software, but reach out to Prof Clark if you do not.

At the end, you'll end up with:

- PowerShell
- Windows Terminal
- Visual Studio Code
- Git for Windows
- Unreal Engine 5+ (through the Epic Games Launcher)
- Twinmotion (through the Epic Games Launcher)
- Conda/mamba using Mambaforge for managing programming environments
- And a few other small utilities

# WinGet

WinGet should already be installed, but if it is not, then you will need to install it using [the instructions found here](https://github.com/microsoft/winget-cli).

# PowerShell

There might already be a version of PowerShell installed on the computer, but it’s likely an older version. The older version typically looks like this:

![Older version of Powershell](/assets/2023-05-24-windows-setup/powershellOLD.png)

You can ue this older version to install the newer version with this command:

~~~bash
winget install --scope machine --id Microsoft.Powershell --source winget
~~~

It’ll look like this when you have it installed:

![Newer version of PowerShell](/assets/2023-05-24-windows-setup/powershellNEW.png)

# Windows Terminal

Windows Terminal is a nice GUI application with additional quality-of-life features not present in the default GUI that comes with PowerShell. For example, multiple tabs and better keyboard handling of copying and pasting text.

If you attempt to install Windows Terminal without administrator privileges yuo might see this error message:

![Error Message in installing Windows Terminal](/assets/2023-05-24-windows-setup/errormessage.png)

To mitigate this, right click on the PowerShell icon and hit “Run as Administrator.” Then, run the following command.

~~~bash
winget install --id Microsoft.WindowsTerminal --source winget
~~~

# Visual Studio Code

Download and install [Visual Studio Code using their provided installer](https://code.visualstudio.com/download).

# git For Windows

Download and install [git for Windows using their provided installer](https://gitforwindows.org/).

# Epic Games Laucher

Download and install the [Epic Games Launcher using their installer](https://store.epicgames.com/en-US/download). You can find the email and password to use in the lab notes (contact Prof Clark if you can't find them).

Once you’re all logged in, your Epic Games screen should look like this:

![Epic Games Launcher](/assets/2023-05-24-windows-setup/epicgames.png)

## Unreal Engine Installation and TwinMotion

Next hit "Install Engine" in the top right corner. Since it takes up a bunch of space (over 100 GB) We want to install it on the second drive (not the `C:` where you'll find Windows OS files), so hit “Browse” and then under the “Devices and Drives” tab within your File Explorer, select the non-`C:` disk. Right click, create a new folder called “Programs,” and select this folder to be your install location. Once you select it, you should see something like this: (It was `D:` on my computer, but Prof Clark mentioned that it’ll probably be `E:` on the other computer).

![Installing Unreal Engine](/assets/2023-05-24-windows-setup/unrealengine.png)

Repeat this same process for Twinmotion (The installation tab is also within Epic Games), which should also be installed on the second drive.

# MambaForge

Download and install [Mambaforge using their installer](https://github.com/conda-forge/miniforge#Mambaforge), you might get a notification that it could be harmful to your device. Just run it anyways! You will need to create a new folder within your Programs folder on the second drive and title it "Mambaforge." Select that, and then the installation should proceed. Another note is when searching for the application within your Windows search, type in "Miniforge" to access it.
