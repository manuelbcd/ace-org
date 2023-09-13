FROM golang:1.17.6-alpine AS build

ARG APPFOLDER
RUN apk add build-base
WORKDIR /app
COPY ${APPFOLDER}/ .

RUN go get ${APPFOLDER}
RUN go build -o app

FROM alpine:3.17.1
WORKDIR /app
COPY --from=build /app/app .

CMD ["./app"]
