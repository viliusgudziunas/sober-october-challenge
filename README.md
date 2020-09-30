# Sober October Challenge

### Small project I created to track mine and my friends october challenge

To deploy, please follow this [gist](https://gist.github.com/bradtraversy/0029d655269c8a972df726ed0ac56b88)

Please note that the last step 'Add table to remote database' is different:

```
heroku run python
>>> from project import create_app, db
>>> app = create_app("ProductionConfig")
>>> app.app_context().push()
>>> db.create_all()
>>> exit()
```
