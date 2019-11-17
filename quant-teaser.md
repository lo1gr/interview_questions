## Statistical Inference (15 questions)

#### 1. Is 1343 a prime number?
maybe combination of 2 primes?
100*10
  17
  49
   3
https://www.codecogs.com/eqnedit.php?latex=\sum&space;67&plus;88999"

$`\sqrt{2}`$

#### 2. What is the singles digit for 2^230?
mutliples of 2: 2 4 8 6 2   and repeat!
modulo 4
pattern is periodic with period 4
230:4 = 57 + 2     so it is 4 ?

2^4 =


#### 3. What is the singles digit for 2^320?
mutliples of 2: 2 4 8 6   an repeat!
modulo 4
pattern is periodic with period 4
320:4 = 80  remainder = 0   so it is 6   (4th number in modulo)
Answer = 6

2^999?
999:4 = 249 r = 3   answer: 8

#### 4. If A, B, and C are integers between 1 and 10 (inclusive),
#### how many different combinations of A, B, and C exist such that A<B<C?
10 choose 3 gives you the number of distinct 3-number combinations in the range [1, 10].
10 choose 3 = 120 and can assign A to the lowest, B to the middle number, and C to the highest number.


#### 5. 89^2?
  89
  89
=7921
90*90 = 8100
8100 - 90 = 8010
8010 - 89 = 7921

#### 6. You have a deck of 52 cards. What’s the probability you draw exactly 1 heart in 2 draws with replacement?
2*(3/4*1/4)


#### 7. Solve x^x^x^… = 2
pattern. x^(x^(x^(x^(x...)))) = 2
x^(x^...) = 2
x^2 = 2
x = sqrt(2)



#### 8. What is the probability you draw two cards of the same color from a standard 52-card deck? You are drawing without replacement.
25/51


#### 9. You can buy chicken nuggets in packs of 5 or 11. What is the maximum number of chicken nuggets you can not buy
#### using only packs of 5 or 11?
1: not expressible
2: not
3: no
4: no
5: yes
...
The Chicken McNugget Theorem states that:
Theorem 2.1 For relatively prime integers m and n, the L;{m,n} is mn - m - n
5*11 -11 -5 = 39

The largest impossible number would be such that
you would have to subtract by 11, 4 times to get a
remainder divisible by 5.
44-5 = 39

7 13
6*13 = 78-7 = 71  

### max number if sell 6, 9 and 20:
The largest impossible number would be such that
you would have to subtract 20 twice to get a
remainder divisible by 3.
20*2 + 3 = 43



#### 10. What is the expected number of dice rolls until we get two 6’s in a row?
combinations:
get 1 first then any number
1: 6
2: 6
...  6 possibilities each
36 possibilities, 1 value.
1/36

#### 11. What is the expected number of dice rolls until we get two 6’s in a row?
a = expected additional rolls if we have not just tossed a 6
b = expected additional rolls if we have just tossed a 6
At beginning, expecting a rolls bc havent tossed a 6
If we have not just tossed a 6, then with probability 5/6 we toss a non-6 (cost: 1 toss)
and our expected additional waiting time is still 𝑎. With probability 1/6 we toss a 6
(cost: 1 toss) and our expected additional waiting time is 𝑏. Thus:

a = 1 + a*(5/6) + b*1/6

If we have just tossed a 6, then with probability 5/6 we toss a non-6 (Cost: 1 toss), and then
our expected additional waiting time is 𝑎. (With probability 1/6 the game is over.)
Thus:

b = 1 + a*(5/6)

a = 1 + a*(5/6) + b*1/6    <=> 6a/6 = 1 + a*(5/6) + (1 + a*(5/6))* (1/6)     <=>   a/6 = 7/6 + a*(5/36) <=> (6a/36)-a*(5/36) = 7/6    <=>  a = 42
b = 1 + a*(5/6)





#### 12. Does the price of a call option increase when volatility increases?
eg: 68% of the time an event will fall inside one standard deviation. 16% of the time it will be higher, 16%, lower.

Now, if my $100 stock has a STD of $10, there's a 16% chance it will trade above $110. But if the STD is $5, the chance is 2.3% per the chart below. The higher volatility makes the option more valuable as there's a highr chance of it being 'in the money.'


#### 13. When is gamma for an option the highest?
The option's delta is the rate of change of the price of the option with respect to its underlying security's price. The delta of an option ranges in value from 0 to 1 for calls (0 to -1 for puts) and reflects the increase or decrease in the price of the option in response to a 1 point movement of the underlying asset price.

Far out-of-the-money options have delta values close to 0 while deep in-the-money options have deltas that are close to 1.
How Delta is expected to change given a $1 move in the underlying is called Gamma.
Gamma is a measure of the rate of change of its delta.


When the option being measured is deep in or out of the money, gamma is small. When the option is near or at the money, gamma is at its largest.
At the money (ATM) is a situation where an option's strike price is identical to the price of the underlying security
All options that are a long position have a positive gamma, while all short options have a negative gamma.

Gamma is the rate of change for an option’s delta based on a single-point move in the delta’s price.

If the strike price is near the market price, then the odds of being in or out of the money could appear to be changing very quickly - even going back and forth repeatedly.

Gamma is the rate of change of the delta, so these sudden lurches in pricing are by definition the gamma.

#### 14. How many times a day does a clock’s hands overlap?
In 12 h the hands cross 11 times.
so they cross 1 time in 12/11 * 3600 = 3927.2727 = 65 min 27 sec.
1h 5min 27sec => 22times

The answer is 22. The angular speed of the minute hand is 360°/hr, whereas the angular speed of the hour hand is 30°/hr. The hands overlap when the difference in the angles swept by the hands is a multiple of 360°, and the angles swept over an amount of time by the hands are given by the formula angle swept = time * angular speed. In other words, 360°/hr*t – 30°/hr*t = n360°, where t is time in hours and n is some integer. You can simplify this to 330°/hr*t = n360°, and then n=11t/12hr. There are 24 hours in a day, so n = 22, which is the total number of times the hands overlap. Therefore, the hands do NOT overlap at 1:05 (30° from 12), 2:10 (60° from 12), etc, they overlap at the t’s that correspond to 30° + 30° * 1/11 (slightly after 1:05), 60° + 30° * 2/11 (slightly after 2:10), etc. The last overlap would be at angle of 330° + 30° * 11/11, which = 360°, or a full cycle. Thus, 11 overlaps in 12 hours, 22 overlaps in 24 hours.

#### 15. There is a car auction. The price of the car is uniform [0,1000], you do not know the actual value of the car. If you bid higher than the value of the car you get it, if you bid lower than the value of the car you don’t. If you know you can sell it on afterwards for x times its worth, what should you should you bid when: x=1.5 (e.g. For x=1.5, you bid 100, the car is worth 80, you get it and sell it on for 120, which is a 20 profit).
x = 1.5. Let's map the PNL from 0 -> 1000:
0: 0 profit
100: 50profit
200: 100profit
500: 250profit
1000: 500profit
so profit is [0,500] uniform
expected value: 1/2 * (500+0) = 250

x is the value of the item
The expected value of p given that you win the auction is x/2.
Thus the expected profit/loss is (1.5*(x/2)) - x = -0.25x
so should go at 0.



There are 10 ways of seating them oldest to youngest (5 ways clockwise, 5 ways counterclockwise). There are 5! = 120 possible seating arrangements. Probability is 10/120, or 8.33%. I believe the OP was right.


### 16. 0


Jane wants to auction off an item, but does not know where to go to find bidders. David offers to find bidders for her, but will charge her $10 per bidder he gets to show up. Each bidder will uniformly value the item between [500,1000). The highest bidder will win the item and pay the second-highest bidder's price (Vickrey auction). How many bidders should Jane pay David to find?

I need to maximize the difference between 𝐸[second largest bid out of n bidders] and 10𝑛. I'm not sure how to find 𝐸[2nd largest big]


### You have eight balls all of the same size. 7 of them weigh the same, and one of them weighs slightly more. How can you find the ball that is heavier by using a balance and only two weighings?

The first weighing determines how you conduct the second.

First weighing: Weigh three balls against three other balls on the balance.  Leave two out.

Second weighing, based on results of the first weighing:
IF they balance, THEN you know that all of the balls weighed are "normal".  So weigh one of them against one of the two-unweighed balls.  If those two balance, then you know that the last unweighed ball is the abnormal one.  If they do not balance, then the freshly-weighed ball will be lower on the lower scale and thus the abnormal one.
IF they do NOT balance, THEN you know that whichever side is lower on the balance contains the heavier ball.  So now you have narrowed it down to those three.  Of those three balls, weigh two of them against each other on the balance.  IF they equal, the unweighed third ball is the abnormal one.  If one of the two is lower on the balance, that is the heavier ball.



SIG:

#throw a die, as many euros as number on die.
#How much would you pay:
(1+2+3+4+5+6)/6 = 7*3/6
pay: 21/6 = 3.5

#now throw a die, if happy take euro, otherwise reroll:
Since expected payoff is 3.5 if get 4 or more we keep, if get 3 or less reroll:
1/2*5
first roll 1-3: 1/2 * 2     
second roll expected: 3.5

1/2 * 3.5 + 1/2 * 5
= 8.5/2 = 4.25


# subarine throws a torpedo, 40% chance sink other boat. If send 2, proba of sinking other boat?
0.4 + 0.6*0.4 = 0.64


#You have are offered a contract on a piece of land which is worth 1,000,000 70% of the time, 500000 20% percent of the time and
#150000 10% of the time. The contract says you can pay x dollars for someone to determine the land's value from where you can decide #whether or not to pay 300000 for the land. What is x? I.e. how much is this contract worth?…

1m 70%
0.5m 20%
0.15m 10%

pay 0.3m for the land dont know the house price. Profit:
0.7*(10-0.3) + 0.2*(0.5-0.3) + 10% * (0.15-0.3) = 515k
  If we pay for the land without knowing how much it's worth, we make $515k on average
  If we know how much the land is worth, we buy it unless it's worth it; 300k, and on average we make
700k * 0.7 + 200k * 0.2 = 530k  
Therefore the knowledge of how much the land is worth is 15k to us (anything more and we're better off gambling)

  Contract worth:   The value of the contract can be determined as a call option, with strike price 300,000, the expected payoff will be just
0.7*700,000 + 0.2*200,000 + 0,1*0= 530,000.


#You start out with 1 dollar and your friend starts out with  2 dollars. You bet 1 dollar until one of you runs out of money. You have a 2/3 chance of winning each bet. What is your chance of winning?
p = (2/3) * (2/3) + (2/3) * (1/3) * p
p = 4/7


#How many ways to sit 6 people around round table?
Do you consider the two seating arrangements above to be different? Because in the first chart, A is in the red chair, but in the second chart F is in the red chair. Yet A is still between F and B and so on.

2 charts: 1 chart ABCDEF other FABCDE, just swithced spots.
If you view the two charts as different then there are 6!, or 720 seating charts. Because there are 6 choices for the red chair, but only 5 choices for blue, 4 choices for purple, and so on down… 6 x 5 x 4 x 3 x 2 x 1 = 6! = 720

However if you view these two charts as the same then, there are only 5!, or 120 arrangements. Because if you lock in the relative positions there are 6 replications of A-B-C-D-E-F so take 6 x 5 x 4 x 3 x 2 x 1 and divide by 6, now you have 5 x 4 x 3 x 2 x 1 = 5! = 120.

#Logical Reasoning Goal: The person to reach 50 first wins . Rules: Play with another person, say a number, and the other person can say any number upto 10 over your number.

Go first, and say 6, 17, 28, 39 and 50.

#What is the fastest amount of time you can get 4 people across a bridge. Each person takes a different amount of time 1 minute, 2, 5, and 10. They can cross 2 at a time but need a flashlight to cross.  

Normal solution:
WHO crosses |  time   |
(1) & (2)   |    2    |
    (1)     |    1    |
(5)&(10)    |    10   |
    (2)     |    2    |
(1) & (2)   |    2    |
17min!

Out of the box solution:
The solution is to have Dave(10) carry the torch and begin to cross with any of the others lets say Adam(1). Each continues at their own pace so in 1 minute Adam has reached the other side and one of the others can begin to cross say Bob(2), when he reaches the other side Clair(5) can begin to cross. Adam, Bob & Clair will be done in 8 minutes and Dave will be done in a further 2.

#70% free throw shooter, if he shoots twice  what are the chances he'll make at least one?
P(X is greater or equal to 1) = P(X=1)+P(X=2) Where X is the number of hits.

P(X is greater or equal to 1) = (0.7)(0.3)+(0.7)(0.7) = 0.7

#The other was the marble question: 8 marbles that all look the same, one is heavier than the rest, using a balance only twice how do #you find the heaviest marble.

Label the marbles as: 1,2,3,4,5,6,7,8. Then split them into three groups:

group A: 1,2,3
group B: 4,5,6
group C: 7,8

Now compare A and B with the balance. Then:

a) If A = B, you know that the lightest marble is either 7 or 8 and by using the balance again you can determine witch of the two is the lightest marble.
b) if A > B do the same steps as in b) but for 4,5,6

This solves the puzzle



#King Arthur, Merlin, Sir Lancelot, Sir Gawain, and Guinevere decide to go to their favorite restaurant to share some mead and grilled meats. They sit down at a round table for five, and as soon as they do, Lancelot notes, "We sat down around the table in age order! What are the odds of that?"

Merlin smiles broadly. "This is easily solved without any magic." He then shared the answer. What did he say the odds were?



Answer
The odds are 11:1. (The probability is 1/12.)

Imagine they sat down in age order, with each person randomly picking a seat. The first person is guaranteed to pick a seat that "works". The second oldest can sit to his right or left, since these five can sit either clockwise or counterclockwise. The probability of picking a seat that works is thus 2/4, or 1/2. The third oldest now has three chairs to choose from, one of which continues the progression in the order determined by the second person, for a probability of 1/3. This leaves two seats for the fourth oldest, or a 1/2 chance. The youngest would thus be guaranteed to sit in the right seat, since there is only one seat left. This gives 1 * 1/2 * 1/3 * 1/2 * 1 = 1/12, or 11:1 odds against.



#We are racing, and can at any time signal to the other that  we would like to double our bet. We've put down 100 to start and during the race I signal to you I want to double the bet, What is the minimum probability of winning for you to accept to continue?
1/3
Lets assume you start with 0 dollars
You know youre going to get 200 dollars with probability p and -100 dollars with probability (1-p).
Therefore, the minimum probability needed to accept and continue would be p such that
200p + (1-p) * (-100) = 0 which would give you an expected payoff of 0 which is what you started with.
So p works out to be 1/3.

#We each have three fair coins, and we flip all of them at once. After we flip them, we look at the outcomes. If we have the same number of heads out of our own coins I pay you $1 and if we have a different number you pay me $2. Do you want to play this game?
The probability of having 3H = 3T = .5*.5*.5 = 1/8
The probability of having 2H 1T = 2T 1H = .5*.5*.5 * 3(ways of getting these combos) = 3/8
So the probability of having the same # of heads on two separate flips of 3 coins is the square of the sum of these probabilities
= (1/8)^2 + (1/8)^2 + (3/8)^2 + (3/8)^2 = 5/16
So expected value = 5/16 * ($1) + 11/16* (-$2) = -$1.06

You'd lose $1.06 on average each time you played this game.
NO dont wanna play the game

#It costs $1 to play a game where you flip a fair coin four times and if you get four straight heads, you win $10. Do you play the game?  
Expected payoff: (1/2)^4 * 9 + (1-(1/2)^4) * (-1) = 9/16 - 15/16 - -6/16 = -3/8

#candy bar A produce 60%, of which 20%damage,B produce  40%, 10% damaged, see a damage bar, probability it come from b
Bayes:
P(B|dam) = P(dam|B) * P(B)/P(dam) = 0.10 * 0.4 / (0.6*0.2+0.4*0.1) = 25%




#I want to have a birthday party outside this weekend (i.e . need sunny weather). On Saturday, the chance of rain is 60 percent, sun 40 percent. On Sunday, rain is 80 percent, sun is 20 percent. From there, the interviewer can ask an array of questions:
#What are the chances I can have my party this weekend? If I have my party, what are the chances my party is on Saturday/Sunday? Etc.

1. P(party)=1-P(no parties)=1-(0.6) * (0.8)=0.52

2. P(Sa | party)= P(Sa &amp; party)/P(party) = 0.4/0.52 = 10/13 (since, sun on Saturday guarantees party on that day, that's how we get the numerator)

3. P(Su | party) = P(Su &amp; party)/P(party) = P(rain Sa and sun on Sun)/P(party)
                            = (0.6)(0.2)/0.52 = .12/.52 = 3/13

OR: just use P(Su | party) + P(Sa | party) =1


#If i toss 3 pieces on a tic-tac-toe board at random, and I  pay you $9 if the pieces create tic-tac-toe, and you pay me $1 if they dont, do you want to play the game? (Expected value problem)
8 ways to create tic tac toe  
number of possibilities: 9C3 = 9!/(3!(9-3)!) = 84

2/21 * 9 - 19/21 = -1/21

If we play a game in which Player 1 picks a number 1-11, and then player 2 can add 1-11 to that (i.e. player 1 picks 5, player 2 can add to make it 6-16), what is the strategy to win this game if Player 1 wants to make 60?  
1 12 24 36 48

#If the chances of you seeing a shooting star outside within  one hour is 84 percent, what is the chance of you seeing at least one shooting star outside in 30 minutes?
The probability that you don't see a star in an hour is 1 - 0.84 = 0.16 = 16%. This means that the probability you don't see a star in 30 min is 0.4 (since 0.4 * 0.4 = 0.16). This makes sense if you think of one hour as two subsequent 30 min intervals. So if the probability you don't see a star in 30 min is 40%, then the probability that you see at least one star in 30 min is 60%.

With Poisson:
Suppose the event meets Poisson distribution. lambda is the rate
P(event happens in one hour) = 1-e^(-lambda) = 0.84
e^(-lambda) = 0.16
P(event happens in .5 hour) = 1-e^(-lambda/2) = 1-sqrt(0.16)=0.6



#Hospital has three boys and an unknown number of girls. A  mother has a baby. A nurse picks up a baby at random and it is a boy. What is the probability that the mother had a boy?

P(F) = .5, probability of giving birth to a female
P(M) =.5, probability of giving birth to a male
P(B) = ?, probability of a nurse choosing a boy
x = number of babies in hospital after mother gave birth

so the question wants you to find P(M|B) = conditional probability of mother giving birth to a male given that the nurse picked up a boy.

so P(M|B) = P(M∩B)/P(B)

If mother gave birth to a boy, then odds of picking a boy is 4/x
If mother gave birth to a girl, odds 3/x
Both these cases have a 50% chance of happening to total probability of picking a boy is: .5(4/x) + .5(3/x) = 3.5/x = P(B)

P(M∩B) = probability that the woman gave birth to a boy AND that the nurse picked it which is .5 * 4/x = 2/x

so P(M|B) = P(M∩B)/P(B) = (2/x)/(3.5/x) = 4/7



#3 people wants to determine their average salary  on the condition that no individual would be able to find out anyone else's salary. How can they accomplish this?
1) X adds a Random Number and his salary and tells the sum to Y.

2) Y also adds a Random Number and his salary to the sum told by X and tells new sum to Z.

3) Z also adds a Random Number and his salary to the sum told by Y and tells new sum to X.

4) X subtracts its random number from the sum told by Z and tells the new number to Y.

5) Y subtracts its random number from the sum told by X and tells the new number to Z.

6) Z subtracts its random number from the sum told by Y and announces the new number.

The new number is now the sum of three salaries and average can be calculated by dividing the sum by 3.

#Person A has 5 fair coins and Person B has 4 fair coins. Person A wins only if he flips more heads than B does. What is the probability of A winning?
Imagine that A and B each toss 4 times. There is a certain probability 𝑝 that A is ahead, and by symmetry the same probability 𝑝 that B is ahead. If A is already ahead, she will win, whatever her 5th toss. If B is already ahead, she will win. And if they are tied, there is probability 1/2 that A will get a head on her 5th toss and win. Thus by symmetry the probability that A wins is 1/2.

Or else we can compute. The probability they are tied after 4 is 1−2𝑝. Thus the probability that A wins is
𝑝+1/2(1−2𝑝)=1/2.
Remark: The same argument applies if B has 𝑛 coins and A has 𝑛+1.


#How can I find the distance between two opposite corners of a cube?
a is the length of a side say a = 10.
Face diagonal: d = sqrt(a^2 + a^2) = sqrt(2(a^2))
Main Diagonal (what we want): sqrt(2(a^2)+a^2) = sqrt(3(a^2)) = sqrt(3(100)) = sqrt(300)



Poisson: P(k events in interval) = [lambda^(k) * e^(-lambda)]/k!
lambda is the mean -> the number expected

- Permutations are for lists (order matters) and combinations are for groups (order doesn't matter).
combination: n choose k: n!/[k!(n-k)!]
permutation: n!/(n-k)!
