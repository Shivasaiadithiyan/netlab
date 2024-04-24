import subprocess

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    """
    
    ping_str = "-n 1" if subprocess.os.name == 'nt' else "-c 1" # Use the appropriate ping command for the operating system
    
    args = ['ping', ping_str, host]                             # Run the ping command with the host as an argument
    return subprocess.call(args) == 0

p1 = ping("www.google.com")
print(p1)

p2 = ping("www.tn.gov.in")
print(p2)

p3 = ping("www.singpass.gov.sg")
print(p3)