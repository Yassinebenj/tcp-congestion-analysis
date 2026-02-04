# TCP Congestion Window Analysis (Mininet Lab)

This project analyzes TCP congestion control behavior using data captured in a Mininet virtual network.

## Overview
- Built a virtual network topology using Mininet
- Generated TCP traffic using Netcat
- Captured packets with Wireshark
- Extracted congestion window values from CSV exports
- Visualized CWND vs time using Python

## Tools Used
- Mininet (Linux VM)
- Wireshark
- Netcat
- tc/netem
- Python, NumPy, Matplotlib

## Files
- congestion_plot.py: Main analysis script
- sample_data/: Sample Wireshark CSV traces

## Results
The plots demonstrate TCP CUBIC behavior under different packet loss conditions.

## Author
Yassine Benjelloun
