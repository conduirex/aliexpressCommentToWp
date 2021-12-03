import requests
from bs4 import BeautifulSoup
import re
from Comment import Comment


class AliExpress:
    productId = None
    ownerMemberId = None

    def __init__(self, url):
        self.url = url
        self.get_productid()


    def get_productid(self):
        url_get = requests.get(self.url)

        regex_owner_id = re.search('sellerAdminSeq":(.*),"tradeCurrencyCode', url_get.text)
        regex_product_id = re.search('"productId":(.*),"rootCategoryId', url_get.text)

        self.productId = regex_product_id.group(1)
        self.ownerMemberId = regex_owner_id.group(1)


    def get_review_page(self, page):
        comment_list = []
        rate_list = []

        post_url = "https://feedback.aliexpress.com/display/productEvaluation.htm"
        myobj = {'ownerMemberId': self.ownerMemberId,
                 'memberType': 'seller',
                 'productId': self.productId,
                 'companyId': '',
                 'evaStarFilterValue': 'all Stars',
                 'evaSortValue': 'sortdefault@feedback',
                 'page': page,
                 'currentPage': '1',
                 'startValidDate': '',
                 'i18n': 'true',
                 'withPictures': 'false',
                 'withAdditionalFeedback': 'false',
                 'onlyFromMyCountry': 'false',
                 'version': '',
                 'isOpened': 'true',
                 'translate': 'Y ',
                 'jumpToTop': 'true',
                 'v': '2'}

        x = requests.post(post_url, data=myobj)
        soup = BeautifulSoup(x.content, "lxml")

        div = soup.find_all("dt", attrs={"class": "buyer-feedback"})
        for span in div:
            span_context = span.find_all("span", attrs={"class": ""})
            str_span_context = str(span_context).replace("<span>", "").replace("</span>", "").replace("]", "") .replace("[", "")
            print(str_span_context)
            comment_list.append(str_span_context)

        div = soup.find_all("div", attrs={"class": "f-rate-info"})
        for star in div:
            star_context = star.find_all("span", attrs={"class": ""})
            str_star_context = str(star_context).replace('<span style="width:', "").replace('%"></span>', "").replace("]", "") .replace("[", "")
            int_star_context = int(str_star_context)/20
            rate_list.append(int(str_star_context)//20)

        comment_post_list = []
        for i in range(0, len(rate_list)-1):
            comment_post_list.append(Comment(comment_list[i], rate_list[i]))

        return comment_post_list
