def play():

    teamA=300;
    teamB=200;

    if(teamA>teamB):
      return "Team-A is the Winner";

    else:
      return "Team-B is the Winner";


print(play());


def calculate(p,n,r):
    return p*n*r;


print(calculate(10000, 12 , 0.1));