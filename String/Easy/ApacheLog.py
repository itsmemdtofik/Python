"""
         * <pre>
         * !Apache Log: Find top ip address which access the site most
         *
         * !Approach: Time complexity: O(n), Space complexity: O(n)
         * * Step1: Build a frequency map to count occurrences of each IP.
         * * Step2: Iterate over the map and find the IP with the highest count.
         * * Step3: Return top ip address with the highest frequency.
         * </pre>
"""


def find_top_IpAddress(lines):
    freq_map = {}
    for line in lines:
        ip_address = line.split(" ")[0]
        freq_map[ip_address] = freq_map.get(ip_address, 0) + 1

    max_count = max(freq_map.values(), default=0)

    result = []
    for ip, count in freq_map.items():
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
