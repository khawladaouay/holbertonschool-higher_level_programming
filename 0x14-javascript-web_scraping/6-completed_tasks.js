#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, f, body) {
  const dic = {};
  for (const res of JSON.parse(body)) {
    if (res.completed) {
      if (dic[res.userId]) {
        data[res.userId] += 1;
      } else {
        dic[res.userId] = 1;
      }
    }
  }
  console.log(data);
});
