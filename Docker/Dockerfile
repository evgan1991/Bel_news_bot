FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip install feedparser
RUN pip install pytelegrambotapi
RUN apt-get install git -y

RUN mkdir /root/.ssh/
RUN chown -R root:root /root/.ssh

RUN touch /root/.ssh/known_hosts
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN echo "-----BEGIN OPENSSH PRIVATE KEY-----" >> /root/.ssh/id_rsa
RUN echo "b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW" >> /root/.ssh/id_rsa
RUN echo "QyNTUxOQAAACCLz1vITnaRZAWC/SKuPTlQwDPVS+jRomdpOnsiICyEvgAAAJhK8gbsSvIG" >> /root/.ssh/id_rsa
RUN echo "7AAAAAtzc2gtZWQyNTUxOQAAACCLz1vITnaRZAWC/SKuPTlQwDPVS+jRomdpOnsiICyEvg" >> /root/.ssh/id_rsa
RUN echo "AAAEC2PI6opmpuD81e28Am4+Qly2i1AFD/bRtglTC30SjjsYvPW8hOdpFkBYL9Iq49OVDA" >> /root/.ssh/id_rsa
RUN echo "M9VL6NGiZ2k6eyIgLIS+AAAAE2V2Z2FuMTk5MUBnbWFpbC5jb20BAg==">> /root/.ssh/id_rsa
RUN echo "-----END OPENSSH PRIVATE KEY-----" >> /root/.ssh/id_rsa

RUN chmod 600 /root/.ssh/id_rsa

WORKDIR /var/lib/
RUN git clone git@github.com:evgan1991/Bel_news_bot.git
RUN rm /root/.ssh/id_rsa

WORKDIR /var/lib/News_bot/bot
ENTRYPOINT ["python3"]
CMD ["feed.py"]