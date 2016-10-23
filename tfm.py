# Tumblr Following Manager
# Author: Ron Smith
# Copyright (c)2016 That Ain't Working, All rights reserved

import click
import pytumblr
#import requests_oauthlib

from datetime import datetime


@click.command()
@click.argument('offset', default=0)
def main(offset):
    client = pytumblr.TumblrRestClient(
      'yeJB1LQWpT6soRtAWlEegWTUJngcmT7YEzVxsuERwhGWRyTtO1',
      'ibwWDimVtKOW1ay54ZoiigEeIRqq6kaKmwiFTWwp8H2emVPzoy',
      '4jpWSxweuN2k6Dtbl4LlXJJdtF8uejN95mQE8kwaSELXM5AY5H',
      '7Hb7dcmVIKosgXec53wLpLW0zIJXWhjxNTsgaQQRE1YK8gtb2I'
    )

    print('name,title,description,url,updated')
    while True:
        following = client.following()
        for blog in following['blogs']:
            print('"%s","%s","%s","%s","%s"' % (
                  blog['name'],
                  blog['title'],
                  blog['description'],
                  blog['url'],
                  datetime.fromtimestamp(blog['updated']).strftime('%Y-%m-%d')))
        offset += 20
        if offset > following['total_blogs']:
            break


if __name__ == '__main__':
    main()
