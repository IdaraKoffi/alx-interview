#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

// Check if the movie ID argument is provided
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// API URL for the specific movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// First request to get the movie data
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Access the character URLs from the movie data
  const characters = movieData.characters;

  // Helper function to fetch each character name and print in order
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  };

  // Sequentially fetch each character and print their names in order
  async function printCharacters () {
    for (const charUrl of characters) {
      try {
        const characterName = await fetchCharacter(charUrl);
        console.log(characterName);
      } catch (err) {
        console.error(err);
      }
    }
  }

  // Call the function to print all characters
  printCharacters();
});
