import requests
url = "https://icanhazdadjoke.com/"
res = requests.get(
    url,
    headers = {
        "Accept":"application/json"
    })

print(res) # <Response [200]>
print(res.ok) # True
print(res.headers) # {'Date': 'Thu, 07 Mar 2019 11:51:04 GMT', 'Content-Type': 'application/json', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': '__cfduid=d250cd7942fe7c1d6ae4259a91f9afffa1551959464; expires=Fri, 06-Mar-20 11:51:04 GMT; path=/; domain=.icanhazdadjoke.com; HttpOnly', 'Cache-Control': 'max-age=0, must-revalidate, no-cache, no-store, public, s-maxage=0', 'X-Frame-Options': 'DENY', 'X-Xss-Protection': '1; mode=block', 'Strict-Transport-Security': 'max-age=15552000; includeSubDomains', 'X-Content-Type-Options': 'nosniff', 'Expect-CT': 'max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"', 'Server': 'cloudflare', 'CF-RAY': '4b3c5aff58b91383-LHR', 'Content-Encoding': 'gzip'}
print(res.text) # String--> {"id":"gNZTCQnWSf","joke":"The other day I was listening to a song about superglue, it\u2019s been stuck in my head ever since.","status":200}

jsonData = res.json() # convert to json, Built-in in "requests"
print(jsonData) # Dictionary--> {'id': 'JmjbxkGJBAd', 'joke': 'Egyptians claimed to invent the guitar, but they were such lyres.\ufeff', 'status': 200}

print(jsonData["joke"])

# QUERY USING THE params property=========================
print('='*40)

res2 = requests.get(
    url + 'search?',
    headers = {
        "Accept":"application/json"
    },
    params={
        "term" : "cat",
        "limit":4
    })

jsonDataWQuery = res2.json()
print(jsonDataWQuery['results'][1])