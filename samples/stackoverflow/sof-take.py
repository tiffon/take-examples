#! /usr/bin/env python
import sys
import time
import urllib2

from take import TakeTemplate


HOMEPAGE_URL = 'http://stackoverflow.com/'
TAG_PAGE_URL = 'http://stackoverflow.com/questions/tagged/web-scraping?sort=newest&pageSize=10'


with open('questions-listing.take', 'rb') as f:
    TAG_LISTING_TMPL = TakeTemplate(f, base_url=HOMEPAGE_URL)

with open('question-page.take', 'rb') as f:
    QUESTION_TMPL = TakeTemplate(f, base_url=HOMEPAGE_URL)


def get_page(tmpl, url):
    time.sleep(1.5)
    print 'url:', url
    try:
        return tmpl(url=url)
    except urllib2.HTTPError as err:
        print 'urllib2.HTTPError: \n\t url: %s \n\t err: %s' % (url, err)


def get_data():
    data = get_page(TAG_LISTING_TMPL, TAG_PAGE_URL)
    if not data:
        return
    for q in data['questions']:
        q['activity'] = get_page(QUESTION_TMPL, q['post_url'])
    return data


# misc code to show the downloaded data, should be the same between both samples
if __name__ == '__main__':
    data = get_data()
    if not data:
        print 'Problem downloading stackover flow page: %r' % data
    else:
        try:
            import simplejson as json
        except ImportError:
            import json
        if len(sys.argv) > 1:
            with open(sys.argv[-1], 'w') as f:
                json.dump(data, f, indent=4)
        else:
            print json.dumps(data, indent=4)
