# RFSoC Frequency Planner
This repository is compatible with [PYNQ image v2.6](https://github.com/Xilinx/PYNQ/releases) for the ZCU111 and RFSoC2x2.

<p align="center">
  <img src="./demonstration.gif" width="884" height="387" />
<p/>

## Quick Start
All that is required to install the RFSoC frequency planner on to your development board is running a simple line of code in the command line. **However, you will need to connect your board to the internet.** Follow the instructions below to install the frequency planner now.
* Power on your RFSoC2x2 or ZCU111 development board with an SD Card containing a fresh PYNQ v2.6 image.
* Navigate to Jupyter Labs by opening a browser (preferably Chrome) and connecting to `http://<board_ip_address>:9090/lab`.
* We need to open a terminal in Jupyter Lab. Firstly, open a launcher window as shown in the figure below:

<p align="center">
  <img src="./open_jupyter_launcher.jpg" width="50%" height="50%" />
<p/>

* Now open a terminal in Jupyter as illustrated below:

<p align="center">
  <img src="./open_terminal_window.jpg" width="50%" height="50%" />
<p/>

* Now simply run the code below that will install the frequency planner to your system.

```sh
pip3 install git+https://github.com/strath-sdr/rfsoc_frequency_planner@rfsoc_studio
```

Once installation has complete you will find the Frequency Planner notebooks in the Jupyter workspace directory. The folder will be named 'frequency-planner'.
