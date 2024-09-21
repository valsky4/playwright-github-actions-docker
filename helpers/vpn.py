import requests


def is_vpn_connected(url_for_check: str) -> bool:
    """
    Checks if the VPN connection is established by making a request to a known internal endpoint.
    Modify this function according to your VPN setup.
    """
    try:
        # Replace with an endpoint accessible only via VPN
        response = requests.get(url_for_check, timeout=10)
        return response.status_code == 200
    except requests.RequestException:
        return False
