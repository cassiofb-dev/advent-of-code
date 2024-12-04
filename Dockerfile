FROM alpine:3.20

RUN apk -U upgrade -a

RUN apk add hyperfine \
            gcc libc-dev \
            rust \
            python3 \
            openjdk17 \
            nodejs \
