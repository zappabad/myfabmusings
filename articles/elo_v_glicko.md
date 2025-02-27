# Elo vs. Glicko in Flesh and Blood

It is not a secret that the Elo system in Flesh and Blood has been subject of many discussions by the community. This article is an attempt to lay out an explanation of both Elo and Glicko in a less mathematical way (mainly because I don't feel *that* confident in making statements about it myself, even though I am a mathematician), but -- if I do my job right -- in an accurate manner.

Before I begin, I want to openly say: I believe FaB should use the Glicko rating system instead of the current Elo based system for ranking. I will also say I like to, sometimes, endulge in a little bit of humor in my text, so humour me.

Okay, let's get into it.


## Are we League of Legends now?

Rating players in a "best to worst" list (or, as it is commonly known in online communities, a *ladder*) is extremely common in competitive games. It can be a source of great pride to know that you are an "eighteen fifty" player, whatever that means.

It can also be motivating to see you were once a lowly "silver" player (again, whatever that means) and now -- every time you boot up the "XBOX three-fitty" you see your name -- in ALL CAPS with a shinier than shiny MONSTROUS logo, you read: **MF_D00MZ0R - PLATINUM.** *Damn,* we actually made it, team.

And... it can also be infuriating to see you're a "wood-ranked" player when your friends -- who are all *MUCH* worse at the game than you, as we all know -- are living the dream being BRONZE chads.

Everyone who has played a competitive online game knows about that feeling. But, hey, at least that stuff is locked away in the land of the no-filter mic-breathing hack-having angry-typing ctrl-c-ctrl-v-spammer online gaming community, right? ... Right?? Oh...


### Everything is rated

I like placing things in an ordered list. Yes, yes... it is a personal hobby of mine, but I would also argue that it is extremely useful for making good matches.

First of all, reasonable rating systems like the ones used in all modern games (and chess) are good at actually predicting the outcome of a match given the participants. I do have some nostalgia for the days where we all just entered the *NO RUSH 20MIN* lobby only to go ahead and rush the unsuspecting victim, feeling good about my win; but that can't last forever.

Now, more than ever, gaming is a hobby in which people pick up to have fun. Winning is not the only fun to be had, as I'm sure you can remember that one match you lost by a razor's edge and had a blast. **Matchmaking systems come in to help you have that game over and over again.**

The idea of matchmaking system is to pair closely-skilled players against each other. To do so, there needs to be a metric of skill, and that's the job of a rating system: to assign a number to the skill of every participant in the system in relation to each other.


## Does FAB need a rating system?

I **LOVE** this article by Richard Garfield on [why even have a rating system in your game.](https://www.gamedeveloper.com/game-platforms/keep-your-numbers-off-of-me-why-tournaments-support-better-communities-than-ladders) The article questions modernity in a way, arguing that matchmaking systems are not the end-all be-all for fostering competitive gaming communities, and it actually just made me a smarter person for reading it, period.

I would say Flesh and Blood already has a "rating" system in the form of the Organized Play Path. It doesn't involve Elo in any way, but making "funnels" of players is a way to "tierize" players according to skill. You get into Nationals by being one of the best in the open field of RTNs. You get to the Pro Tour by being the best in the open field of Pro Quests or doing well at your Nationals. And that's kinda where it stops.

Now, I'm not arguing for more ladders to climb on before you get to the prestigious tournaments, although I think there *could* be merits to it. I'm simply not sure about the cons to have an opinion.

What I just said about the path to get to the top tier tournaments is trumped by Elo, though. LSS just announced there will be no more invites by XP to top tier tournaments, being replaced by Elo only invites. Again, I won't get into the merits of that, I will simply roll with it.


## So who's Elo and why do they hate Glicko?

I will give a brief introduction to both systems, but I **strongly** encourage you to read [these](https://www.englishchess.org.uk/wp-content/uploads/2012/04/Elo_vs_Glicko.pdf) [articles](https://medium.com/@osmanelsoz/dota-2-new-ranking-system-elo-rating-vs-glicko-rating-f1c84c0109ef) if you want to delve deeper on the merits of both systems.


### The Elo rating system

Elo as a system hinges on the idea that the skill of a population of players could be measured as a random variable. What exactly does that mean?

Imagine you have a population of 100 players of a newly-made game. These 100 players start playing each other, and after many of these matches we want to bet on how two specific players, Alice and Bob, would fare against each other, even though they never did so before. We want to predict who's more likely to win their match.

Out of these 100 players, some of them will have extremely high winrates, some extremely bad winrates, and most of them will sit somewhere around these margins. If we could plot the amount of players with a given record after many of these matches have been played, we would end up with a bell shaped distribution.

Our two players would have an overall record too. Alice won 60 out of their 100 matches played, while Bob won 55. Elo provides a way of predicting the chance of Alice winning against Bob by looking not only at their overall record, but all the opponents they played.

Let's introduce a third person, Cathy, who's just a *monster* at this game. She won 98 out of 100 matches played. Of those two losses, one of them way to Bob. Meanwhile, Alice played some of the worse performing players and lost to them. I think you can agree there is more merit to winning against Cathy than to an average person. Well, Elo would agree too.

The Elo rating of two players with the same overall record can be different depending on who they've played. That's the whole idea of Elo. When you sit down for a match, Elo has already assigned a number representing the skill of you and your opponent. If your opponent is higher rated than you -- given a large enough sample size -- then Elo would believe they are more likely to win this match you're about to play.

It then will assign points that "balance out" this match. For example, if Elo believes your opponent is 80% likely to win against you because of the difference in rating between both of you, then, if your opponent **actually wins** against you, that was an expected outcome, thus they will win fewer points and you will lose fewer points. That's the way Elo basically says *"hey, I'm sorry I let you play this guy who is much better than you,"* you don't suffer that hard of a loss.

If you manage to win, though, then you've "beaten the odds" and get rewarded with a lot more points, while your opponent also suffers greatly for losing a match they were heavily favored in.

Over time, this population of 100 players would converge to their "real skill level." What that means is: suppose there is an actual "best to worst" scale for the 100 players in terms of their overall ranking against each other. Each player has a "true skill" number associated with them, and, given enough matches, each player would have an Elo rating that would closely replicate that best to worst scale. In that sense, Elo truly is a system that ranks players.


### Glicko enters the chat...

Glicko shares the same assumption as Elo, and also reaches the same conclusion as Elo. Afterall, Glicko was invented using Elo as an inspiration. What changes from Elo to Glicko is the addition of a few other hypothesis that make it a better system.

In Glicko, not only does a player's rating get updated after each match, but also another variable called **RD.** The Rating Deviation is another positive number that is basically a concession to small sample sizes. RD says *"look, I'm not too sure if your true skill is more close to that of a 1800 rated player or a 1900 player, so I'll just say I'm not too confident in either."*

That means that, at each point in time, Glicko has a number that shows how unsure of your current rating it is. In Elo, when you beat one of the best players in the world, it will change how much that win increases your rating in a more conservative manner, while Glicko might give you more rating, while still being unsure that you really are one of the best by keeping your RD high until more data comes in.

That's all, really.

There is also an incentive in Glicko to keep playing in order to decrease your RD. Being inactive increases the uncertainty (RD) that Glicko has on your current rating the more time you spend not playing, while disincentivizes you from "sitting on your Elo," a common complaint I've read about using Elo as invites for FAB.


### Where's the catch?

The catch mainly comes from the fact that Glicko contains more complex calculations in order to determine rating and RD than Elo does. Elo can be easily tabulated to see how much you would win or lose against a given opponent, while Glicko has to take into account RD as another variable to determine points won or lost.

That means Glicko needs an actual computer to carry out the updates to ratings after each tournament. *A real downside, really... who has computers in this day and age?*


## But FAB isn't chess

Flesh and Blood (and many other games) have specifications unlike chess does, which makes it so any rating system has more uncertainty to it.

In the Elo system, when an 1800 player plays a 1400 player, they have an *almost 91% win percentage chance.* Both Elo and Glicko have a way higher predictive power in a game with zero variance like chess than it does for a game like FAB. A player who just started, playing the one of the top rated players indeed has little to no chance. However, for higher ratings, variance starts to take hold in a way that any "copy and paste" system can't account for.

If I'm playing against Michael "Michael Hamilton" Hamilton and he's on Bravo, not packing any AB god bless his soul, and I'm on Kano, it just **can't** be the same chance I win the game than if we were both playing a mirror (like every match of chess really is). These "outside the table" decisions you make *before* you sit down and play have no parallel in Elo or Glicko, and they surely influence the win percentage of each player in a game like FAB.

This means that rating systems in a game like FAB are *inherently* less reliable than in a game with no variance. That's not the end of the world, though, and we should certainly not throw any sort of rating system out of the window.

The saving grace here is "the long haul." Over a long period of time, these match up inherent advantages and disadvantages will even themselves out. If I play a "high rolly" hero, yes I'll win against better players, but I'll also lose to worse players. Meanwhile, Hamilton is ticking up his tunic and taking names left, right and -- merhaps -- center.

What that means is that, at any point in time, my rating is indeed not correct, but that is accounted by Glicko in a way that Elo doesn't account for. There are some variables that can influence how RD should change over time, and one can simply set that parameter to be higher than it would be in a less variance prone game. It's all just weight tuning. It is a more transparent system in how it communicates to the player that it's not sure how good at the game you actually are, even though you have a rating.


## So do we really need a rating system part 2

The rating system for FAB is really only used to secure invites to premiere tournaments as of now. Personally, I just don't think there's any service to the game done by having it be an entry ticket.

The only thing it does is reward players that are indeed good at the game but didn't get a chance to qualify for the tournaments in a given season. Why do we even need that? With events becoming more and more available as the Organized Play grows, I say: if you didn't qualify, you shouldn't go... At least that's what I believe if we continue to use Elo.

To give LSS the benefit of the doubt, I'm sure they have looked at the list of qualified players and matched it to the Elo leaderboards to see how many of these contestants *wouldn't* attend the PT if it weren't for Elo invites and ended up deciding it's a good thing to keep it.

To try and probe LSS's mind, they probably also see Elo as a "league badge" much like the huge DIAMOND LEAGUE displays in online games, seeing it as something that inspires players to get improve at the game. I'm just not sure it achieves that goal as much as they imagined or wanted it to, and that's just the fault of expectations, not of anyone (be it LSS or the community) themselves.

I see what LSS is doing for the Deathmatch leaderboards during HVY season as an attempt to fiddle with different rating systems. It is akin to leaderboards or world records for specific speedrun categories, and I just love it. I think the spirit of the leaderboards is awesome, and accounts for the whole "I'll just play the most reliable or the most high rolly hero and rack in wins" since there are multiple brackets for different heroes.

We should look at that attempt with a critical mind but an open heart. They are listening and looking into solutions, experimenting on a smaller scale to, hopefully, learn something and find a place where rating players actually make sense.


## Elo vs. Glicko Simulation

Okay, time to get into the weeds. I promised no math but I lied. Get over it.

I made some simulations on how long a player of "true skill" X would take to within a 10 point margin difference to their rating both in Elo and Glicko. **The results will shock you!!**

To be more precise. I "created" a player that has 1500 rating (the starting rating for both Elo and Glicko), but, when calculating the chance to win a match against another player, I used their "true skill" rating. As an example: a 2000 true-skill player would win against a 1600 player 91% of the time. However, for dishing out the points, I assumed both players were actually 1600 (as the system might think they are).

This is useful for calculating how many events a population needs to, roughly, get into their true rating. It's useful for Japan, for example, who already had great players but no OP events to award them with Elo, which means that even if they had world-class players, they simply weren't at their true rating because they didn't have a chance to prove it yet.

So, I just did that 2500 times **for each true-skill rating between 1200 and 2300.** To choose the opponents for each player, I just picked an opponent that was always within 100 rating points of their *current* rating. This means that our Hero player, true-skill of 2000 or whatever, while at 1700 Elo, fought opponents that were between 1650 and 1750 and gained points accordingly. Their true-skill was only considered in order to calculate the chance he actually won those matches. This is an optimist scenario, as for new regions, chances are good players will, eventually, face against much lower rated opponents, meaning they'd take more time to reach their full true rating as they would win less points and lose more.

I then just took the geometric mean of how many games it took to reach the 10 point margin of their true skill, and plotted the Elo and Glicko numbers. Here they are:

![Elo vs. Glicko True-skill Convergence](elovglicko.png "Glicko converges faster than Elo")

Shocking, right? Glicko takes almost half the time to get players settled within their true rating as Elo does. Ignore the range close to the starting rating of 1500. That's just because Glicko is indeed more volatile and will take some matches to narrow down your RD, and this makes it harder to get into the specific "10 point margin" I just decided upon.

I suppose Elo is okay when you don't care about making it big THIS year, like they are in chess and Go. In those games, progress *actually* takes way more than a full season to happen. A 1800 chess player doesn't get to 2200 in a year, so it's as if Elo's "RD equivalent" from Glicko was a low enough number to model the fact that progress takes a lot of matches and time to come through.**But that ain't true for FAB.** We have prodigies all over the place, but Elo won't let them shine until next year when they actually play enough matches to appear on the leaderboards.


## What I propose

Given the above example, I believe there is a sizeable improvement both for older regions (who would feel little to no difference) and new regions (who would be able to prove their worth more easily than playing "catch up" for 3 seasons) by changing Elo for Glicko.

**Tierize more.** I would try to experiment with one more tier between open entry and the Pro Tour, this way we have more events on the calendar and still do the "ranking" of players to get them all the way to the Pro Tour. Make PQs more scarce, but give more slots to the PT to them instead of being winner takes all like it currently is (maybe I'm proposing this because I lost a PQ finals? Who knows!).

**Use rating a "stepping stone" reward.** Instead of directly inviting players to the premiere events for achieving a big rating, do what MtG already did for Hall of Famers in the past. Give them byes on qualifiying events. Building on the "more tiers" example I gave above, have qualifying (maybe open entry) events and reward the highest rated players of a given region by letting them start with two byes, effectively entering the tournament 2-0.

I believe this makes sense given the variance point I made before in this article. A person who got 1900 rating at some point might just not be a 1900 player now that their deck got LL, so while it makes sense to reward them with *something,* I still believe they need to prove themselves. I mean, if they indeed are such a high rated player, they should have no trouble plowing through a bunch of *noobs* and securing their invite that way, no?

Also, I guess I didn't talk about this before, but *it's just not a thing* to say that an 1800 player in region A is the same skill of an 1800 player in region B **if** their region doesn't frequently play together. Rating is a measure of a population that plays against each other frequently and loses meaning when talking about two segregated regions. I say this to support my claim that inviting "top 50 rating in the world" being just too weird to me. If they want to promote diversity, have a top X in each region, and if they want to promote actual skill, looking at rating ain't gonna do it for different regions that just got the game until they've had enough matches and have mixed with the global population for a long enough time.


## To conclude...

I like rating systems. I think they serve a nice purpose for FAB in the fact that -- repeating myself -- given enough matches, they truly show who is more skilled in a way that looking *just* at tournament results doesn't. **It's a number that embodies consistency, good deck choices and performance over the long run.**

What I *don't* like is how the current rating system works. Both in how it's outclassed by more sophisticated systems like Glicko and how it tries to assert itself as a source of meaning in a game with much more variance and faster progress rate like FAB is when compared to chess. I don't like how Elo, currently, incentivizes top players to just "sit it out," waiting in their piles of early season success until the general population plays catch up enough to threaten them in a *much* harsher field than they once had when they conquered their rating.

Yes, this latter problem *will* sort itself out given enough time, but it jeopardizes the competitive spirit that exists in FAB and one of it's mottos: *play the game, see the world.*

There needs to be a compromise of long-term solutions (a better fitted purpose for rating leaderboards) and patches (as Glicko could be) and a more active hand from LSS to not hand over the solutions to "give it enough time." I believe we are already heading that way with some measures from LSS, and I would love to hear what *you* think could be done better. Conversation and understanding is the fastest way to get to satisfactory solutions, so, **let's get there!**