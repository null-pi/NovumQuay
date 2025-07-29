FROM novumquay/environment:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    python3-venv \
    build-essential

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY ./src/script.sh /app/script.sh

RUN chmod +x /app/script.sh

COPY ./src /app/src

ENTRYPOINT [ "/app/script.sh" ]