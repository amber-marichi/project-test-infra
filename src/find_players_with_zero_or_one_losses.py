'''
2225. Find Players With Zero or One Losses

You are given an integer array matches where matches[i] = [winneri, loseri]
indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:
You should only consider the players that have played at least one match.
The testcases will be generated such that no two matches
will have the same outcome.
'''


def find_winners(matches: list[list[int]]) -> list[list[int]]:
    'Solution for 2225. Find Players With Zero or One Losses'
    winners, onnes, outs = set(), set(), set()
    for win, lost in matches:
        if win not in outs and win not in onnes:
            winners.add(win)
        if lost in outs:
            continue
        if lost in winners:
            winners.remove(lost)
        if lost in onnes:
            onnes.remove(lost)
            outs.add(lost)
        else:
            onnes.add(lost)

    return [sorted(list(winners)), sorted(list(onnes))]
