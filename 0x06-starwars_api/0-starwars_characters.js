#!/usr/bin/node
const request = require('request');

// Check if movie ID is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

// Get the Movie ID from command line arguments
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  // Parse response body
  const filmData = JSON.parse(body);

  // Fetch characters in the order provided
  const characters = filmData.characters;
  const fetchCharacter = (index) => {
    if (index === characters.length) return; // Base case: stop when done

    request(characters[index], (err, res, charBody) => {
      if (err) {
        console.error(err);
        return;
      }
      if (res.statusCode !== 200) {
        console.error(`Error: ${res.statusCode}`);
        return;
      }

      const character = JSON.parse(charBody);
      console.log(character.name); // Print character name
      fetchCharacter(index + 1); // Recursively fetch the next character
    });
  };

  fetchCharacter(0); // Start fetching characters
});
