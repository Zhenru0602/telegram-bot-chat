var util = require("util");
var spawn = require("child_process").spawn;

var process = spawn('python',["index.py"]);

console.log('runing python');