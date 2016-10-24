# Tumblr Following Manager
# Author: Ron Smith
# Copyright (c)2016 That Ain't Working, All rights reserved

import sys
import click
import pytumblr

from datetime import datetime
from time import sleep
from config import Keys


@click.command()
@click.argument('days', type=click.INT)
@click.option('--offset', '-o', default=0, type=click.INT, help="Start requesting blogs at this offest")
@click.option('--trial', '-t', is_flag=True, help="Find older blogs but don't unfollow")
def main(days, offset, trial):
    days = int(days)
    offset = int(offset)
    now = datetime.now()

    client = pytumblr.TumblrRestClient(Keys.consumer_key, Keys.consumer_secret, Keys.oauth_token, Keys.oauth_secret)

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
