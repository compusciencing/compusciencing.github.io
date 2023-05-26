---
layout: post
title: "ARCS Lab Windows PC Setup"
tags: ["windows", "setup", "how to", "installation"]
author: "Anjali Nuggehalli"
---

Here are some instructions on how to set up a Windows PC for use in the ARCS lab. The campus is currently using Windows 10, and the lab machines are on the campus-wide system. You should have permission to install software, but reach out to Prof Clark if you do not.

**Please install software for all users whenever given the chance.**

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

To mitigate this, right click on the PowerShell icon and hit "Run as Administrator." Then, run the following command.

~~~bash
winget install --id Microsoft.WindowsTerminal --source winget
~~~

# MambaForge

Begin by creating a folder named "Programs" on the second drive (not the `C:` where you'll find Windows OS files). On one lab machine the second drive is called the `D:` and on the other it is called the `E:`. Create a folder named "Mambaforge" inside "Programs" and then download and install [Mambaforge using their installer](https://github.com/conda-forge/miniforge#Mambaforge). You might get a notification that it could be harmful to your device. Just run it anyways! When asked for an installation location make sure you choose the non-`C:`.

You can launch the Mambaforge shell by running the `miniforge` prompt, but I recommend using Windows Terminal. You can create a "Mambaforge" profile by

1. Click on the down arrow next to the plus sign (in the top bar to the right of the tabs) and select "Settings."
2. Scroll down on the left pane and click "Add a new profile."
3. Duplicate the "PowerShell" profile.
4. Change the following fields:
  - Name to `Mambaforge`
  - Command line to `pwsh.exe -ExecutionPolicy ByPass -NoExit -Command "& 'D:\Programs\Mambaforge\shell\condabin\conda-hook.ps1' ; conda activate 'D:\Programs\Mambaforge' "` 

# Utilities

Install the following applications using their installers

- [Visual Studio Code](https://code.visualstudio.com/download)
- [git for Windows](https://gitforwindows.org/)
- [7-Zip](https://www.7-zip.org/) (install the 64-bit version onto local drive)
- [Git LFS](https://git-lfs.com/)
- [Slack](https://slack.com/downloads/windows)
- [Zoom](https://zoom.us/download)

You'll also need to download [Open Stage Control](https://openstagecontrol.ammd.net/). It does not come with an installer. Instead, you will download the zip file and extract it to the "Programs" folder that you created earlier.

# Epic Games Laucher, Unreal Engine, and TwinMotion

Download and install the [Epic Games Launcher using their installer](https://store.epicgames.com/en-US/download). You can find the email and password to use in the lab notes (contact Prof Clark if you can't find them).

Once you’re all logged in, your Epic Games screen should look like this:

![Epic Games Launcher](/assets/2023-05-24-windows-setup/epicgames.png)

Next hit "Install Engine" in the top right corner. Since it takes up a bunch of space (over 100 GB) We want to install it on the second drive (not the `C:` where you'll find Windows OS files), so hit “Browse” and then under the “Devices and Drives” tab within your File Explorer, select the non-`C:` disk. Right click, create a new folder called “Programs,” and select this folder to be your install location. Once you select it, you should see something like this: (It was `D:` on my computer, but Prof Clark mentioned that it’ll probably be `E:` on the other computer).

![Installing Unreal Engine](/assets/2023-05-24-windows-setup/unrealengine.png)

Repeat this same process for Twinmotion (The installation tab is also within Epic Games), which should also be installed on the second drive.