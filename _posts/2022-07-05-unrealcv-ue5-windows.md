---
layout: post
title: "Using UnrealCV with Unreal Engine 5 on Windows"
tags: ["unrealcv", "unreal engine", "windows"]
author: "Anthony J. Clark"
include_mathjax: false
---

[UnrealCV](https://unrealcv.org/) is a fantastic tool for interacting with Unreal Engine from an external program. For example, in my research lab, we use it to collect datasets for computer vision projects using a Python script.

Unfortunately, the documentation is a bit out-of-date, and the owners of the repository are not very receptive to pull requests. So I am documenting the process here for my research assistants (RAs).

Here is what we are trying to achieve: **package a Windows binary with UnrealCV and communicate with the locally running binary from a server running Linux.**

Throughout this document, words in **ALL_CAPS** denote something that you must fill in for yourself.

# Setup PowerShell

I am not a heavy Windows user, but I generally like PowerShell over the older command prompt.

1. Follow Microsoft's instructions for [installing PowerShell on Windows](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2).
2. Setup SSH keys
    - (On Windows) Generate SSH keys: `ssh-keygen -t ed25519 -C "EMAIL@ADDRESS"`
    - (On Windows) Copy the contents of `~/.ssh/id_ed25519.pub`
    - (On Linux) Append the contents to `~/.ssh/authorized_keys`
3. Add some SSH configuration. Here are some examples I like to add to my Windows `~/.ssh/config` file

    ~~~bash
    # Quickly login to SERVER_HOSTNAME with: ssh NICKNAME1
    Host NICKNAME1
        HostName SERVER_HOSTNAME
        User MY_USERNAME

    # Quickly login to SERVER_HOSTNAME using port forwarding with: ssh NICKNAME2
    Host NICKNAME2
        HostName SERVER_HOSTNAME
        User MY_USERNAME
        RemoteForward 9000 localhost:8000
    ~~~

# Setup PuTTY

Although I prefer PowerShell to [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), PowerShell's implementation of SSH is apparently bugged and does not properly work with remote forwarding. So, my we'll also need PuTTY.

1. Download and install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html).
2. Use `puttygen` to convert the SSH key created above to a PPK.
    - Load `~/.ssh/id_ed25519`
    - Save private key
3. Create a new session.
    - Set the "Host Name" and optionally include your username (`USER@HOST`)
    - Setup the needed tunnel (Connection->SSH->Tunnels)
        - Check "Remote"
        - Source: `8000` (choose your own port as appropriate)
        - Destination: `localhost:9000` (UnrealCV uses `9000` by default)
    - Tell PuTTY about the PPK file (Connection->SSH->Auth)
        - Set "Private key file for authentication:" to the newly converted key
    - Save the session (Session dialog box)
4. Optionally [create a shortcut for easy use of session](https://www.smarthomebeginner.com/putty-shortcut-to-saved-session/).

# Setup Unreal Engine 5

My lab is using UE5 for its support of photogrammetry models (via nanite).

1. Install [UE5 through the Epic Games Launcher](https://www.unrealengine.com/en-US/download) (this is the primary method Epic Games provides).
2. Update graphics driver if prompted.
    - The driver page for [NVIDIA](https://www.nvidia.com/Download/index.aspx?lang=en-us)

# Setup Visual Studio

We will need to install Visual Studio and some of its extras so that we can compile the UnrealCV plugin.

1. Download [Visual Studio Community 2022](https://visualstudio.microsoft.com/vs/).
2. Install with the following options:
    - .NET desktop development
    - Desktop development with C++
    - Game development with C++ with the extra component called
        - Unreal Engine
    - Individual components
        - .NET Core 3.1 Runtime (LTS)
        - .NET Framework 4.6.2 SDK

Here are some additional resources:

- [The UE5 documentation](https://docs.unrealengine.com/5.0/en-US/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine/)
- [The Microsoft documentation](https://devblogs.microsoft.com/visualstudio/installing-the-unreal-engine-in-visual-studio/) for Unreal Engine
- [A YouTube video walking through the steps](https://www.youtube.com/watch?v=8xJRr6Yr_LU)

# Setup Mambaforge

Although we'll use our Linux server for the heavy lifting, it is nice to test things out locally on Windows. My preferred method of managing Python is to use [Mamba](https://mamba.readthedocs.io/en/latest/installation.html).

1. Download and install [Mambaforge](https://github.com/conda-forge/miniforge#Mambaforge=).
    - Use all recommended settings
2. Create a PowerShell shortcut
    - Duplicate the installed "Miniforge Prompt" shortcut
    - Replace the target with

    ~~~
    %ProgramFiles%\PowerShell\7\pwsh.exe -WorkingDirectory ~ -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\ajcd2020\AppData\Local\mambaforge\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\ajcd2020\AppData\Local\mambaforge' "
    ~~~

# Setup UnrealCV

We'll first create a conda environment, and then we'll use that to build the UnrealCV plugin.

1. Create a new conda environment:

    ~~~bash
    # This will create a new environment with Python3 and git installed.
    mamba create --name NAME python git
    ~~~

2. Activate the environment:

    ~~~bash
    # Yes, you'll use `conda` here
    conda activate NAME
    ~~~

4. Clone the UnrealCV fork that has been slightly updated for UE5:

    ~~~bash
    git clone https://github.com/Lap1n/unrealcv.git
    ~~~

5. Navigate to the local Python package:

    ~~~bash
    cd unrealcv/client/python
    ~~~

6. Install the local package:

    ~~~bash
    python -m pip install -e .
    ~~~

7. Navigate to the repository root:

    ~~~bash
    cd ../..
    ~~~

8. Build the plugin:

    ~~~bash
    python build.py --UE4 "C:\Program Files\Epic Games\UE_5.0"
    ~~~

# Setup a UE5 Binary

Now we'll put this all together to start an Unreal Engine binary and connect to it from a server.

1. [Modify the specified UE5 config file](https://docs.unrealcv.org/en/master/plugin/package.html#modify-an-ue4-config-file) (section 1 of this article). This only needs to be completed one time for the UE5 installation.
2. Launch UE5 and create a new project using the "Game + Blank + C++" options.
    - The official UnrealCV documentation states to use a "First Person + BluePrint" project, but using a BluePrint leads to errors. You can use "First Person" if it is useful.
3. Close the project after it opens (it will open Visual Studio as well as UE5).
4. Copy the "Plugins" directory from the unrealcv directory to the newly created project directory.
5. Reopen the UE5 project.
    - The UnrealCV plugin should already be enabled at this stage. But if it is not, manually enable by going to settings in the UE5 project, clicking 'Plugins', and searching for 'Unreal CV'. If it not already enabled, you will have to close and reopen UE5 after enabling it. 
6. Click the button to package a binary for Windows and wait for it to build.
    - Note: originally this could be done via the 'File' tab on the taskbar. But on most recent UE5.1 update, this option has been moved and the documentation does not match the UI. You must go to 'Platforms' (near the play button) -> 'Windows' -> 'Package Project'.
7. Edit the `Windows\PROJECT\Saved\Config\Windows\GameUserSettings.ini` file.
    - Update `ResolutionSizeX` and `Y` to your preferences
    - Update `LastUserConfirmedResolutionSizeX` and `Y` to your preferences
    - Set `FullscreenMode=2`
    - Set `LastConfirmedFullscreenMode=2`
8. Edit the `Windows\PROJECT\Binaries\Win64\unrealcv.ini` file if needed.
    - It makes sense to at least set the resolution to match.
9. Launch the binary.
10. SSH to your server with remote port forwarding using PuTTY.
11. Once this PuTTY connection is active, you can switch to a terminal of your choice.
    - Make certain that ports match between UnrealCV, PuTTY, and the client on the server.
12. Activate any needed environment on the server and open a Python REPL.
13. Press play in your UE5 project.
    - Requests are not able to be returned if not in play mode.
14. Test the connection using the following commands:

    ~~~python
    from unrealcv import Client
    client = Client(('localhost', 9000))
    client.connect(timeout=5)
    ~~~

If all goes well, you see a confirmation message stating the the connection occurred in both terminal and the UE5 output log. You may also want to ensure your able to complete requests via the following command:

~~~python
client.request('vget /unrealcv/status')
~~~

If you see a message that says something along the lines of "Is Listening", you should be fine. 

If you run into a port connection error:
1. Check if the client port and UE5 project port are the same.
    - Search 'Port' in the 'Output Log' of your project and use whatever port it specifies as default in your creation of the Client object.
2. Check if the port UE5 is using is in use. You may need to [kill the process that is using the port](https://stackoverflow.com/questions/39632667/how-do-i-kill-the-process-currently-using-a-port-on-localhost-in-windows) then restart UE5.

We should also put the project under version control. Here is one method:

1. Create a repository on the host (e.g., GitHub).
2. Clone the repository to a temporary directory.
3. Move the contents of the temporary directory into the UE5 project directory.
4. Install git lfs `git lfs install`.
5. Add the following `.gitattributes` file (and modify as needed).
   ~~~bash
   # UE file types
   *.uasset filter=lfs diff=lfs merge=lfs -text
   *.umap filter=lfs diff=lfs merge=lfs -text
   
   # Raw Content types
   *.fbx filter=lfs diff=lfs merge=lfs -text
   *.3ds filter=lfs diff=lfs merge=lfs -text
   *.psd filter=lfs diff=lfs merge=lfs -text
   *.png filter=lfs diff=lfs merge=lfs -text
   *.mp3 filter=lfs diff=lfs merge=lfs -text
   *.wav filter=lfs diff=lfs merge=lfs -text
   *.xcf filter=lfs diff=lfs merge=lfs -text
   *.jpg filter=lfs diff=lfs merge=lfs -text
    ~~~
6. Check for untracked files with: `git -C "$(git rev-parse --show-cdup)" ls-files --others --exclude-standard -z | xargs -0 ls -lR | awk '{sum += $5; print $5 "\t" $9}END{print sum}' | numfmt --field=1 --to=iec | sort -h | column -t`
7. Remove all unused assets (Content Drawer -> Add an asset filter. -> Other Filters -> Not Used In Any Level).
8. Use repository normally.
