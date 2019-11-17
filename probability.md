# Probability

You might encounter probability questions in two different ways during your interview process: They might ask you some probability-based brain teasers during the technical in-person interview to see how approach this kind of problem, or you might need to answer probability question in the qunatitative aptidude test.

Here is a reminder of some mathematical formulas and concepts that you should have in mind to tackle these questions:

...
nCr
independnce
conditional probability
Bayes
disjoint probability
total probability
P(A annd B)
expectation formula
...


The following questions are a mix of 3 types of questions:
- practical probability problems
- theoretical probability problems (mainly focusing on distributios)
- brain teasers that might involve some probabilities in the solution

## Easy questions

#### Tom has a 40% chance of winning a hand at blackjack. If he wins a hand, he gets double the amount of money he bet. If he looses a hand, he will loose the money at that he bet. He has 200€ and bets 50€ a hand. What is the probability that he will still have money at the end of the forths hand?
We need to reformulate the question: to still have moneey after 4 hands, he needs to win at least one hand (otherwise he will be out of money).
P("win at least 1 hand") = 1- P("win no hands") = 1 - (1-0,4)^4 = 1 - 0.6^4 = 87.04%

Final answer: 87.04%

#### You call 2 UberX’s and 3 Lyfts at the same time. If the time that each takes to reach you is identically and independtly distributed, what is the probability that all the Lyfts arrive first? What is the probability that all the UberX’s arrive first?
For the first Lyft, there is a 3/5 chane that it arrives first. For the second one, there are 4 cars left out of which 2 are lyfts (i.e. 2/4 chance), etc.
Due to independence:
P("all Lyfts arrive first") = (3/5) * (2/4) * (1/3) = 1/10
P("all Ubers arrive firs") = (2/5) * (1/4)=1/10

Final answer: 1/10 (for both questions)

#### In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the probability that you see at least one shooting star in the period of an hour?
There are 4 15-min intervals in one hour.
P("at least 1 shooting star in an hour") = 1- P("no shooting star in an hour") = 1 - 0.8^4 = 59.04%

Final answer: 59.04%

#### For numbers reaching from 1 to 300, how many are divible by 3 or 5 or 3 and 5?
  - divisible by 3: 3, 6... 300: 300/3 = 100
  - divisible by 5: 5, 10...300: 300/5 = 60
  - divisible by 3 and 5 so divisible by 3*5=15: 15,30...300 = 300/15 = 20
  - TOTAL = 100+60-20=140

Final answer: 140

#### A glass contains 10 red balls, 4 white balls, and 3 green balls. Two are drawn in sequence, without replacment. What is the probability that the 2 balls are green?
For the first ball, we have 3 choices, after that we are left  wiith 2 balls. As such:
P("2 balls are green") = 3*2/16*15 = 0.025 0 2.5%

Final answer = 2.5%



## Medium-level questions

#### On a dating site, users can select 5 out of 24 adjectives to describe themselves. A match is declared between 2 users if they match on at least 4 adjectives. If Alice and Bob randomly pick adjectives, what is the probability that they form a match?
We need to distinguish between 2 different scenarios:
1) They have 4/5 common adjectives
2) They have 5/5 common adjectives

1)
Alice has chosen 5 adjectives.
There are (5C4)=5 sets of 4 adjectives that Bob can receive that Alice chose.
Lets say she chose A, B, C, D & E.
Bob can choose A,B,C & D or A,B, D & E, ... or (5C4)
Similarly, there are (19C1)=19 adjectives that Bob can receive that were NOT given to Alice.
2)
There is only onee possible way to have the same adjectivs

Note that there are (24C5) different sets of adjectives that a test-taker can receive.

We get:
[(5C4)x(19C1)+1]/(24C5)

#### You are a prisoner sentenced to death. The Emperor offers you a chance to live by playing a simple game. He gives you 50 black marbles, 50 white marbles and 2 empty bowls. He then says, "Divide these 100 marbles into these 2 bowls. You can divide them ANY WAY YOU LIKE as long as you use all the marbles. Then I will blindfold you and mix the bowls around (without mixing the marbles). You then can choose one bowl and remove ONE marble. If the marble is WHITE you will live, but if the marble is BLACK... you will die." How do you divide the marbles up so that you have the greatest probability of choosing a WHITE marble?
The best way to divide them is to put 1 white marble into 1 bowl. The other bowl is filled with 99 marblkes (49 white & 50 black).
This way: if you get the first container (which you can get with 50% chance), you win 100% of the time. If you get the other bowl, you still win almost 50% of the time.

## Hard questions

#### A line of 100 airline passengers is waiting to board a plane. They each hold a ticket to one of the 100 seats on that flight. (For convenience, let's say that the nth passenger in line has a ticket for the seat number n.) Unfortunately, the first person in line is crazy, and will ignore the seat number on their ticket, picking a random seat to occupy. All of the other passengers are quite normal, and will go to their proper seat unless it is already occupied. If it is occupied, they will then find a free seat to sit in, at random. What is the probability that the last (100th) person to board the plane will sit in their proper seat (#100)?
There is a trick to solve this problem. To get the right  probability, we need to simplify thee problem.
1) There  are only 2 passengers:
A sits on the good seat, so will  B
A sits on the wrong seat, so will B
--> The probability is thus 50%
2) There are 3 passngrs:
A sits on the rights seat, so B & C will as well. C will be on the correct seat
A sits on B's seat, B comes in and sits on A's seat. C will be on the correct seat
A sits on B's seat, B comes in and sits on C's seat. C will be on the wrong seat
A sits on C's seat, B will therefore sit on B's seat. C will b on the wrong seat
--> The probability is thus 50%
3) and so on

correct answer: 50%



------------------------------------------------------------
! Transfer into above structure !
------------------------------------------------------------



#### 1. Bobo the amoeba has a 25%, 25%, and 50% chance of having 0, 1, or 2 children, respectively. Each of Bobo’s descendants also have the same probabilities. What is the probability that Bobo’s lineage dies out?
  - p=1/4+1/4*p+1/2*p^2 => p=1/2
  - find the roots of 2p^2-3p+1=0
  - x= [-b+-sqrt(b^2-4ac)]/2a
  - it has roots 1/2 and 1, but would expect it lower than 1 hence it is 1/2.

#### 3. How can you generate a random number between 1 - 7 with only a die?
Depends on the probability distribution.

If you want a binomial distribution, roll the dice 6 times, and write down the number of odd numbers (or the number of even numbers), then add 1.

For a uniform distribution, here’s what I’d do:

Roll the die 3 times. If the roll is even, write down 0; if odd, write down 1. If you get all 0s, reroll.

Let’s assume you wrote down a, b, c. Compute 4a + 2b + c.

This gives you a uniform random distribution.
#### 4. How can you get a fair coin toss if someone hands you a coin that is weighted to come up heads more often than tails?
Flip it twice.

- If you get heads first and then tails, call it "Heads".

- If you get tails first and then heads, call it "Tails".

- If you get the same result twice, start over.

You may need to do this a few times, even lots of times if you're unlucky, but eventually you'll get either HT or TH and the likelihood of either is the same.
#### 5. You have an 50-50 mixture of two normal distributions with the same standard deviation. How far apart do the means need to be in order for this distribution to be bimodal?
  - more than two standard deviations
#### 6. Given draws from a normal distribution with known parameters, how can you simulate draws from a uniform distribution?
  - plug in the value to the CDF of the same random variable
#### 7. A certain couple tells you that they have two children, at least one of which is a girl. What is the probability that they have two girls?
  - In a family with 2 children there are four possibilities:
  - 1) the first child is a boy and the second child is a boy (bb)
  - 2) the first child is a boy and the second child is a girl (bg)
  - 3) the first child is a girl and the second child is a boy (gb)
  - 4) the first child is a girl and the second child is a girl (gg)

Since we are given that at least one child is a girl there are three possibilities: bg, gb, or gg. Out of those three possibilities the only one with two girls is gg. Hence the probability is 1/3.
  - 1/3
#### 8. You have a group of couples that decide to have children until they have their first girl, after which they stop having children. What is the expected gender ratio of the children that are born? What is the expected number of children each couple will have?
  - gender ratio is 1:1. Expected number of children is 2. let X be the number of children until getting a female (happens with prob 1/2). this follows a geometric distribution with probability 1/2
#### 9. How many ways can you split 12 people into 3 teams of 4?
 - Permutations are for lists (order matters) and combinations are for groups (order doesn't matter).
  - the outcome follows a multinomial distribution with n=12 and k=3. but the classes are indistinguishable
  -12 people. The first team: 12 choose 4 = (12 choose 4). Then the second team would be 4 of the remaining 8 people: (8 choose 4). The last team would be 4 of the remaining 4, which obviously equals 1, but to be thorough: (4 choose 4).

(12 choose 4)(8 choose 4)(4 choose 4)=495*70*1=34,650.

However, this sorting assumes that which team each person is on is important - ie, team 1, team 2, etc. If there are no “team numbers” and we’re just dividing people up, then you also need to divide by the ways to assign team numbers = 3!. So 34650/3!=5,775.


combination: n choose k: n!/[k!(n-k)!]
permutation: n!/(n-k)!

#### 10. Your hash function assigns each object to a number between 1:10, each with equal probability. With 10 objects, what is the probability of a hash collision? What is the expected number of hash collisions? What is the expected number of hashes that are unused.
  - the probability of a hash collision: 1-(10!/10^10) = 1-no hash collision : first can choose 10 then 9 then 8 so 10!/10^10 possibilities

  - Let 𝐻​ be the number of hash collisions. This is equal to the number of unused buckets because for there to be a collision, then a bucket must be empty.

  Denote by I(k) the indicator that the integer 1≤𝑘≤10​ is used. Notice that for distinct indices, these are independent random variables. The expectation of 𝐼1​ is the probability that at least one of the objects get hashed to the bucket 1 . This is equal to 1 minus the probability that none of the 10 objects get hashed to 1.
  𝔼(𝐼1)=1−(9/10)^10.
  𝔼(𝑁)=𝔼(𝐼1+𝐼2+…+𝐼10) = 𝔼(𝐼1)+𝔼(𝐼2)+…+𝔼(𝐼10)​ = 10(1−(9/10)^10)≈6.5132.​
  This is the number of hash collisions but also the number of used buckets.

  - the expected number of hashes that are unused: 10 - 10(1−(9/10)^10) ≈ 3.4868.






#### 16. What’s the expected number of coin flips until you get two heads in a row? What’s the expected number of coin flips until you get two tails in a row?
Let x the expected number of coin flips required for getting two heads in a row.
1) if the first flip turns out to be tail - you need x more flips since the events are independent. Probability of the event 1/2. Since 1 flip was wasted total number of flips required (1+x).
2) if the first flip becomes head, but the second one is tail(HT) - 2 flips are wasted, here total number flips required would be (2+x). Probability of HT out of HH, HT, TH, TT is (1/4)
3) the best case, the first two flips turn out to be heads both(HH). Probability, 1/4 i.e. HH out of HH, HT, TH, TT.  No of flips required 2.

So from the above scenarios,
     x = 1/2(1+x) + 1/4(2+x) + (1/4)* 2
=>   x = 1/2 [ (1+x) + 1/2(2+x) + 1 ]
=>   x = 1/2 [ 1 + x + 1 + x/2 + 1 ]
=>   x = 3/2 + (3/4)x
=>   x / 4 = 3/2
=>   x = 6

So the expected number of flips would be '6'
#### 17. Let’s say we play a game where I keep flipping a coin until I get heads. If the first time I get heads is on the nth coin, then I pay you 2n-1 dollars. How much would you pay me to play this game?
 - 1: 1, 2: 3, 3: 5
 - 0.5*1+3*(0.5)^2+ 5*(0.5)^3
 - lim = inf!
  - less than $3


#### 18. You have two coins, one of which is fair and comes up heads with a probability 1/2, and the other which is biased and comes up heads with probability 3/4. You randomly pick coin and flip it twice, and get heads both times. What is the probability that you picked the fair coin?
proba HH with fair: (1/2)^2 = 1/4
proba HH with unfair: (3/4)^2 = 9/16

P(A|B) = [P(B|A)* P(A)]/P(B)    (Bayes formula)
A is pick fair B is HH both times

p(B) = 0.5 * 1/4 + 0.5*9/16
[1/4 * 0.5]/[0.5*1/4+0.5*9/16]
[1/8]/[1/8+9/32]
[1/8]/[13/32]
= [32]/[8*13]
=4/13


#### 19. You have a 0.1% chance of picking up a coin with both heads, and a 99.9% chance that you pick up a fair coin. You flip your coin and it comes up heads 10 times. What’s the chance that you picked up the fair coin, given the information that you observed?
P(A|B) = [P(B|A)* P(A)]/P(B)(Bayes formula)

B is Head 10 times
A is proba fair coin


P(B|A) is proba 10 Heads knowing coin is fair =
(1/2)^10

P(B) = proba 10 Heads:
0.001*1 + 0.999*(1/2)^10
fake coin has to do all H + fair coin * proba

P(A|B) = [(1/2)^10 * 0.999]/[0.001*1 + 0.999*(1/2)^10]
With 2^10 ≈ 1000 and 0.999 ≈ 1 this simplifies to:
so (1/2)^10 ≈ 0.001
hence 0.001/[0.001+0.001] = 1/2



#### 20. What is a P-Value ?
In hypothesis test, The P value, or calculated probability, is the probability of finding the observed, or more extreme, results when the null hypothesis (H0) of a study question is true.
P is also described in terms of rejecting H0 when it is actually true, however, it is not a direct probability of this state.

Many people decide, before doing a hypothesis test, on a maximum p-value for which they will reject the null hypothesis. This value is often denoted α (alpha) and is also called the significance level = Type I error


P-low reject H0
The p-value is used as an alternative to rejection points to provide the smallest level of significance at which the null hypothesis would be rejected. A smaller p-value means that there is stronger evidence in favor of the alternative hypothesis.

The distance between the data and the model prediction is measured using a test statistic (such as a t-statistic or a chi-squared statistic). The P-value is then the probability that the chosen test statistic would have been at least as large
as its observed value if every model assumption were correct, including the test hypothesis. This definition embodies a crucial point lost in traditional definitions: In logical terms, the P-value tests all the assumptions about how the data were generated (the entire model), not just the targeted hypothesis it is supposed to test (such as a null hypothesis).

#### 21. Type I and Type II error ?
A type I error occurs when the null hypothesis (H0) is true, but is rejected. = significance level = False positive
A type II error occurs when the null hypothesis is false, but erroneously fails to be rejected. =

+---------------------+--------------+--------------+
| NULL hypothesis is: |              |              |
+---------------------+--------------+--------------+
| True                | False        |              |
| Fail to reject      | test         | Content Cell |
| Reject              | Type I error | Content Cell |
+---------------------+--------------+--------------+



#### 22. There's a game where you are given two fair six-sided dice and asked to roll. If the sum of the values on the dice equals seven, then you win $21. However, you must pay $5 to play each time you roll both dice. Do you play this game?

36 combinations: 6*6.
6 possibilities to get 7: 5&2 2&5  3&4 4&3  6&1  1&6
21*1/6 -5 = -1.5
negative expectation NO dont play!


### 23. You have 8 pennies, 7 weight the same, one weighs less. you  also have a judges scale. Find the one that weighs the least in less than 3 steps.
Split the 8 pennies into 3 groups of 3,3,2 pennies. Weight the first two groups of 3 pennies each.

Case 1) - They weight the same. Therefore, take third group of 2 pennies and find the lighter coin.

Case 2) Group 1 weights more than Group 2. Take group 2 (3 pennies) and pick any 2 out of 3. If they weight the same, then the third penny is lighter. Answer is trivial if they don't weight the same.

It works for any scenario. Always split the groups in 3.


### 24. Suppose that there is a building with 100 floors. You are given 2 identical eggs. The most interesting property of the eggs is that every egg has it’s own “threshold” floor. Let’s call that floor N. What this means is that the egg will not break when dropped from any floor below floor N, but the egg will definitely break from any floor above floor N, including floor N itself. For example, if the property of the eggs is that N equals 15, those eggs will always break on any floor higher than or equal to the 15th floor, but those eggs will never break on any floor below floor 15. The same holds true for the other egg since they are identical. These are very strong eggs, because they can be dropped multiple times without breaking as long as they are dropped from floors below their “threshold” floor, floor N. But once an egg is dropped from a floor above it’s threshold floor. Here is the puzzle: What strategy should be taken in order to minimize the number of egg drops used to find floor N (the threshold floor) for the egg? Also, what is the minimum number of drops for the worst case using this strategy?/ Remember that you are given 2 identical eggs which both have the same exact threshold floor.

Binary search would be easy if infinite number of search: try floor 50, then 25...
However only 2 eggs
The next solution takes a little bit of the linear approach and mixes in a little of the splitting from our binary approach. We can start off by dropping an egg at floor 10, increasing the drop floor by 10 at a time, then going back to drop one floor at a time until we find that n. If our egg breaks at floor 10, we know n is one of the 9 floors below us.
Worst case, the egg drops and doesn’t break until floor 100 (10 drops) and we drop the second egg but don’t break it for floors 91–99.
It brings our worst case drop count to 19 drops.
NEXT:
What we should try to get with our next approach is to try to reduce the worst case scenario by trying to make all possible scenarios take the same number of drops.
What if we tried to reduce the number of drops that would be required with the linear search (with the 2nd egg) after we get to one of the higher floors? This way we counteract the fact that getting to the higher floor took so many drops, and if we use less drops for the linear search we are balancing out the worst case.

Let’s try to figure this out using some simple algebra. Suppose we drop an egg from floor x. If the egg breaks, then we would have to go through the previous x-1 floors one by one using a linear search.

But, if the egg doesn’t break, in our original algorithm we would go up x floors to find the next floor to test from. Why not just go up x-1 floors instead of x floors? This would save us 1 drop if we have to do a linear search with the 2nd egg whenever the first egg breaks. This means that the next floor that should be attempted to drop from is x + (x-1) if the egg does not break from floor x.
Hence: x representing the floor we throw the first egg. And this is the worst case:
We throw the egg at floor x, then x-1, then x-2 ... until it breaks.
x + (x-1) + (x-2) + (x-3) + ... + 1
This is a triangular series.
Which simplifies to:
x(x + 1)/2

x(x+1)/2 = 100
x = 13.651
so initial floor count is 14! then 13, then 12.

The worst case:
The solution for the worst case in this scenario occurs when the threshold floor is floor number 14 – because we will drop the first egg on floor 14, and it will break. Then we have to test floors 1-13 with the 2nd egg to see where the egg breaks again, and the egg will not break on any of those floors. But since the egg broke on the floor 14, we can conclude that the threshold floor is floor number 14.



### 25. On an otherwise deserted and isolated island, 200 perfect logicians are stranded. The islanders are perfectly logical in every decision they make, and they will not do anything unless they are absolutely certain of the outcome. However, they cannot communicate with each other. They are forbidden from speaking with one another, or signing, or writing messages in the sand, else they be shot dead by the captain of a mysterious ship that visits the island each night. Of the 200 islanders, 100 have blue eyes, and 100 have brown eyes. However, no individual knows what color their own eyes are. There are no reflective surfaces on the island for the inhabitants to see a reflection of their own eyes. They can each see the 199 other islanders and their eye colors, but any given individual does not know if his or her own eyes are brown, blue, or perhaps another color entirely. And remember, they cannot communicate with each other in any way under penalty of death. Each night, when the captain of the ship comes, the islanders have a chance to leave the barren and desolate spit of land they have been marooned on. If an islander tells the captain the color of his or her own eyes, they may board the ship and leave. If they get it wrong, they will be shot dead. Now, there is one more person on the island: the guru, who the islanders know to always tell the truth. The guru has green eyes. One day, she stands up before all 200 islanders and says: I see a person with blue eyes. Who leaves the island? And when do they leave?
You know that if there were only one person with blue eyes, they would realize it immediately after hearing the guru's statement because they see no one else with blue eyes. Therefore, that person would leave on the first night.

You also know that if there were two people with blue eyes, then they would both leave on the second night, because they would each look at the other blue-eyed person on the second morning and realize that the only reason the other blue-eyed person wouldn't leave on the first night is because they see another person with blue eyes. Seeing no one else with blue eyes, each of these two people realize it must be them.
Now consider the case of three blue-eyed islanders. It has been established that if only two people had blue eyes they would leave on the second night. You, the third blue-eyed person in our example, know this, as do the other two blue-eyed people. So when you wake up on the third morning, and the two other blue-eyed people have not left, you know that they must see another person with blue eyes, and you can see that no one else on the island has blue eyes, so you know it must be you. All three of you realize this simultaneously, and all three leave on the third night.

Each blue-eyed islander knows from looking around the island that there are 99 other people with blue eyes and 100 people with brown eyes. But because they cannot depart the island without being certain, they cannot begin the process of leaving until the guru speaks, and common knowledge is attained. Without knowing that everyone knows that everyone knows that there is at least one person with blue eyes, they cannot leave.

However people with brown eyes cannot leave.



### 26. a player is randomly dealt a sequence of 13 cards from a deck of 52 cards. All sequences of 13 cards are equally likely.
In an equivalent model, the cards are chosen and dealt one at a time. When choosing a card, the dealer is
equally likely to pick any of the cards that remain in the deck
a) if you dealt 13 cards, what is the probability that the 13th card is a king:

Since we are not told anything about the first 12 cards that are dealt, the proba that the 13th card is a King is the same as the proba that the first card dealt
or in fact any particular card dealt is a King, = 4/52


### 27. Fair six sided die is rolled 6 times. Proba of getting all outcomes as unique?
6/6 * 5/6 * 4/6 * 3/6 * 2/6 * 1/6


### 28. A group of 60 students is randomly split into 3 classes of = size. All partitions are =ly likely. Jack and Jill are 2 students belonging to that group. What is the probability that Jack and Jill will end up in the same class?
19/59


### 29. If you had 3 coins where you get $1 for all HHH or all TTT or lose $1 otherwise, would you play the game? How about if you can re-flip one coin?
2 possibilities at each stage (H or T)
2^3 possiblities = 8
2/8 to win (HHH and TTT):
2/8 * 1 - 6/8 * 1 = -0.5EUR
Dont play the game.

What if can reflip a coin?
Can reflip either coin:
will reflip in those cases:   HTT TTH THH THH THT HTH
will reflip the "odd one out every time": 50% chance of winning.
so average gain is now:
2/8 * 1 + (6/8) * 0.5 * 1 - (6/8) * 0.5 * 1 =


### 30. Player A has a thirty-sided and Player B has a twenty-sided die. They both roll the dies and whoever gets the higher roll wins. If they roll the same amount Player B wins. What is the probability that Player B win?

Case: A rolls between 21-30   Proba happens: 1/3     Output: 0% winning chance for B
Case: A rolls between 1-20 & diff number from B   Proba happens: 2/3*(19/20)     Output: 50% winning chance for B
Case: A rolls between 1-20 & same number as B  Proba happens: (1/20) * (2/3) Output: 100% winning chance for B
P(B win) = 0 * 1/3 + 2/3 * 1/20 + 2/3 * 19/20 * 1/2
0% * P(A bw 21-30) + P(A bw 1-20) * P(land same) * 100% + P(A bw 1-20) * P(land diff) * P(B win when not equal and in the same range: coin toss aka 50%)
P(B win) = 42/120 = 7/20 = 0.35





<!-- This stuff i had for interview @ a Fintech firm in South America -->

### 30. We have 2 die (6 faces each): one biased other one fair. The biased die
### has a proba of 50% of landing on the 1 face, while it lands on the other faces
### with the same probability. it is known that one of the die was chosen randomly, played 3 times and in the 3 throws landed on 1. What is the probability of playing the same dice and the next face is 2?
This comes down to breaking the problem into sizeable chunks.
Here are the steps:
Step1: Probability the die is fair knowing it landed 3 times on 1
Step2: Probability the die is biased knowing it landed 3 times on 1
Step3: Die was randomly chosen, what is the probability that the next is 2

Step1:
P(fair | landed 3x 1) = P( landed 3x1 | fair) * P( fair ) / P( landed 3x1 )
P( landed 3x1 | fair) = (1/6)^3
P(fair) = 0.5

P( landed 3x1 ) = P(biased) * P(3x1 | biased) + P(fair) * P(3*1 | fair)
= 0.5 * (0.5)^3 + 0.5 * (1/6)^3

Thus, P(fair | landed 3x 1) = ((1/6)^3 * 0.5) / [0.5 * (0.5)^3 + 0.5 * (1/6)^3]
= 0.04

Step2:
P(biased | landed 3x 1) = P( landed 3x1 | biased) * P( biased ) / P( landed 3x1 )
P( landed 3x1 | biased) = (0.5)^3
P(biased) = 0.5

P( landed 3x1 ) = same as step 1 = 0.5 * (0.5)^3 + 0.5 * (1/6)^3

Thus, P(biased | landed 3x 1) = ((0.5)^3 * 0.5) / [0.5 * (0.5)^3 + 0.5 * (1/6)^3]
= 0.96

Or just 1 - P(fair | landed 3x 1)

Step3:
P(lands on 2 | landed 3 x 1) = P(biased | landed 3 x 1) * P(lands 2 | biased) +
P(fair | landed on 3 x 1) * P(lands 2 | fair)
= 0.96 * 0.1 + (1-0.96) * (1/6) = 10.24%



Henry has been caught stealing cattle, and is brought into town for justice. The judge is his ex-wife Gretchen, who wants to show him some sympathy, but the law clearly calls for two shots to be taken at Henry from close range. To make things a little better for Henry, Gretchen tells him she will place two bullets into a six-chambered revolver in successive order. She will spin the chamber, close it, and take one shot. If Henry is still alive, she will then either take another shot, or spin the chamber again before shooting.

Henry is a bit incredulous that his own ex-wife would carry out the punishment, and a bit sad that she was always such a rule follower. He steels himself as Gretchen loads the chambers, spins the revolver, and pulls the trigger. Whew! It was blank. Then Gretchen asks, "Do you want me to pull the trigger again, or should I spin the chamber a second time before pulling the trigger?"

What should Henry choose?

In successive order:

OOOOBB
BBOOOO
OBBOOO
OOBBOO
OOOBBO
BOOOOB

1/4 prob that fell on one that will kill him next (one next to a B)
if spin again: 2/6 will die, aka 1/3

so should shoot again


Mr. Black, Mr. Gray, and Mr. White are fighting in a truel. They each get a gun and take turns shooting at each other until only one person is left. Mr. Black, who hits his shot 1/3 of the time, gets to shoot first. Mr. Gray, who hits his shot 2/3 of the time, gets to shoot next, assuming he is still alive. Mr. White, who hits his shot all the time, shoots next, assuming he is also alive. The cycle repeats. All three competitors know one another's shooting odds. If you are Mr. Black, where should you shoot first for the highest chance of survival?

He should shoot at the ground.

If Mr. Black shoots the ground, it is Mr. Gray's turn. Mr. Gray would rather shoot at Mr. White than Mr. Black, because he is better. If Mr. Gray kills Mr. White, it is just Mr. Black and Mr. Gray left, giving Mr. Black a fair chance of winning. If Mr. Gray does not kill Mr. White, it is Mr. White's turn. He would rather shoot at Mr. Gray and will definitely kill him. Even though it is now Mr. Black against Mr. White, Mr. Black has a better chance of winning than before.



"I'm a very rich man, so I've decided to give you some of my fortune. Do you see this bag? I have 5001 pearls inside it. 2501 of them are white, and 2500 of them are black. No, I am not racist. I'll let you take out any number of pearls from the bag without looking. If you take out the same number of black and white pearls, I will reward you with a number of gold bars equivalent to the number of pearls you took."

How many pearls should you take out to give yourself a good number of gold bars while still retaining a good chance of actually getting them?



Answer
Take out 5000 pearls. If the remaining pearl is white, then you've won 5000 gold bars!



A hiker climbs all day up a steep mountain path and arrives at the mountain top where he camps overnight. The next day he begins the descent down the same trail to the bottom of the mountain when suddenly he looks at his watch and exclaims, "That is amazing! I was at this very same spot at exactly the same time of day yesterday on my way up."
What is the probability that a hiker will be at exactly the same spot on the mountain at the same time of day on his return trip, as he was on the previous day's hike up the mountain?
Is the probability closest to (A) 99% or (B) 50% or (C) 0.1% ?



Answer
The answer is (A). Since it must happen, the probability is actually 1 (100%).
Explanation: Firstly, consider 2 men, one starting from the top of the mountain and hiking down while the other starts at the bottom and hikes up. At some time in the day, they will cross over. In other words they will be at the same place at the same time of day.
Now consider our man who has walked up on one day and begins the descent the next day. Imagine there is someone (a second person) shadowing his exact movements from the day before. When he meets his shadower (it must happen) it will be the exact place that he was the day before, and of course they are both at this spot at the same time.
Contrary to our common sense, which seems to say that this is an extremely unlikely event, it is a certainty.
NOTE: There is one unlikely event here, and that is that he will notice the time when he is at the correct location on both days, but that was not what the question asked.


Mike proba win: 3/4 * 1/6 + 3/4 * 5/6 * 3/5 = 1/2

they both have = chances




Mismatched Joe is in a pitch dark room selecting socks from his drawer. He has only six socks in his drawer, a mixture of black and white. If he chooses two socks, the chances that he draws out a white pair is 2/3. What are the chances that he draws out a black pair?



Answer
He has a ZERO chance of drawing out a black pair.

6 choose 2 there are 15 possibilities of pairs
if 2/3 chance of white pair: 10 white pairs, the 5 others are 1 black pair paired with a white

Since there is a 2/3 chance of drawing a white pair, then there MUST be 5 white socks and only 1 black sock. The chances of drawing two whites would thus be: 5/6 x 4/5 = 2/3 . With only 1 black sock, there is no chance of drawing a black pair.












In a box you have 13 white marbles and 15 black marbles. You also have 28 black marbles outside the box. Remove two marbles, randomly, from the box. If they are of different colors, put the white one back in the box. If they are the same color, take them out and put a black marble back in the box. Continue this until only one marble remains in the box. What color is the last marble?


Answer
The last marble will be WHITE.

Since marbles can only be taken out in pairs and you started off with an odd number of whites there is always going to be one white left over that you'll keep putting back in the box until it's left on its own.





A swindler once approached an honest man with a die. He handed him the die and told him about the bet. The die had six sides. If the man rolled a ONE, he wins, and gets back twice the amount of his bet. If not, the swindler would keep the bet.

"But...my chances are only one out of six," retorted the man.

"True," grinned the swindler, "But I'll give you three tries to get a one."

The man considered. Three tries, with each try having a 1/6 chance of winning. So his chances of winning are 1/2. Why not give it a try?

Is the bet really fair? If not, what are the chances of the man winning?


Expectation: (1/6) * 2 + (5/6) * (1/6) * 2 + (5/6)^2 * 1/6 * 2 + (5/6)^3 * (-1)
2/6 + 10/36 + 50/216 - 125/216  = (72+60+50-125)/216 = 27/216
postive expectancy
The probability of the man not getting a ONE in three throws is: 5/6 x 5/6 x 5/6, which is 125/216. This is the probability of the swindler winning.

Hence, the remaining fraction, 91/216, is the actual chance of the man winning.





A line of 100 airline passengers is waiting to board a plane. They each hold a ticket to one of the 100 seats on that flight. (For convenience, let's say that the nth passenger in line has a ticket for the seat number n.)
Unfortunately, the first person in line is crazy, and will ignore the seat number on their ticket, picking a random seat to occupy. All of the other passengers are quite normal, and will go to their proper seat unless it is already occupied. If it is occupied, they will then find a free seat to sit in, at random.
What is the probability that the last (100th) person to board the plane will sit in their proper seat (#100)?



Answer
The whole thing stops when someone else sits in Crazy Guy's seat. The chances of that range from 1/99 (First person) to 1/1 for the last guy. So:

1/99 + Summation from 98 to 2 of ( 1/ n(n+1) )
This returns 0.5 or 50%.

Also, the answer remains 50% no matter how many people are added to the line!




Timothy and Urban play a game with two dice. But they do not use the numbers. Some of the faces are painted red and the others blue. Each player throws the dice in turn. Timothy wins when the two top faces are the same color. Urban wins when the colors are different. Their chances are even.
The first die has 5 red faces and 1 blue face. How many red and how many blue are there on the second die?

timothy: same color win
urban: diff color win
chances are 50 50

x is number red in other die
tim: red red or blue blue:   5/6 * (x/6) + 1/6 * ((6-x)/6) = 5x/36 + (6-x)/36 = (6+4x)/36 = 1/2
6+4x = 18    x = 3

in the second die there are 3 red and 3 blue




Gretchen and Henry were discussing their new neighbors, the Gardners. Gretchen mentioned that she met two of the daughters, and they each had blond hair.

"I have met all of the sisters," replied Henry, "and the probability that both of the girls you met would have had blond hair, assuming you were equally likely to meet any of the sisters, is exactly 50%. Do you know how many children there are?"

After thinking for a minute, Gretchen asks if the family is abnormally large. When Henry replies that it is not, Gretchen tells him how many girls are in the family. What number did she say?


Answer
Gretchen said that there were 4 girls in the family, three of whom were blond.

This would make the probability that she saw two blonds (3/4) * (2/3), which equals 1/2.

Other numbers would work, but the next pair would lead to a rather large family.

2 blond

y/x * (y-1)/(x-1) = 1/2
y(y-1)/x(x-1) = 1/2





Little Billy has a calculator with 15 buttons. He has 10 keys for 0-9, a key for addition, multiplication, division, and subtraction. Finally, he has an = sign. However, Mark the Meanie messed up the programming on Billy's calculator. Now, whenever Billy presses any of the number keys, it comes up with a random single-digit number. The same goes for the four operations keys (+,-,x, /). So whenever Billy tries to press the + button, the calculator chooses randomly between addition, multiplication, subtraction, and division. The only key left untouched was the = sign.

Now, if Billy were to press one number key, one operation key, then another number key, then the = button, what are the chances the answer comes out to 6?



Answer
There is a 4% chance.

There are 16 possible ways to get 6.

0+6
1+5
2+4
3+3
6+0
5+1
4+2
9-3
8-2
7-1
6-0
1x6
2x3
6x1
3x2
6/1

There are 400 possible button combinations.

When Billy presses any number key, there are 10 possibilities; when he presses any operation key, there are 4 possibilities.

10(1st#)x4(Operation)x10(2nd#)=400

16 working combinations/400 possible combinations= .04 or 4%



odd: odd+even  even odd
even: even even odd odd









Suppose I flip two coins without letting you see the outcome, and I tell you that at least one of the coins came up heads. What is the probability that the other coin is also heads?



Answer
1/3.

For two coins, there are four possible outcomes: HH, HT, TH, and TT. Since we know that at least one was a head, we can eliminate TT. Of the remaining three possibilities, only 1 allows the second head: HH.


### 5 new employees A B C D and E are sitting in two rows at their training.
B is sitting on the left end of Row 1, which contains 2 seats
A is sitting on the left end of Row2, which has 3 seats.
How many combinations?

O here is empty seat
B-O
E-O-O
3 choices for first seat next to B, 2 for the next, one for the following: 3*2*1 = 6
