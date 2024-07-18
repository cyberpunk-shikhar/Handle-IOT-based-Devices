# # ping_script.py
# import time
# from ping3 import ping


# def ping_ip(ip_address, interval=60):
#     """
#     Ping the specified IP address at regular intervals.

#     :param ip_address: The IP address to ping.
#     :param interval: The interval between ping attempts in seconds.
#     """
#     while True:
#         response = ping(ip_address)

#         if response is not None:
#             print(f'IP address {ip_address} online. Response time: {response} ms')
            
#         else:
#             print(f'IP address {ip_address} offline')

#         time.sleep(interval)

# if __name__ == "__main__":
#     # Replace with the actual IP address of your ESP32
#     esp32_ip = '10.17.5.111'

#     # Run the ping function
#     ping_ip(esp32_ip)

import subprocess
from ping3 import ping


def ping_script(ip_address):
    try:
        # Use subprocess to run the ping command and capture the output
        result = subprocess.run(['ping', '-n', '4', ip_address], capture_output=True, text=True, timeout=5)
        print(result)
        
        # Check if the ping was successful (return code 0)
        if result.returncode == 0:
            print(result.returncode)
            return f"IP {ip_address} is reachable."
         
        else:
         return f"IP {ip_address} is not reachable."
    except subprocess.TimeoutExpired:
        return f"Timeout: Unable to ping {ip_address}."
    except Exception as e:
        return f"An error occurred: {str(e)}"
