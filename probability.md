# Probability

You might encounter probability questions in two different ways during your interview process: They might ask you some probability-based brain teasers during the technical in-person interview to see how approach this kind of problem, or you might need to answer probability question in the qunatitative aptidude test.

Here is a reminder of some mathematical formulas and concepts that you should have in mind to tackle these questions:

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
P("all Lyfts arrive first") = (3/5)*(2/4)*(1/3) = 1/10
P("all Ubers arrive firs") = (2/5)*(1/4)=1/10

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



## Medium-level questions


## Hard questions



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




#### 13. On a dating site, users can select 5 out of 24 adjectives to describe themselves. A match is declared between two users if they match on at least 4 adjectives. If Alice and Bob randomly pick adjectives, what is the probability that they form a match?
There are (5C4)=5 sets of 4 adjectives that Bob can receive that Alice chose.
Similarly, there are (19C1)=19 adjectives that Bob can receive that were NOT given to Alice.

Note that there are (24C5) different sets of adjectives that a test-taker can receive.

[(5C4)x(19C1)+(5C5)x(19C0)]/(24C5)=41771≈0.2

#### 14. A lazy high school senior types up application and envelopes to n different colleges, but puts the applications randomly into the envelopes. What is the expected number of applications that went to the right college?
proba that 1 letter gets to right college is 1/n
number of letters sent (and colleges) is n
so:
n * 1/n
  - 1
#### 15. Let’s say you have a very tall father. On average, what would you expect the height of his son to be? Taller, equal, or shorter? What if you had a very short father?
  - Shorter. Regression to the mean
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
