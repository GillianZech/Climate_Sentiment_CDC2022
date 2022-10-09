/* 
We initially tried using javascript's sentiment library to analyze our data, but chose
to keep everything in python to make it easier to communicate between files
*/

var Sentiment = require('sentiment');
var sentiment = new Sentiment();
var result = sentiment.analyze('Cats are stupid.');
console.dir(result);