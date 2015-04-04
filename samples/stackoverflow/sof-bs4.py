#! /usr/bin/env python
import sys
import time
import urllib2

from bs4 import BeautifulSoup


HOMEPAGE_URL = 'http://stackoverflow.com/'
TAG_PAGE_URL = 'http://stackoverflow.com/questions/tagged/web-scraping?sort=newest&pageSize=10'


def get_page(url):
    time.sleep(1.5)
    print 'url:', url
    try:
        return urllib2.urlopen(url).read()
    except urllib2.HTTPError as err:
        print 'urllib2.HTTPError: \n\t url: %s \n\t err: %s' % (url, err)


def get_questions():
    html = get_page(TAG_PAGE_URL)
    soup = BeautifulSoup(html)
    questions = []
    for question in soup.select('.question-summary'):
        q = {}
        # activity metrics
        q['attn'] = {
            'votes': question.find(class_='votes').get_text(),
            'answers': question.find(class_='status').get_text(),
            'views': question.find(class_='views').get_text()
        }
        # question info
        summary = question.find(class_='summary')
        post_details = summary.h3.a
        q['post_url'] = post_details['href']
        q['title'] = post_details.get_text()
        q['excerpt'] = summary.find(class_='excerpt').get_text()
        q['tags'] = [
            {
                'url': a['href'],
                'name': a.get_text()
            }
            for a in summary.select('.tags a')
        ]
        questions.append(q)
    return questions


def get_poster_details(elm):
    user_info = elm.find(class_='user-details').a
    return {
        'user_login': None if not user_info else user_info.get_text(),
        'user_url': None if not user_info else user_info['href'],
        'date': elm.find(class_='user-action-time').span['title']
    }


def get_comment_activity(elm):
    user_link = elm.find(class_='comment-user')
    return {
        'user_login': user_link.get_text(),
        'user_url': user_link['href'],
        'date': elm.find(class_='comment-date').span['title']
    }


def get_question_activity(url):
    rv = {}
    html = get_page(url)
    soup = BeautifulSoup(html)
    # question poster and comments
    question = soup.find(class_='question')
    poster = question.select('.postcell .post-signature.owner')[0]
    rv['question'] = {
        'asked_by': get_poster_details(poster),
        'comments': [
            get_comment_activity(elm)
            for elm in question.select('.comments .comment-body')
        ]
    }
    answers = []
    for answer in soup.select('#answers .answer'):
        poster = answer.select('.answercell .user-info')[-1]
        answers.append({
            'answered_by': get_poster_details(poster),
            'comments': [
                get_comment_activity(elm)
                for elm in answer.select('.comments .comment-body')
            ]
        })
    rv['answers'] = answers
    return rv


def get_data():
    questions = get_questions()
    if not questions:
        return
    for q in questions:
        q['activity'] = get_question_activity(HOMEPAGE_URL + q['post_url'])
    return questions


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
