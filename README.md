# Morris Variant Strategy Game AI

This project implements Artificial Intelligence (AI) strategies for playing a variant of the Morris game, focusing on different phases of the game and incorporating both traditional and advanced techniques to decide the best moves. The project is divided into several parts, each aiming to explore and implement AI strategies like MINIMAX and ALPHA-BETA pruning, along with improvements in the static estimation functions for game state evaluations.

## Visual Explanation of NINEN MEN MORRIS GAME
<img width="410" alt="image" src="https://github.com/nishan2293/PySparkKMeansImageCompression/assets/157925518/762349af-c1cb-429d-aee7-e10786042159">

## Part I: MINIMAX

### MiniMaxOpening
- **Description**: This program is designed to play the opening phase of the Morris game. It uses the MINIMAX algorithm to decide the best move for White.
- **Usage**: `MiniMaxOpening <input board file> <output board file> <search depth>`

### MiniMaxGame
- **Description**: This program takes over from the opening phase to play through the midgame/endgame phases, continuing to utilize the MINIMAX algorithm for White's moves.
- **Usage**: `MiniMaxGame <input board file> <output board file> <search depth>`

## Part II: ALPHA-BETA

### ABOpening
- **Description**: Similar to MiniMaxOpening but employs the ALPHA-BETA pruning algorithm to enhance performance while ensuring the same move quality.
- **Usage**: `ABOpening <input board file> <output board file> <search depth>`

### ABGame
- **Description**: Continues from the ABOpening phase into the midgame/endgame, using ALPHA-BETA pruning for improved efficiency.
- **Usage**: `ABGame <input board file> <output board file> <search depth>`

## Part III: PLAY A GAME FOR BLACK

### MiniMaxOpeningBlack
- **Description**: Adapts MiniMaxOpening to calculate the best move for Black during the opening phase.
- **Usage**: `MiniMaxOpeningBlack <input board file> <output board file> <search depth>`

### MiniMaxGameBlack
- **Description**: Extends MiniMaxGame's strategies to Black for the midgame/endgame phases.
- **Usage**: `MiniMaxGameBlack <input board file> <output board file> <search depth>`

## Part IV: STATIC ESTIMATION IMPROVEMENT

### MiniMaxOpeningImproved
- **Description**: Revises MiniMaxOpening with an improved static estimation function for more strategic opening moves.
- **Usage**: `MiniMaxOpeningImproved <input board file> <output board file> <search depth>`

### MiniMaxGameImproved
- **Description**: Implements the improved static estimation function in the midgame/endgame phases.
- **Usage**: `MiniMaxGameImproved <input board file> <output board file> <search depth>`

## EXAMPLES

### Alpha beta pruning improves the minimax algorithm 

#### 21 positions in the game in total 
##### x: position not occupied
##### W: Position occupied by white pawn player 
##### B: Position occupied by black pawn player
<img width="993" alt="image" src="https://github.com/nishan2293/PySparkKMeansImageCompression/assets/157925518/97364091-43be-4148-bc33-fe4e489d6992">


### As shown below drastic reduction in number of static function evaluations after alpha beta algorithm
<img width="1178" alt="image" src="https://github.com/nishan2293/PySparkKMeansImageCompression/assets/157925518/4514a6a3-d3fc-499f-ad12-bdd6e9fb5159">


## Important Notes
- Ensure that the input and output files follow the specified format for representing board positions.
- While ALPHA-BETA programs should perform faster due to reduced node evaluations, they must arrive at the same moves as their MINIMAX counterparts for consistency.
- The improved static estimation function should demonstrably enhance game strategy, justified with specific examples and explanations.

