#!/usr/bin/node
const file = require('fs');
file.writeFile(process.argv[2], process.argv[3], 'utf8', function(error, content){
	console.log(error || content);
});
