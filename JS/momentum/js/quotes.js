'use strict';

const quotes = [{
    quote: "If you want something you have never had, you must be willing to do something you have have never done.",
    author: "Thomas Jefferson",
  },
  {
    quote: "Stay hungry, Stay foolish.",
    author: "Steve Jobs",
  },
  {
    quote: "Life begins at the end of your comfort zone.",
    author: "Neale Donald Walsch",
  },
  {
    quote: "You don't have to be great to start, but you have to start to be great.",
    author: "Zig Ziglar",
  },
  {
    quote: "A river cuts through rock, not because of its power, but because of its persistance.",
    author: "Jim Watkins",
  },
  {
    quote: "I am not what happened to me, I am what I choose to become.",
    author: "Carl Gustav Jung",
  },
  {
    quote: "If you want to live a happy life, tie it to a goal, not to people or things.",
    author: "Albert Einstein",
  },
  {
    quote: "Doubt kills more dreams than failure ever will.",
    author: "Suzy Kassem",
  },
  {
    quote: "Don't quit. Suffer now and live the rest of your life as a champion.",
    author: "Muhammad Ali",
  },
  {
    quote: "어떻게 날아야 하는지 고민하지 말아요, 소중한 한 조각 추억이 당신을 날게 할 거예요.",
    author: "금강선",
  },
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");

const randomQuo = Math.floor(Math.random() * quotes.length);
const todaysQuote = quotes[randomQuo];

quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;