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

# Demo
[Demo video](https://youtu.be/l9325HEatEE?si=HZOXQ1ofK071V4dt)

# Bad idea: Don't do this unless you know what you are doing

If the attacker script is kept on the same machine as the target, the IP can be set to localhost or 127.0.0.1 and this script can be scheduled to run as a service at startup.

```
schtasks /create /sc onstart /tn "BAAS" /tr "python C:\path\to\baas.py" /rl highest /f
```
This will continuously cause BSODs.
