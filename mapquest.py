import requests


def get_ip_info():
    try:
        response = requests.get("https://ipapi.co/json/")
        response.raise_for_status()  
        data = response.json()


        print("\n========== Public IP Information ==========")
        print(f"IP Address     : {data.get('ip')}")
        print(f"Version        : {data.get('version')}")
        print(f"City           : {data.get('city')}")
        print(f"Region         : {data.get('region')}")
        print(f"Country        : {data.get('country_name')} ({data.get('country_code')})")
        print(f"Postal Code    : {data.get('postal')}")
        print(f"Latitude       : {data.get('latitude')}")
        print(f"Longitude      : {data.get('longitude')}")
        print(f"ISP / Org      : {data.get('org')}")
        print(f"ASN            : {data.get('asn')}")
        print("===========================================\n")


    except requests.exceptions.RequestException as e:
        print(f"[Error] Could not retrieve IP info: {e}")


if __name__ == "__main__":
    get_ip_info()
