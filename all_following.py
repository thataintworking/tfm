# Tumblr Following Manager
# Author: Ron Smith
# Copyright (c)2016 That Ain't Working, All rights reserved

import sys
import click
import pytumblr
# import requests_oauthlib

from datetime import datetime
from time import sleep


@click.command()
@click.argument('offset', default=0)
def main(offset):
    now = datetime.now()

    client = pytumblr.TumblrRestClient(
        'yeJB1LQWpT6soRtAWlEegWTUJngcmT7YEzVxsuERwhGWRyTtO1',
        'ibwWDimVtKOW1ay54ZoiigEeIRqq6kaKmwiFTWwp8H2emVPzoy',
        '4jpWSxweuN2k6Dtbl4LlXJJdtF8uejN95mQE8kwaSELXM5AY5H',
        '7Hb7dcmVIKosgXec53wLpLW0zIJXWhjxNTsgaQQRE1YK8gtb2I'
    )

    if offset == 0:
        print('name,title,url,updated,days')

    while True:
        print('Requesting offset', offset, file=sys.stderr)
        following = client.following(offset=offset, limit=20)
        if 'blogs' in following:
            for blog in following['blogs']:
                last_updated = datetime.fromtimestamp(blog['updated'])
                print('"%s","%s","%s","%s",%d' % (
                    blog['name'],
                    blog['title'].replace('"', "'"),
                    blog['url'],
                    last_updated.strftime('%Y-%m-%d'),
                    (now-last_updated).days))
                sys.stdout.flush()
            offset += 20
            if offset >= following['total_blogs']:
                break
        else:
            print('No blogs in response from tumblr, but have not reached total_blogs', file=sys.stderr)
            print(following, file=sys.stderr)
        sleep(15)


if __name__ == '__main__':
    main()
