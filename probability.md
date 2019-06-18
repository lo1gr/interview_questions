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

(12 choose 4)(8 choose 4)(4 choose 4)=495∗70∗1=34,650.

However, this sorting assumes that which team each person is on is important - ie, team 1, team 2, etc. If there are no “team numbers” and we’re just dividing people up, then you also need to divide by the ways to assign team numbers = 3!. So 34650/3!=5,775.


combination: n choose k: n!/[k!(n-k)!]
permutation: n!/(n-k)!

#### 10. Your hash function assigns each object to a number between 1:10, each with equal probability. With 10 objects, what is the probability of a hash collision? What is the expected number of hash collisions? What is the expected number of hashes that are unused.
  - the probability of a hash collision: 1-(10!/10^10) = 1-no hash collision : first can choose 10 then 9 then 8 so 10!/10^10 possibilities
  - the expected number of hash collisions: 1-10*(9/10)^10
  - the expected number of hashes that are unused: 10*(9/10)^10
#### 11. You call 2 UberX’s and 3 Lyfts. If the time that each takes to reach you is IID, what is the probability that all the Lyfts arrive first? What is the probability that all the UberX’s arrive first?
  - Lyfts arrive first: 2!*3!/5!
  - Ubers arrive first: same
#### 12. I write a program should print out all the numbers from 1 to 300, but prints out Fizz instead if the number is divisible by 3, Buzz instead if the number is divisible by 5, and FizzBuzz if the number is divisible by 3 and 5. What is the total number of numbers that is either Fizzed, Buzzed, or FizzBuzzed?
  - 100+60-20=140
#### 13. On a dating site, users can select 5 out of 24 adjectives to describe themselves. A match is declared between two users if they match on at least 4 adjectives. If Alice and Bob randomly pick adjectives, what is the probability that they form a match?
  - 24C5*(1+5(24-5))/24C5*24C5 = 4/1771
#### 14. A lazy high school senior types up application and envelopes to n different colleges, but puts the applications randomly into the envelopes. What is the expected number of applications that went to the right college?
  - 1
#### 15. Let’s say you have a very tall father. On average, what would you expect the height of his son to be? Taller, equal, or shorter? What if you had a very short father?
  - Shorter. Regression to the mean
#### 16. What’s the expected number of coin flips until you get two heads in a row? What’s the expected number of coin flips until you get two tails in a row?
#### 17. Let’s say we play a game where I keep flipping a coin until I get heads. If the first time I get heads is on the nth coin, then I pay you 2n-1 dollars. How much would you pay me to play this game?
  - less than $3
#### 18. You have two coins, one of which is fair and comes up heads with a probability 1/2, and the other which is biased and comes up heads with probability 3/4. You randomly pick coin and flip it twice, and get heads both times. What is the probability that you picked the fair coin?
  - 4/13
#### 19. You have a 0.1% chance of picking up a coin with both heads, and a 99.9% chance that you pick up a fair coin. You flip your coin and it comes up heads 10 times. What’s the chance that you picked up the fair coin, given the information that you observed?
  * Events: F = "picked a fair coin", T = "10 heads in a row"
  * (1) P(F|T) = P(T|F)P(F)/P(T) (Bayes formula)
  * (2) P(T) = P(T|F)P(F) + P(T|¬F)P(¬F) (total probabilities formula)
  * Injecting (2) in (1): P(F|T) = P(T|F)P(F)/(P(T|F)P(F) + P(T|¬F)P(¬F)) = 1 / (1 + P(T|¬F)P(¬F)/(P(T|F)P(F)))
  * Numerically: 1/(1 + 0.001 * 2^10 /0.999).
  * With 2^10 ≈ 1000 and 0.999 ≈ 1 this simplifies to 1/2
#### 20. What is a P-Value ?
  * The probability to obtain a similar or more extreme result than observed when the null hypothesis is assumed.
  * ⇒ If the p-value is small, the null hypothesis is unlikely
