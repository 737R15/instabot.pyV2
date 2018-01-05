# In My Repo
1. liked medias saving to sqlite3
1. followed usernames saving to sqlite3
1. Doesn't try to like again and time saving.
1. Dosn't follow a person again.
1. not liked 400 error fixed.
1. Start and stop time.

## In Progress
1. Done

# InstaBot

> Toolkit for building automated Instagram bots without direct access to the Instagram API or passsing through the review process.

## Parameters
| Parameter            | Type|                Description                           |        Default value             |
|:--------------------:|:---:|:----------------------------------------------------:|:--------------------------------:|
| login                | str | Your instagram username                              |      |
| password             | str | Your instagram password                              |      |
| start\_at\_h         | int | Start program at the hour                            | 0    |
| start\_at\_m         | int | Start program at the min                             | 0    |
| end\_at\_h           | int | End program at the hour                              | 23   |
| end\_at\_m           | int | End program at the min                               | 59   |
| database\_name       | str | change the name of database file to use multiple account | "follows\_db.db"   |
| like\_per\_day       | int | Number of photos to like per day (over 1000 may cause throttling) | 1000 |
| media\_max\_like     | int | Maximum number of likes on photos to like (set to 0 to disable) | 0    |
| media\_min\_like     | int | Maximum number of likes on photos to like (set to 0 to disable) | 0    |
| follow\_per\_day     | int | Photos to like per day                               | 0    |
| follow\_time         | int | Seconds to wait before unfollowing                   | 5 * 60 * 60 |
| unfollow\_per\_day   | int | Users to unfollow per day                            | 0    |
| comments\_per\_day   | int | Comments to post per day                             | 0    |
| comment\_list        | [[str]] | List of word lists for comment generation        | [['this', 'your'], ['photo', 'picture', 'pic', 'shot'], ['is', 'looks', 'is really'], ['great', 'super', 'good'], ['.', '...', '!', '!!']] |
| tag\_list            | [str] | Tags to use for finding posts                      | ['cat', 'car', 'dog'] |
| tag\_blacklist       | [str] | Tags to ignore when liking posts                   | [] |
| user\_blacklist      | {str: str} | Users whose posts to ignore                   | {} |
| max\_like\_for\_one_tag | int | How many media of a given tag to like at once (out of 21) | 5 |
| unfollow\_break\_min | int | Minimum seconds to break between unfollows           | 15 |
| unfollow\_break\_max | int | Maximum seconds to break between unfollows           | 30 |
| log_mod              | int | Logging target (0 log to console, 1 log to file, 2 no log.) | 0 |
| proxy                | str | Access instagram through a proxy. (host:port or user:password@host:port) | |

## Methods
| Method | Description |
|:------:|:-----------:|
| get\_media\_id\_by\_tag(tag) | Add photos with a given tag to like queue |
| like\_all\_exist\_media(num) | Like some number of media in queue |
| auto_mod() | Automatically loop through tags and like photos |
| unlike(id) | Unlike media, given its ID. |
| comment(id, comment) | Write a comment on the media with a given ID. |
| follow(id) | Follow the user with the given ID. |
| unfollow(id) | Unfollow the user with the given ID. |
| logout() | Log out of Instagram. |

## Usage examples
Basic bot implementation:
```py
bot = InstaBot('login', 'password')
bot.auto_mod()
```

Standard use with custom tags:
```py
bot = InstaBot('login', 'password', tag_list=['with', 'your', 'tag'])
bot.auto_mod()
```

Standard use with change default settings (you should know what you do!):
```py
bot = InstaBot('login', 'password',
               like_in_day=1000,
               media_max_like=50,
               media_min_like=5,
               tag_list=['like', 'follow', 'f4f'],
               max_like_for_one_tag=50,
               log_mod=1)
bot.auto_mod()
```

Get media by one tag `'python'` and like 4 of them:
```py
bot = InstaBot('login', 'password')
bot.get_media_id_by_tag('python')
bot.like_all_exist_media(4)
```

## Video Tutorials
The following video tutorials demo setting up and running the bot:
* [Windows](https://www.youtube.com/watch?v=V8P0UCrACA0)
* [Mac/Linux](https://www.youtube.com/watch?v=ASO-cZO6uqo)

## Community

- [Telegram Group](https://t.me/joinchat/DYKH-0G_8hsDDoN_iE8ZlA)
- [Facebook Group](https://www.facebook.com/groups/instabot/)
