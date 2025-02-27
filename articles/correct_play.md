# Fast Find the Correct Play

## How to evaluate cards

I have already talked in length to justify my method of evaluating an individual card and why it has it's merits. I will not pressupose you already know it, but I will be more "direct" in here and just say it how it is. For justifications on why I think like this you can check out other resources.

### Philosophy behind indivual card evaluation
When evaluating a whole set of plays, like going CnC into tunic Pummel, or going Surging Strike, Gustwave Kodachi Fluster Fist, I propose that **you can always break it down into individual cards, sum their values and get to the final answer, no matter if they interact with each other.**

This means, then, that knowing how to evaluate single cards is the "building block" for evaluating a sequence of plays. As an example:

Whleming Gustwave Red has only two instances it can be while on the chain: either its combo is **on** or **off.** If it's off, then it is 1 below rate, as you get 2 value out of it and 1 value out of your action point while you should **always get 3 value out of using a card,** be it on block, pitch or play, if possible.

Now I will also say: most red or blue cards in FAB have a dimension in which it gets 3 value, the dimensions being: on block, on pitch or on play.

Coming back to Gustwave then, it is either 1 below value on play (in short **-1,** in which case, blocking with it is worth 1 more) or it is worth 1 above rate with an on hit that is worth between 0 and 3 (convince yourself of this by looking at the fact that it attacks for 4, doesn't cost you your Action Point and has an on hit to draw a card).

*That's it.* Those are the only two modes it can be. Now, deciding whether or not to play, block or pitch with a red Gustwave comes down to knowing if it's going to be off or on. Most of the time this is trivial to know, but it can sometimes be left to chance, say in the case you cast an Art of War hoping to draw a new card, or depend on Surging Strike hitting in order to get the Whelming in the first place. In those cases, that **does not** change the value of Whelming Gustwave. It does, however, make it so you don't know at the point of decision (to block with it or not) if you will indeed use it as a 1 above rate card.

Sometimes you will have to do below rate interactions in order to rake in above rate value. In those cases, looking at the aggregate (e.g. the sequence of plays ended up being on rate) "hides" information from you, whereas looking at the individual plays will let you know exactly what's the good and bad part of your plays.

### The axioms of the Head Jab system
I will now say, succintly, what I believe is true and how to evaluate cards the way I do. The rest of this article is going to be examples of how to count the way I do.

1. Using 1 Action Point (AP) is worth 1 value. You should detract this out of cards that use it. Another way to think of it is that 1 of the value coming out of your card isn't coming from it, it's from the fact that the card is consuming your AP.
2. 1 Resource is worth 1 value. This means that pitching a red card for 1 means you used the whole card as 1 value. Ending your turn with a floating resources should subtract 1 value from the card you pitched.
3. 1 Block is worth 1 value.

For point number 1, I also like to think of it as: cards that have Go Again written on them are the norm. Cards that **DON'T** have Go Again written have a specific clause on them that reads *"As an additional cost to play this, pay 1 AP to get +1 value"* and their text is dimished by 1. In that sense, Wounding Blow Red attacks for 3 and has the AP clause written on it to get +1 damage. The **source** of that 1 damage is, thus, the AP, not Wounding Blow itself, in a way.

Out of these "commendments" a lot of things come out. For example, the fact that most cards are worth 3 value on one or more dimensions. A Blue block 3 can be often used as 3 value on pitch and 3 value on block, but not 3 value on play (most of the time). We will get into more implications, but first, let me say this:

If you consistently produce less than 13 value (damage threatened + blocked, basically) out of your turn cycles, then your deck is, simply, **trash.** But why?

#### The worst FAB deck
Think of the hand: **Wounding Blow Red, Raging Onslaught Blue, Head Jab Red and Raging Onslaught Red.**

Acronyms:

**Wounding Blow Red = WB R**

**Raging Onslaught Red = RO R**

**Head Jab = HJ**

These are all play sequences of this hand that produce 13 value:
* Block with **WB**, Play **HJ** pitch **RO B** to play **RO R.**
* Block with both **ROs**, play **HJ** play **WB**.

Anything other than doing this means you will get less than 13 value.

How can I arrive at that quickly? Let's do it together through individual card evaluation.

**Head Jab R** is only worth 3 value on play. If you block or pitch it, you will be getting less value than playing it.

**Wounding Blow R** is worth 3 on play and on block. Why 3? Because 1 of it's value comes from the Action Point required to play it.

**Raging Onslaught R** is worth 3 on play and 3 on block too. Why? It costs 3 more than WB and produces 3 more value. Remember it still should subtract 1 from the AP needed to play it.

**Raging Onslaught B** is worth 3 on block and on pitch. When you convert 3 resources into 3 damage, that value should be associated to the pitch card, not the played card.

Thus, whatever line you take to maximize value it **definitely** involves playing the Head Jab. Thus, this is a non-decision. You will NOT block with the Head Jab (more on this later).

Now you can choose to play either the **RO** or the **WB.** However, to play the **RO** you will need to also keep the blue around. This means that they are "coupled." That is, you can *only* get 3 value out of **RO R** on play if you also pitch **RO B**.

Finally, the **WB** is the same on play and on block as established.

Now the decision is either play the **WB** or play the **RO,** since you only have 1 Action Point at your disposal and need to use it in order to "get" 1 value. Whichever you choose, you *need* to block with the other, and since **RO B** and **RO R** are coupled, if you block with one, you will have no use for the other and thus need to also block with it.

That's it. It's equivalent to play **WB** block with **ROs** and block with **WB** play **RO R** pitching **RO B.**

This then means that in order to decide which line to take, you should be looking not only at yourself but at your opponent. Did they attack for 7? Then you indeed need to choose to block 3 versus 6. It will be the same overall value either way, unless blocking more has an added value of stopping an on hit (that generates value) from happening.

#### All decks are the worst FAB deck plus or minus something
This is basically at the core of Head Jab theory. Cards can be stripped down to their primary parts and be compared to Head Jab plus or minus something. Why Head Jab specifically? Because that's what I landed on. Head Jab Red embodies the simplest card in FAB.

Let's evaluate Scar for a Scar Red. It has two modes: Head Jab +1 or WB on play. On block it's always 2 value. On play it's either worth 3 or 4. That's a good card.

Snatch Red is WB with an on hit. Of course it blocks worse, making it a less versatile card when drawn, forcing you to keep it on play much like a Head Jab Red, but, on play, you would **ALWAYS** rather play Snatch than play WB.

So, no matter how complex your deck is, do the exercise of thinking of the individual building blocks of value when playing a sequence of cards and you will start to find the play lines much, much quicker.

### Hands are "forced"
As in the example above, you are forced by the fact that you only have 1 AP to decide which "AP spender" to keep.

Blue block 3s (as there are many in the game) are special in the sense that they also are worth 3 value in two dimensions: pitch and block. This is the same as WB being worth 3 on play and block. However, just like how blocking an attack for 2 with a 3 block means your card was worth 2, pitching a blue and ending your turn with a floating resource means you used it as 2 value only.

This follows from the fact that 1 resource can be converted into 1 value by cards, and, thus, not converting it means you wasted 1 possible value you could've gotten.

If, on the example before this, Raging Onslaught Red was, instead, a Brutal Assault Red, what would happen?

Brutal Assault is on rate (costs 2 and an AP and is worth 3 by itself, which is why it attacks for 6), but the turn would be 1 below rate, because the blue pitched (the blue Raging Onslaught) would've been used as 1 card for 2. In that scenario, you could **only** get maximum value out of that hand if you blocked with both Brutal Assault and the Raging Onslaught Blue. *Your hand is forced if you want to maximize value.*

What becomes a lot harder and takes practice is doing this "coupling and decoupling" of cards fast. Searing Emberblade is 1 above rate (2 resources into 3 damage) if it's **on,** and on rate if it's **off.** Thus, any turn that wants to have it on will need a draconic card at the start. This already forces you: if you want to be 1 above rate, you will need to keep this other card and a blue. If the kept card is on rate, then we're good to go except if you end with a resource floating (in which case, you're back to being on rate in the sense that you went 1 above rate to use the blue as 1 below rate).

Using Fai's ability to get a Phoenix Flame back for 1 resource is a 1-for-1 conversion of resources into value. Thus, if you get it back for 0 resources, you were 1 above rate. Lava Burst is 1 above rate (it is WB +1), and Tiger Stripe Shuko sometimes gets 1 value by itself. This means that a hand that goes: Draconic Head Jab into Searing Emberblade pitching a blue into get back Phoenix Flame into Lava Burst is what?

Draconic Head Jab: **on rate**
Active Searing Emberblade: **+1**
Pay 1 for Phoenix Flame: **on rate**
Active Lava Burst: **+1**
Active Tiger Stripe Shuko: **+1**
End with 0 resources floating: **on rate**

Thus, without knowing the cards per se, if you just told me: "hey I had a turn where I was 3 above rate", I already know you are doing well. Being 3 above rate means you "got an extra card's worth of value" out of simply playing your turn. If your opponent is being on rate and you are 3 above rate, you will get to lethal much sooner than they will.

To make it clear what "being on rate" means, its quite simple: getting 3 value per card plus 1 from your AP. That is, on a normal turn, getting 13 value out of the turn cycle. If you simply do *on rate* every turn for the whole game, you are doing *well.* Use 13 as a benchmark, truly. It is enough to win a lot of games of CC.

### Blocking with a Head Jab. (aka. On Hits)

We just said that you should never block with a Head Jab Red. That is absolutely true, *if the game had no on hits.*

However, deciding play lines becomes easy again when you simply start to factor them into your blocking decisions, you will get "forced" hands again. For example, that same hand as before: **Wounding Blow Red, Raging Onslaught Blue, Head Jab Red and Raging Onslaught Red.**

If you are being attacked for 6 or more damage with no on hits, as we said, then it's simply a matter of "preference" to choose whether to block with **WB** or the **ROs** in terms of overall value. However, say you are being attacked by a card that attacks for 4 and says: "When this hits, deal 3 damage." In that case, blocking for 6, even though the second card is, technically, blocking only for 1, it is also making you take 3 less damage, and, thus, blocking for 4 total.

That is, if you block for 6, you will rake in 1 more value than you would if you blocked for 3 because of the fact you will take 1 less damage that way on that turn cycle.

In that sense, then, the only reason to block with a Head Jab is because it is effectively blocking for more than 2. And as long as there is an on hit for 1, then blocking for 2 will be effectively 3, and thus the same as playing a Head Jab.

Thankfully, as we'd rather play a game than a math equation, FAB is full of on hits, cards that are indeed very complex to value as a number. However, I'd argue that **1.** you can just try and do your best and **2.** having a rough estimate is a better way to go about it than acting based on more heuristic-based decisions.

## Evaluation tricks

This section is full of "tricks" to evaluate cards that look hard to evaluate. In the end it kinda looks like an algorithm, and the more cards you have in your "arsenal" of evaluated cards, the more you can reference them and easily expand it. I will simply say a bunch of tricks and then give some examples after.


### Separate on and off and don't aggregate
I am vehemently against saying that anything in this whole game is worth a fraction of value (except for extremely rare cases). A card that is either 3 or 4 depending on other things is just that. It's not "worth 3.5", as it will never deal that much damage or gain that much value, so don't even bother.

Scar for a Scar is +1 or on rate (when played, obviously). That's it.

### Some cards only show their true value after some time
An inertia token is worth however much it gets at the end of the opponent's turn. Sometimes it is somewhat "invisible" how much value it got, but in those cases what you should do is: imagine there was **no Inertia** and calculate the value of that. Now see what happened when you **do** have an Inertia and see how it would change the optimal value.

Sometimes the Inertia will only make it so the opponent plays out a Head Jab now instead of saving it for later. In that case, it was worth something more ephemeral, which is the opportunity cost of playing it now versus saving it for a 5-card turn later that could take that simple Head Jab and turn it into something else more valuable (like Art of War, for example).

Sometimes it will make the opponent pitch a blue and end with 1 resource floating, or even playing out the blue for 1 value. That's the value of your Inertia (1 or 2). You won't know until it actually happens, because sometimes the opponent already wouldn't want to keep an arsenal at the end of that turn.

Same can be said for Co

### Calculate blocks ASAP

As soon as you draw up, think of the actual optimal value line. In the example we've already used twice, it will definitely involve blocking with at least 1 card, otherwise you will keep a dead card (or have to arsenal it, more on that later, for now let's assume you can't arsenal it).

This means we can already "frontload" our decision process to "at some point, I will need to block for 3 or 6". This is independent of what's happening on the other side of the board. Thus, we can focus on our attention to deciding *when* to block, not if to block at all.

This trick of identifying what to block with before even being attacked makes you play *so* much faster it's crazy. But what happens if there are many cards that can block or be played for the same value?

Well, in that case, you just look at on hits. If a card is worth 3 on play and on block equally, as we said, then it is a matter of preference. Is an on hit coming your way? Then add that to the blocking decision: "if I block for 3 here I will be effectively blocking 2 but preventing an on hit for 2, which means I will be blocking 4 and that's more than I'll get by playing this card". *Boom,* decision made.

Sometimes the card you're debating on whether to block or play itself is worth 3 but it packs an on hit. On hits can't be added to the value of playing the card per se since - as we've seen - having on hits effectively "increase" the blocking value of the opponent sometimes. To see this, imagine you are attacking with a Command and Conquer and the maximum value of your opponent already involves blocking with 2 cards. In that case, Command and Conquer might as well have been Brutal Assault.

However, having the possibility of being greater than 3 value on play because of a possible on hit should increase your propensity to play the card based on what you expect the opponent's maximum value to be. That's why you might've heard that "breakpoints provide value". Truly, they don't, but the fact you're attacking for quantities hard to block profitably (aka attacking for 4 with an on hit for 2 will get 6 block out of the opponent) makes it so, no matter if they block with 0, 1 or 2 cards, you are getting your 6 value worth's anyway. What may end up happening, though, is that you "upgrade" a 2 block out of them into a 3 value block (say they block 3 + 2) in the sense that they prevented 6 damage with 2 cards anyway.

### Evaluating on hits and on hit threats

This idea of evaluating on hits and how much the threat of them can make the opponent "respect" you is a bit like the last paragraph highlighted. As long as you actively put a number to an on hit threatening you, you can easily get to a "forced" hand. Evaluating the other side, though, is a bit harder.

What I mean is: knowing how much you are forcing the opponent out of their highest value play by your own actions is extremely hard and involves probability. You might or might not force their hand into a lower value ceiling with an on hit, and it is almost impossible to know for certain. This is where heuristics come in, as well as a general knowledge of the opponent's "hand textures".

To continue on the same example: Command and Conquer is a Brutal Assault if their highest value play already involves blocking with 2 cards. However, it basically reads "on hit diminish opponent's value by 3", since a card is worth 3, and that is very strong. It might end up making them use a 3 value card as 2 or even 1 value, or force them out of a higher value play, effectively gaining you value that a Brutal Assault never could.

### Diminish the AP cost

The most common trap error in applying this whole framework I see is forgetting to diminsh 1 value from cards that use your AP. If you don't do this, then playing out a Head Jab seems like 3 value while playing out a Wounding Blow seems to be 4 value. That is *strictly not true,* because, as already said, cards that use your AP gain that 1 value extra precisely from the fact that it **costs** your AP to play it.

With this, it is very important to see your AP as a resource waiting to be claimed. Of course between casting a Head Jab and passing and a Wounding Blow and passing the latter will be better. That happens because you have found a way to use your AP, **the only free resource you gain every turn.**

### Calculating overall turn value

I personally look at cards as "+1", "on rate" or "-1". For example I see Searing Emberblade as +1, activating Fai as "on rate" or "+1", and so on. Then, I count how many +1s I'll get as well as if I'll end my turn with an AP left or a resource floating. Of course there is value attached to equipments too, so I'll account them aswell, and finally I just do 13 plus and cancel out any +1s from -1s.

A quick example on Azalea: Hand is 2 buffs, a 1 cost arrow and a Blue.

Since Death Dealer (DD) is effectively 1 resource for 1 card, it's a +2. However, I will end this turn with 1 resource floating as long as I don't draw a playable 1 cost card.

Okay, so this turn wants to block with no cards (even if I have tunic, convince yourself of that by thinking of how many resources will be floating anyway on end of turn) and every card is on rate (arrows are 1 resource, 1 AP and 1 card for 5, so that tracks).

Which means I'll have +2 from DD, -1 from a floating resource, thus, I will be +1 overall on the turn which, since it started as a 4 card turn, will be 14. If I did use the tunic, I would end up adding 1 value from the resource that came from tunic but would have 2 floating resources, which still means +1 overall. *Boom,* done, its going to be an 11 damage arrow that ends with me having an arsenal or a 14 damage arrow and I get no arsenal.

I wouldn't factor in on hits right now, because, as we've established, they might not hit or not be relevant, it's really up to the opponent to decide. I'm already above rate without relying on any on hits, which is where I want to be, and then **on hits are purely additional value.**

## How this differs from other frameworks

### Decoupling cards

The most common way to view cards I've seen from other players involves coupling cards together and assigning their value to the couple. As an example, Raging Onslaught + Blue + your AP is worth 7. This is obviously true, however, I feel like it just makes getting to the highest value line more time consuming for no apparent gain.

The idea of saying that your Blue was 3 and the Raging Onslaught 3 more while your AP got spent as 1 makes it easier - in my opinion - to arrive at the conclusion to block with the couple and send another on rate AP consumer.

### On hits don't add value

I see people valuing playing a Command and Conquer with higher priority than they should off of the fact that, if it works, you'll get a ton of value. This simply isn't a good enough metric for me. Pitching a card to play CnC and pass is, in my book, a -1 line, so I will always start off on that to then judge my opponent's deck and decide if it's worth being -1 for the possible upside of possibly diminishing their best play by 1 or more, making it on rate again.

At the point of decision of playing an attack with an on hit you can't know whether or not it will force "awkward blocks" or diminish the opponent's value, thus it's just unreasonable in my evaluation to attach it to the card's value. What you can do is say "this is on rate and, if it hits, 2 above rate". With that you can start to think "is my opponent likely to awkwardly block this?", "what kind of hands would this punish?" or "what kind of hands would punish me for playing it?". This last question is relevant whenever the card isn't on rate but can be above rate if it hits (as is the case with Command and Conquer).


## Playing Blue Cards

I want to dedicate a whole section to this with a focus mainly on new players. Seasoned FAB players already know, at least intuitively, how to roughly value a card. Blue block 3 cards are, generally, not on rate because, if they were to be, then they can achieve maximum value on all 3 dimensions (block, pitch and play). This is very, very hard to come by, and, thus, Blue block 3s require something very specific to be on rate. This might either be that you meet a specific condition (such as the new Chi cards), or the opponent is in a particular condition (no equipment left to block such as with Tear Asunder).

To calculate the value of playing a blue card, just do the same as you would normally. You will probably arrive at the conclusion that it is worse than playing a Red. This is why having your Blues blocking 3 is so important for most decks, because you don't have a way to sink them into a card while being on rate you can simply block with the excess.

## Evaluating effects constructively

The main key to start building a foundation for what complex paragraphs of effects are worth is thinking of them inside a reasonable context. Crouching Tiger is worth 0 by itself, but can reasonably be thought of as being worth 1 given there are many effects that buff it by 1. Yes, it's not worth 1, but it can be enabled to attack for 1.

Whenever possible, get a very simple card (commons and rares) and simply **assume** that they're on rate. Subtract whatever you already know about card evaluation (e.g. 1 resource should be getting 1 damage, AP should subtract 1, etc) and then "isolate" the effect you're trying to guess the value of in the equation. Assume the card is worth 3, and, thus, you get the value of the effect you're tring to find out about.

The more you do this, the bigger your "dictionary of FAB" is going to be and the more associations you can make, so that the next time you evaluate a new card, you already know its value because it relates to two different cards whose value you already know, albeit with slight modifications, generally speaking.