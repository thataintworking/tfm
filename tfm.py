# Tumblr Following Manager
# Author: Ron Smith
# Copyright (c)2016 That Ain't Working, All rights reserved

import pytumblr


client = pytumblr.TumblrRestClient(
  'yeJB1LQWpT6soRtAWlEegWTUJngcmT7YEzVxsuERwhGWRyTtO1',
  'ibwWDimVtKOW1ay54ZoiigEeIRqq6kaKmwiFTWwp8H2emVPzoy',
  '4jpWSxweuN2k6Dtbl4LlXJJdtF8uejN95mQE8kwaSELXM5AY5H',
  '7Hb7dcmVIKosgXec53wLpLW0zIJXWhjxNTsgaQQRE1YK8gtb2I'
)

# Make the request
print(client.info())