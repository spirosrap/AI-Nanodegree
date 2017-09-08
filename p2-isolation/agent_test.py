"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent_test

from importlib import reload
from sample_players import RandomPlayer
from sample_players import HumanPlayer
from game_agent_test import IsolationPlayer
from game_agent_test import MinimaxPlayer
from sample_players import GreedyPlayer

class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent_test)
        self.player1 = MinimaxPlayer(IsolationPlayer())
        self.player2 = GreedyPlayer()
        self.game = isolation.Board(self.player1, self.player2)


    def test(self):
    	for i in range(0,50):
    		p1Move = self.player1.minimax(self.game,3)
    		if p1Move == (-1,-1):
    			print("exasa")
    			break
	    	self.game.apply_move(p1Move)    		
	    	
    		p2Move = self.player2.get_move(self.game,1)
    		if p2Move == (-1,-1):
    			print("nikisa")
    			break
	    	self.game.apply_move(p2Move)

if __name__ == '__main__':
	unittest.main()

