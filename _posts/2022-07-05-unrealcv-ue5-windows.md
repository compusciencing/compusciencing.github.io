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

# Setup PowerShell

I am not a heavy Windows user, but I generally like PowerShell over the older command prompt.

1. Follow Microsoft's instructions for [installing PowerShell on Windows](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2).
2. Setup SSH keys
    - `ssh-keygen -t ed25519 -C "email@address"`
    - Manually copy the contents of your newly created local (on Windows) `~/.ssh/id_ed25519.pub` and append them to the end of the `~/.ssh/authorized_keys` on your server.
3. Add SSH configuration. Here are some examples I like to add to my Windows `~/.ssh/config` file

    ~~~bash
    Host dgx01
        HostName SERVER_HOSTNAME
        User MY_USERNAME

    Host dgx01ucv
        HostName SERVER_HOSTNAME
        User MY_USERNAME
        RemoteForward 9000 localhost:8000
    ~~~

# Setup PuTTY

Although I prefer PowerShell to [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), PowerShell's implementation of SSH is apparently bugged and does not properly work with remote forwarding. So, my RAs will also need PuTTY.

1. Download and install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
2. Use `puttygen` to convert the SSH key created above to a PPK
3. Create a new session
    - Set the "Host Name" and optionally include your username (`user@host`)
    - Setup the needed tunnel (Connection->SSH->Tunnels)
    - Remote
        - Source: `8000` (choose your own port)
        - Destination: `localhost:9000` (UnrealCV uses `9000` by default)
    - Tell PuTTY about the PPK file (Connection->SSH->Auth)
        - Set "Private key file for authentication:"
5. Save the session
6. [Create a shortcut for easy use of session](https://www.smarthomebeginner.com/putty-shortcut-to-saved-session/)

# Setup Unreal Engine 5

My lab is using UE5 for its support of photogrammetry models (via nanite).

1. Install through Epic Games Launcher
2. Update graphics driver if prompted
    - The driver page for [NVIDIA](https://www.nvidia.com/Download/index.aspx?lang=en-us)

# Setup Visual Studio

To compile the UnrealCV plugin, we'll need to install Visual Studio.

1. Download and install [Visual Studio Community 2022](https://visualstudio.microsoft.com/vs/)
2. Include the following options
    - .NET desktop development
    - Desktop development with C++
    - Game development with C++
        - Unreal Engine
    - Individual components
        - .NET Core 3.1 Runtime (LTS)
        - .NET Framework 4.6.2 SDK
    - See [the UE5 documentation](https://docs.unrealengine.com/5.0/en-US/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine/), [the Microsoft documentation](https://devblogs.microsoft.com/visualstudio/installing-the-unreal-engine-in-visual-studio/), and [How to Setup Visual Studio 2022 for Unreal Engine - YouTube](https://www.youtube.com/watch?v=8xJRr6Yr_LU) for more information

# Setup Mambaforge

Although we'll use our Linuz server for the heavy lifting, it is nice to test things out locally on Windows. My preferred method of managing Python is to use []().

1. Install [Mambaforge](https://github.com/conda-forge/miniforge#Mambaforge=).
    - Use all recommended settings
2. Create a PowerShell shortcut
    - Duplicate the installed "Miniforge Prompt" shortcut
    - Replace the target with `%ProgramFiles%\PowerShell\7\pwsh.exe -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\ajcd2020\AppData\Local\mambaforge\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\ajcd2020\AppData\Local\mambaforge' "`

# Setup UnrealCV

We'll first create a conda environment, and we'll use that to build the UnrealCV plugin.

1. Create a conda environment: `mamba create --name NAME python`
2. Activate the environment: `conda activate NAME`
3. Install git: `mamba install git`
4. Clone the UnrealCV fork that has been slightly updated for UE5: `git clone https://github.com/Lap1n/unrealcv.git`
5. Navigate to the local Python package: `cd unrealcv/client/python`
6. Install the local package: `python -m pip install -e .`
7. Navigate to the root: `cd ../..`
8. Build the plugin: `python build.py --UE4 "C:\Program Files\Epic Games\UE_5.0"`

# Setup a UE5 Binary

Now we'll put this all together to start an Unreal Engine binary and connect to it from a server.

1. Launch UE5 and create a new project using the "Game+Blank+C++" options.
2. Close the project after it opens (it will open Visual Studio as well as UE5).
3. Copy the "Plugins" directory from the unrealcv directory to the newly created project directory.
4. Reopen the UE5 project.
    - The UnrealCV plugin should already be enabled at this stage.
5. Click the button to package a binary for Windows.
6. Edit the `Windows\PROJECT\Saved\Config\Windows\GameUserSettings.ini` file.
    - Update `ResolutionSizeX` and `Y`
    - Update `LastUserConfirmedResolutionSizeX` and `Y`
    - Update `FullscreenMode=2`
    - Update `LastConfirmedFullscrenMode=2`
7. Edit the `Windows\PROJECT\Binaries\Win64\unrealcv.ini` file if needed.
8. Launch the binary.
9. SSH to your server with remote port forwarding using PuTTY.
10. Once this PuTTY connection is active, you can switch to a terminal of your choice.
    - Make certain that ports match between UnrealCV, PuTTY, and the client on the server.
