from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, ArticleViewSet, CategoryViewSet, TagViewSet, RegisterViewSet, ArticleList, ImageUrlview, UserInfoView, UserArticles

router =  DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)
router.register(r'user', RegisterViewSet)
# router.register(r'articlelist', ArticleListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('list', ArticleList.as_view()),
    path('image/', ImageUrlview.as_view(), {'filename': 'img.jpg'}),
    path('user-info/', UserInfoView.as_view()),
    path('user-articles/<int:pk>/', UserArticles.as_view()),
]




"""

TODO: Api Endpoints are not complited yet.

## API Endpoints

### Authentication

| Method | Endpoint | Description |
| --- | --- | --- |
| POST | /api/token/ | Get JWT token |
| POST | /api/token/refresh/ | Refresh JWT token |

### Users

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/users/ | Get all users |
| GET | /api/users/{id}/ | Get user by id |
| POST | /api/users/ | Create new user |
| PUT | /api/users/{id}/ | Update user by id |
| DELETE | /api/users/{id}/ | Delete user by id |

### Authors

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/authors/ | Get all authors |
| GET | /api/authors/{id}/ | Get author by id |
| POST | /api/authors/ | Create new author |
| PUT | /api/authors/{id}/ | Update author by id |
| DELETE | /api/authors/{id}/ | Delete author by id |

### Categories

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/categories/ | Get all categories |
| GET | /api/categories/{id}/ | Get category by id |
| POST | /api/categories/ | Create new category |
| PUT | /api/categories/{id}/ | Update category by id |
| DELETE | /api/categories/{id}/ | Delete category by id |

### Tags

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/tags/ | Get all tags |
| GET | /api/tags/{id}/ | Get tag by id |
| POST | /api/tags/ | Create new tag |
| PUT | /api/tags/{id}/ | Update tag by id |
| DELETE | /api/tags/{id}/ | Delete tag by id |

### Images

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/images/ | Get all images |
| GET | /api/images/{id}/ | Get image by id |
| POST | /api/images/ | Create new image |
| PUT | /api/images/{id}/ | Update image by id |
| DELETE | /api/images/{id}/ | Delete image by id |

### Posts

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/posts/ | Get all posts |
| GET | /api/posts/{id}/ | Get post by id |
| POST | /api/posts/ | Create new post |
| PUT | /api/posts/{id}/ | Update post by id |
| DELETE | /api/posts/{id}/ | Delete post by id |

### Comments

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/comments/ | Get all comments |
| GET | /api/comments/{id}/ | Get comment by id |
| POST | /api/comments/ | Create new comment |
| PUT | /api/comments/{id}/ | Update comment by id |
| DELETE | /api/comments/{id}/ | Delete comment by id |

### Likes

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/likes/ | Get all likes |
| GET | /api/likes/{id}/ | Get like by id |
| POST | /api/likes/ | Create new like |
| PUT | /api/likes/{id}/ | Update like by id |
| DELETE | /api/likes/{id}/ | Delete like by id |

### Dislikes

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/dislikes/ | Get all dislikes |
| GET | /api/dislikes/{id}/ | Get dislike by id |

### Favorites

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/favorites/ | Get all favorites |
| GET | /api/favorites/{id}/ | Get favorite by id |

### Bookmarks

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/bookmarks/ | Get all bookmarks |
| GET | /api/bookmarks/{id}/ | Get bookmark by id |


### Ratings

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/ratings/ | Get all ratings |
| GET | /api/ratings/{id}/ | Get rating by id |
| POST | /api/ratings/ | Create new rating |
| PUT | /api/ratings/{id}/ | Update rating by id |
| DELETE | /api/ratings/{id}/ | Delete rating by id |

### Followers

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/followers/ | Get all followers |
| GET | /api/followers/{id}/ | Get follower by id |
| POST | /api/followers/ | Create new follower |
| PUT | /api/followers/{id}/ | Update follower by id |
| DELETE | /api/followers/{id}/ | Delete follower by id |

### Followings

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/followings/ | Get all followings |
| GET | /api/followings/{id}/ | Get following by id |
| POST | /api/followings/ | Create new following |
| PUT | /api/followings/{id}/ | Update following by id |
| DELETE | /api/followings/{id}/ | Delete following by id |

### Subscriptions

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/subscriptions/ | Get all subscriptions |
| GET | /api/subscriptions/{id}/ | Get subscription by id |
| POST | /api/subscriptions/ | Create new subscription |
| PUT | /api/subscriptions/{id}/ | Update subscription by id |
| DELETE | /api/subscriptions/{id}/ | Delete subscription by id |

### Notifications

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/notifications/ | Get all notifications |
| GET | /api/notifications/{id}/ | Get notification by id |
| POST | /api/notifications/ | Create new notification |
| PUT | /api/notifications/{id}/ | Update notification by id |
| DELETE | /api/notifications/{id}/ | Delete notification by id |

### Messages

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/messages/ | Get all messages |
| GET | /api/messages/{id}/ | Get message by id |
| POST | /api/messages/ | Create new message |
| PUT | /api/messages/{id}/ | Update message by id |

### Chats

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/chats/ | Get all chats |

"""