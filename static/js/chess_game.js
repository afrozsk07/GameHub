// Chess Game Implementation using chess.js and chessboard.js
// Supports: Local multiplayer (human vs human), Human vs Computer (easy, medium, hard)

let board = null;
let game = null;
let mode = null;
let aiLevel = null;
let isPlayerWhite = true;
let statusElement = null;

function onDragStart (source, piece, position, orientation) {
    if (game.game_over()) return false;
    if (mode !== 'human') {
        if ((game.turn() === 'w' && !isPlayerWhite && piece.search(/^w/) !== -1) ||
            (game.turn() === 'b' && isPlayerWhite && piece.search(/^b/) !== -1)) {
            return false;
        }
    }
}

function makeRandomMove() {
    const possibleMoves = game.moves();
    if (possibleMoves.length === 0) return;
    const move = possibleMoves[Math.floor(Math.random() * possibleMoves.length)];
    game.move(move);
    board.position(game.fen());
    updateStatus();
}

function minimax(depth, isMaximizing) {
    if (depth === 0 || game.game_over()) {
        return evaluateBoard(game.board());
    }
    const moves = game.moves();
    let bestEval = isMaximizing ? -Infinity : Infinity;
    for (let move of moves) {
        game.move(move);
        const evalScore = minimax(depth - 1, !isMaximizing);
        game.undo();
        if (isMaximizing) {
            if (evalScore > bestEval) bestEval = evalScore;
        } else {
            if (evalScore < bestEval) bestEval = evalScore;
        }
    }
    return bestEval;
}

function evaluateBoard(boardArr) {
    const pieceValues = { p: 1, n: 3, b: 3, r: 5, q: 9, k: 0 };
    let evalScore = 0;
    for (let row of boardArr) {
        for (let piece of row) {
            if (!piece) continue;
            const value = pieceValues[piece.type] || 0;
            evalScore += piece.color === 'w' ? value : -value;
        }
    }
    return evalScore;
}

function getBestMove(depth) {
    let bestMove = null;
    let bestEval = -Infinity;
    for (let move of game.moves()) {
        game.move(move);
        const evalScore = -minimax(depth - 1, false);
        game.undo();
        if (evalScore > bestEval) {
            bestEval = evalScore;
            bestMove = move;
        }
    }
    return bestMove;
}

function makeAIMove() {
    if (aiLevel === 'easy') {
        makeRandomMove();
    } else {
        let depth = aiLevel === 'medium' ? 2 : 3;
        const move = getBestMove(depth);
        if (move) {
            game.move(move);
            board.position(game.fen());
            updateStatus();
        }
    }
}

function onDrop (source, target) {
    let move = game.move({ from: source, to: target, promotion: 'q' });
    if (move === null) return 'snapback';
    updateStatus();
    if (mode !== 'human' && !game.game_over()) {
        setTimeout(makeAIMove, 400);
    }
}

function updateStatus() {
    let status = '';
    let moveColor = game.turn() === 'w' ? 'White' : 'Black';
    if (game.in_checkmate()) {
        status = 'Game over, ' + (game.turn() === 'w' ? 'Black' : 'White') + ' wins by checkmate!';
    } else if (game.in_draw()) {
        status = 'Game over, drawn position.';
    } else {
        status = moveColor + ' to move';
        if (game.in_check()) {
            status += ' (in check)';
        }
    }
    if (statusElement) statusElement.textContent = status;
}

function onSnapEnd () {
    board.position(game.fen());
}

function startNewGame() {
    game = new Chess();
    board.orientation('white');
    board.position(game.fen());
    updateStatus();
}

function showChessArea() {
    document.getElementById('mode-selection').classList.add('hidden');
    document.getElementById('difficulty-selection').classList.add('hidden');
    document.getElementById('chess-area').classList.remove('hidden');
    // Only initialize board if not already done
    if (!board) {
        statusElement = document.getElementById('chess-status');
        board = Chessboard('chess-board-container', {
            draggable: true,
            position: 'start',
            width: 400,
            pieceTheme: 'https://chessboardjs.com/img/chesspieces/wikipedia/{piece}.png',
            onDragStart: onDragStart,
            onDrop: onDrop,
            onSnapEnd: onSnapEnd
        });
        document.getElementById('newGameBtn').addEventListener('click', startNewGame);
    }
    startNewGame();
}

document.addEventListener('DOMContentLoaded', () => {
    // Hide chess area initially
    document.getElementById('chess-area').classList.add('hidden');
    document.getElementById('difficulty-selection').classList.add('hidden');
    // Mode selection
    document.getElementById('select-human').addEventListener('click', () => {
        mode = 'human';
        aiLevel = null;
        showChessArea();
    });
    document.getElementById('select-computer').addEventListener('click', () => {
        document.getElementById('mode-selection').classList.add('hidden');
        document.getElementById('difficulty-selection').classList.remove('hidden');
    });
    // Difficulty selection
    document.querySelectorAll('.difficulty-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            mode = 'computer';
            aiLevel = e.target.getAttribute('data-difficulty');
            showChessArea();
        });
    });
}); 