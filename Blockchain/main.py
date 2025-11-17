import key

# 1. Get information from the pass-off server
difficulty_parameter = 24
genesis_block_hash = "4aa5a8eaf07c08ace062516353c6b9485e299154c5f3cd4727e20ed7945cda1b"
quote = "The opposite of love is not hate, it's indifference. -- Elie Wiesel"

# generate block 1
# hash = H( H(previous_block) || nonce || quote)
# nonce, hash = key.hash_24(genesis_block_hash, quote, difficulty_parameter)
nonce = 1724979620
hash = "0000007078a2e235ca19cbcea0712a641b2b37bbd415118df7a6f4a852d1b4e9"

# generate block 2
quote = "We now come to the decisive step of mathematical abstraction: we forget about what the symbols stand for. ...[The mathematician] need not be idle; there are many operations which he may carry out with these symbols, without ever having to look at the things they stand for. -- Hermann Weyl, The Mathematical Way of Thinking"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 36_464_970
nonce = 505914239
hash = "0000006bb87cd7293f461c07d0344979629ef036e6a2ff186770ba1ff86da107"

# generate block 3
quote = "It's like a condom; I'd rather have it and not need it than need it and not have it. -- some chick in Alien vs. Predator, when asked why she always carries a gun"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 10_558_390
nonce = 328838608
hash = "0000001abfb678d90d53b2a7ffdd36799af0b3a909514b93e803907a61774921"

# generate block 4
quote = "Wear your best for your execution and stand dignified. Your last recourse against randomness is how you act if you can't control outcomes, you can control the elegance of your behaviour. You will always have the last word. -- Nassim Taleb"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 14_880_094
nonce = 33730371
hash = "0000002b1a3ba71e65023c9d35880682bb59c0dd3d93c809ce5c5229a12e35f9"

# generate block 5
quote = "A society that puts equality -- in the sense of equality of outcome -- ahead of freedom will end up with neither equality nor freedom. The use of force to achieve equality will destroy freedom, and the force, introduced for good purposes, will end up in the hands of people who use it to promote their own interests. -- Milton Friedman (Thomas Sowell: A Conflict of Visions, p130)"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 7_207_927
nonce =  1869208573
hash = "000000225447bb9a740825dd4b13c9fd92547aff7a8a4f911873c4bc6f1d561d"

# generate block 6
quote = "It's easier to ask forgiveness than it is to get permission. -- Rear Admiral Dr. Grace Hopper"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
nonce = 782989665
hash = "00000065967d91e0abb96fa3fc4a7b22f07badbabbee30652ed4d5c0ca1da0f1"

# generate block 7
quote = "If there is a will, there is a way. -- unknown"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 26_034_528
nonce = 1799677666
hash = "00000005d9645298a8dfbbd4560a1ebb190bfb1647a679c03fa21bb5b359ff43"

# generate block 8
quote = "If I tell you I'm good, you would probably think I'm boasting. If I tell you I'm no good, you know I'm lying. -- Bruce Lee"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 12986806
nonce = 996977345
hash = "00000095a5a2f6f3c9ba7cc08770c9fa9ca97ed1e4f5d66a05ab2ebb7192c3f8"

# generate block 9
quote = "You have to write for your audience. I would never write (1..5).map &'*2' in Java when I could write ListFactoryFactory.getListFactoryFromResource( new ResourceName('com.javax.magnitudes.integers'). setLowerBound(1).setUpperBound(5).setStep(1).applyFunctor( new Functor () { public void eval (x) { return x * 2; } })) I'm simplifying, of course, I've left out the security and logging wrappers. -- Reginald Braithwait"
# nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 11_208_349
nonce = 1957704774
hash = "000000a718e862154df80fd4ba409860eb9a89df51217ee207388690d23a0444"

# generate block 10
quote = "Software is like sex: It's better when it's free. -- Linus Torvalds"
nonce, hash = key.hash_24(hash, quote, difficulty_parameter)
# counter = 5_322_719
nonce = 1194625318
hash = "000000570a3b7470e1db7d451f81deabd30c510a8cebe0e09b3650e8b6b382b4"