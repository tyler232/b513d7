import requests

url = "https://apply-to-avantos.dev-sandbox.workload.avantos-ai.net"
payload = {"email": "lchangbo1227@gmail.com"}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Content-Type": "application/json",
    "Origin": "https://apply-to-avantos.dev-sandbox.workload.avantos-ai.net",
    "Referer": "https://apply-to-avantos.dev-sandbox.workload.avantos-ai.net/",
    "X-Requested-With": "XMLHttpRequest"
}

response = requests.post(url, json=payload, headers=headers)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
