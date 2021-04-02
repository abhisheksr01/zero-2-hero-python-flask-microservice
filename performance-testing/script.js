import http from 'k6/http';
import { check, group, sleep } from "k6";

export default function () {
  let response = http.get(`http://${__ENV.ROOT_ENDPOINT}/greetings/abhishek`)
  check(response, {
      'is status 200': (r) => r.status === 200,
    });
}