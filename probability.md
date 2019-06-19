## Probability


#### 1. Bobo the amoeba has a 25%, 25%, and 50% chance of producing 0, 1, or 2 o spring, respectively. Each of Bobo’s descendants also have the same probabilities. What is the probability that Bobo’s lineage dies out?
  - p=1/4+1/4*p+1/2*p^2 => p=1/2
  - find the roots of 2p^2-3p+1=0
  - x= [-b+-sqrt(b^2-4ac)]/2a
  - it has roots 1/2 and 1, but would expect it lower than 1 hence it is 1/2.
#### 2. In any 15-minute interval, there is a 20% probability that you will see at least one shooting star. What is the probability that you see at least one shooting star in the period of an hour?
 - at least one shooting star in 1 h = 1-no shooting stars in 1 h
  - 1-(0.8)^4. Or, we can use Poisson processes
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
#### 11. You call 2 UberX’s and 3 Lyfts. If the time that each takes to reach you is IID, what is the probability that all the Lyfts arrive first? What is the probability that all the UberX’s arrive first?
(3/5)(2/4)(1/3) = 1/10
(2/5)(1/4)=1/10

#### 12. I write a program should print out all the numbers from 1 to 300, but prints out Fizz instead if the number is divisible by 3, Buzz instead if the number is divisible by 5, and FizzBuzz if the number is divisible by 3 and 5. What is the total number of numbers that is either Fizz, Buzz, or FizzBuzz?
  - Fizz: divisible by 3: 3, 6... 300: 300/3 = 100
  - Buzz: divisible by 5: 5, 10...300: 300/5 = 60
  - Fizzbuzz: divisible by 3and5 so divisible by 3*15=15: 15,30...300 = 300/15 = 20
  - TOTAL = 100+60-20=140

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
The P value, or calculated probability, is the probability of finding the observed, or more extreme, results when the null hypothesis (H0) of a study question is true.
P is also described in terms of rejecting H0 when it is actually true, however, it is not a direct probability of this state.

Many people decide, before doing a hypothesis test, on a maximum p-value for which they will reject the null hypothesis. This value is often denoted α (alpha) and is also called the significance level = Type I error


P-low reject H0
The p-value is used as an alternative to rejection points to provide the smallest level of significance at which the null hypothesis would be rejected. A smaller p-value means that there is stronger evidence in favor of the alternative hypothesis.

P-values are calculated using p-value tables or spreadsheet/statistical software.

For ease of comparison, researchers often feature the p-value in the hypothesis test and allow the reader to interpret the statistical significance themselves. This is called a p-value approach to hypothesis testing.

#### 21. Type I and Type II error ?
A type I error occurs when the null hypothesis (H0) is true, but is rejected. = significance level = False positive
A type II error occurs when the null hypothesis is false, but erroneously fails to be rejected. =

|                NULL hypothesis is:            |
|                |    True      |    False      |
|                 ------------- | ------------- |
| Fail to reject |  test            | Content Cell  |
| Reject         | Type I error | Content Cell  |



#### 22. There's a game where you are given two fair six-sided dice and asked to roll. If the sum of the values on the dice equals seven, then you win $21. However, you must pay $5 to play each time you roll both dice. Do you play this game?

36 combinations: 6*6.
6 possibilities to get 7: 5&2 2&5  3&4 4&3  6&1  1&6
21*1/6 -5 = -1.5
negative expectation NO dont play!
