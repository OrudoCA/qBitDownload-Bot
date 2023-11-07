FROM alpine:latest
COPY bot /opt/bot
RUN apk update && apk add tzdata bash python3 py-pip wget icu-libs krb5-libs libgcc libintl libssl1.1 libstdc++ zlib && pip install telebot
RUN wget https://github.com/fedarovich/qbittorrent-cli/releases/download/v1.7.22315.1/qbt-linux-alpine-x64-1.7.22315.1.tar.gz && \
  mkdir /opt/qbt && \
  tar -zxf qbt-linux-alpine-x64-1.7.22315.1.tar.gz -C /opt/qbt && \
  chmod a+x /opt/qbt/* && \
  ln -sf /opt/qbt/qbt /bin/qbt && ln -sf /opt/bot/bot.py /bin/bot
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENTRYPOINT ["/bin/bot"]
