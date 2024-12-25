# YAtube_API social nework



## DESCRIPTION:

- _This projects is a social network, for people who want to create posts, comment others posts, subscribe to other user profiles and view their activities._
- _This project also uses ***JWT authentication*** for providing better experience and secure interaction with API._



## LOCAL DEPLOYATION:

**To deploy this project on your computer:**
- _Clone this repository to your ***working directory***._
- _Install requirements via - `pip install -r requirements.txt`._
- _Apply migrations via - `python(3) manage.py migrate`._
- _Run server via - `python(3) manage.py runserver`._



## API request examples:

- _To fetch list of posts - `GET /api/posts/`._
- _To fetch list of comments - `GET /api/posts/{post_id}/comments/`._
- _Subscribtion to certain user - `POST /api/follow/` <ins>with body</ins> `{"following": "username"}`._



## CREATORS:

***Maksim Chernikov a.k.a. MaximSupreme***
