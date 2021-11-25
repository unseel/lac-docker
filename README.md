## Intro

Dockerize [lac](https://github.com/baidu/lac)


## Usage

```
> docker run --rm -e LAC_HOST=0.0.0.0 -e LAC_PORT=5000 -p 5000:5000 lac-docker:latest
```

sample call

```bash
curl http://127.0.0.1:5000/lac/seg?text=剪刀T恤香蕉台灯蜡烛手表杯子叶子钥匙勺子
```

