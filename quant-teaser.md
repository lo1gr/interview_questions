## Statistical Inference (15 questions)

#### 1. Is 1343 a prime number?
maybe combination of 2 primes?
100*10
  17
  49
   3

<a href="https://www.codecogs.com/eqnedit.php?latex=\sum&space;67&plus;88999" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\sum&space;67&plus;88999" title="\sum 67+88999" /></a>


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
10 choose 3 = 120 and can assign A to the lowest every time.


#### 5. 89^2?
  89
  89
=7921

#### 6. You have a deck of 52 cards. What’s the probability you draw exactly 1 heart in 2 draws with replacement?
2*(3/4*1/4)


#### 7. Solve x^x^x^… = 2
pattern. x^(x^x^x^x...) = 2
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
Not 24!
how long does it take for them to cross?, intuitively a bit more than 1h.
M = min hand    H = hour hand
minute: 1 lap in T=1h
hour: 1/12 lap in T=1h
start both at 12. when min has done 1 rotation (1h),  h has done 1/12 of rotation.
when H moves 5 min (takes him 60/5 = 12min), M moves T

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
