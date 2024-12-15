const socket = io('https://28d1b37c-5d30-43a0-ad54-be983c9a3584-00-3ak9nkob3bwsz.janeway.replit.dev/'); // Replace with your Replit URL

let board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
];

function initializeBoard() {
    const boardContainer = document.getElementById('board');
    boardContainer.innerHTML = '';
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            const cell = document.createElement('div');
            cell.textContent = board[row][col];
            cell.onclick = () => makeMove(row, col);
            boardContainer.appendChild(cell);
        }
    }
}

function makeMove(row, col) {
    if (board[row][col] === ' ') {
        board[row][col] = 'X'; // Player's move, change 'X' to the actual player marker
        socket.emit('move', { row, col, board });
    }
}

function resetGame() {
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ];
    socket.emit('reset');
}

socket.on('updateBoard', (updatedBoard) => {
    board = updatedBoard;
    initializeBoard();
});

initializeBoard();