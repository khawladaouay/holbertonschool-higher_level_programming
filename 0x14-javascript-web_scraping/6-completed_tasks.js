#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, f, body) {
  const dic = {};
  for (const resp of JSON.parse(body)) {
    if (resp.completed) {
      if (dic[resp.userId]) {
        data[resp.userId] += 1;
      } else {
        dic[resp.userId] = 1;
      }
    }
  }
  console.log(data);
});
