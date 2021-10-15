FROM python
ARG tu_environment=development
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN apt-get upgrade -y && apt-get update && apt-get install -y \
    nano \
    sudo \
    libffi-dev \
    libssl-dev \
    sqlite3 \
    libjpeg-dev \
    libopenjp2-7-dev \
    locales \
    cron \
    postgresql-client \
    gettext \
    build-essential \
    python3 \
    python3-dev \
    uwsgi-plugin-python3 \
    uwsgi-plugins-all
RUN useradd -m statesng && \
    echo "tu:tu" | chpasswd && \
    adduser tu sudo && \
    pip install --upgrade pip
USER statesng
COPY --chown=tu . /srv/http/tu
WORKDIR /srv/http/tu
ENV TU_ENVIRONMENT tu.settings.$tu_environment
RUN pip install -r requirements.txt --no-warn-script-location
CMD ["uwsgi", "--emperor", "uwsgi.ini"]
EXPOSE 8000
