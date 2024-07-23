# BSOD as a Service
A fun project inspired from the CrowdStrike incident on 19th July 2024 that crashed 8.5 Million devices into BSOD

# Setting up target machine:
## No app installation needed

Go to Settings -> System -> For developers -> Enable developer mode, Enable Device portal -> Disable 'Restrict to loopback' -> Setup username and password
Ensure the said port is allowed in the firewall.

# For attacker's machine
Use the script with the IP, port, username, password of the target machine

```
python baas.py <IP> <PORT> <USERNAME> <PASSWORD>
```
