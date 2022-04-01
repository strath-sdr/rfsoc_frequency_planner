<img src="./strath_banner.png" align="left">

# RFSoC Frequency Planner
This RFSoC Frequency Planning tool is derived from an original tool released by Xilinx for their Zynq Ultrascale+ RFSoC line of devices. The original tool, and more information about the RFSoC can be found [here](https://www.xilinx.com/products/silicon-devices/soc/rfsoc.html).

This repository consists of two branches. The ```main``` branch is used for the standalone web application that is hosted on [Heroku](https://rfsoc-frequency-planner.herokuapp.com/). The ```rfsoc_studio``` branch is compatible with [PYNQ image v2.7](https://github.com/Xilinx/PYNQ/releases).

<p align="center">
  <img src="./demonstration.gif" />
<p/>

## PYNQ Quick Start
All that is required to install the RFSoC frequency planner on to your development board is running a simple line of code in the command line. **However, you will need to connect your board to the internet.** Follow the instructions below to install the frequency planner now.
* Power on your PYNQ enabled development board with an SD Card containing a fresh PYNQ v2.7 image.
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
pip3 install git+https://github.com/strath-sdr/rfsoc_frequency_planner
```

Once installation has complete you will find the Frequency Planner notebooks in the Jupyter workspace directory. The folder will be named 'rfsoc-studio/frequency-planner'.
