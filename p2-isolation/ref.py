        previous_move = game.get_player_location(game.inactive_player)
        def reflect(x,y):
            z = 6 - x
            k = 6 - y
            return (z,k)
        if previous_move != None:
            (x,y) = previous_move    
            if reflect(x,y) in legalMoves:
                return reflect(x,y)
        else:
            print(3,3)
            return (3,3)        
