import subprocess
import platform 
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, Style, init
init()
def check_ping(ip):
    param= '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', str(ip)]
    response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if response ==0:
        print(f"{Fore.GREEN}[+] {ip} is UP{Style.RESET_ALL}")
        return str(ip)
    return None
def run_ping_sweeper():
    network_input="10.0.0.0/24"
    network =ipaddress.ip_network(network_input, strict=False)
    print(f"{Fore.CYAN} Scanning network: {network_input}...{Style.RESET_ALL}")
    active_hosts = []
    max_workers=50
    with ThreadPoolExecutor(max_workers=50) as executor:
        results= executor.map(check_ping,network.hosts())
    for ip in results:
        if ip: 
            active_hosts.append(ip)
    print(f"\n{Fore.YELLOW}---Scan complete ---")
    print(f"Total active hosts found: {len(active_hosts)}{Style.RESET_ALL}")
if __name__ == "__main__":
    run_ping_sweeper()