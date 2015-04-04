An example of scraping the title, excerpt and user activity for the [last 10 web-scraping questions](http://stackoverflow.com/questions/tagged/web-scraping?sort=newest&pageSize=10) on stackoverflow.

It's with [Beautiful Soup 4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [take templates](https://github.com/tiffon/take).

A sample of the data that is scraped for each question:

```json
{
"tags": [
    {
        "url": "http://stackoverflow.com/questions/tagged/javascript",
        "name": "javascript"
    },
    {
        "url": "http://stackoverflow.com/questions/tagged/vba",
        "name": "vba"
    },
    {
        "url": "http://stackoverflow.com/questions/tagged/web-scraping",
        "name": "web-scraping"
    }
],
"title": "VBA scraping generated content which is not in the HTML source file",
"excerpt": "I have made a VBA code to scrape some product prices from web pages.\n\nI can make it work for all the websites I want except for one. On this particular site, the prices are not shown in the HTML code ...",
"post_url": "http://stackoverflow.com/questions/29422436/vba-scraping-generated-content-which-is-not-in-the-html-source-file",
"activity": {
    "question": {
        "asked_by": {
            "date": "2015-04-02 21:04:46Z",
            "user_login": "user3254924",
            "user_url": "http://stackoverflow.com/users/3254924/user3254924"
        },
        "comments": [
            {
                "date": "2015-04-02 23:53:01Z",
                "user_login": "Tim Williams",
                "user_url": "http://stackoverflow.com/users/478884/tim-williams"
            }
        ]
    },
    "answers": [
        {
            "answered_by": {
                "date": "2015-04-02 21:30:40Z",
                "user_login": "Ali Sheikhpour",
                "user_url": "http://stackoverflow.com/users/4700922/ali-sheikhpour"
            },
            "comments": [
                {
                    "date": "2015-04-03 13:08:45Z",
                    "user_login": "user3254924",
                    "user_url": "http://stackoverflow.com/users/3254924/user3254924"
                },
                {
                    "date": "2015-04-03 13:43:14Z",
                    "user_login": "Ali Sheikhpour",
                    "user_url": "http://stackoverflow.com/users/4700922/ali-sheikhpour"
                },
                {
                    "date": "2015-04-03 15:16:54Z",
                    "user_login": "user3254924",
                    "user_url": "http://stackoverflow.com/users/3254924/user3254924"
                }
            ]
        }
    ]
}
```
