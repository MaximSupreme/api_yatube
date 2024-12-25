# YAtube_API social nework



## DESCRIPTION:

- _This projects is a social network, for people who want to create posts, comment others posts, subscribe to other user profiles and view their activities._
- _This project also uses ***JWT authentication*** for providing better experience and secure interaction with API._



## LOCAL DEPLOYATION:

**To deploy this project on your computer:**
- _Clone this repository to your ***working directory***._
- _Install requirements through pip:_
```bash
pip install -r requirements.txt
```
- _Apply migrations:_
```bash
python(3) manage.py migrate
```
- _Run server:_
```bash
python(3) manage.py runserver
```



## API request examples:

- _To fetch list of posts - `GET /api/posts/`._
- _To fetch list of comments - `GET /api/posts/{post_id}/comments/`._
- _Subscribtion to certain user - `POST /api/follow/` with body `{"following": "username"}`._



## CREATORS:

***Maksim Chernikov a.k.a. MaximSupreme***
