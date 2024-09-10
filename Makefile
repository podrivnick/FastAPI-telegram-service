DC = docker compose
BOT_APP = docker_compose/bot.yaml
ENV = --env-file .env


.PHONY: bot
bot:
	${DC} -f ${BOT_APP} ${ENV} up --build -d

.PHONY: bot-down
bot-down:
	${DC} -f ${BOT_APP} ${ENV} down -v

.PHONY: bot-logs
bot-logs:
	${DC} -f ${BOT_APP} logs -f
