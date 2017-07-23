# Python CNN that plays Crash Bandicoot

This project is forked from sentdex's pygta5 self-driving AI project.
The goal of this project is to utilize the same environment to teach an AI how to play Crash Bandicoot.

Starting from trying to complete the first level all on it's own to perhaps completing multiple levels on its own
and navigating the main menu.

This readme is going to be a kind of a notebook "recording" all the past iterations of the AI.

## v0.01
First iteration of the project was basically to see if the alexnet training model could make any sense of the game.
And it did! Suprisingly well, in fact. 

The setup was similar to v0.01 of pygta5. Some tweaks and notes:

- The 1280x720 game screen was scaled down to 160x120 grayscale
- Output was 27 different key combinations, which was overly complex, I know
- 20 thousand frames of training data, balanced to around 6000 frames as there was a lot of no keys and a lot of forward
- 40 epochs that took around 30 minutes got the model into a good accuracy with GPU training
- I tried with an increased resolution of 320x240 with no significant difference
 - It probably just caused more uncertainty, making it worse
 - Crash Bandicoot is already at low resolution, even 1280x720 scales the actual game resolution upwards, so increasing resolution might just be pointless altogether
- The AI was able to go about 75% of the first level quite well, being able to spin off crabs and turtles, and most of the time doing perfect jumps across pits.

Some ideas for v0.02

- Reduce output complexity. All the AI really needs is key combinations so it can run&jump and run&spin in 4 different directions, which would total about 15 combinations
- Maintain resolution, but record color. Sometimes there is too much background complexity in the game that could make it difficult for the AI to identify where Crash is and where it should be going
- Try out inception v3
- More training data! Around 100 thousand frames, possibly gameplay from other levels as well which could help the AI manage in more unpredictable setups. There were some moments where the AI jumped at the wrong position when a turtle was in a different place, causing it to fall to a pit, and other times just simply walking towards a turtle and dying