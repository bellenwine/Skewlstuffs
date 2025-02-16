start
    input questionsRemain
    display gameBoard with categories and point values

    while questionsRemain:
        input category and value
        display correspondingQuestion
        start timer

        if player responds before timer ends:
            if response is correct:
                award points
                allow player to choose nextQuestion
            else:
                deduct points
                allow nextPlayer to answer
        else:
            no points awarded
            allow nextPlayer to answer

    display finalJeopardyRound
    input playersWager
    display finalQuestion
    start timer
    input playersResponse
    adjust scores

    declare winner
stop
