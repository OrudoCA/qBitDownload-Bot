# qBitDownload Bot

![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/pgxm2mKT5KHEHFE?file=/&fileId=23795&x=1920&y=1200&a=true&etag=430e9d84364f13b79e42991fede6609a)

## Telegram бот, предназначенный для удаленного добавление загрузок в очередь на qBitTorrent сервер

| [**git.orudo.ru**](https://git.orudo.ru/OrudoCA/qBitDownload-Bot) | [**GitHub**](https://github.com/OrudoCA/qBitDownload-Bot) | [**DockerHub**](https://hub.docker.com/r/orudoca/qbitdownload-bot) |
| ---------------- | ---------- | ------------- |
| [![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/AmggNTQWgR6KkyB?file=/&fileId=23836&x=1920&y=1200&a=true&etag=0ef9694cea6e4d85c05aef9be72b927a)](https://git.orudo.ru/OrudoCA/qBitDownload-Bot) | [![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/ip5qtGcwKHMPMAG?file=/&fileId=23819&x=1920&y=1200&a=true&etag=c540068d990ac47217a31f7450afc0ee)](https://github.com/OrudoCA/qBitDownload-Bot) |[![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/7AEeEAzHYikFd5B?file=/&fileId=23806&x=1920&y=1200&a=true&etag=59894ecdfa7aaa6fb832cc4bf99c418d)](https://hub.docker.com/r/orudoca/qbitdownload-bot) |

### Для работы бота требуется [**qBitTorrent**](https://www.qbittorrent.org/) сервер

---

### Текущие фичи:
---
- **Авторизация по паролю**
- **Добавление загрузок в очередь через .torrent файлы / Magnet-ссылки**
- **Добавление/Удаление директорий для загрузок**

---

### В образе используется ["fedarovich/qbittorrent-cli"](https://github.com/fedarovich/qbittorrent-cli)

---

[![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/rRcdSnCEaA85tWf?file=/&fileId=23784&x=1920&y=1200&a=true&etag=32928842bc4e76adaba194cdd9ec1351)](https://hub.docker.com/r/orudoca/qbitdownload-bot)

## Развертывание через Docker:
#### 1. Соберите образ или склонируйте образ с [Dockerhub](https://hub.docker.com/r/orudoca/qbitdownload-bot)

**Склонировать репозиторий и перейти в его директорию**
```bash
git clone https://git.orudo.ru/OrudoCA/qBitDownload-Bot.git && cd qBitDownload-Bot
```

**Сбор образа**
```bash
docker build -t <IMAGE_NAME> .
```

#### 2. Развернуть через docker-cli или docker-compose

**Docker-cli**
```bash
docker run \
 --name qbitdl_bot \
 --restart=unless-stopped \
 -v /path/to/config:/etc/dbot \
 -v /path/to/media:/path/to/media \
 -e TOKEN="<YOUR_BOT_TOKEN_HERE>" \
 -e PASS="change_me" \
 -e QURL="<http://<YOUR_QBIT_SERVER_IP_HERE>:<PORT>" \
 -e QUSER="<YOUR_QBIT_USERNAME>"
 -e QPASS="<YOUR_QBIT_PASSWORD>"
 -d your_image_here
```

##### или

**docker-compose**
```yml
services:
  qbitdl_bot:
    image: <YOUR_IMAGE_HERE>
    container_name: qbitdl_bot
    volumes:
      - /path/to/config:/etc/bot
      - /path/to/data/:/path/to/data
    restart: 'unless-stopped'
    environment:
      TOKEN: "<YOUR_BOT_TOKEN_HERE>"
      PASS: "change_me"
      QURL: "<http://<YOUR_QBIT_SERVER_IP_HERE>:<PORT>"
      QUSER: "<YOUR_QBIT_USERNAME>"
      QPASS: "<YOUR_QBIT_PASSWORD>"
```

```bash
docker compose up -d
```
