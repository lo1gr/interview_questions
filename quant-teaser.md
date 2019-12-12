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

The answer is 22. The angular speed of the minute hand is 360°/hr, whereas the angular speed of the hour hand is (360/12=30)
30°/hr. The hands overlap when the difference in the angles swept by the hands is a multiple of 360°, and the angles swept over an amount of time by the hands are given by the formula angle swept = time * angular speed. In other words, 360°/hr*t – 30°/hr*t = n360°, where t is time in hours and n is some integer.
You can simplify this to 330°/hr*t = n360°, and then n=11t/12hr. There are 24 hours in a day, so n = 22, which is the total number of times the hands overlap. Therefore, the hands do NOT overlap at 1:05 (30° from 12), 2:10 (60° from 12), etc, they overlap at the t’s that correspond to 30° + 30° * 1/11 (slightly after 1:05), 60° + 30° * 2/11 (slightly after 2:10), etc. The last overlap would be at angle of 330° + 30° * 11/11, which = 360°, or a full cycle. Thus, 11 overlaps in 12 hours, 22 overlaps in 24 hours.

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

### You have eight balls all of the same size. 7 of them weigh the same, and one of them weighs slightly more. How can you find the ball that is heavier by using a balance and only two weighings?

The first weighing determines how you conduct the second.

First weighing: Weigh three balls against three other balls on the balance.  Leave two out.

Second weighing, based on results of the first weighing:
IF they balance, THEN you know that all of the balls weighed are "normal".  So weigh one of them against one of the two-unweighed balls.  If those two balance, then you know that the last unweighed ball is the abnormal one.  If they do not balance, then the freshly-weighed ball will be lower on the lower scale and thus the abnormal one.
IF they do NOT balance, THEN you know that whichever side is lower on the balance contains the heavier ball.  So now you have narrowed it down to those three.  Of those three balls, weigh two of them against each other on the balance.  IF they equal, the unweighed third ball is the abnormal one.  If one of the two is lower on the balance, that is the heavier ball.



#throw a die, as many euros as number on die.
#How much would you pay:
(1+2+3+4+5+6)/6 = 7*3/6
pay: 21/6 = 3.5

#now throw a die, if happy take euro, otherwise reroll, can reroll twice:
Since expected payoff is 3.5 if get 4 or more we keep, if get 3 or less reroll:
We choose reroll when our payoff is < expected payoff from next reroll
Thus take 1st roll if it is 4 or better, reroll otherwise. Expected payoff:
1/2 * 5 + 1/2 * 3.5 = 8.5/2 = 4.25

Now we can reroll one more time.
Let's start from the last roll:
Roll1=R1 Roll2 = R2...

E(R1 then the rest) = 1/6 * 6 + 1/6 * 5
E(R2 then R3) = 4.25

payoff is then: 2/6 * 5.5 + 4/6 * 4.25 = 8/3
2/6: 2 out of 6 to get 5 or 6
4/6: 1-2-3-4 out of 6 choices

# There are 4 sealed boxes. There is 100 pounds in one box and the others are empty.
# A player can pay X to open the box and take the contents as many times as they like.
# Assuming this is a fair game, what is the value of X?

E(cost) = X*P(win 1st try) + 2X*P(win 2nd try) + 3X*P(win 3rd try) + 4X*P(win 4th try)
P(win 1st try) = 1/4
P(win 2nd try) = 3/4 * 1/3
P(win 3rd try) = 3/4 * 2/3 * 1/2
P(win 4th try) = 3/4 * 2/3 * 1/2

It is a fair game. Hence:
100 = X(1/4) + 2X(1/4) + 3X(1/4) + 4X(1/4)
100 = (10/4)X <==> 100 = 2.5X
X = 40

X/4 + X/2 + 3X/4 + X = 10X/4

# I pick a number n from 1 to 100. If you guess correctly, I pay you $n and zero otherwise. How much would you pay to play this game?

Suppose we just take 𝑛=3 for simplicity. Suppose the picker chooses 1 with probability 𝑝1, chooses 2 with probability 𝑝2, and 3 with probability 𝑝3. The selection of 𝑝1,𝑝2,𝑝3 constitutes the picker's strategy.

The indifference criterion means that 1𝑝1 = 2𝑝2 = 3𝑝3. However, also 𝑝1 + 𝑝2 + 𝑝3 = 1. To solve, plug in and get
𝑝1 + (1/2)𝑝1 + (1/3)𝑝1 = 1
Hence, 𝑝1 = (1 + 1/2 + 1/3)^(-1). This is also the average amount that the guesser wins, regardless of which number guessed. This is also the expected value of the game.

Our expected payout is then:
(SUM(j=1 to 100) 1/j)^(-1)

# Suppose you have a fair coin. You start with a dollar, and if you toss a H, your position doubles, if you toss T, your position halves. What is the expected value of the money you have if you toss infinitely.

Let's calculate the expectation of 1 toss and then expand it to inifinity:
E(X) = 1/2 * 2 + 1/2 * 1/2 = 5/4

Provided the tosses are independent, the product of the expectationa is the expectation
of the product.
E(PROD (i= 1 to n) Xi) = Prod(i=1 to n) E(Xi) = (5/4)^n which tends to infinity.


# subarine throws a torpedo, 40% chance sink other boat. If send 2, proba of sinking other boat?
0.4 + 0.6*0.4 = 0.64


#You have are offered a contract on a piece of land which is worth 1,000,000 70% of the time, 500000 20% percent of the time and
#150000 10% of the time. The contract says you can pay x dollars for someone to determine the land's value from where you can decide #whether or not to pay 300000 for the land. What is x? I.e. how much is this contract worth?…

1m 70%
0.5m 20%
0.15m 10%

pay 0.3m for the land dont know the house price. Profit:
0.7*(1-0.3) + 0.2*(0.5-0.3) + 10% * (0.15-0.3) = 515k
  If we pay for the land without knowing how much it's worth, we make $515k on average
  If we know how much the land is worth, we buy it unless it's worth it; 300k, and on average we make
700k * 0.7 + 200k * 0.2 = 530k  
Therefore the knowledge of how much the land is worth is 15k to us (anything more and we're better off gambling)

  Contract worth:   The value of the contract can be determined as a call option, with strike price 300,000, the expected payoff will be just
0.7*700,000 + 0.2*200,000 + 0,1*0= 530,000.

#How can I find the distance between two opposite corners of a cube?
a is the length of a side say a = 10.
Face diagonal: d = sqrt(a^2 + a^2) = sqrt(2(a^2))
Main Diagonal (what we want): sqrt(2(a^2)+a^2) = sqrt(3(a^2)) = sqrt(3(100)) = sqrt(300)


#You start out with 1 dollar and your friend starts out with 2 dollars. You bet 1 dollar until one of you runs out of money. You have a 2/3 chance of winning each bet. What is your chance of winning?
p = (2/3) * (2/3) + (2/3) * (1/3) * p
p = 4/7


#How many ways to sit 6 people around round table?
Do you consider the two seating arrangements above to be different? Because in the first chart, A is in the red chair, but in the second chart F is in the red chair. Yet A is still between F and B and so on.

2 charts: 1 chart ABCDEF other FABCDE, just turned clockwise.
If you view the two charts as different then there are 6!, or 720 seating charts. Because there are 6 choices for the red chair, but only 5 choices for blue, 4 choices for purple, and so on down… 6 x 5 x 4 x 3 x 2 x 1 = 6! = 720

However if you view these two charts as the same then, there are only 5!, or 120 arrangements. Because if you lock in the relative positions there are 6 replications of A-B-C-D-E-F so take 6 x 5 x 4 x 3 x 2 x 1 and divide by 6, now you have 5 x 4 x 3 x 2 x 1 = 5! = 120.

#Logical Reasoning Goal: The person to reach 50 first wins . Rules: Play with another person, say a number, and the other person can say any number up to 10 over your number.

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
1 - P(make 0) = 1 - 0.09 = 0.91

#The other was the marble question: 8 marbles that all look the same, one is heavier than the rest, using a balance only twice how do you find the heaviest marble.

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



# We are racing, and can at any time signal to the other that we would like to double our bet. We've put down 100 to start and during the race I signal to you I want to double the bet, What is the minimum probability of winning for you to accept to continue?
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
Expected payoff: (1/2)^4 * 9 + (1-(1/2)^4) * (-1) = 9/16 - 15/16 = -6/16 = -3/8

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

8/84 * 9 - 76/84 = -4/84
= 2/21 * 9 - 19/21 = -1/21

If we play a game in which Player 1 picks a number 1-11, and then player 2 can add 1-11 to that (i.e. player 1 picks 5, player 2 can add to make it 6-16), what is the strategy to win this game if Player 1 wants to make 60?  
Make Player2 start, then player 1 wants: 12 24 36 48

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



#3 people want to determine their average salary  on the condition that no individual would be able to find out anyone else's salary. How can they accomplish this?
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



#You choose one of two identical looking bags at random. One bag has three black marbles and one white marble. The other has three white marbles and one black marble. After choosing a bag you draw one marble out at random. You notice it is black. You then put it back and draw another marble out of the same bag at random. What is the probability that the second marble drawn is black?
Bag1: 3B1W
Bag2: 3W1B

P(2nd black & first black)/P(1st black)
P(1st black) = 1/2 (3/4) + 1/2 (1/4) = 1/2


P(2nd black & first black):
if B1: 3/4
if B2: 1/4
P(B1) = 3/4
P(B2) = 1/4

Answer: 3/4 * 3/4 + 1/4 * 1/4


In this case A is drawing a black marble and B is having already drawn a black marble.
This can be expressed as Pr(A|B)=Pr(A and B)/Pr(B).

Pr(A and B) = (1/2) * [(3/4)^2 + (1/4)^2] = 5/16.

Pr(B) = 1/2.

Pr(A|B) = Pr(A and B)/Pr(B) = (5/16)/(1/2) = 10/16 = 5/8.


#In how many different ways can you rearrange the letters in the word "CHICAGO"?

Answer
At first glance, the response may seem to be simply 7!, or 5040. However, duplicates of the letter "C" poses a problem in the response. Any combination of letters, such as "ICCHOGA" can be created with C#1 coming first followed by C#2 or with C#2 preceding C#1. Any distinct possibility comes in pairs such as this. Therefore, to get rid of all duplicates, we divide 5040 (7!) in half to arrive at 2520, the answer to this problem.



Poisson: P(k events in interval) = [lambda^(k) * e^(-lambda)]/k!
lambda is the mean -> the number expected

- Permutations are for lists (order matters) and combinations are for groups (order doesn't matter).
combination: n choose k: n!/[k!(n-k)!]
permutation: n!/(n-k)!




Whacky:
#Question: Five pirates discover a chest containing 100 gold coins. They decide to sit down and devise a distribution strategy. The pirates are ranked based on their experience (Pirate 1 to Pirate 5, where Pirate 5 is the most experienced). The most experienced pirate gets to propose a plan and then all the pirates vote on it. If at least half of the pirates agree on the plan, the gold is split according to the proposal. If not, the most experienced pirate is thrown off the ship and this process continues with the remaining pirates until a proposal is accepted. The first priority of the pirates is to stay alive and second to maximize the gold they get. Pirate 5 devises a plan which he knows will be accepted for sure and will maximize his gold. What is his plan?

To understand the answer, we need to reduce this problem to only 2 pirates. So what happens if there are only 2 pirates. Pirate 2 can easily propose that he gets all the 100 gold coins. Since he constitutes 50% of the pirates, the proposal has to be accepted leaving Pirate 1 with nothing.

Now let’s look at 3 pirates situation, Pirate 3 knows that if his proposal does not get accepted, then pirate 2 will get all the gold and pirate 1 will get nothing. So he decides to bribe pirate 1 with one gold coin. Pirate 1 knows that one gold coin is better than nothing so he has to back pirate 3. Pirate 3 proposes {pirate 1, pirate 2, pirate 3} {1, 0, 99}. Since pirate 1 and 3 will vote for it, it will be accepted.

If there are 4 pirates, pirate 4 needs to get one more pirate to vote for his proposal. Pirate 4 realizes that if he dies, pirate 2 will get nothing (according to the proposal with 3 pirates) so he can easily bribe pirate 2 with one gold coin to get his vote. So the distribution will be {0, 1, 0, 99}.

Smart right? Now can you figure out the distribution with 5 pirates? Let’s see. Pirate 5 needs 2 votes and he knows that if he dies, pirate 1 and 3 will get nothing. He can easily bribe pirates 1 and 3 with one gold coin each to get their vote. In the end, he proposes {1, 0, 1, 0, 98}. This proposal will get accepted and provide the maximum amount of gold to pirate 5.


#You are in a canoe in a swimming pool, and you have a penny in your
pocket. You toss the penny into the water. What happens to the water level in
the swimming pool?

When the rock is in the boat, the weight of both the rock and boat is pressuring the water which causes the water level to rise. When the rock is at the bottom of the water, it displaces its volume in the water rather than the weight. Due to the fact that the rock’s density is greater than that of water and volume, the water level will fall.

# There are one hundred coins on the table. You and an opponent take turns
# removing 1, 2, 3, or 4 coins at a time. You win if there are no coins left at the
# end of your turn. You may choose whether to go first or second. What do you
# do and why?
backward induction: remove 5 at every iteration:
I want to get:
95 90 85 80... 5 0
So i start second.





IMC:

# How long to swim from Amsterdam to NY?
6,000 km
swimmer: 1 km in 30min
2km h

6,000/2 = 3,000 swim hours
8h of swim per day:

3,000 / 8 = 375 days


# You have a 4x4 grid, and three balls. If you manage to get "at least" 2 balls in the same row/column, you win. What is the probability to win ?
if assume that 2 or 3 balls can be on the same square:
proba win = 1 - proba lose  
if 1st ball is placed, second ball is a "lose" in 9/16 cases
if 1st ball placed and second ball placed, and it is a lose, then the last ball is a lose in
4/16 cases (count them)

1 - (9/16 * 4/16) = 55/64
if no ball can be on the same square:
1 - (9/15 * 4/14) = 1 - 18/105 = 87/105 = 29/35   (multiples of 3)


|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

#If a family has two children, and we know that one is a girl, what is the probability that the family has two girls?
gg
bb
gb
bg

1/3

#What is the chance you throw an increasing sequence when you throw a dice three times?
By implication, the numbers are all different.
There are 20 ways to choose three different numbers from six:
combination: 6C3 = 6!/(3! * (6-3)!) = 20, and once they are chosen there is only one valid order, i.e. there are 20 allowable ordered choices.
There are 6^3 = 216 possibilities for the results of throwing dice.

So the probability is 20/216=5/54.

#In how many ways can 5 identical balls be placed in a (3x3) grid such that each row contains at least one ball?
1) Total ways of selecting 5 places out of 9 = 9C5 = 9!/(5!4!) = 126

2) ways in which the 5 places are in just two rows..
Selecting 2 rows out of 3=3C2=3.
These two rows have 6 cells, so choosing 5 out of 6 cells=6C5=6.
So total ways in which the balls are NOT in all three= 3*6=18.

Ways in which the balls are in all three cells=126-18=108


#Tom has six pairs of black gloves and six pairs of brown gloves in her drawer. In complete darkness, how many gloves must she take from the drawer in order to be sure to get a pair that match?
He could possibly take out 6 black left hand gloves and then 6 brown left hand gloves, the next one would have to be either the black right hand or brown right hand match.


# in a room of n people, how many handshakes possible? Cannot handshake own hand. eg n =25
answer = n(n-1)/2
First person can shake hands w n-1 people, second n-2...
(n-1) + (n-2) + ... + 2 + 1

for n = 25:
24 + 23 + ... + 2 + 1 = 24 * (1+24)/2 = 300


#A group of about twenty friends decide to exchange gifts as secret Santas. Each person writes their name on a piece of paper and puts it in a hat and then each person randomly draws a name from the hat to determine who has them as their secret Santa.
#What is the probability that at least one person draws their own name?
step1 : Total number of draws
First, let us count the number of possible draws for a group of size n. The first person can select any of the n names. The second person can select any of the remaining n – 1 names the first person did not pick. The third person is left with n – 2 names, and the pattern continues.
n * (n-1) * ... * 2 * 1
= n!

step2: Total number unsuccessful draws:
@ least 1 person gets own name: C(n,1) ways, remaining have (n-1)! possibilities => C(n,1) * (n-1)!
@ least 2 people get own names: C(n,2) ways, remaining have (n-2)! possibilities => C(n,2) * (n-2)!
@ least k people get own names: C(n,k)(n-k)! = n!/k! possiblities

avoid double counting: inclusion exclusion technique
Unsuccessful draws = “at least 1” – “at least 2” + “at least 3” + … + (-1)n+1(“at least n“)

Since “at least k” is equal to n!/k!, we have:

Unsuccessful draws possibilites = n!/1! – n!/2! + … + (-1)^(n+1)n!/n!
Factor n! to get: n!(1/1! - 1/2! + ... + (-1)^(n+1)/n!)

Step3: probability successful draw
probability unsuccessful draw: n!(1/1! - 1/2! + ... + (-1)^(n+1)/n!)/n! = (1/1! - 1/2! + ... + (-1)^(n+1)/n!)

Pr(Successful) = 1/2! + … + (-1)n/n!
Recalling e^x = 1 + x + x^2/2 + ...
if substitute x = -1 then get:
e^(-1) = 1/2! – 1/3! + 1/4! + … +
= 1/e = 37%


# You have 100 quarters in a jar. One of the quarters is double sided (heads). You pick out a random quarter and flip it 7 times, and get all heads. What is the probability you picked the double sided quarter? Then, given that you flipped it 7 times with all heads, what is the probability that you'll get heads on the 8th flip?
Bayesian probabilities:
P( you picked double sided | you flipped 7 heads in a row) = P (7 heads in a row | double sided) P (double sided) / P(7 heads in a row)

P(7 heads in a row | double sided) = 1
P(double sided) = 1/100
P(7 heads in a row) = (99/100) * (1/2)^7 + (1/100)

Hence P (double sided) = 1/ (99/128 + 1) = 128/227

Thus, the chance that the next flip will be heads is P(double sided) + P(one sided) * P(make head)
= (128/227 + (227-128)/227 * 0.5)

# Hundred tigers and one sheep are put on a magic island that only has grass. Tigers can live on grass, but they want to eat sheep. If a Tiger bites the Sheep then it will become a sheep itself. If 2 tigers attack a sheep, only the first tiger to bite converts into a sheep. Tigers don’t mind being a sheep, but they have a risk of getting eaten by another tiger. All tigers are intelligent and want to survive. Will the sheep survive?
If there is 1 tiger, then it will eat the sheep because he does not need to worry about being eaten. Sheep will not survive.
If there are 2 tigers, both of them knows that if one eats the Sheep, the other tiger will eat him. So, the sheep will survive.

If there are 3 tigers, then they each of them knows that if one tiger eats up the sheep, then Iceland will be left with 1 sheep and 2 tigers and as shown in the previous case, the sheep will survive. Hence each tiger will try to eat up the sheep. The sheep will not survive.

If there are 4 tigers, then the sheep will survive.

And so on….

So, If there are even number of tigers the sheep will survive, else it will die. Hence, if there are 100 tigers the sheep will survive.

# There are 100 ropes in a bag. In each step, two rope ends are picked at random, tied together and put back into a bag. The process is repeated until there are no free ends.
# What is the expected number of loops at the end of the process?

Of the (2𝑛C2) ways of choosing two ends, 𝑛 of them result in the first case, so the first case has probability 𝑛/(2𝑛(2𝑛−1)/2)=1/(2𝑛−1). So the expected number of loops you add in the first step, when you start with 𝑛 ropes, is:

First pick: probability pick the same rope is 1/(how many ends left) = 1/(2n-1)
probability pick other rope is 1 - 1/(2n-1)
(1/(2𝑛−1)) * 1 + (1−1/(2𝑛−1))* 0 = 1/(2𝑛−1)

second pick: ?
You remove 1 rope: either it is 'out of the market', or 2 ropes tied together
n = n-1

1/(2(n-1)-1) = 1/2n-3
...

After this, you start over with 𝑛−1 ropes. Since what happens in the first step and later are independent (and expectation is linear anyway), the expected number of loops is
1/(2𝑛−1)+1/(2𝑛−3)+⋯+1/3+1 =

n = 100 so:
1 + 1/3 + 1/5 + 1/7 + ... + 1/(200-1)

Hn = 1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6 + 1/7 + ... + 1/n
Hn/2 = 1/2 + 1/4 + 1/6 + ... + 1/2n

H(2n) = 1 + 1/2 + ... + 1/2n = 1 + 1/2 + ... + 1/200
H(2n) = ln(200) + 0.57721567
= 5.8755

H(n)/2 = [ln(100) + 0.57721567]/2
= 2.5912

H(2n) - H(n)/2 = 3.28



More or less closed form of harmonic series:
Hn = ln(n) + y
= ln(n) + 0.57721567

Hn/2 = 2.5937




# Trading in Amsterdam:

# You’re driving and there is two traffic lights, each green for 100 secs and then red for 100 secs. You have a magic wand which turns red lights green, you can only use it once. With this wand, what is your expected waiting time ?

waiting time in all these cases is 0: RG GG GR
waiting time not 0: RR
(1/2) * (1/2) * 50 = 12.5secs

# There is a timer which tells you, when the light is red, when it turns green. What is the optimal strategy now?
Expected waiting time if no wand and only one light:
P(Red) * Expected waiting time if red
= (1/2) * 50 = 25
Hence, if the waiting time at the first light > 25, we should use the wand bc wait now > expected wait next light.
Otherwise, if the waiting time at the first light < 25, we should just wait and keep the wand bc wait now < expected wait next light.

Expected waiting time now couple of new cases:
R(>25)G: 1/2 * 3/4 * 1/2: p(red) * p(wait bw 25&100) * p(green) : 0
R(<25)G | R(<25)R :1/2 * 1/4 * (25/2) = p(red) * p(wait bw 0 and 25) * expected wait time -> keep the wand so next light doesnt matter
R(>25)R: 1/2 * 3/4 * 1/2 * 50 = p(red) * p(wait bw 25 & 100) * p(red after) * expected wait time if red and no wand

Hence expected wait time now is:
1/2 * 1/4 * (25/2) + 1/2 * 3/4 * 1/2 * 50 = 25/16 + (3/16)* 50 = 12.5/8 + 75/8 = 10.93


28 trinquements dans une salle: combien de  personnes ?
n(n-1)/2 = 28
n^2-n = 56
n = 8

# Expected coin flips in order to get 2 heads in a row:
X being the event 2 heads in a row:
E(X) = 1/2(1+E(X|H)) + 1/2*(1+E(X))
E(X|H) = 1/2*(1) + 1/2*(1+E(X)) = proba head * 1 flip + proba tail * 1 flip * #flips back original state

Plugging back in:
E(X) = 1/2(1+1/2*(1) + 1/2*(1+E(X))) + 1/2*(1+E(X))
E(X) = 6

or:
outcomes: T, HT, HH
x being the number of flips:
x = 1/2 (x+1) + 1/4(x+2) + 1/4(2)
x = 6

# Expected coin flips in order to get 3 heads in a row:
Consider the outomes 𝑇,𝐻𝑇,𝐻𝐻𝑇,𝐻𝐻𝐻. All but the last put you back to the start. So if 𝑥 is the expected number of tosses to get HHH we have:
x = 1/2(x+1) + 1/4(x+2) + 1/8(x+3) + 1/8(3)
x = 14


# You cover the two squares diagonally opposite on a  chessboard, Using domino tiles, that are 2x1 squares, can you cover the remaining squares on the board?
No you cannot. The easy way is to note that the two squares diagonally opposite have the same colour, and every tile covers one white and one black square.
Each domino we set on the chessboard will always take 1 Black and 1 White square.Therefore, 31 dominos will take 31 white square and 31 black squares exactly. On this chessbord however, we must have 32 black and 30 white squares. Hence it is not possible to do so.



# How many seconds in a year:
24*365*60*60 = 31.536m
#minutes in year:
24*365*60 = 525.6k
#hours in year
24*365 = 8760

I highly recommend all of the puzzles at GeekforGeeks:
https://www.geeksforgeeks.org/puzzle-1-how-to-measure-45-minutes-using-two-identical-wires/

# How do we measure forty-five minutes using two identical wires, each of which takes an hour to burn. We have matchsticks with us.
0 minutes – Light stick 1 on both sides and stick 2 on one side.
30 minutes – Stick 1 will be burnt out. Light the other end of stick 2.
45 minutes – Stick 2 will be burnt out.

#Two trains are on same track and they are coming toward each other. The speed of first train is 50 KMs/h and the speed of second train is 70 KMs/h. A bee starts flying between the trains when the distance between two trains is 100 KMs. The bee first flies from first train to second train. Once it reaches the second train, it immediately flies back to the first train … and so on until trains collide. Calculate the total distance travelled by the bee. Speed of bee is 80 KMs/h.

Let the first train moves at u km/h
second train moves at v km/h
distance between trains be d km
speed of bee is b km/h
time taken by trains to collide = d/(u+v)
distance travelled by bee = b*d/(u+v) = 80 * 100/(50+70) = 66.67(approx.)

# In a Medical Laboratory, you have 240 Injections, one of which is for Anesthesia for a rat. After injecting, one rat fainted exactly in 24 hours. You have 5 rats whom you are willing to sacrifice in order to determine which injections contains the Anesthesia. How do you achieve this in 48 hours ?
Let us number the Injections with 5 digit numbers consisting of 0, 1 and 2. Let us number the Rats as 1, 10, 100, 1000, 10000.

Number 0 on a Injections represents the Anesthesia will not be inject to rat.
Number 1 on a Injections represents the Anesthesia will be injected to rat on 1st day.
Number 2 on a Injections represents the Anesthesia will be injected to rat on 2nd day (after 24 hours).



The action corresponding to the digit in the unit place will be executed by rat numbered 1.
The action corresponding to the digit in the tenth place will be executed by rat numbered 10.
The action corresponding to the digit in the 100th place will be executed by rat numbered 100.
The action corresponding to the digit in the 1000th place will be executed by rat numbered 1000.
The action corresponding to the digit in the 10000th place will be executed by rat numbered 10000.

Example: Let us say the Injection is numbered 11201. The Injections is injected on the first day to rat numbered 10000, 1000 and 1. It is injected on the second day to rat numbered 100. And it is not injected to rat numbered 10.

So if the rat numbered 10000, 1000 and 1 faints within first 24 hours, rat numbered 100 faints in the next 24 hours and the rat numbered 10 does not faint, then the Anesthesia Injection has to be 11201.

This way total number possible is,

= 3 * 3 * 3 * 3 * 3 = 3^5 = 243 Injections
So with the help of 5 rats and within 48 hours we will be able to find a Anesthesia Injection among 243 Injections.


# You have 5 jars of pills. Each pill weighs 10 grams, except for contaminated pills contained in one jar, where each pill weighs 9 grams. Given a scale, how could you tell which jar had the contaminated pills in just one measurement?
Take out 1 pill from jar 1, 2 pills from jar 2, 3 pills from jar 3, 4 pills from jar 4 and 5 pills from jar 5. Put all these 15 pills on scale. The correct weight is 150 (15*10). But one of the jars has contaminated pills. So the weight will definitely be less than 150. If the weight is 149 then jar 1 has contaminated pills because there is only one contaminated pill. If the weight is 148 then jar 2, if the weight is 147 then jar 3, if 146 then jar 4, if 145 then jar 5.

# Consider a two-player coin game where each Player A and Player B gets the turn one by one. There is a row of even number of coins, and a player on his/her turn can pick a coin from any of the two corners of the row. The player that collects coins with more value wins the game. Develop a strategy for the player making the first turn i.e, Player A, such that he/she never loses the game. Note that the strategy to pick a maximum of two corners may not work. In the following example, the first player, Player A loses the game when he/she uses a strategy to pick a maximum of two corners.
Suppose you are given the following rows of coins:

18 20 15 30 10 14
Coins at even places: 20, 30, 14
Coins at odd places: 18, 15, 10
These places are fixed independent of whether the choice of selection must begin from the left or the right-hand side.

Step 1: Sum of all even placed coins = 20 + 30 + 14 = 64
Step 2: Sum of all odd placed coins = 18 + 15 + 10 = 43
Step 3: Comparing the even and the odd placed coins where EVEN > ODD

Therefore, Player A must start selecting from the right-hand side and choose all the even-placed coins every time(here they are 14, 30 and 20). So first picker, Player A picks 14. Now, irrespective of whether the second Player B starts selecting from the left-hand side i.e., 18 or from the right-hand side i.e., 20, the even placed coins i.e., 14, 30 and 20 are booked for the Player A. Therefore, be any situation arise, the first picker Player A will always win the game.


# There are 100 doors in a row, all doors are initially closed. A person walks through all doors multiple times and toggle (if open then close, if close then open) them in following way:
In first walk, the person toggles every door
In second walk, the person toggles every second door, i.e., 2nd, 4th, 6th, 8th, …
In third walk, the person toggles every third door, i.e. 3rd, 6th, 9th, …
………
……….
In 100th walk, the person toggles 100th door.

A door is toggled in ith walk if i divides door number. For example the door number 45 is toggled in 1st, 3rd, 5th, 9th, 15th and 45th walk.
The door is switched back to initial stage for every pair of divisors. For example 45 is toggled 6 times for 3 pairs (5, 9), (15, 3) and (1, 45).
It looks like all doors would become closes at the end. But there are door numbers which would become open, for example 16, the pair (4, 4) means only one walk. Similarly all other perfect squares like 4, 9, ….

So the answer is 1, 4, 9, 16, 25, 36, 49, 64, 81 and 100.


#In a country, all families want a boy. They keep having babies till a boy is born. What is the expected ratio of boys and girls in the country?
X being the number of kids expected:

X = 1 * proba get a boy + proba get a girl (1 + back to beginning: X)
X = 1/2 * 1 + 1/2 * (1+X)
X = 2
Meaning the proportion would be 1:1

# There are 1000 wine bottles. One of the bottles contains poisoned wine. A rat dies after one hour of drinking the poisoned wine. How many minimum rats are needed to figure out which bottle contains poison in hour.
We need to figure out in hour. We need 10 rats to figure out the poisoned bottle. The result is based on binary number system. We get 10 using ⌈ Log21000 ⌉.
The idea is to number bottles from 1 to 1000 and write their corresponding binary numbers on the bottle. Each rat is assigned a position in the binary numbers written on bottles. Let us take an example. Rat 1 represents first bit in every bottle, rat 2 represents second bit and so on. If rat numbers 5, 7 and 9 die, then bottle number 42 (Binary 0000101010) is poisoned.

# There are 3 ants sitting on three corners of a triangle. All ants randomly pick a direction and start moving along edge of the triangle. What is the probability that any two ants collide?
2 choices for each: 2^3 = 8 combos total. only 2 combinations lead to no collisions (all go clockwise or all counterclockwise)
P(any 2 ants collide) = 1 - 2/8 = 3/4


# You have 15 Rs with you. You go to a shop and shopkeeper tells you price as 1 Rs per chocolate. He also tells you that you can get a chocolate in return of 3 wrappers. How many maximum chocolates you can eat?
Buy and eat 15 chocolates
Return 15 wrappers and get 5 more chocolates.
Return 3 wrappers, get 1 chocolate and eat it (keep 2 wrappers)
Now we have 3 wrappers. Return 3 and get 1 more chocolate.
So total chocolates = 15 + 5 + 1 + 1

# How can you represent days of month using two 6 sided dice? You can write one number on each face of the dice from 0 to 9 and you have to represent days from 1 to 31, for example for 1, one dice should show 0 and another should show 1, similarly for 29 one dice should show 2 and another should show 9.
Dice 1: 0 1 2 3 5 7
Dice 2: 0 1 2 4 6 8
Trick is that 9 could be made from the 6: can read from top of bottom hehe

# You are blindfolded and 10 coins are place in front of you on table. You are allowed to touch the coins, but can’t tell which way up they are by feel. You are told that there are 5 coins head up, and 5 coins tails up but not which ones are which.
# Can you make two piles of coins each with the same number of heads up? You can flip the coins any number of times.
Make 2 piles with equal number of coins. Now, flip all the coins in one of the pile.

# Three Employees want to know the average of their salaries. They are not allowed to share their individual salaries.
1) X adds a Random Number and his salary and tells the sum to Y.
2) Y also adds a Random Number and his salary to the sum told by X and tells new sum to Z.
3) Z also adds a Random Number and his salary to the sum told by Y and tells new sum to X.
4) X subtracts its random number from the sum told by Z and tells the new number to Y.
5) Y subtracts its random number from the sum told by X and tells the new number to Z.
6) Z subtracts its random number from the sum told by Y and announces the new number.
The new number is now the sum of three salaries and average can be calculated by dividing the sum by 3.
Finally, nobody knows the salary of others, but all know average.
This can be extended to more than 3 employees also.

# Given two hourglass of 4 minutes and 7 minutes, the task is to measure 9 minutes.
At 0 minutes: Start both hourglasses at the same time.
At 4 minutes: 4 minutes hourglass runs out and flip it. 7 minutes hourglass is left with 3 minutes.
At 7 minutes: 4 minutes hourglass is left with 1 minute. 7 minutes hourglass runs out and flip it.
At 8 minutes: 4 minutes hourglass runs out and 7 is filled with 6 minutes and 1 minute on the other side. Flip it as the sand is left with 1 minute.
At 9 minutes: 7 minutes hourglass becomes empty from above side.

# A newspaper made of 16 large sheets of paper folded in half. The newspaper has 64 pages altogether. The first sheet contains pages 1, 2, 63, 64. If we pick up a sheet containing page number 45. What are the other pages that this sheet contains?
On the back of 45, it is 46. The pages are such that for each page p, 65-p will be also on the same page.
Then,
65-45 = 20
65-46 = 19
So the four pages in this sheet are 19, 20, 45, 46.

# A car has 4 tyres and 1 spare tyre. Each tyre can travel a maximum distance of 20000 miles before wearing off. What is the maximum distance the car can travel before you are forced to buy a new tyre? You are allowed to change tyres (using the spare tyre) unlimited number of times.
25000
Divide the lifetime of spare tire into 4 equal part i.e., 5000 and swap it at each completion of 5000 miles distance.
20k + 20k/4 = 25k

# In year 2001 on October 2, 2001, the date in MMDDYYYY format was a palindrome (same forwards as backwards), 10/02/2001 -> “10022001”
# When was the last palindrome date before 10/02/2001?
One year can have only one palindrome as the year fixes the month and date too, so the year has to be less than 2001 since we already have the palindrome for 10/02. It can’t be any year in 1900 because that would result in a day of 91, same for 1800 down to 1400. it could be a year in 1300 because that would be the 31st day.
So what’s the latest year in 1300 that would make a month?

When you first look at it, 12th month comes to mind as we have to find the latest date, so it seems it would be 1321. But we have to keep in mind that we want the maximum year in 1300 century with a valid date, so lets think about 1390 that will give the date as 09/31, is this a valid date…? No, because September has only 30 days, so last will be the 31st August. Which means the correct date would be 08/31/1380.

# You have got someone working for you for five days and a gold bar to pay him. You must give them a piece of gold at the end of every day. What are the fewest number of cuts to the bar of gold that will allow you to pay him 1/5th each day?
2 cuts:
After two cut there are three pieces of 1 unit and two 2 unit.
On 1st day: Give him 1 unit.
On 2nd day: Give him 2 unit and take back 1 unit.
On 3rd day: Give him 1 unit (he already have 2 unit)
On 4th day: Give him 2 unit and take back 1 unit.(he already have 2 unit)
On 5th day: Give him 1 unit.(he already have  two 2 unit)


# A man is allocated a task. He doubles the task done everyday. If the man completely does the task in 18 days, how many days did it take for the man to complete 25% of the task?
100% of task = 18 days
As he doubles the task everyday. So,
50% of task = 17 days
25% of task = 16 days.

# A Lady (L) bought an item of Rs 100 from the Shopkeeper (C). She paid him through a 500 Rs Note. Realizing that he did not have change, the shopkeeper C got change for that note from another shopkeeper (S) and paid Rs 400 to the Lady.
# After a few days, S realized that the note is fake, And this railed at C and took 500 Rs back from him.
# So in this whole process how much money did C loose in the end?
The total loss for shopkeeper = 500 ( given back to the person who had provided the change )

Consider a transaction box, the lady came with a counterfeit 500 Rs note which can be considered of 0 value.
Now the lady took the item (cost of the item 100 Rs ) and 400 Rs (the change given by shopkeeper(C) to the lady)
from the transaction box, total of 500 Rs. Now the equivalent amount should be lost by someone, thus shopkeeper(C) lost 500 Rs. Another shopkeeper(S) gave 500 Rs and took back the same amount hence no loss for him.

# Policeman decided to punish the Prisoner and asked him to make a statement. The Prisoner should make such a statement so that he would be alive.
# If the statement is held true by Policeman, the Prisoner will be hanged to death and if the statement is held false, the Prisoner will be shot dead.
The Prisoner said, ‘I will be shot dead’
If Policeman says the statement is true, the Prisoner will be hanged to death which will make his statement false.
If Policeman says the statement is false, the Prisoner will be shot dead which will make the statement true.

# egg problem
The next approach can reduce our worse case scenario by balancing the linear drops and our 10 floor drop increment. If getting to the higher floors means more drops overall, we need to decrease the drops we need to perform linearly. We’re essentially trying to make all possible scenarios take the same number of drops to solve.
If we drop our first egg from floor x (10 in our 10 floor strategy), the linear portion of our strategy is x-1 (9 in the above strategy). Our drop count is:
x + (x - 1)
If the egg doesn’t break on the first drop our drop count increases by one, so we’ll need to remove a drop from our floor by floor drop count — the next drop should be from x-1 floors up. Every additional floor jump will need to have one less floor, so that when we get to the linear portion of the solution we’ll have one less floor to check. We continue removing one floor until we only have 1 floor to check:
x + (x-1) + (x-2) + (x-3) + ... + 1
Which simplifies to:
x(x + 1)/2
Because there are 100 floors in our problem, we solve for x when the entire summation is equal to 100:
x(x + 1)/2 = 100
And some math...
x = 13.651
This means we want to start dropping from floor 14, jump up 13 floors to drop from floor 27, jump up 12 floors to drop from floor 39, and so on. Our worst case scenario is then a drop count total of 14.


# Question : 100 coins are lying flat on a table. 10 of them are heads up and 90 are tails up.You can’t see which one is which.How can we split the coins into two piles such that there are same number of heads up in each pile?

Answer : Make 2 piles with 10 coins and 90 coins each. Now, flip all the coins in the smaller pile.

# We are given an excel sheet which contains integers from 1 to 50, including both. However, the numbers are in a jumbled form and there is 1 integer missing. You have to write a code to identify the missing integer. Only the logic is required.
We know that the sum of all the numbers from 1 to n is (n*(n+1)/2)
Therefore, sum of all the numbers from 1 to 50 is:
50*(50+1)/2  (Here, n = 50)
  = 50*(51)/2
  = 25*51
  = 1275.
Therefore, all we need to do is to sum all the integers present in the file and subtract the sum from 1275. The difference between 1275 and this sum would give us the missing integer.

# There are 20 people standing in a line, one behind the other. Each is made to wear a hat, which can either be white or black. There can be any number of white or black hats between 0 and 20. Each person can see the hat of all the persons ahead of him in the line, but not those of the people standing behind. Each person is required to guess (loudly) the color of his/her own hat. The objective is for the group to get as many correct guesses as possible. The group is allowed to discuss and form a strategy before the exercise. What is the best strategy? What is the maximum number of correct guesses in this strategy?
The person who stands last in the queue, behind everyone else, will count the number of white hats on the heads of the 19 people present ahead of him. If this number is even, he (loudly) guesses the hat on his head as ‘Black’. if the number is odd, he guesses ‘White’. The probability of the hat on his head being what he guessed is 50%. There is no way this person can guess the hat on his head correctly. However, his guess functions as a message to others in front of him.
Suppose the 20th person guesses ‘Black’. Now, the person who is 19th in the queue knows that the number of white hats on the first 19 people (the 18 people in front of him and himself) is even. He then checks whether the number of white hats in front of him is even or odd. If the number is even, that means the hat on his head is black. If the number is odd, that means the hat on his head is white and calls that out (loudly). Therefore, the 19th person in the queue always guesses correctly, based on the message the 20th person passed on.
A similar strategy is followed by each person in turn. Therefore, everyone except the last (20th) person guesses correctly for sure. The answer to this puzzle, therefore, is 19.


# Place the numbers 1, 2, 3, 4, 5, 6, 7, 8 into the eight circles in figure given below, in such a way that no number is adjacent to a number that is next to it in the sequence.For example 1 should not be adjacent to 2 but can be adjacent to 3, 4, 5, 6, 7, 8. Similarly for others.
middle line: 7 1 8 2



Books:
-Hull’s classic Options, Futures & Other Derivatives: https://math.dartmouth.edu/~m86f17/Downloads/Hull8thedition.pdf
Options like futures provide a form of leverage. For a given investment, the use of
options magnifies the financial consequences. Good outcomes become very good, while
bad outcomes result in the whole initial investment being lost.

CAPM: expected return asset = Rf + Beta(Rm-Rf)
if rate is compounded m times per annum, terminal value of the investment is A(1 + R/m)^(mn)
if continuous compounding: Ae^(Rn)


Natenberg’s classic Option Volatility & Pricing: http://1.droppdf.com/files/23rd5/option-volatility-and-pricing-advanced-tr-sheldon-natenberg.pdf

Nassim Taleb Black Swan:
My idea is that not only are some scientific results useless in real life, because they underestimate the impact of the highly improbable (or lead us to ignore it), but that many of them may be actually creating Black Swans.
==> efficient market hypothesis ironically increases the number and magnitude of black swans
History makes jumps ==> there are weeks in which decades happen

=> intuitively we underweight unlikely events.
=> if you are making black swan bets then you actually want less data bc the data will drive you to quit.

Show two groups of people a blurry image of a fire hydrant, blurry enough for them not to recognize what it is. For one group, increase the resolution slowly, in ten steps. For the second, do it faster, in five steps. Stop at a point where both groups have been presented an identical image and ask each of them to identify what they see. The members of the group that saw fewer intermediate steps are likely to recognize the hydrant much faster. Moral? The more information you give someone, the more hypotheses they will formulate along the way, and the worse off they will be. They see more random noise and mistake it for information.

=> benefit to having multiple things going on is less time to pay attention to noise


Nassim Taleb Fooled By Randomness:
“Mild success can be explainable by skills and labor. Wild success is attributable to variance.”
“Remember that nobody accepts randomness in his own success, only his failure.”
Skewness and expectations: you can't just look at the odds of something happening, but also the payoff you receive if it works (and the cost of it failing). A bet on something very unlikely can be smart if the payoff is large and you have rules to limit the many small losses that are likely.
Minor stalemates in life can often be solved by choosing randomly. In many cases it doesn't really matter so long as you choose something and move forward.


High frequency trading (HFT) is a technology-driven trading method that provides liquidity and saves investors money by utilizing advanced algorithms to analyze multiple markets and execute orders based on market conditions to transact many orders at fractions of a second at the most efficient price    

What is an automated market maker?
- Solves the buyer/seller matching problem. The automated market maker guarantees that the market is always available to trade, even at 2 in the morning in your local time zone, even at the market’s initiation, and even if no other traders are currently active. By giving traders confidence that they can obtain liquidity for their wagers whenever they choose, automated market makers create additional incentives to participate.
- Enables large markets with many events.
- Concisely expresses the market’s current state.
- Allows for precise control of worst-case loss by market sponsors.
- Automated Market Makers prevent common trader errors and information redundancy.
