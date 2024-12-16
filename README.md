# SaTC: EDU: Developing Ready-to-Use Hands-on Labs with Portable Operating Environments for Digital Forensics Education

Please find the project website [here](https://wp.wpi.edu/infer/).

## How to download and use this Repository

### Prerequisites

1. Install [Git](https://git-scm.com/downloads)

### Instructions

1. Open your terminal of choice and run the following command for either SSH or HTTPS:
   ```bash
   git clone git@github.com:WPI-LIONS-Group/INFER.git
   ```
   Using HTTPS
   ```bash
   git clone https://github.com/WPI-LIONS-Group/INFER.git
   ```
   At this stage the repository should be cloned to your local machine but all the submodules are not yet initialized so they will show as empty directories.

2. Change directory to the cloned repository:
   ```bash
   cd INFER
   ```

3. Initialize the submodules:
   ```bash
    git submodule update --init --recursive
    ```

## How to use the lab materials

Each lab will have a Release that contains and `iso` file. This `iso` file is contains all the necessary files have when performing the labs. You can attach these `iso` files to virtual machines using a virtual DVD drive on VMWare.

### How to use an ISO file in VMWare

1. Go to the INFER repository and navigate to the [Release section](https://github.com/WPI-LIONS-Group/INFER/releases).

2. Download the `iso` file for the lab you want to perform.
   ![ISO Page](.github/imgs/Screenshot%20from%202024-12-16%2008-56-12.png)

3. Open VMWare and power on the virtual machine you want to use the `iso` file with. (Some labs may require you to mount the `iso` file to the virtual machine before powering it on)
   ![VMWare](.github/imgs/Screenshot%20from%202024-12-16%2009-06-07.png)

4. Click on VM on the top menu bar and navigate to settings. This will open the settings window for the virtual machine. On that menu click on CD/DVD (SATA) and then click on the Use ISO image file option. This will open a file picker dialog where you can select the `iso` file you downloaded. Save the settings and close the settings window.
   ![Settings](.github/imgs/Screenshot%20from%202024-12-16%2009-09-58.png)

5. Then on the bottom right corner of the VMWare window you will see a CD icon. Click on that and select the Connect option. This will mount the `iso` file to the virtual machine.

6. The lab files will be available in the virtual machine and you can start performing the lab.