import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  vus: 100,
  duration: '30s',
};

export default function () {
  const res = http.get('http://127.0.0.1:5000/lac/seg?text=剪刀T恤香蕉台灯蜡烛手表杯子叶子钥匙勺子');
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}