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

## Benchmark

```
❯ k6 run benchmark.js

          /\      |‾‾| /‾‾/   /‾‾/
     /\  /  \     |  |/  /   /  /
    /  \/    \    |     (   /   ‾‾\
   /          \   |  |\  \ |  (‾)  |
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: benchmark.js
     output: -

  scenarios: (100.00%) 1 scenario, 100 max VUs, 1m0s max duration (incl. graceful stop):
           * default: 100 looping VUs for 30s (gracefulStop: 30s)


running (0m30.5s), 000/100 VUs, 3000 complete and 0 interrupted iterations
default ✓ [======================================] 100 VUs  30s

     ✓ status was 200

     checks.........................: 100.00% ✓ 3000      ✗ 0
     data_received..................: 795 kB  26 kB/s
     data_sent......................: 453 kB  15 kB/s
     http_req_blocked...............: avg=43.98µs min=2µs    med=4µs    max=2.72ms   p(90)=6µs      p(95)=15µs
     http_req_connecting............: avg=38.16µs min=0s     med=0s     max=2.68ms   p(90)=0s       p(95)=0s
     http_req_duration..............: avg=11.11ms min=2.24ms med=4.78ms max=202.95ms p(90)=18.82ms  p(95)=33.74ms
       { expected_response:true }...: avg=11.11ms min=2.24ms med=4.78ms max=202.95ms p(90)=18.82ms  p(95)=33.74ms
     http_req_failed................: 0.00%   ✓ 0         ✗ 3000
     http_req_receiving.............: avg=91.07µs min=23µs   med=42µs   max=1.4ms    p(90)=248.09µs p(95)=397.04µs
     http_req_sending...............: avg=23.4µs  min=7µs    med=15µs   max=2.33ms   p(90)=29µs     p(95)=39µs
     http_req_tls_handshaking.......: avg=0s      min=0s     med=0s     max=0s       p(90)=0s       p(95)=0s
     http_req_waiting...............: avg=10.99ms min=2.18ms med=4.69ms max=202.83ms p(90)=18.74ms  p(95)=33.46ms
     http_reqs......................: 3000    98.395736/s
     iteration_duration.............: avg=1.01s   min=1s     med=1s     max=1.2s     p(90)=1.01s    p(95)=1.03s
     iterations.....................: 3000    98.395736/s
     vus............................: 100     min=100     max=100
     vus_max........................: 100     min=100     max=100
```