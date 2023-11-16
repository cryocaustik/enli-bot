# enli-bot

enl-i discord bot

## run

```sh
# copy and fill in the .env
cp .env.template .env

# install dependencies
pdm install

# run
python ./src/bot.py
```

## docker run

```sh
# copy and fill in the .env
cp .env.template .env

# run the container
docker run --env-file .env enli-bot
```

## development

### export requirements

```sh
pdm export --prod > requirements.txt
```

### docker build & run

```sh
docker build -t enli-bot .
docker run --env-file .env enli-bot
```