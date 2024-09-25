import platform
import requests

# Get OS and platform details
def get_os_info():
    os_type = platform.system()
    os_platform_info = platform.platform()
    os_version = platform.release()
    return os_type, os_platform_info, os_version

# Replace 'your_ip' with your actual IP address
def send_os_info(os_type, os_platform_info, os_version):
    url = "http://192.168.1.101:369"  # Specify the port if needed

    # Data to be sent
    data = {
        "os_type": os_type,
        "os_platform_info": os_platform_info,
        "os_version": os_version
    }

    # Send the data via a POST request
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print("Data sent successfully!")
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def get_and_send_os_info():
    os_type, os_platform_info, os_version = get_os_info()
    send_os_info(os_type, os_platform_info, os_version)

if __name__ == "__main__":
    get_and_send_os_info()