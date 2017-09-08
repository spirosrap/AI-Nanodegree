class AlphaBetaPlayer(IsolationPlayer):

    def get_move(self, game, time_left):

        self.time_left = time_left

        legalMoves = game.get_legal_moves(game.active_player)
        if(len(legalMoves)==0):
            return (-1,-1)
        elif (len(legalMoves)==1):
            return legalMoves[0]    
        best_move = legalMoves[0]
        depth = 1
        try:
            while True:
                if depth >= 151:
                    return best_move
                best_move = self.alphabeta(game, depth)
                depth += 1

        except SearchTimeout:
            pass

        return best_move

    def max_value(self, game, depth,alpha,beta):
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()          
        legalMoves = game.get_legal_moves(game.active_player)
        depth -= 1
        if (not legalMoves) or depth <= 0:
            return self.score(game,self)
                      
        v = float('-inf')
        for move in legalMoves:
            v = max(v, self.min_value(game.forecast_move(move),depth,alpha,beta))
            if v >= beta:
                return v
            alpha = max(alpha,v)    
        return v
            
    def min_value(self, game, depth,alpha,beta):

        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
                     
        legalMoves = game.get_legal_moves(game.active_player)
        depth -= 1
        if (not legalMoves) or depth <= 0:
            return self.score(game,self)
            
        v = float('inf')
        for move in legalMoves:
            v = min(v, self.max_value(game.forecast_move(move),depth,alpha,beta))
            if v <= alpha:
                return v
            beta = min(beta,v)    
        
        return v


    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        legalMoves = game.get_legal_moves(game.active_player)
        if(len(legalMoves)==0):
            return (-1,-1)
        elif (len(legalMoves)==1):
            return legalMoves[0]    
        best_move = legalMoves[0]

        if depth <= 0:
            return best_move

        v = float("-inf")
        for move in legalMoves:
            try:
                v = self.min_value(game.forecast_move(move),depth,alpha,beta)
                if v > alpha:
                    alpha = v
                    best_move = move
            except SearchTimeout:
                pass
                        

        return best_move

            