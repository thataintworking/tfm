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
@click.argument('days', type=click.INT)
@click.option('--offset', '-o', default=0, type=click.INT, help="Start requesting blogs at this offest")
@click.option('--trial', '-t', is_flag=True, help="Find older blogs but don't unfollow")
def main(days, offset, trial):
    days = int(days)
    offset = int(offset)
    now = datetime.now()

    client = pytumblr.TumblrRestClient(
        'yeJB1LQWpT6soRtAWlEegWTUJngcmT7YEzVxsuERwhGWRyTtO1',
        'ibwWDimVtKOW1ay54ZoiigEeIRqq6kaKmwiFTWwp8H2emVPzoy',
        '4jpWSxweuN2k6Dtbl4LlXJJdtF8uejN95mQE8kwaSELXM5AY5H',
        '7Hb7dcmVIKosgXec53wLpLW0zIJXWhjxNTsgaQQRE1YK8gtb2I'
    )

    if trial:
        print('Trial mode enabled. No blogs will be unfollowed.')

    while True:
        print('Requesting offset', offset, file=sys.stderr)
        following = client.following(offset=offset, limit=20)
        if 'blogs' in following:
            for blog in following['blogs']:
                last_updated = datetime.fromtimestamp(blog['updated'])
                since_last = (now-last_updated).days
                if since_last >= days:
                    print('It has been %d days since blog "%s" has posted anything. %s' %
                          (since_last, blog['name'], '' if trial else 'Unfollowing.'))
                    if not trial:
                        client.unfollow(blog['url'])
            offset += 20
            if offset >= following['total_blogs']:
                break
        else:
            print('No blogs in response from tumblr, but have not reached total_blogs', file=sys.stderr)
            print(following, file=sys.stderr)
        sys.stdout.flush()
        sleep(15)


if __name__ == '__main__':
    main()
