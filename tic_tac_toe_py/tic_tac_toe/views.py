from django.views.generic import TemplateView
from django.shortcuts import render, redirect

# Using a generic class based view and specifically TemplateView to handle displaying of dynamic data in the template
class HomePageView(TemplateView):
    template_name = "index.html" 

    def get(self, request, *args, **kwargs): # using 'get' method
        # Display the first player's turn
        if 'playButton' not in request.session:
            request.session['currentplayer'] = "X"
            request.session['subCurrentPlayer'] = "It's " + request.session['currentplayer'] + "'s turn"
            request.session['gamestatus'] = request.session['subCurrentPlayer']   
        # Get session variables and store each of them separate variables   
        gameState0 = request.session.get('gamestate0')
        gameState1 = request.session.get('gamestate1')
        gameState2 = request.session.get('gamestate2')
        gameState3 = request.session.get('gamestate3')
        gameState4 = request.session.get('gamestate4')
        gameState5 = request.session.get('gamestate5')
        gameState6 = request.session.get('gamestate6')
        gameState7 = request.session.get('gamestate7')
        gameState8 = request.session.get('gamestate8')
        disable = request.session.get('disable')
        gameStatus = request.session.get('gamestatus')
        # Go to the template and pass along the dynamic data that will be displayed in the template
        return self.render_to_response({'gamestate0': gameState0,'gamestate1': gameState1,'gamestate2': gameState2,'gamestate3': gameState3,'gamestate4': gameState4,'gamestate5': gameState5,'gamestate6': gameState6,'gamestate7': gameState7,'gamestate8': gameState8,'disable': disable,'gamestatus': gameStatus})

# Using a function-based view to receive input from the game's form and store it in session variables
def gameSave(request):
    if request.method == "POST":
        #Get the values from the game's form and store them in variables
        request.session['playButton'] = request.POST.get('playButton')
        cell0 = request.POST.get('cell0')
        cell1 = request.POST.get('cell1')
        cell2 = request.POST.get('cell2')
        cell3 = request.POST.get('cell3')
        cell4 = request.POST.get('cell4')
        cell5 = request.POST.get('cell5')
        cell6 = request.POST.get('cell6')
        cell7 = request.POST.get('cell7')
        cell8 = request.POST.get('cell8')
        request.session['restartButton'] = request.POST.get('restartButton')
        
        # Check if the restart button has been clicked and if so redirect the program execution to the restart function
        if request.session['restartButton'] == "Restart Button": 
            return redirect('restart/')
        
        """
        Store the player's value for the corresponding clicked box, each in a separate session variable
        and then redirect to the resultsValidation function
        """
        if cell0 == "0": 
            request.session['gamestate0'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell1 == "1": 
            request.session['gamestate1'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell2 == "2": 
            request.session['gamestate2'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell3 == "3": 
            request.session['gamestate3'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell4 == "4": 
            request.session['gamestate4'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell5 == "5": 
            request.session['gamestate5'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell6 == "6": 
            request.session['gamestate6'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell7 == "7": 
            request.session['gamestate7'] = request.session['currentplayer']
            return redirect('resultsValidation/')
        if cell8 == "8": 
            request.session['gamestate8'] = request.session['currentplayer']
            return redirect('resultsValidation/')

# Using a function-based view to handle validation of the game for a win, draw or continued play 
def resultsValidation(request):
   # Validate the game's state after a player has played for a win, draw or if the game continues
   if ((request.session.get('gamestate0') == request.session.get('gamestate1') and request.session.get('gamestate1') == request.session.get('gamestate2') and request.session.get('gamestate2') == "X") or
        (request.session.get('gamestate0') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate8') and request.session.get('gamestate8') == "X") or
        (request.session.get('gamestate0') == request.session.get('gamestate3') and request.session.get('gamestate3') == request.session.get('gamestate6') and request.session.get('gamestate6') == "X") or
        (request.session.get('gamestate1') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate7') and request.session.get('gamestate7') == "X") or
        (request.session.get('gamestate2') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate6') and request.session.get('gamestate6') == "X") or
        (request.session.get('gamestate2') == request.session.get('gamestate5') and request.session.get('gamestate5') == request.session.get('gamestate8') and request.session.get('gamestate8') == "X") or
        (request.session.get('gamestate3') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate5') and request.session.get('gamestate5') == "X") or
        (request.session.get('gamestate6') == request.session.get('gamestate7') and request.session.get('gamestate7') == request.session.get('gamestate8') and request.session.get('gamestate8') == "X") ):
        del request.session['gamestatus']
        request.session['gamestatus'] = "Player X has won!"
        request.session['disable'] = "disabled"
        return redirect('/')
   elif ((request.session.get('gamestate0') == request.session.get('gamestate1') and request.session.get('gamestate1') == request.session.get('gamestate2') and request.session.get('gamestate2') == "O") or
        (request.session.get('gamestate0') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate8') and request.session.get('gamestate8') == "O") or
        (request.session.get('gamestate0') == request.session.get('gamestate3') and request.session.get('gamestate3') == request.session.get('gamestate6') and request.session.get('gamestate6') == "O") or
        (request.session.get('gamestate1') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate7') and request.session.get('gamestate7') == "O") or
        (request.session.get('gamestate2') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate6') and request.session.get('gamestate6') == "O") or
        (request.session.get('gamestate2') == request.session.get('gamestate5') and request.session.get('gamestate5') == request.session.get('gamestate8') and request.session.get('gamestate8') == "O") or
        (request.session.get('gamestate3') == request.session.get('gamestate4') and request.session.get('gamestate4') == request.session.get('gamestate5') and request.session.get('gamestate5') == "O") or
        (request.session.get('gamestate6') == request.session.get('gamestate7') and request.session.get('gamestate7') == request.session.get('gamestate8') and request.session.get('gamestate8') == "O")): 
            del request.session['gamestatus']
            request.session['gamestatus'] = "Player O has won!"
            request.session['disable'] = "disabled"
            return redirect('/')
   elif ('gamestate0' in request.session and 'gamestate1' in request.session and 'gamestate2' in request.session and 'gamestate3' in request.session and 'gamestate4' in request.session and 'gamestate5' in request.session and 'gamestate6' in request.session and 'gamestate7' in request.session and 'gamestate8' in request.session):
            del request.session['gamestatus']
            request.session['gamestatus'] = "Game ended in a draw!"
            return redirect('/')
   else:
            if request.session.get('currentplayer') == "X":
                request.session['currentplayer'] = "O"
            else:
                request.session['currentplayer'] = "X"
            subCurrPlayerDuringGame = "It's " + request.session["currentplayer"] + "'s turn"
            request.session["gamestatus"] = subCurrPlayerDuringGame
            return redirect('/')

# Using a function-based view to handle a restart of the game  
def restart(request):

    """
    Erase the game's session variables so as to start the game afresh and they are placed in separate 'try except'
    blocks so as to allow the game to delete them independent of each other
    """
    try:
        del request.session["currentplayer"]
    except KeyError:
          pass
    try:
        del request.session["gamestate0"]
    except KeyError:
          pass
    try:
        del request.session["gamestate1"]
    except KeyError:
          pass
    try:
        del request.session["gamestate2"]
    except KeyError:
          pass
    try:
        del request.session["gamestate3"]
    except KeyError:
          pass
    try:
        del request.session["gamestate4"]
    except KeyError:
          pass
    try:
        del request.session["gamestate5"]
    except KeyError:
          pass
    try:
        del request.session["gamestate6"]
    except KeyError:
          pass
    try:
        del request.session["gamestate7"]
    except KeyError:
          pass
    try:
        del request.session["gamestate8"]
    except KeyError:
          pass
    try:
        del request.session["gamestatus"]
    except KeyError:
          pass
    try:
        del request.session["disable"]
    except KeyError:
          pass
    # Start new session variables for the game to start afresh with the displaying of the first player's turn
    request.session['currentplayer'] = 'X'
    request.session['gamestatus'] = request.session.get('subCurrentPlayer')
    # Redirect to the root function
    return redirect('/')



