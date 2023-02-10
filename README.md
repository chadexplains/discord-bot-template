## setup environment
1. `virtualenv env`
1. `source env/bin/activate`
1. create a file `.env` one level up from where this `README.md` file is and fill it with the required secrets (`discord_secret_token=<put stuff here>`)
1.`make setup`


## run the discord bot
```
make discord_bot
```

this automatically installs python dependencies and starts the bot as a python process
