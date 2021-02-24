def MassVote(N, Votes):
    #int N, int [] Votes
    sumOfVotes = sum(Votes)
    percents = []
    maxVotes = 0
    winner = -1
    for votes in Votes:
        if votes > maxVotes:
            winner = Votes.index(votes) + 1
            maxVotes = votes
        elif votes == maxVotes:
            winner = -1

    if winner == -1:
        return "no winner"

    if maxVotes / sumOfVotes > 0.5:
        return "majority winner " + str(winner)
    else:
        return "minority winner " + str(winner)