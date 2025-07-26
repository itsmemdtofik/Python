def find_top_IpAddress(lines):

    map = {}
    for line in lines:
        ip_address = line.split(" ")[0]
        map[ip_address] = map.get(ip_address, 0) + 1

    max_count = max(map.values(), default=0)

    result = []
    for ip, count in map.items():
        if count == max_count:
            result.append(ip)
            result.append(str(count))
    return result


logs = [
    "192.168.1.1 - - [24/Jul/2025] GET /index.html",
    "192.168.1.2 - - [24/Jul/2025] GET /about.html",
    "192.168.1.1 - - [24/Jul/2025] GET /contact.html",
    "192.168.1.3 - - [24/Jul/2025] GET /index.html",
    "192.168.1.3 - - [24/Jul/2025] GET /index.html",
    "192.168.1.3 - - [24/Jul/2025] GET /index.html",
    "192.168.1.1 - - [24/Jul/2025] GET /home.html"
]

print(find_top_IpAddress(logs))  # Output: ['192.168.1.1', '3']

