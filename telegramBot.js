
const TelegramBot = require('node-telegram-bot-api');

const pualToken = '576441925:AAGE_O8rtJ70pU5UqtO_r0tD-ldrTUnvTjc';

const zhenruToken = '605119890:AAFLpkOguOSDexbm5Gmbm2bMEP8veKrjIq8';

const pualBot = new TelegramBot(pualToken, {polling: false});

const zhenruBot = new TelegramBot(zhenruToken, {polling: false});

const groupId = -277055326;

var counter = 0;

console.log("bots are runing!");

while(true){
  setTimeout(function(){
     chat(counter);
     counter++;
  }, 5000);
}

function chat(counter){
if(counter % 2 == 0 && counter < 100){
    console.log("pual is runing!");
    pualBot.sendMessage(groupId, "Hello, i am pual's robot!");
  }
  
  else if(counter % 2 == 1 && counter < 100){
     console.log("Zhenru is runing!");
     zhenruBot.sendMessage(groupId, "Hello, i am zhenru's robot!");
  } 
  else{
    break;
  } 
}