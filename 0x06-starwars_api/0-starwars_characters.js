#!/usr/bin/node

const request = require('request');

const film = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

request(filmURL + film, async function (err, res, body) {
  if (err) return console.error(err);
  const characters = JSON.parse(body).characters;
  for (const character of characters) {
    await new Promise(function (resolve, reject) {
      request(character, (err, res, body) => {
        if (err) return console.error(err);
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
