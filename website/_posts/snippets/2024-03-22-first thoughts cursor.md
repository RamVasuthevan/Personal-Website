---
layout: post
title:  "First Thoughts Cursor"
image: "/assets/snippets/First-Thoughts-Cursor/Photo_of_Interchanged_by_Willem_de_Kooning.jpg"
permalink: snippets/First-Thoughts-Cursor
categories: snippets
---

{% include image.html 
   src="/assets/snippets/First-Thoughts-Cursor/Photo_of_Interchanged_by_Willem_de_Kooning.jpg" 
   alt="Photo of Interchange by Willem de Kooning taken by Andrew Cho"
   caption="Photo of Interchange by Willem de Kooning taken by [Andrew Cho/Wikipedia](https://en.wikipedia.org/wiki/File:Photo_of_Interchanged_by_Willem_de_Kooning.jpg)" 
%}

- Very esay to downloand and setup
- was sceptical at first because https://github.com/getcursor/cursor/issues/718

This helped get 1passwaord and github to work togther:
https://1password.community/discussion/142814/1password-ssh-within-local-devcontainer-in-vscode

Must open Cursor from CLI for it to work work with 1passwaord and devcontainer

I ran out of free token the first day I started using it.


Let's get started with FEN2SVG
- [Forsyth-Edwards Notation (FEN)
](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) is a notation for describing a particular board position of a chess game. Looks pretty simple to parse
- [Portable Game Notation (PGN)](https://en.wikipedia.org/wiki/Portable_Game_Notation) is a standard plain text format for recording chess games. A PGN file can have many games


Similar Tools
- Chess.com and I assume most chesse sites all you to upload an FEN string
- http://www.fen-to-image.com/
- https://fen2image.chessvision.ai/
- https://fen2png.com/
- [chess-image-generator](https://github.com/andyruwruw/chess-image-generator) 53 stars
- [https://github.com/Hart-House-Chess-Club/fen-to-image](https://github.com/Hart-House-Chess-Club/fen-to-image) 1 star
- [fen-image-generator.ts](https://gist.github.com/loicmarie/6426394790fb0155225fa4994f89cbdf) 1 star


It took a couple of attempts to get this write this;

Cursor tried to write code like:
// This is a placeholder for the actual implementation
// You would need to parse the FEN string and render the chess pieces on the SVG chessboard

>I want a page with the following:
>- Nice looking page with an svg chess board, a textbox for FEN strings, and a download button
>- The FEN String should appear on the cheeseboard
>- The pieces on the cheese board should be able to be moved
>- The URL should be based on the FEN string
>- Any changes to the FEN string, cheeseboard and URL should be reflected in all 3
>- The chessboard, fen string should start at the starting position of a chess game
>- If there is an error on the FEN string, an error text should appear in red, and the URL should not be updated
>You can only create index.html, script.js, style.css

>Think carefully, write all of the code, and ensure the project is done. There should be no comments. No examples of all production code

I tried a bunch of times but I couldn't get it to zero-shot