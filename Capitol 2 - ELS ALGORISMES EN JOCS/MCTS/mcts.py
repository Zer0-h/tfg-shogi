import numpy as np
from view_board import render
from game import place_piece

board = np.array(
    [
        [0, -1, -1, -1, 1, 0, -1],
        [0, 1, -1, 1, 1, 0, 1],
        [-1, 1, -1, 1, 1, 0, -1],
        [1, -1, 1, -1, -1, 0, -1],
        [-1, -1, 1, -1, 1, 1, -1],
        [-1, 1, 1, -1, 1, -1, 1],
    ]
)


def dummy_model_predict(board):
    """Dummy model prediction function returning fixed value and policy head."""
    value_head = 0.5
    policy_head = [0.5, 0, 0, 0, 0, 0.5, 0]
    return value_head, policy_head


class Node:
    def __init__(self, prior, turn, state):
        """Initialize a Monte Carlo Tree Search (MCTS) node."""
        self.prior = prior
        self.turn = turn
        self.state = state
        self.children = {}
        self.value = 0

    def expand(self, action_probs):
        """Expand the node by creating child nodes for available actions."""
        for action, prob in enumerate(action_probs):
            if prob > 0:
                next_state = place_piece(
                    board=self.state, player=self.turn, action=action
                )
                self.children[action] = Node(
                    prior=prob, turn=self.turn * -1, state=next_state
                )


# Initialize root node
root = Node(prior=0, turn=1, state=board)

# Expand the root node
value, action_probs = dummy_model_predict(root.state)
root.expand(action_probs=action_probs)

# Render results
# render(root.children[0].state)
render(root.children[5].state)
