import streamlit as st
from main import TicTacToe

# Persistent state initialization
if 'tic_tac_toe' not in st.session_state:
    st.session_state.tic_tac_toe = TicTacToe()
    st.session_state.tic_tac_toe.player_turn = st.session_state.tic_tac_toe.get_random_first_player()

game = st.session_state.tic_tac_toe

# Apply text styles
st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Draw board function
def draw_board():
    # Game board displayed with buttons
    for row in range(1, 10, 3):
        cols = st.columns(3)
        for i in range(3):
            col = cols[i]
            with col:
                if st.button(game.board[row + i] if game.board[row + i] != "" else " ", key=row + i):
                    if game.board[row + i] == "":
                        game.board[row + i] = game.player_turn
                        if game.has_player_won(game.player_turn):
                            st.success(f"Player {game.player_turn} wins!")
                            game.board = [''] * 10
                        elif game.is_board_full():
                            st.error("It's a tie!")
                            game.board = [''] * 10
                        else:
                            game.player_turn = game.swap_player_turn()

# Header
st.markdown('<p class="big-font">Tic Tac Toe</p>', unsafe_allow_html=True)

# Display the board
draw_board()

# Show whose turn it is
st.write("Player Turn: ", game.player_turn)

# Reset game button
if st.button('Restart game'):
    game.board = [''] * 10
    game.player_turn = game.get_random_first_player()