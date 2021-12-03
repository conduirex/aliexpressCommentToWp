import Nickname
from JWToken import WordpressRest
from Post import PostComments
from AliExpress import AliExpress


if __name__ == '__main__':
    # Wordpress Id Password
    auth_token = WordpressRest("username", "password")

    # Web site Product ID http://localhost/wp-admin/post.php?post=24092&action=edit
    # Product ID: 24092
    post_id = int(input("Product ID: "))

    # https://www.aliexpress.com/item/1005003122934995.html
    # Product ID: 1005003122934995
    aliexpress_url = input("aliexpress Product ID: ")

    aliexpress_url = "https://www.aliexpress.com/item/" + aliexpress_url + ".html"
    page_number = int(input("how many pages 1 pages = 10 comment: "))

    # 1-Mixed
    # 2-Women
    # 3-Men
    gender = int(input("choose gender 1 Mixed 2 Women 3 Men: "))


    Ali_Express = AliExpress(aliexpress_url)


    for i in range(0, page_number):
        reviews = Ali_Express.get_review_page(i+1)
        for review in reviews:
            post_now = PostComments(review.context, review.rate, post_id, Nickname.choice_function(gender), auth_token)
            post_now.send_comment()



