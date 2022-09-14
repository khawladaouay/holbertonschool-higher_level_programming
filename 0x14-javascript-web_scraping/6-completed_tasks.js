#!/usr/bin/node
const axios = require('axios').default;
const Url = process.argv[2];
const dic = {};
let i = 0;
axios.get(Url)
  .then(function (response) {
    for (i = 0; i < response.data.length; i++) {
      if (!dic[response.data[i].userId]) {
        dic[response.data[i].userId] = 0;
      }
      if (response.data[i].completed === true) {
        dic[response.data[i].userId] += 1;
      }
    }
    console.log(dic);
  });
