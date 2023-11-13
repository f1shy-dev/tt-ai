import tiktoken

speech = """
0:00:00> (dramatic music) - Joe Rogan, one pass, check it out.
0:00:04> - The Joe Rogan, experience.
0:00:06> - Train by day, Joe Rogan, podcast by night, all day.
0:00:09> (upbeat music) - All right, Sam, what's happening? - Not much, how many? - Thanks for coming in here, appreciate it.
0:00:16> - Thanks for having me.
0:00:17> - So, what have you done? (laughs) - Like ever? - No, I mean, what have you done with AI? I mean, it's one of things about this is, I mean, I think everyone is fascinated by it.
0:00:32> I mean, everyone is absolutely blown away at the current capability and wondering what the potential for the future is and whether or not that's a good thing.
0:00:42> - I think it's gonna be a great thing, but I think it's not gonna be all a great thing.
0:00:49> And that is where, I think that's where all of the complexity comes in for people.
0:00:56> It's not this like clean story of we're gonna do this and it's all gonna be great.
0:01:00> It's we're gonna do this, it's gonna be net great, but it's gonna be like a technological revolution.
0:01:05> It's gonna be a societal revolution.
0:01:07> And those always come with change.
0:01:10> And even if it's like net wonderful, there's things we're gonna lose along the way, some kinds of jobs, some parts of our way of life, some parts of the way we live are gonna change, or go away.
0:01:20> And no matter how tremendous the upside is there, and I believe it will be tremendously good, there's a lot of stuff we gotta navigate through to make sure.
0:01:29> That's a complicated thing for anyone to wrap their heads around, and there's deep and super understandable emotions around that.
0:01:39> - That's a very honest answer.
0:01:41> That it's not all gonna be good.
0:01:44> But it seems inevitable at this point.
0:01:47> - Yeah, I mean, it's definitely inevitable.
0:01:50> My view of the world, you're like a kid in school, you learn about this technological revolution, and then that one, and then that one.
0:01:57> And my view of the world now, sort of looking backwards and forwards, is that this is like one long technological revolution.
0:02:04> And we had, sure, like first we had to figure out agriculture so that we had the resources and time to figure out how to build machines, then we got this industrial revolution, and that made us learn about a lot of stuff, a lot of other scientific discovery too, let us do the computer revolution, and that's now letting us, as we scale up to these massive systems, do the AI revolution.
0:02:24> But it really is just one long story of humans discovering science and technology and co-evolving with it.
0:02:31> And I think it's the most exciting story of all time.
0:02:34> I think it's how we get to this world of abundance.
0:02:36> And although we do have these things to navigate, and there will be these downsides, if you think about what it means for the world, and for people's quality of lives, if we can get to a world where the cost of intelligence and the abundance that comes with that, the cost dramatically falls, the abundance goes way up.
0:03:00> I think we'll do the same thing with energy.
0:03:01> And I think those are the two sort of key inputs to everything else we want.
0:03:05> So if we can have abundant and cheap energy and intelligence, that will transform people's lives largely for the better.
0:03:11> And I think it's gonna, in the same way that if we could go back now 500 years and look at someone's life, we'd say, "Well, there's some great things, "but they didn't have this, they didn't have that.
0:03:20> "Can you believe they didn't have modern medicine?" That's what people are gonna look back at us like, but in 50 years.
0:03:26> - When you think about the people that currently rely on jobs that AI will replace, when you think about whether it's truck drivers or automation workers, people that work in factory assembly lines, what, if anything, what strategies can be put to mitigate the negative downsides of those jobs being eliminated by AI? - So, I'll talk about some general thoughts, but I find making very specific predictions difficult because the way the technology goes has been so different than even my own intuitions, or certainly my own intuitions.
0:04:08> - Maybe we should stop there and back up a little.
0:04:11> What were your initial thoughts? - If you had asked me 10 years ago, I would have said first AI is gonna come for blue collar labor, basically.
0:04:22> It's gonna drive trucks and do factory work, and it'll handle heavy machinery.
0:04:27> Then maybe after that, it'll do some kinds of cognitive labor, but not, it won't be off doing what I think of personally as the really hard stuff.
0:04:38> It won't be off proving new mathematical theorems, won't be off discovering new science, won't be off writing code.
0:04:46> And then eventually, maybe, but maybe last of all, maybe never because human creativity is this magic special thing, last of all, it'll come for the creative jobs.
0:04:57> That's what I would have said.
0:04:59> Now, A, it looks to me like, and for a while, AI is much better doing tasks than doing jobs.
0:05:06> It can do these little pieces super well, but sometimes it goes off the rails.
0:05:11> It can't keep like very long coherence.
0:05:13> So people are instead just able to do their existing jobs way more productively, but you really still need the human there today.
0:05:21> And then B, it's going exactly the other direction.
0:05:23> You could do the creative work first, stuff like Cody in Second, or they can do things like other kinds of cognitive labor, Third, and we're the furthest away from my humanoid robots.
0:05:33> - So back to the initial question.
0:05:39> If we do have something that completely eliminates a factor workers, completely eliminates truck drivers, delivery drivers, things on those lines, that creates this massive vacuum in our society.
0:05:55> - So I think there's things that we're gonna do that are good to do, but not sufficient.
0:06:03> So I think at some point, we will do something like a UBI or some other kind of like very long term unemployment insurance something, but we'll have some way of giving people, like redistributing money in society as a cushion for people, as people figure out the new jobs.
0:06:20> But, and maybe I should touch on that.
0:06:23> I'm not a believer at all that there won't be lots of new jobs.
0:06:27> I think human creativity, desire for status, wanting different ways to compete, invent new things, feel part of a community, feel valued.
0:06:37> That's not gonna go anywhere.
0:06:39> People have worried about that forever.
0:06:41> What happens is we get better tools and we just invent new things and more amazing things to do.
0:06:47> And there's a big universe out there.
0:06:48> And I think, I mean that like literally that there's like space is really big, but also there's just so much stuff we can all do if we do get to this world of abundant intelligence where you can sort of just think of a new idea and it gets created.
0:07:03> But, but again, that doesn't, to the point we started with that, that doesn't provide like great solace to people who are losing their jobs today.
0:07:16> So saying there's gonna be this great indefinite stuff in the future, people are like, what are we doing today? So, you know, I think we will as a society do things like UBI and other ways of redistribution.
0:07:28> But I don't think that gets at the core of what people want.
0:07:31> I think what people want is like agency, self-determination, the ability to play a role in architecting the future along with the rest of society, the ability to express themselves and create something meaningful to them.
0:07:46> And also I think a lot of people work jobs they hate and I think there's, we as a society are always a little bit confused about whether we wanna work more or work less.
0:07:57> But, but somehow that we all get to do something meaningful and we all get to play our role in driving the future forward, that's really important.
0:08:10> And what I hope is as those truck driving, long haul truck driving jobs go away, which, you know, people have been wrong about predicting how fast that's gonna happen, but it's gonna happen.
0:08:21> We figure out not just a way to solve the economic problem by like giving people the equivalent of money every month, but that there's a way that, and we've got a lot of ideas about this, there's a way that we like share ownership and decision making over the future.
0:08:40> I think I say a lot about AGIs that everyone realizes we're gonna have to share the benefits of that, but we also have to share like the decision making over it and access to the system itself.
0:08:54> Like I'd be more excited about a world where we say, rather than give everybody on Earth like one eight billionth of the AGI money, which we should do that to, we say, you get like one eight billionth of, a one eight billionth slice of the system.
0:09:09> You can sell it to somebody else, you can sell it to a company, you can pool it with other people, you can use it for whatever creative pursuit you want, you can use it to figure out how to start some new business.
0:09:18> And with that, you get sort of like a voting right over how this is all gonna be used.
0:09:25> And so the better the AGI gets, the more your little one eight billionth ownership is worth to you.
0:09:31> >> We were joking around the other day on the podcast where I was saying that what we need is an AI government.
0:09:37> >> What is that? >> AI president and have AI right now.
0:09:41> >> Just make all the decisions.
0:09:42> >> Yeah, I have something that's completely unbiased, absolutely rational, has the accumulated knowledge of the entire human history at its disposal, including all knowledge of psychology and psychological study, including UBI, 'cause that comes with a host of pitfalls and issues that people have with it.
0:10:04> >> So I'll say something there.
0:10:06> I think we're still very far away from a system that is capable enough and reliable enough that any of us would want that, but I'll tell you something I love about that.
0:10:17> Someday, let's say that thing gets built.
0:10:19> The fact that it can go around and talk to every person on earth, understand their exact preferences at a very deep level, how they think about this issue and that one and how they balance the trade-offs and what they want, and then understand all of that and collectively optimize for the collective preferences of humanity or of citizens of the US, that's awesome.
0:10:41> >> As long as it's not co-opted, right? Our government currently is co-opted.
0:10:47> >> That's for sure.
0:10:48> We know for sure that our government is heavily influenced by special interests.
0:10:52> If we could have an artificial intelligence government that has no influence, nothing has influence on it.
0:11:01> >> What a fascinating idea.
0:11:02> >> It's possible, and I think it might be the only way where you're gonna get completely objective the absolute most intelligent decision for virtually every problem, every dilemma that we face currently in society.
0:11:19> >> Would you truly be comfortable handing over like final decision-making and say, all right, AI, you got to fail? >> No, but I'm not comfortable doing that with anybody.
0:11:28> I mean, I don't, I was uncomfortable with the Patriot Act.
0:11:32> I'm uncomfortable with many decisions that are being made.
0:11:36> It's just there's so much obvious evidence that decisions that are being made are not being made in the best interests of the overall well of the people.
0:11:45> It's being made in the decisions of whatever gigantic corporations that have donated to and whatever the military industrial complex and pharmaceutical industrial complex.
0:11:57> And then just the money.
0:11:59> It's that's really what we know today, that the money has a massive influence on our society and the choices that get made and the overall good or bad for the population.
0:12:09> >> Yeah, I have no disagreements at all that the current system is super broken, not working for people super corrupt and for sure like unbelievably run by money.
0:12:20> >> Yeah.
0:12:21> >> And I think there is a way to do a better job than that with AI just in some way, but this might just be like a factor of sitting with the systems all day and watching all of the ways they fail, we got a long way to go.
0:12:37> >> A long way to go, I'm sure.
0:12:38> But when you think of AGI, when you think of the possible future, like where it goes to, do you ever extrapolate? Do you ever like sit and pause and say, well, if this becomes sentient and it has the ability to make better versions of yourself, how long before we're literally dealing with a God? >> So the way that I think about this is, it used to be that like AGI was this very binary moment, it was before and after.
0:13:10> And I think I was totally wrong about that.
0:13:12> And the right way to think about it is this continual move of intelligence, this smooth exponential curve, back all the way to that sort of smooth curve of technological revolution.
0:13:24> The amount of compute power we can put into the system, the scientific ideas about how to make it more efficient and smarter to give it the ability to do reasoning, to think about how to improve itself, that will all come.
0:13:40> But my model for a long time, I think if you look at the world of AGI thinkers, there's sort of two, particularly around the safety issues you're talking about, there's two axes that matter.
0:13:52> There's the short timelines or long timelines, to the first milestone of AGI, whatever that's gonna be, is that gonna happen in a few years, a few decades, maybe even longer, although at this point, I think most people are a few years or a few decades.
0:14:07> And then there's take-off speed.
0:14:08> Once we get there, from there to that point, you're talking about where it's capable of the rapid self-improvement, is that a slower, a fast process? The world that I think we're in, and also the world that I think is the most controllable and the safest, is the short timelines and slow take-off quadrant.
0:14:29> And I think we're gonna have, there were a lot of very smart people for a while where the thing you were just talking about happens in a day or three days.
0:14:40> And that doesn't seem likely to me given the shape of the technology, as we understand it now.
0:14:45> Now, even if that happens in a decade or three decades, it's still like the blink of an eye from a historical perspective, and there are gonna be some real challenges to getting that right.
0:14:59> And the decisions we make, the sort of safety systems and the checks that the world puts in place, how we think about global regulation or rules of the road from a safety perspective for those projects, it's super important, 'cause you can imagine many things going horribly wrong.
0:15:18> But I feel cheerful about the progress the world is making towards taking this seriously.
0:15:26> And it reminds me of what I've read about the conversations that the world had around the development of nuclear weapons.
0:15:35> It seems to me that this is, at least in terms of public consciousness, this is emerged very rapidly, where I don't think anyone was really aware, people were aware of the concept of artificial intelligence, but they didn't think that it was gonna be implemented so comprehensively, so quickly.
0:15:56> So chat GPT is on what, 4.5 now? - Four.
0:16:00> - Four.
0:16:01> - And with 4.5, there'll be some sort of an exponential increase in its abilities.
0:16:06> - It'll be somewhat better.
0:16:08> Each step, from each half step like that, you kind of, humans have this ability to get used to any new technology so quickly.
0:16:18> The thing that I think was unusual about the launch of chat GPT 3.5 and then four, was that people hadn't really been paying attention.
0:16:27> And that's part of the reason we deploy.
0:16:29> We think it's very important that people and institutions have time to gradually understand this, react, co-design the society that we want with it.
0:16:38> And if you just build AGI in secret and a lab and then drop it on the world all at once, I think that's a really bad idea.
0:16:43> So we had been trying to talk to the world about this for a while.
0:16:48> People, if you don't give people something they can feel and use in their lives, they don't quite take it seriously, everybody's busy.
0:16:55> And so there was this big overhang from where the technology was to where public consciousness was.
0:17:00> Now, that's caught up, we've deployed.
0:17:03> I think people understand it.
0:17:05> I don't expect the jump from like four to whenever we finish 4.5, which be a little while.
0:17:11> I don't expect that to be the crazy, I think the crazy switch, the crazy adjustment that people have had to go through has mostly happened.
0:17:20> I think most people have gone from thinking that AGI was science fiction and very far off to something that is gonna happen.
0:17:27> And that was like a one-time reframe.
0:17:29> And now, every year you get a new iPhone.
0:17:32> Over the 15 years or whatever, since the launch, they've gotten dramatically better.
0:17:36> But iPhone to iPhone, you're like, yeah, okay, it's a little better.
0:17:39> But now if you go hold up the first iPhone to the 15 or whatever, that's a big difference.
0:17:43> GPT 3.5 to AGI, that'll be a big difference.
0:17:47> But along the way, it'll just get incrementally better.
0:17:49> - Do you think about the convergence of things like Neuralink and there's a few competing technologies where they're trying to implement some sort of, some sort of a connection between the human biological system and technology? - Do you want one of those things in your head? - I don't until everybody does.
0:18:14> And I have a joke about it.
0:18:16> But the idea is like once it gets, you have to kind of, because everybody's gonna have it.
0:18:22> So one of the hard questions about the merge, all of the related merge stuff is exactly what you just said.
0:18:30> Like as a society, are we gonna let some people merge with AGI and not others? And if we do, then, and you choose not to, like what does that mean for you? - Right, and will you be protected? - How you get that moment right, if we imagine all the way out to the sci-fi future, there'd been a lot of sci-fi books written about how you get that moment, right? Who gets to do that first? What about people who don't want to? How do you make sure the people that do it first, like actually help lift everybody up together? How do you make sure people who wanna just live their very human life get to do that? That stuff is really hard and honestly, so far off from my problems of the day that I don't get to think about that as much as I'd like to, 'cause I do think it's super interesting.
0:19:18> I, but yeah, it seems like if we just think logically, that's gonna be a huge challenge at some point and people are gonna want wildly diversion things, but there is a societal question about how we're gonna, like the questions of fairness that come there and what it means for the people who don't do it, super, super complicated.
0:19:49> Anyway, on the neural interface side, I'm in the short term, like before we figure out how to upload someone's conscience into a computer, if that's even possible at all, which I think there's plenty of sides you could take on why it's not.
0:20:04> The thing that I find myself most interested in is what we can do without drilling a hole in someone's head, how much of the inner monologue can we read out with an externally mounted device? And if we have a imperfect, low bandwidth, low accuracy neural interface, can people still just learn how to use it really well in a way that's quite powerful for what they can now do with a new computing platform? And my guess is we'll figure that out.
0:20:36> - I'm sure you've seen that headpiece, there's a demonstration where there's someone asking someone a question, they have this headpiece on, they think the question, and then they literally Google the question and get the answers through their head.
0:20:48> - That's the kind of thing we've been in.
0:20:50> That's the kind of direction we've been exploring.
0:20:51> - Yeah, that seems to me to be step one, that's the pong of the eventual immersive 3D video games.
0:21:00> Like you're going to get these first steps and they're gonna seem sort of crude and slow.
0:21:05> I mean, it's essentially slower than just asking Siri.
0:21:08> - I think if someone built a system where you could think words, doesn't have to be a question, it could just be your passive rambling in our monologue, but certainly could be a question.
0:21:21> And that was being fed into GPT-5 or six and in your field of vision, the words in response were being displayed, that would be the pong.
0:21:29> - Yeah.
0:21:30> - That's still soup, that's a very valuable tool to have.
0:21:33> - And that seems like that's inevitable.
0:21:35> - There's hard work to get there on the neural interface side, but I believe it will happen.
0:21:40> - Yeah.
0:21:41> - I think so too, and my concern is that the initial adopters of this will have such a massive advantage over the general population.
0:21:48> - Well, that doesn't concern me 'cause that's like, you know, that's just like better, that's a better computer.
0:21:56> You're not like jacking your brain into something in a high risk thing.
0:21:59> You know what you do when you don't want them when you take off the glasses.
0:22:03> So that feels fine.
0:22:05> - Well, this is just the external device then.
0:22:08> - Oh, I think we can do the kind of like, read your thoughts with an external device at some point.
0:22:13> Read your internal monologue.
0:22:15> - Interesting.
0:22:16> And do you think we'll be able to communicate with an external device as well, telepathically? - Or semi telepathically through technology? - I do, yeah, I do.
0:22:26> - I think so too.
0:22:27> My real concern is that once we take this step to use an actual neural interface, when there's an actual operation, and they're using some sort of an implant, and then that implant becomes more sophisticated.
0:22:45> It's not the iPhone one, now it's the iPhone 15.
0:22:48> And as these things get better and better, we're on the road to cyborgs.
0:22:54> We're on the road to like, why would you want to be a biological person? Do you really want to live in a fucking log cabin when you can be in the matrix? I mean, it seems like we're not, we're on this path.
0:23:07> - We're already a little bit down that path, right? Like if you take away someone's phone, and they have to go function in the world today, they're at a disadvantage relative to everybody else.
0:23:20> So that's like a, maybe that's like the lightest weight version of a merge we could imagine, but I think it's worth like, if we go back to that earlier thing about the one exponential curve, I think it's worth saying we've like lifted off the X axis already down this path, the tiniest bit.
0:23:36> And yeah, even if you don't go all the way to like a neural interface, VR will get so good that some people just don't want to take it off that much.
0:23:45> That's fine for them.
0:23:51> As long as we can solve this question of how do we like think about what a balance of power means in the world? I think there will be many people.
0:24:00> I'm certainly one of them who's like, actually the human body and the human experience is pretty great.
0:24:04> That log heaven in the woods, pretty awesome.
0:24:06> I don't want to be there all the time.
0:24:07> I'd love to go play the great video game, but like I'm really happy to get to go there sometimes.
0:24:14> - Yeah, there's still human experiences that are just like great human experience, just laughing with friends, you know, kissing someone that you've never kissed before, that you're on a first date.
0:24:27> Those kind of things are real moments.
0:24:31> It just laughs, having a glass of wine with a friend and just laughing.
0:24:36> - Not quite the same in VR.
0:24:37> - Yeah, it's not.
0:24:38> - When the VR goes super far, so you can't, you know, it's like you are jacked in on your brain and you can't tell what's real and what's not.
0:24:45> And then everybody gets like super deep on the simulation hypothesis or the like Eastern religion or whatever and I don't know what happens at that point.
0:24:53> - Do you ever fuck around with simulation theory? Because the real problem is when you combine that with probability theory and you talk to the people that say, well, if you just look at the numbers, the probability that we're already in a simulation is much higher than the probability that we're not.
0:25:09> - It's never been clear to me what to do about it.
0:25:16> It's like, okay, that actually makes a lot of sense.
0:25:20> I think probably sure that seems convincing, but this is my reality, this is my life and I'm gonna live it.
0:25:27> And I've, you know, from like, two AM in my college freshman dorm hallway till now, I've made no more progress on it than that.
0:25:39> - Mm, well it seems like one of those, it's, there's no, you know, it's, if it is a possibility, if it is real.
0:25:51> First of all, once it happens, what are you gonna do? I mean, that is the new reality.
0:25:56> And in many ways, our new reality is as alien to, you know, 100 gatherers from 15 years ago, as that would be to us now.
0:26:08> I mean, we're already, we've already entered into some very bizarre territory where, you know, I was just having a conversation with my kids, we were asking questions about something and, you know, like I always say, let's guess, what percentage of that is this? And then we just Google it and then just ask Siri and we pull it up like, look at that.
0:26:27> Like that alone is so bizarre compared to how it was when I was 13 and you had to go to the library.
0:26:34> I'd hoped that the book was accurate.
0:26:37> - Totally.
0:26:38> I was very annoyed this, I was reading about how horrible systems like chat GBT and Google are from an environmental impact because it's, you know, using like some extremely tiny amount of energy for each query.
0:26:50> And, you know, how we're destroying the world.
0:26:52> And I was like, before that people drove to the library.
0:26:55> Let's talk about how much carbon they burn to answer this question versus what it takes now.
0:26:58> Come on.
0:26:59> - But that's just people looking for some reason why something's bad.
0:27:03> That's not a logical perspective.
0:27:04> - Totally.
0:27:05> - Well, what we should be looking at is the spectacular changes that are possible through this.
0:27:12> And all the problems, the insurmountable problems that we have with resources, with the environment, with cleaning up the ocean, climate change, there's so many problems that we have.
0:27:23> - We need this to solve all of everything else.
0:27:24> - And that's why we need President AI.
0:27:28> - If AI could make every scientific discovery, but we still had human presidents, do you think we'd be okay? - No, 'cause those creeps would still be pocketing money and they'd have offshore accounts.
0:27:40> And it would always be a weird thing of corruption and how to mitigate that corruption, which is also one of the fascinating things about the current state of technology is that we're so much more aware of corruption.
0:27:52> We're so much more, there's so much independent reporting and we're so much more cognizant of the actual problems that are in place.
0:28:01> - This is really great.
0:28:03> One of the things that I've observed, obviously many other people too, is corruption is such an incredible hindrance to getting anything done in a society to make it forward progress.
0:28:14> And my worldview had been more US centric when I was younger and as I've just studied the world more and had to work in more places in the world, it's amazing how much corruption there still is.
0:28:27> But the shift to a technologically enabled world, I think, is a major force against it because everything is, it's harder to hide stuff.
0:28:36> And I do think corruption in the world will keep trending down.
0:28:40> - Because of its exposure through technology.
0:28:45> - Yeah, I mean, it comes at a cost and I think the loss, I am very worried about how far the surveillance state could go here, but in a world where payments for example, are no longer like bags of cash, but done somehow digitally and somebody, even if you're using Bitcoin, can like watch those flows.
0:29:09> I think that's like a corruption reducing thing.
0:29:12> - I agree, but I'm very worried about central bank digital currency and that being tied to a social credit score.
0:29:20> - Super against.
0:29:22> - Yeah, that scares the shit out of me.
0:29:24> And the push to that is not, that's not for the overall good of society, that's for control.
0:29:30> - Yeah, I think like, I mean, there's many things that I'm disappointed that the US government has done recently, but the war on crypto, which I think is a like, we can't give this up, like we're gonna control this and all this, that's like, that's a thing that like makes me quite sad about the country.
0:29:51> - It makes me quite sad about the country too, but then you also see with things like FTX, like, oh, well, this can get without regulation and without someone overseeing it, this can get really fucked.
0:30:03> - Yeah, I'm not anti-regulation.
0:30:07> Like I think there's clearly a role for it.
0:30:10> And I also think FTX was like a sort of comically bad situation that we shouldn't.
0:30:18> - It's like worst case scenario.
0:30:20> - Yeah.
0:30:21> (laughs) - Yeah, but it's a fun one.
0:30:22> - Like it's totally fun and you talk.
0:30:24> - I love that story.
0:30:25> - I mean, you clearly, I really do.
0:30:29> I love the fact that they were all doing drugs and having sex with each other.
0:30:32> - No, no, I had every part of the dramas.
0:30:34> I mean, it's a gripping story 'cause they had everything there.
0:30:39> - They did their taxes with, like, what was the program that they used? - Quick books.
0:30:45> (laughs) - They're dealing with billions of dollars.
0:30:48> - I don't know why I think the word polycule is so funny.
0:30:51> - But polycule? - That was what they, like, when you call a relationship, like a poly but closed, like polyamorous molecule put together.
0:30:59> - Oh, I see.
0:31:00> - So they were like, this is our polycule? - So there's nine of them in their poly-- - Or 10 of them or whatever.
0:31:04> - Yeah, you call that a polycule.
0:31:05> I think that was the funny, like, that became like a meme in Silicon Valley for a while that I thought was hilarious.
0:31:11> You clearly want enough regulation that that can't happen, but they're like-- - Well, I'm not against that happening.
0:31:20> I'm against them doing what they did with the money.
0:31:22> - No, that's what I mean.
0:31:23> - Polycule is kinda fun.
0:31:24> - Go for it.
0:31:25> No, no, I mean, you want enough thing that, like, FTX can't lose all of its depositors money.
0:31:29> - Yes.
0:31:30> - But I think there's an important point here, which is you have all of this other regulation that people, and it didn't keep us safe.
0:31:38> And the basic thing, which was like, you know, let's do that, that was not all of the crypto stuff people were talking about.
0:31:46> - Mm.
0:31:47> - Yes, I mean, the real fascinating crypto is Bitcoin.
0:31:52> To me, I mean, that's the one that I think has the most likely possibility of becoming a universal viable currency.
0:32:01> And it's limited in the amount that there can be.
0:32:06> It's, you know, people mine it with their own, it's like, that to me is very fascinating.
0:32:12> And I love the fact that it's been implemented.
0:32:15> And that at least some, like, I've had Andreas Antinopoulos on the podcast, and he's, when he talks about it, he's living it.
0:32:25> He's spending all of his money, everything he has paid is in Bitcoin, he pays his rent in Bitcoin.
0:32:31> Everything he does is in Bitcoin.
0:32:33> - I helped start a project called WorldCoin a few years ago.
0:32:36> And so I've gotten to like learn more about the space.
0:32:41> I'm excited about it for the same reasons.
0:32:44> I'm excited about Bitcoin too.
0:32:46> But I think this idea that we have a global currency that is outside of the control of any government is a super logical and important step on the tech tree.
0:32:58> - Yeah, agreed.
0:33:00> I mean, why should the government control currency? I mean, the government should be dealing with all the pressing environmental, social, infrastructure issues, foreign policy issues, economic issues, the things that we need to be governed in order to have a peaceful and prosperous society that's equal and equitable.
0:33:20> What do you think happens to money in currency after AGI? - I've wondered about that because I feel like with money, especially when money goes digital, the bottleneck is access.
0:33:32> If we get to a point where all information is just freely shared everywhere, there are no secrets, there are no boundaries, there are no borders, we're reading minds, we have complete access to all of the information of everything you've ever done, everything everyone's ever said.
0:33:52> There's no hidden secrets.
0:33:55> What is money then? Money is this digital thing about how can you possess it? How can you possess this digital thing if there is literally no bottleneck? There's no barriers to anyone accessing any information 'cause essentially it's just ones and zeros.
0:34:12> - Yeah, I mean, I think the information frame makes sense.
0:34:15> Another way is that money is like a sort of way to trade labor or trade like a limited number of hard assets like land and houses and whatever.
0:34:26> And if you think about a world where intellectual labor is just readily available and super cheap, then that's somehow very different.
0:34:41> I think there will always be goods that we want to be scarce and expensive, but it'll only be those goods that we want to be scarce and expensive that's in services that still are.
0:34:51> And so money in a world like that, I think is just a very curious idea.
0:34:55> - Yeah, it becomes a different thing.
0:34:57> I mean, it's not a bag of gold and a leather pouch that you're carrying around.
0:35:01> - Not gonna do you a much good probably.
0:35:03> - It's not gonna do you much good.
0:35:04> But then the question becomes, how is that money distributed and how do we avoid some horrible Marxist society where there's one totalitarian government that just-- - Don't tell it.
0:35:15> - That would be bad.
0:35:16> I think you've got to like, my current best idea and maybe there's something better is I think you act like if we are right, a lot of reasons we could be wrong, but if we are right that like the AGI systems of which there will be a few become the high order bits of sort of influence, whatever in the world, I think you do need like not to just redistribute the money but the access so that people can make their own decisions about how to use it and how to govern it.
0:35:45> And if you've got one idea, you get to do this, if I've got one idea, I get to do that.
0:35:51> And I have like rights to basically do whatever I want with my part of it.
0:35:55> And if I come up with better ideas, then you know, I get rewarded for that by whatever the society is or vice versa.
0:36:00> - Yeah.
0:36:01> You know, the hardliners, the people that are against like welfare and against any sort of UG, universal basic income, UBI, what they're really concerned with is human nature, right? They believe that if you remove incentives, if you just give people free money, they become addicted to it, they become lazy.
0:36:23> But isn't that a human biological and psychological bottleneck? And perhaps with the implementation of artificial intelligence combined with some sort of neural interface, whether it's external or internal, it seems like that's a problem that can be solved.
0:36:48> That you can essentially, and this is where it gets really spooky, you can re-engineer the human biological system and you can remove all of these problems that people have that are essentially problems that date back to human reward systems when we're tribal people, hunter-gatherer people, whether it's jealousy, lust, envy, all these variables that come into play when you're dealing with money and status and social status, if those are eliminated with technology and essentially we become a next version of what the human species is possible.
0:37:28> Like, look, we're very, very far removed from tribal, brutal societies of cave people.
0:37:36> We all agree that this is a way better way to live.
0:37:40> It's way safer.
0:37:43> Like I was talking about this in my comedy club last night 'cause my wife was, we were talking about DNA and my wife was saying that look, everybody came from cave people, which is kind of a fucked up thought, that everyone here is here because of cave people.
0:37:59> Well, all that's still in our DNA, all that's still, and these reward systems can be hijacked and they can be hijacked by just giving people money and like, you don't have to work, you don't have to do anything, you don't have to have ambition, you'll just have money and just lay around and do drugs.
0:38:17> That's the fear that people have of giving people free money.
0:38:21> But if we can figure out how to literally engineer the human biological vehicle and remove all those pitfalls, if we can enlighten people technologically, maybe enlighten is the wrong word, but advance the human species to the point where those are no longer dilemmas because those are easily solvable through coding.
0:38:51> They're easily solvable through enhancing the human biological system, perhaps raising dopamine levels to the point where anger and fear and hate are impossible, they don't exist.
0:39:05> And if you just had everyone on Molly, how many wars would there be? There'd be zero wars.
0:39:11> I mean, I think if you could get everyone on Earth to all do Molly once on the same day, that'd be a tremendous thing.
0:39:17> It would be.
0:39:18> If you got everybody on Earth to do Molly every day, that'd be a real loss.
0:39:21> But what if they did a low dose of Molly where you just get to, where everybody greets people with love and affection and there's no longer concerned about competition.
0:39:34> Instead, the concern is about the fascination of innovation and creation and creativity.
0:39:41> - Man, we could talk the rest of the time about this one topic.
0:39:45> It's so interesting.
0:39:46> I think, if I could like push a button to like, remove all human striving and conflict, I wouldn't do it, first of all.
0:39:59> Like, I think that's a very important part of our story and experience.
0:40:04> And also, I think we can see both from our own biological history and also from what we know about AI, that very simple goal systems, fitness functions, reward models, whatever you wanna call it, lead to incredibly impressive results.
0:40:26> You know, if the biological imperative is survive and reproduce, look how far that has somehow gotten us as a society.
0:40:34> All of this, all this stuff, we have all this technology, this building, whatever else, like that got here through an extremely simple goal in a very complex environment leading to all of the richness and complexity of people fulfilling this biological imperative to some degree and wanting to impress each other.
0:41:01> So I think like evolutionary fitness is a simple and unbelievably powerful idea.
0:41:07> Now, could you carefully edit out every individual manifestation of that? Maybe, but I don't wanna like live in a society of drones where everybody is just sort of like on Molly all the time either.
0:41:24> Like that doesn't seem like the right answer.
0:41:28> Like I want us to continue to strive, I want us to continue to push back the frontier and go out and explore.
0:41:34> And I actually think something's already gotten a little off track in society about all of that.
0:41:42> And we're, I don't know, I think like I don't, I thought I'd be older by the time I felt like the old guy complaining about the youth.
0:41:53> But I think we've lost something and I think that we need more striving, maybe more risk taking, more like explore spirit.
0:42:07> What do you mean by you think we've lost something? I mean, here's like a version of it very much from my own lens.
0:42:15> I was a startup investor for a long time and it often was the case that the very best startup founders were in their early or mid 20s or late 20s maybe even.
0:42:36> And now they skew much older.
0:42:39> And what I want to know is in the world today where the super great 25 year old founders, and there are a few, it's not fair to say there are none, but there are less than there were before.
0:42:49> And I think that's bad for society at all levels.
0:42:54> I mean like tech company founders is one example, but like people who go off and create something new, who push on a disagreeable or controversial idea, we need that to drive forward.
0:43:08> We need that sort of spirit.
0:43:11> We need people to be able to put out ideas and be wrong and not be ostracized from society for it or not have it be like something that they get canceled for or whatever.
0:43:22> We need people to be able to take a risk in their career because they believe in some important scientific quest that may not work out or it may sound like really controversial or bad or whatever.
0:43:32> Certainly when we started OpenAI and we were saying, we think this AGI thing is real and could be done unlikely, but so important if it happens.
0:43:44> And all of the older scientists in our field were saying, those people are irresponsible.
0:43:49> You shouldn't talk about AGI, that's like they're selling a scam or they're like, you know, they're kind of being reckless and it's going to lead to an AGI winter.
0:43:59> Like we said, we believed, we said at the time, we knew it was unlikely, but it was an important quest.
0:44:04> And we were going to go after it and kind of like fuck the haters.
0:44:08> That's important to a society.
0:44:10> What do you think is the origin? Like why do you think there are less young people that are doing those kind of things now as opposed to a decade or two ago? I am so interested in that topic.
0:44:27> I'm tempted to blame the education system, but I'm sure that I think that like interacts with society in all of these strange ways.
0:44:38> It's funny, there was this like thing all over my Twitter feed recently trying to talk about like what caused the drop in testosterone in American men over the last few decades.
0:44:50> And no one was like, this is a symptom, not a cause.
0:44:54> And everyone was like, oh, it's the microplastics, it's the birth control pills, it's the whatever, it's the whatever, and I think this is like not at all the most important piece of this topic, but it was just interesting to me sociologically that there was only talk about it being, about what caused it, not about it being an effective, some sort of change in society.
0:45:22> But isn't what caused it, well, there's biological reasons why, like when we talk about the phthalates and microplastic pesticides, environmental factors, those are real.
0:45:37> Totally.
0:45:38> And I don't like, again, I'm so far out of my depth and expertise here.
0:45:41> This was just it was just interesting to me that the only talk was about like biological factors that somehow society can have some sort of effect.
0:45:49> Well, society most certainly has an effect.
0:45:52> Do you know what the answer to this is? I don't, I mean, I've had a podcast with Dr.
0:45:57> Shana Swan, who wrote the book Countdown, and that is all about the introduction of petrochemical products and the correlating drop in testosterone, rise in miscarriages, the fact that these are ubiquitous endocrine disruptors that when they do blood tests on people, they find some insane number.
0:46:19> It's like 90 plus percent of people have phthalates in your system.
0:46:23> And you I appreciate the metal cups.
0:46:25> Yeah, we try to mitigate it as much as possible.
0:46:29> But I mean, you're getting it.
0:46:30> If you're microwaving food, you're you're fucking getting it.
0:46:33> You're just getting it.
0:46:34> You're getting, if you eat processed food, you're getting it.
0:46:36> You're getting a certain amount of microplastics in your diet and estimates have been that it's as high as a credit card of microplastics in your body.
0:46:45> You consume a credit card of that a week.
0:46:47> Well, the real concern is with mammals because the introductions, when they've done studies with mammals, when they've introduced phthalates into their body, there's a correlating.
0:46:59> One thing that happens is the these animals, their taint shrink, like the taint of them.
0:47:07> Yeah, the mammal, when you look at males, it's 50 percent to 100 percent larger than the females.
0:47:12> With the introduction of thalates on the males, the taints start shrinking, the penises shrink, the testicles shrinks, sperm count shrinks.
0:47:20> So we know there's a direct biological connection between the these chemicals and how they interact with with bodies.
0:47:30> So that's that's a real one.
0:47:32> And it's also the amount of petrochemical products that we have, the amount of plastics that we use.
0:47:39> It's it is such an integral part of our culture and also our society, our civilization.
0:47:46> It's everywhere and I've wondered if you think about how these territorial apes evolve into this new advanced species, wouldn't one of the very best ways be to get rid of one of the things that causes the most problems, which is testosterone.
0:48:13> We need testosterone, we need aggressive men and protectors, but why do we need them? We need them because there's other aggressive men that are evil, right? So we need protectors from ourselves.
0:48:24> We need the good, strong people to protect us from the bad, strong people.
0:48:29> But if we're in the process of integrating with technology, if technology isn't an escapable part of our life, if it is everywhere, you're using it, you have the Internet of everything that's in your microwave, your television, your computers, everything you use.
0:48:47> As time goes on, that will be more and more part of your life.
0:48:52> And as these plastics are introduced into the human biological system, you're seeing a feminization of the males of the species.
0:49:01> You're seeing a downfall in birth rate.
0:49:04> You're seeing all these correlating factors that would sort of lead us to become this more peaceful, less violent, less aggressive, less ego-driven thing.
0:49:19> Which the world is definitely becoming all the time.
0:49:23> And I'm all for less violence, obviously.
0:49:27> But I don't.
0:49:30> Look, obviously testosterone has many great things to say for it.
0:49:38> And some bad tendencies too.
0:49:41> But I don't think a world, if we leave that out of the equation and just say like a world that has a a spirit that, you know, we're going to defend ourselves, we're going to, we're going to find a way to like protect ourselves and our tribe and our society into this future, which you can get with lots of other ways.
0:50:07> I think that's an important impulse.
0:50:09> More than that though, what I meant is about, if we go back to the issue of like where the young founders, why don't we have more of those? And I don't think it's just the tech startup industry.
0:50:25> I think you could say that about like young scientists or many other categories.
0:50:29> Those are maybe just the ones that I know the best.
0:50:35> In a world with any amount of technology, I still think we we've got to.
0:50:43> It is our destiny in some sense to stay on this on this curve.
0:50:48> And we still need to go figure out what's next and after the next hill and after the next hill.
0:50:54> And it would be.
0:50:55> My perception is that there is some long term societal change happening here.
0:51:03> And I think it makes us less happy too.
0:51:05> Right.
0:51:08> It may make us less happy.
0:51:10> But what I'm saying is if the human species does integrate with technology, wouldn't a great way to facilitate that, to be to kind of feminize the primal apes and to sort of downplay the role.
0:51:26> You mean like the tech, like should the AGI, the phthalates in the world? Well, maybe, I don't know if it's AGI.
0:51:31> I mean, maybe it's just an inevitable, inevitable consequence of technology.
0:51:35> Because especially the type of technology that we use, which does have so much plastic in it.
0:51:41> And then on top of that, the technology that's involved in food, food systems, preservatives, all these different things that we use to make sure that people don't starve to death.
0:51:49> We've made incredible strives in that.
0:51:51> There are very few people in this country that starve to death.
0:51:54> Yeah.
0:51:55> It is not a, it's not a primary issue, but violence is a primary issue.
0:52:01> But our, our concerns about violence are, and our concerns about testosterone and strong men and powerful people is only because we need to protect against others.
0:52:13> We need to protect against other, same thing.
0:52:16> Is that really the only reason? Sure.
0:52:18> I mean, how many like incredibly violent women are out there running gangs? No, no, that part for sure.
0:52:23> Yeah.
0:52:24> We're not very many.
0:52:26> What I meant more is, is that the only reason that society values like strong masculinity? Yeah, I think so.
0:52:33> I think it's a biological imperative, right? And I think that biological imperative is because we used to have to defend against incoming tribes and predators and animals.
0:52:42> And, and we, we needed someone who was stronger than most to defend the rest.
0:52:48> And like that's the concept of the military.
0:52:51> That's why Navy SEAL training is so difficult.
0:52:53> We want the strongest of the strong to be at the tip of the spear.
0:52:57> But that's only because there's people like that out there that are bad.
0:53:01> If general, artificial general intelligence and the implementation of some sort of a device that changes the biological structure of human beings to the point where that is no longer a concern.
0:53:14> Like if you are me and I am you and I know this because of technology, violence is impossible.
0:53:20> Yeah.
0:53:21> But look, by the time if this goes all the way down the sci-fi path and we're all like merge into this one single like planetary universal whatever consciousness, then then then yes, you don't need to test a strong need test, dastarone, but you still we can reproduce through other methods.
0:53:37> Like this is the alien hypothesis, right? Like why do they look so spindly and without any gender and you know, when they have these big heads and they don't have physical strength.
0:53:46> They don't need physical strength.
0:53:47> They they have some sort of a telepathic way of communicating.
0:53:51> They probably don't need sounds with their mouths and they don't need this urge that we have to conquer and to spread our DNA.
0:53:59> Like that's so much of what people do is these reward systems that were established when we were territorial apes.
0:54:07> There's a question to me about how much you can ever get rid of rid of that.
0:54:15> If you make an AGI and it decides actually we don't need to expand, we don't need more territory.
0:54:23> We're just like happy.
0:54:24> We at this point, you, me, it, the whole thing altogether all motion or happy here on earth.
0:54:29> Um, we don't need to give me bigger.
0:54:31> We don't need to reproduce.
0:54:32> We don't need to grow.
0:54:32> We're just going to sit here and run.
0:54:34> A, that sounds like a boring life.
0:54:37> I don't agree with that.
0:54:38> I don't agree that that would be the logical conclusion.
0:54:42> I think the logical conclusion would be they would look for problems and frontiers that are insurmountable to our current existence, like intergalactic communication and transportation.
0:54:57> What happens when it meets another AGI, the other galaxy over? What happens if it meets an AGI that's a million years more advanced or that, like what does that look like? Yeah.
0:55:06> That's what I've often wondered if we are, I call ourselves the biological caterpillars that create the electronic butterfly that we're making a cocoon right now.
0:55:15> We don't even know what we're doing.
0:55:16> And I think it's also tied into consumerism.
0:55:19> Consi- because what does consumerism do? Consumerism facilitates the creation of newer and better things because you always want the newest, latest, greatest.
0:55:28> So you have more advanced technology and automobiles and computers and cell phones and, and all of these different things, including medical science.
0:55:40> That's all for short, true.
0:55:43> The thing I was like reflecting on as you were saying, that is, I don't think I.
0:55:48> I'm not as optimistic that we can or even should.
0:55:55> Overcome our biological base to the degree that I think you think we can.
0:56:01> And, you know, to even go back one further level, like I think, I think society is the happiest where there's like roles for strong femininity and strong masculinity in the same people and in different people.
0:56:16> And, and I don't like.
0:56:20> And I don't think a lot of these like deep seated things are.
0:56:29> Gonna be able to get pushed aside very easily and still have.
0:56:34> A system that works.
0:56:36> Like, sure, we can't really think about what, if there were consciousness in a machine someday or whatever, what that would be like.
0:56:43> And maybe, maybe I'm just like thinking too small mindedly, but I think there is something.
0:56:50> About us that has worked in a super deep way.
0:56:56> And it took evolution a lot of search space to get here, but I wouldn't discount it too easily.
0:57:04> But don't you think that cave people would probably have those same logical conclusions about life and sedentary lifestyle and sitting in front of a computer and not interacting with each other except through text? Well, I mean, isn't that like what you're saying is correct? How different do you think our motivations are today and kind of what really brings us genuine joy and how we're how we're wired at some deep level, differently than cave people? Clearly lots of other things have changed.
0:57:33> We've got better, much better tools.
0:57:34> Mm hmm.
0:57:35> But how different do you think it really is? I think that's the problem is that genetically at the base level, there's not much difference and that these reward systems are all there.
0:57:48> We interact with all of them, whether it's ego, lust, passion, fury, anger, jealousy, all these different things.
0:57:59> And you think will be some people will upload and edit those out.
0:58:01> Yes.
0:58:02> Yeah.
0:58:03> I think that our concern with losing this aspect of what it means to be a person, this like the idea that we should always have conflict and struggle because conflict and struggle is how we facilitate progress, which is true.
0:58:17> Right.
0:58:18> And combating evil is how the good gets greater and stronger if the good wins.
0:58:23> But my concern is that that is all predicated on the idea that the biological system that we have right now is correct and optimal.
0:58:35> And I think one of the things that we're dealing with with the heightened states of depression and anxiety and the lack of meaning and existential angst that people experience, a lot of that is because the biological reality of being a human animal doesn't really integrate that well with this world that we've created.
0:58:58> That's for sure.
0:58:59> Yeah.
0:59:00> And I wonder if the solution to that is not find ways to find meaning with the biological vessel that you've been given, but rather engineer those aspects that are problematic out of the system.
0:59:21> To create a truly enlightened being.
0:59:23> Like one of the things if you ask someone today, what are the odds that in three years there will be no war in the world? That's zero.
0:59:31> Like nobody thinks, no, there's never been a time in human history where we haven't had war.
0:59:36> If you had to say, what is our number one problem as a species? Well, I would say our number one problem is war.
0:59:44> Our number one problem is this idea that it's okay to send massive groups of people who don't know each other to go murder massive groups of people that are somehow opposed because of the government and because of lines in the sand.
0:59:58> That's clearly the same thing.
0:59:59> It's an insane thing.
1:00:00> How do you get rid of that? Well, one of the ways you get rid of that is to completely engineer out all the human reward systems that pertain to the acquisition of resources.
1:00:12> So what's left at that point? Well, we're a new thing.
1:00:15> I think we become a new thing.
1:00:16> And what does that thing do once? I think that new thing would probably want to interact with other new things that are even more advanced than it.
1:00:24> I do believe that scientific curiosity can drive quite that.
1:00:32> That can be a great frontier for a long time.
1:00:35> Yeah.
1:00:37> I think it can be a great frontier for a long time as well.
1:00:40> I just wonder if what we're seeing with the drop into testosterone, the because of microplastics, which sort of just snuck up on us.
1:00:49> We didn't even know that it was an issue until people started studying.
1:00:51> How certain is that at this point that that's what's happening? I don't know.
1:00:55> I'm going to study.
1:00:56> I guess it's a very good question.
1:00:57> Dr.
1:00:58> Shana Swan believes that it's the primary driving factor of the sort of drop into testosterone and all miscarriage issues and low birth weights.
1:01:08> All those things seem to have a direct, there seems to be a direct factor environmentally.
1:01:14> I'm sure there's other factors too.
1:01:16> I mean, the drop in testosterone, I mean, it's been shown that you can increase males testosterone through resistance training and through making.
1:01:24> There's certain things you can do.
1:01:26> Like one of the big ones they found through a study in Japan is cold water immersion before exercise.
1:01:33> It radically increases testosterone.
1:01:35> So you could cold water immersion and then exercise.
1:01:39> I wonder why.
1:01:39> Yeah.
1:01:40> I don't make this to you.
1:01:41> You could find that.
1:01:43> But it's a fascinating field of study, but I think it has something to do with resilience and resistance and the fact that your body has to combat this external factor that's very extreme that causes the body to go into this state of preservation and the implementation of cold shock proteins and the reduction of inflammation, which also enhances the body's endocrine system.
1:02:08> But then on top of that, this imperative that you have to become more resilient to survive this external factor that you've introduced into your life every single day.
1:02:17> So there's ways, obviously, that you can make a human being more robust.
1:02:26> You know, we know that we can do that through strength training and that all that stuff actually does raise testosterone.
1:02:31> Your diet can raise testosterone and the poor diet will lower it and will hinder your integrin system, hinder your ability to produce growth, hormone, melatonin, all these different factors.
1:02:45> That seems to be something that we can fix in terms or at least mitigate in terms with decisions and choices and effort.
1:02:54> But the fact that these petrochemical pro...
1:02:58> Like there's a graph that Dr.
1:03:00> Shana Swan has in her book that shows during the 1950s when I started using petrochemical products and everything, microwave, plastic, saran wrap, all those different stuff.
1:03:11> There's a direct correlation between the implementation and the dip and it all seems to line up.
1:03:19> Like that seems to be a primary factor.
1:03:22> Does that have an equivalent impact on like estrogen related hormones? That's a good question.
1:03:29> Some of them actually...
1:03:31> I know some of these chemicals that they're talking about actually increase estrogen in men.
1:03:38> I don't know, but I do know that it increases miscarriages.
1:03:41> So I just think it's overall disruptive to the human body.
1:03:46> Definitely a societal wide disruption of the endocrine system in a short period of time.
1:03:51> Seems like a...
1:03:51> Madan.
1:03:53> Sure.
1:03:54> Difficult to wrap our heads.
1:03:55> And then pollutants and environmental toxins on top of the pesticides and herbicides and all these other things in microplastics.
1:04:03> There's a lot of factors that are leading our systems to not work well.
1:04:06> But I just really wonder if this...
1:04:13> Are we just clinging on to this monkey body? Are we deciding that...
1:04:17> I like my monkey body.
1:04:18> I do do.
1:04:19> Listen, I love it.
1:04:20> But I'm also...
1:04:22> I try to be very objective.
1:04:24> And when I objectively look at it in terms of like, if you take where we are now and all of our problems and you look towards the future and like, what would be one way that you could mitigate a lot of these? And well, it would be the implementation of some sort of a telepathic technology where you couldn't just text someone or tweet at someone something mean because you would literally feel what they feel when you put that energy out there.
1:04:52> And you would be repulsed.
1:04:55> Yeah.
1:04:56> And then violence would be if you were committing violence on someone and you literally felt the reaction of that violence in your own being.
1:05:07> That's fascinating.
1:05:09> You would also have no motivation for violence.
1:05:12> If we had no aggressive tendencies, no primal chimpanzee tendencies, you know, it's true that violence in the world has obviously gone down a lot over the decades, but emotional violence is up a lot.
1:05:26> And the internet has been horrible for that.
1:05:28> Yeah.
1:05:28> Like, I don't walk...
1:05:29> I'm not going to walk over there and punch you because you look like a big strong guy.
1:05:32> You're going to punch me back.
1:05:32> And also there's a societal convention not to do that.
1:05:35> But if I didn't know you, I might like send a mean tweet about you and I feel nothing on that.
1:05:41> Yeah.
1:05:42> And clearly that has become like a mega epidemic in society that we did not evolve the biological constraints on somehow.
1:05:55> Yeah.
1:05:55> And I'm actually very worried about how much that's already destabilized, Dustin made us all miserable.
1:06:04> It's certainly accentuated.
1:06:06> It's exacerbated all of our problems.
1:06:09> It's...
1:06:09> I mean, if you read Jonathan Hates' book, The Coddling of the American Mind, have you read it? Great book.
1:06:14> Yeah, it's great book.
1:06:14> And it's very damaging to women, particularly young girls.
1:06:18> Young girls growing up, there's a direct correlation between the invention of social media, the introduction to the iPhone, self-harm, suicide, online bullying.
1:06:28> You know, like people have always talked shit about people when no one's around.
1:06:32> I think the fact that they're doing it now openly to harm people.
1:06:37> Horrible, obviously.
1:06:38> I think it's super damaging to men too.
1:06:40> Maybe they just like talk about it less, but I don't think any of us are like set up for this.
1:06:44> No, no one's set up for it.
1:06:46> And, you know, I think famous people know that more than anyone.
1:06:49> We all get used to it.
1:06:50> Yeah.
1:06:51> You just get numb to it.
1:06:52> And or if you're wise, you don't engage.
1:06:54> You know, I don't even have any apps on my new phone.
1:06:57> Yeah.
1:06:58> I've decided I got a new phone and I said, OK, nothing.
1:07:01> That's really smart.
1:07:01> No Twitter.
1:07:02> I saw I have a separate phone that if I have to post someone up something, I pick up.
1:07:07> But all I get on my new phone is text messages.
1:07:09> And is that more just to like keep your mind pure and polluted? Yeah.
1:07:14> And not tempt myself into just.
1:07:16> You know, many fucking times I've got up to go to the bathroom first thing in the morning and spent an hour just sitting on the toilet, scrolling through Instagram, like for nothing does zero for me.
1:07:27> And there's this thought that I'm going to get something out of it.
1:07:31> I was thinking actually just yesterday about how, you know, we all have talked for so long about these algorithmic feeds are going to manipulate us in these big ways and that will happen.
1:07:44> But in the small ways already where like scrolling Instagram is not even that fulfilling, like you finish that hour and you're like, I know that was a waste of my time.
1:07:53> But it was like over the threshold where you couldn't quite.
1:07:57> It's hard to put the phone down.
1:07:59> Right.
1:07:59> You just hoping that the next one's going to be interesting.
1:08:02> And every now and then the problem is every like 30th or 40th reel that I click on is wild.
1:08:09> I wonder, by the way, if that's more powerful than if everyone was wild, if everyone was great, you know, it's like the slob.
1:08:17> You have to mine for gold.
1:08:18> Yeah.
1:08:18> You don't just go out and pick it like daisy.
1:08:20> So if the algorithm is like intentionally feeding you some shit along the way.
1:08:25> Yeah.
1:08:25> Well, there's just a lot of shit out there, unfortunately.
1:08:29> But it's all it's just in terms of, you know, I was talking to Sean O'Malley, who's this UFC fighter, who's, you know, obviously it was a very strong mind, really interesting guy.
1:08:39> But one of the things that Sean said is like, I get this like low level anxiety from scrolling through things.
1:08:45> And I don't know why.
1:08:46> Like, what is that? And I think it's part of the logical mind realizes is a massive waste of your resources.
1:08:54> I also deleted a bunch of that stuff off my phone because I just didn't have the self control.
1:08:59> I mean, I had the self control to delete it, but like not to stop once I was scrolling through.
1:09:03> Yeah.
1:09:04> And so I, I think we're just like, yeah, we're getting attention hacked in some ways.
1:09:13> There's some good to it too, but we don't, yeah, have the stuff in place.
1:09:18> The tools, the societal norms, whatever to modulate it well.
1:09:22> Right.
1:09:23> And we're not designed for it.
1:09:24> So this is a completely new technology that, again, hijacks are human reward systems and hijacks.
1:09:32> All of the checks and balances that are in place for communication, which historically has been one on one.
1:09:40> Historically, communication has been one person to another.
1:09:43> And when people write letters to each other, it's generally things like if someone likes a love letter or, you know, they miss you.
1:09:52> Like they're writing this thing where they're kind of exposing a thing that maybe they have a difficulty in expressing in front of you.
1:09:59> And it was not, you know, generally, unless the person was a psycho, they're not hateful letters.
1:10:05> Whereas the ability to just communicate, fuck that guy.
1:10:08> I hope he gets hit by a bus is so simple and easy and a, and you don't experience Twitter seems to be particularly horrible for this as the mechanics work.
1:10:20> Yeah.
1:10:21> It really rewards in ways that I don't think anybody fully understands that like taps into something about human psychology.
1:10:28> Yeah.
1:10:28> Where, but that's kind of like that's how you get engagement.
1:10:33> That's how you get like followers.
1:10:36> That's how you get what like, you know, the dopamine hits or whatever.
1:10:39> And like the people who I know that spend all day on Twitter, more of them are unhappy about it than happy.
1:10:50> Oh, yeah.
1:10:51> They're the most unhappy.
1:10:52> I mean, there's quite a few people that I follow that I only follow because they're crazy and then I'll go and check in on them and see what the fuck they're tweeting about.
1:11:01> And some of them are on there eight, 10 hours a day.
1:11:04> I'll, I'll see tweets all day long.
1:11:07> And I know that person cannot be happy.
1:11:10> They're unhappy and they cannot stop.
1:11:11> It can't stop.
1:11:12> And it seems like it's their life.
1:11:16> It's, it's a, and they get, they get meaning out of it in terms of reinforcement.
1:11:23> You know, they get short-term.
1:11:25> Yeah.
1:11:25> So yeah, I think maybe each day you go to bed feeling like you accomplished something and got your dopamine and the end of each decade, you probably are like, where did that decade go? I was talking to a friend of mine who was having a real problem with it.
1:11:35> And he would be literally walking down the street and he'd have to check his phone to see who's replying and he wasn't even looking where he's walking.
1:11:42> It was just like caught up in the anxiety of these exchanges.
1:11:46> And it's not because of the nice things people say.
1:11:48> No, no, no, no, it's all.
1:11:50> And with him, he was recognizing that, you know, he was dunking on people and then seeing people respond to the dunking and yeah, I stopped doing that a long time ago.
1:12:00> I stopped interacting with people on Twitter in a negative way.
1:12:02> I just won't do it.
1:12:03> Yeah.
1:12:03> And just even if I disagree with someone, I'll say something as peacefully as possible.
1:12:08> I have like more of an internet troll streak than I would like to admit.
1:12:12> And so I try to just like not give myself too much of the temptation, but I slip up sometimes.
1:12:16> Yeah, it's so tempting.
1:12:18> Totally.
1:12:19> It's so tempting to and it's fun.
1:12:20> It's fun to say something shitty.
1:12:22> I mean, I mean, again, whatever this biological system we were talking about earlier, that that gets a positive reward.
1:12:28> Well, again, there's a react.
1:12:30> You know, there's reactions.
1:12:32> You say something outrageous and someone's going to react and that reaction is like energy and there's there's all these other human beings engaging with your idea.
1:12:41> But ultimately, it's just not productive for most people and it's psychologically.
1:12:49> It's just fraught with peril.
1:12:53> There's just so much going on.
1:12:54> I don't know anybody ages all day long.
1:12:57> That's happy.
1:12:57> That's certainly not.
1:12:59> I don't like.
1:13:00> I mean, I think I've watched it like destroys too strong of a word, but like knock off track the careers or life or happiness or human relationships of people that are like good, smart, conscientious people.
1:13:16> Yeah.
1:13:17> Just like God couldn't fight this demon.
1:13:19> Yeah.
1:13:20> Like hacked there and COVID really accentuated that because people were alone and isolated and that made it even worse because then they felt they felt even better saying shitty things to people.
1:13:33> I'm unhappy.
1:13:34> I'm going to say even worse things about you.
1:13:36> And then there was a psychological aspect of it.
1:13:38> Like the angst that came from being socially isolated and terrified about this invisible disease.
1:13:45> It's going to kill us all.
1:13:46> And you know, and so you have is like, and then you're interacting with people into it and then you're caught up in that anxiety and you're doing it all day.
1:13:54> And I know quite a few people, especially comedians that really lost their minds and lost their respect to their peers by doing that.
1:14:02> I have a lot of sympathy for people who lost their minds during COVID because what a natural thing for us all to go through and isolation was just brutal.
1:14:11> But a lot of people did.
1:14:12> And I don't think the internet, particularly not the kind of like social dynamics of things like Twitter, I don't think that like brought to anyone's best.
1:14:21> No, but I mean, some people, I think if they're not, they're not inclined to be shitty to people.
1:14:29> I think some people did seek comfort and they did interact with people in positive ways.
1:14:34> Yeah.
1:14:35> I see there's plenty of positive.
1:14:36> I think the thing is that the negative interactions are so much more impactful.
1:14:41> Yeah.
1:14:42> Look, I think there are a lot of people who use these systems for wonderful things.
1:14:46> I didn't mean to imply that's not the case, but that's not what drives people's emotions after getting off the platform.
1:14:53> Right.
1:14:53> Right.
1:14:53> Right.
1:14:54> Right.
1:14:54> And it's also probably not if you looked at a pie chart of the amount of interactions on Twitter, I would say a lot of them are shitting on people and being angry about how many of the people that you know that use Twitter, those eight or ten hours a day are just saying wonderful things about other people all day versus the virulent.
1:15:13> Very few.
1:15:14> Yeah.
1:15:14> Very few.
1:15:15> I don't know any of them.
1:15:17> I know.
1:15:18> But then again, I wonder with the implementation of some new technology that makes communication a very different thing than what we're occurring.
1:15:29> Like what we're doing now with communication is less immersive than communicating one on one.
1:15:35> You and I are talking, we're looking into each other's eyes, we're getting social cues, we're smiling at each other, we're laughing.
1:15:41> It's a very natural way to talk.
1:15:44> I wonder if through the implementation of technology, if it becomes even more immersive than a one on one conversation, even more interactive and eat, you will understand even more about the way a person feels about what you say, about that person's memory, that person's life, that person's history, their education, how it comes out of their mind, how their mind interacts with your mind and you see them, you really see them.
1:16:20> I wonder if that, I wonder if what we're experiencing now is just like the first time people invented guns, they just started shooting at things.
1:16:28> Yeah, if you can like feel what I feel when you say something mean to me or nice to me, like that's clearly going to change what you decide to say.
1:16:39> Yes.
1:16:40> Yeah.
1:16:40> Yeah, unless you're a psycho.
1:16:42> Unless you're a psycho.
1:16:43> And then what causes someone to be a psycho and can that be engineered out? Imagine what we're talking about when we're dealing with the human mind, when we're dealing with various diseases, bipolar schizophrenia.
1:16:57> Imagine a world where we can find the root cause of those things and through coding and some sort of an implementation of technology that elevates dopamine and serotonin and does some things to people that eliminates all of those problems and allows people to communicate in a very pure way.
1:17:24> It sounds great.
1:17:27> It sounds great, but you're not going to have any rock and roll.
1:17:29> You'll stand up comedy will die.
1:17:31> You'll have no violent movies.
1:17:35> You know, there's a lot of things that are going to go out the window, but maybe that is also part of the process of our evolution to the next stage of existence.
1:17:43> Maybe I feel genuinely confused on this.
1:17:49> Well, I think you should be.
1:17:50> I mean, to be we're going to find out.
1:17:52> Yeah, I mean, to be sure how it's good.
1:17:54> Yeah, yeah, yeah.
1:17:55> That's the same.
1:17:55> But I don't even have like a.
1:17:56> You burst beyond belief.
1:17:57> Right.
1:17:58> I mean, you just you from the when did open AI, when did you first start this project? Are like the very beginning and end of 2015 early 2016.
1:18:07> And when you initially started this project, what kind of timeline did you have in mind? And has it stayed on that timeline or is it just wildly out of control? I remember talking with John Schulman, one of our co-founders early on, and he was like, yeah, I think it's going to be about a 15 year project.
1:18:30> And I was like, yeah, it sounds about right to me.
1:18:32> And I've always sort of thought since then now I no longer think of like AGI is quite the end point, but to get to the point where we like accomplish the thing we set out to accomplish.
1:18:44> I, you know, that would take us to like 2030, 2031.
1:18:47> That has felt to me like all the way through kind of.
1:18:52> A reasonable estimate with huge Arab ours.
1:18:57> And I kind of think we're on the trajectory.
1:19:00> I sort of would have assumed.
1:19:01> And what did you think the impact.
1:19:05> On society would be like, did you when you first started doing this? And you said, OK, if we are successful.
1:19:14> And we do create some massively advanced AGI.
1:19:18> What, what is the implementation and how, what is the impact on society? Have, did you, did you sit there and have like a graph like you had to pros on one side, the cons on the other? Did you just sort of abstractly consider? Well, we definitely talked a lot about the cons, you know, many of us were super worried about and still are about safety and alignment.
1:19:47> And if we build these systems, we can all see the great future.
1:19:50> That's easy to imagine.
1:19:51> But if something goes horribly wrong, it's like really horribly wrong.
1:19:54> And so there was a lot of discussion about and really a big part of the funding spirit.
1:20:01> If this is like, how are we going to solve the safety problem? What did that even mean? One of the things that we believe is that the greatest minds in the world cannot sit there and solve that in a vacuum.
1:20:11> You've got to like have counter-thriology.
1:20:14> You've got to see where the technology goes.
1:20:16> Practice plays out in a stranger way than theory.
1:20:19> And that's certainly proven true for us.
1:20:22> But we had a long list of, well, I don't know if we had a long list of cons.
1:20:27> We had a very intense list of cons because, you know, there's like all of the last decades of sci-fi telling you about how this goes wrong.
1:20:35> You're supposed to shoot me right now.
1:20:36> Yeah.
1:20:37> And I'm sure you've seen the John Connor chat GPT.
1:20:42> I haven't.
1:20:43> What is it? It's like, you know, John Connor from the Terminator, the kid looking at you when you open up chat GPT.
1:20:52> Yeah.
1:20:55> So that stuff, we were like very clear in our minds on now.
1:21:00> I think we understand there's a lot of work to do, but we understand more about how to make AI safe in the.
1:21:07> AI safety gets overloaded.
1:21:11> Like, you know, does it mean don't say something? People find defensive or does it mean not don't destroy all of humanity or some continuum? And I think the word is like gotten overloaded.
1:21:20> But in terms of the like not destroy all of humanity version of it, we have a lot of work to do.
1:21:26> But I think we have finally more ideas about what can work and given the way the systems are going, we have a lot more opportunity.
1:21:35> So it's available to us to solve it than I thought we would have given the direction that we initially thought the technology was going to go.
1:21:41> So that's good.
1:21:42> On the positive side, the thing that I was most excited about then and remain most excited about now is what if this system can dramatically increase the rate of scientific knowledge in society? That is a I think that kind of like all real sustainable economic growth, the future getting better progress in some sense comes from increased scientific and technological capacity.
1:22:15> So we can solve all the problems.
1:22:17> And if the AI can help us do that, that's always been the thing I've been most excited about.
1:22:22> Well, it certainly seems like that is the greatest potential, greatest positive potential of AI.
1:22:29> It is to solve a lot of the problems that human beings have had forever, a lot of the societal problems that seem to be I mean, that's what I was talking about it in AI president.
1:22:40> I'm kind of not joking because I feel like if something was hyper intelligent and aware of all the variables with no human bias and no incentives, no other than here's your program, the greater good for the community of the United States and the greater good for that community as it interacts with the rest of the world.
1:23:04> The elimination of these dictators, these whether they're elected or non elected who impose their will on the population because they have a vested interest in protecting special interest groups and and industry.
1:23:26> I think I think as long as the thing that I find scary when you say that is it does it feels like it's humanity not in control and I reflexively don't like that.
1:23:38> But if it's if it's if it's if it's instead like it is the collective will of humanity being expressed without the mistranslation and corrupting influences along the way, then I can see it.
1:23:51> Is that possible? It seems like it would be.
1:23:54> It seems like if it was programmed in that regard to do the greater good for humanity and and take into account the values of humanity, the needs of humanity.
1:24:05> There's something about the phrase do the greater good for human.
1:24:08> I know it's terrifying.
1:24:09> It's very Orwellian.
1:24:10> All of it is.
1:24:11> But also so is artificial general intelligence for sure, for sure.
1:24:15> Open the door.
1:24:16> I wish I had worked on, you know, something that was less morally fraught.
1:24:20> But do you? Because it's really exciting.
1:24:22> I mean, I can't imagine a I cannot imagine a cooler thing to work on.
1:24:26> I feel unbekably I feel like the luckiest person on Earth.
1:24:29> That's awesome.
1:24:29> It is not.
1:24:30> It's not on easy mode.
1:24:33> I'll say that.
1:24:34> Oh, yeah.
1:24:34> This is not life on easy mode.
1:24:35> No, no, no, no.
1:24:37> I mean, you are at the forefront of one of the most spectacular changes in human history.
1:24:44> And I would say as no, I would say more spectacular than the implementation of the Internet.
1:24:52> I think the implement the implementation of the Internet was the first baby steps of this and that artificial general intelligence is.
1:25:00> Yeah.
1:25:01> It is the Internet on steroids.
1:25:03> It's the the Internet in, you know, hyperspace.
1:25:07> What I would say is it's it's the next step and there'll be more steps after.
1:25:12> But it's our most exciting step yet.
1:25:13> You know, my my wonder is what are those next steps after? Isn't that so exciting to think about? It's very exciting.
1:25:21> I think we're the last people.
1:25:23> I really do.
1:25:24> I think we're the last of the biological people with all the biological problems.
1:25:28> I think there's a very excited about that.
1:25:32> I just think that's just what it is.
1:25:35> You're just fine with it.
1:25:36> It is what it is.
1:25:37> You know, I mean that I don't think you can control it at this point other than some massive natural disaster that resets us back to the Stone Age, which is also something we should be very concerned with.
1:25:49> Because it seems like that happens a lot and we're not aware of it because the timeline of a human body is so small.
1:25:54> You know, the timeline of the human existence as a person is a hundred years if you're lucky, but yet the timeline of the earth is billions of years.
1:26:03> And if you look at how many times life on earth has been reset by comets slamming into the earth and just completely eliminating all technological advancement.
1:26:15> It seems like it's happened multiple times in recorded history.
1:26:19> I do think I always think we don't think about that quite enough.
1:26:25> We talked about the simulation hypothesis earlier.
1:26:31> It's had this big resurgence in the tech industry recently.
1:26:34> One of the things one of the new takes on it is we get closer to AGI is that, you know, if ancestors were simulating us, the time they'd want to simulate again and again is right up to the lead up to the creation of AGI.
1:26:47> Yeah.
1:26:48> So it seems very crazy we're living through this time, but it's not in coincidence at all.
1:26:51> You know, this is the time that is after we had enough cell phones out in the world, like recording tons of video to train the video model of the world.
1:26:59> That's all being like jacked into us now via brain implants or whatever.
1:27:02> And before everything goes really crazy with AGI.
1:27:05> And it's also this interesting time to simulate like, can we get through? Does the asteroid come right before we get there for dramatic tension? Like, do we figure out how to make this safe? Do we figure out a societal degree on it? So that's led to like a lot more people believing in it than before, I think.
1:27:20> Yeah, for sure.
1:27:21> And again, I think this is just where it's going.
1:27:26> I mean, I don't know if that's a good thing or a bad thing.
1:27:30> It's just a thing, but it's certainly better to live now.
1:27:32> I would not want to live in the 1800s and being a covered wagon trying to make my way across the country.
1:27:39> Yeah, we got the most exciting time in history yet.
1:27:41> It's the best.
1:27:42> It's the best, but it's also has the most problems, the most social problems, the the most awareness of social, environmental infrastructure.
1:27:52> The issue is we have to go solve them.
1:27:55> Yeah.
1:27:55> And I intuitively, I think I feel something.
1:28:00> Somewhat different than you, which is, I think humans in something close to this form are going to be around for a lot longer than I don't think we're the last humans.
1:28:16> How long do you think we have? Um, like longer than a time frame, I can reason about really now there may be like, I could totally imagine a world where some people decide to merge and go off exploring the universe with AI and there's a big universe out there, but like, can I really imagine a world where short of a natural disaster, there are not humans pretty similar to humans from today on earth doing human like things and the sort of spirit of humanity merged into these other things that are out there, doing their thing in the universe.
1:28:55> It's very hard for me to actually see that happening.
1:29:00> And maybe that means I'm like going to turn out to be a dinosaur and let I mean horribly wrong in this prediction, but I would say I feel it more over time as we make progress with AI, not less.
1:29:10> Yeah, I don't feel that at all.
1:29:11> I feel like we're done in like a few years, no, few decades, maybe a generation or two, it'll probably be a gradual change, like wearing of clothes.
1:29:22> You know, I don't think everybody wore clothes and they invented clothes.
1:29:25> I think it probably took a while when someone figured out shoes.
1:29:29> I think that probably took a while when they figured out structures, doors, houses, cities, agriculture, all those things were slowly implemented over time and then now become everywhere.
1:29:39> And I think this is far more transformative.
1:29:43> And it's part of that because you don't think there'll be an option for some people not to merge.
1:29:48> Right.
1:29:48> Just like there's not an option for some people to not have telephones anymore.
1:29:52> It's like, I used to have friends like, I don't even have email.
1:29:55> Those those three people don't exist anymore.
1:29:57> They all have email.
1:29:57> Everyone has a phone, at least a flip phone.
1:30:00> I know some people that they just can't handle social media and all that jazz.
1:30:04> They went to a flip phone.
1:30:05> Good.
1:30:06> I don't know if this is true or not.
1:30:07> I've heard you can't like walk into an AT&T store anymore and still buy a flip phone.
1:30:10> I heard they just changed.
1:30:11> You can.
1:30:11> Oh, really? Someone told me this, but I don't know if it's Verizon still has them.
1:30:15> I was just there.
1:30:16> They still have flip phones.
1:30:17> I was like, I like it.
1:30:18> I like this fucking little thing that you just call people.
1:30:21> And I always like romanticized about going to that.
1:30:24> But my step was to go to a phone that has nothing on it, but text messages.
1:30:29> And that's been a few days.
1:30:30> Feeling good so far? Yeah, it's good.
1:30:33> You know, I still have my other phone that I use for social media.
1:30:37> But when I pick that motherfucker up, I start scrolling through YouTube and watching videos and scrolling through TikTok or Instagram and I don't have TikTok.
1:30:46> But I have I've tried threads for a little while, but I was like, fucking ghost town.
1:30:52> Went right back to X.
1:30:54> I live on a ranch during the weekends and there's not a fight in the house, but there's no cell phone coverage anywhere else.
1:31:01> And it's every week, I forget how nice it is and what a change it is to go for a walk.
1:31:12> Yeah, no cell phone coverage.
1:31:14> It's good for your mind.
1:31:15> For it's unbelievable for your mind.
1:31:17> And I think we have like so quickly lost something.
1:31:21> Like out of service just doesn't happen.
1:31:24> That doesn't have any airplanes anymore.
1:31:25> You know, like, but that like hours where your phone just cannot buzz.
1:31:34> Yeah.
1:31:35> No text message either.
1:31:36> Nothing.
1:31:37> I think that's a really healthy thing.
1:31:41> I dropped my phone once when I was in LaNai and I think it was the last time I dropped the phone.
1:31:46> The phone was like, we're done.
1:31:47> And it just started calling people randomly.
1:31:50> Like it would just call people and I'd hang it up and call another person.
1:31:53> I'd hang it up.
1:31:54> And I was showing my wife, I was like, look at this.
1:31:56> This is crazy.
1:31:56> It's just calling people.
1:31:57> And so the phone was broken.
1:31:59> And so I had an order of phone and we were on vacation for like eight days.
1:32:03> And it took three days for Apple to get me a phone.
1:32:06> I bet you had a great three days.
1:32:07> It was amazing.
1:32:09> It was amazing because when I was hanging out with my family, I was totally present.
1:32:14> There was no options.
1:32:15> And I wasn't thinking about checking my phone because it didn't exist.
1:32:19> I didn't have one.
1:32:21> And there was an alleviation of again, what Sean was talking about, that low level of anxiety, this sort of like, that you have when you always want to check your phone.
1:32:34> Yeah, I think, I think that thing, it's so bad.
1:32:37> We have not figured out yet, like the technology has moved so fast.
1:32:42> Biology moves very slowly.
1:32:44> We have not figured out how we're going to function in a society and get those occasional times when your phone is broken for three days or you go for a walk with no service.
1:32:53> But it's like, I very much feel like my phone controls me, not the other way around.
1:33:03> And I hate it, but I haven't figured out what to do about it.
1:33:07> Well, that's what I'm worried about with future technology is that this, which was so unanticipated, if you'd imagine a world when you'd imagine going up to someone in 1984 and pointing to a phone and saying one day that'll be in your pocket, it's going to ruin your life.
1:33:24> Like what? Like, yeah, one day people are going to be jerking off to that thing.
1:33:29> You're like, what? One day people are going to be watching people get murdered on Instagram.
1:33:33> I see so many murders on Instagram over the last few months.
1:33:35> Really? I've never seen a bit of bad timeline.
1:33:38> Me and my friend, Tom Segura, every morning, we text each other the worst things that we find on Instagram.
1:33:44> Why? For fun.
1:33:45> He's a comedian or a growth comedian.
1:33:47> That's fun to you.
1:33:48> Yeah.
1:33:48> This is fucking just ridiculous.
1:33:51> I mean, I mean, just crazy car accidents.
1:33:54> People get gored by bulls and like every, like we try to top each other.
1:33:59> So every day he's setting me the most every day when I wake up and I check, Tom, fuck, what are you not? You know, can you explain what's fun about that? Well, he's a comic and I'm a comic and comics like chaos.
1:34:12> We like, we like ridiculous, outrageous shit that is just so far beyond the norm of what you experience in a regular day.
1:34:22> Just and also the understanding of the wide spectrum of human behavior.
1:34:29> If you're a nice person and you surround yourself with nice people, you very rarely see someone get shot.
1:34:35> You very rarely see people get stabbed for no reason randomly on the street, but on Instagram, you see that every day.
1:34:43> And there's something about that.
1:34:46> We're just reminds you, oh, we're crazy.
1:34:50> Like the human species, like there's a certain percentage of us that are just off the rails and just out there, just causing chaos and jumping dirt bikes and landing on your neck and all that stuff is out there.
1:35:05> Even to hear that makes me like physically like, I know that happens, of course.
1:35:09> Mm-hmm.
1:35:09> And I know like not looking at it doesn't make it not happen.
1:35:14> Right.
1:35:15> But it makes me so uncomfortable and I'm happy to watch.
1:35:17> Oh, yeah, it makes me uncomfortable too.
1:35:19> But yeah, we do it to each other every day.
1:35:20> And it's not good.
1:35:24> It's definitely not good, but it's also I'm not going to stop.
1:35:26> It's fun, but why is it fun? It's fun because it's my friend Tom and we're both kind of the same in that way, which just look at that.
1:35:34> Look at this.
1:35:34> That I get.
1:35:35> Look at this.
1:35:35> And it's just a thing we started doing a few months ago.
1:35:38> It just can't stop.
1:35:39> And Instagram has like learned that you do that.
1:35:42> So just keep showing you more and more.
1:35:43> Instagram knows when I my search page is a mess.
1:35:46> When I go to the discover page.
1:35:48> Oh, it's just crazy.
1:35:50> But the thing is that it shows up in your feed too.
1:35:53> That's what I understand about the algorithm.
1:35:54> It shows it knows your fucked up.
1:35:56> So it shows up in your feed of things like even if they're not people I follow, but Instagram shows them to me anyway.
1:36:04> I heard an interesting thing a few days ago by Instagram and the feed.
1:36:08> Which is if you use it at off hours, when they have more processing capability available, because less people are using it, you get better recommendations.
1:36:15> So your feed will be better in like the middle of the night.
1:36:18> What is better though? Doesn't your feed more addictive to you or whatever? Right.
1:36:23> So for me, better would be more murders, more animal attacks.
1:36:27> Sounds horrible.
1:36:28> It's horrible.
1:36:29> It's, but it's just, it seems to know that's what I like.
1:36:33> It seems to know that that's what I interact with.
1:36:36> So it's just sending me that most of the time.
1:36:39> Yeah, that probably has all kinds of crazy psychological.
1:36:44> I'm sure.
1:36:44> Yeah, I'm sure that's also one of the reasons why I want to get rid of it and move away from it.
1:36:48> Yeah.
1:36:49> So maybe, maybe it went too far.
1:36:52> I don't even know if it's too far, but what it is is it's showing me.
1:36:57> The darker regions of society, of civilization, of human behavior.
1:37:04> But you think we're about to edit all that out.
1:37:06> I wonder if that is a solution.
1:37:08> I really do because I don't think it's outside the realm of possibility.
1:37:13> If we really, truly can engineer that.
1:37:16> Like one of the talks about neural link that's really promising is people with spinal cord issues, injuries, people that can't move their body and being able to hot wire that where essentially it controls all these parts of your body that you couldn't control anymore.
1:37:35> And so that would be an amazing thing for people that are injured, for amazing thing for people that are, you know, they're paralyzed.
1:37:44> They have all sorts of neurological conditions.
1:37:46> That is probably one of the first.
1:37:49> And that's what Elon's talked about as well, when the first implementations, the restoration of sight, you know, cognitive function enhanced from people that have brain issues.
1:38:00> That's tremendously exciting.
1:38:03> Yeah.
1:38:04> And like many other technologies, I don't think we can stop neural in our faces, nor because of the like great good that's going to happen along the way.
1:38:12> But I also don't think we know where it goes.
1:38:14> It's Pandora's box for sure.
1:38:16> And I think when we open it, it's just we're not going to go back, just like we're not going to go back to no computers without some sort of natural disaster.
1:38:25> By the way, I mean, this is a great compliment.
1:38:27> You are one of the most neutral people I have ever heard talk about the merge coming.
1:38:33> You're just like, yeah, I think it's going to happen.
1:38:35> You know, it's be good in these ways, bad in these ways, but you seem like unbelievably neutral about it, which is always something I admire.
1:38:43> I try to be as neutral about everything as possible, except for corruption, which I think is just like one of the most massive problems with the way our culture is governed.
1:38:56> I think corruption is just a and the influence of money is just a giant, terrible issue.
1:39:02> But in terms of like social issues and in terms of the way human beings believe and think about things, I try to be as neutral as possible.
1:39:12> Because I think the only way to really, truly understand the way other people think about things is try to look at it through their mind.
1:39:19> And if you have this inherent bias and this.
1:39:22> You have this like very rigid view of what's good and bad and right and wrong.
1:39:31> I don't think that serves you very well for understanding why people differ.
1:39:36> So I try to be as neutral and as objective as possible when I look at anything.
1:39:41> This is a skill that I've learned.
1:39:43> This is not something I had in 2009 when I started this podcast.
1:39:46> This podcast, I started just fucking around with friends and I had no idea what it was.
1:39:51> I mean, there's no way I could have ever known.
1:39:53> And but also I had no idea what it was going to do to me and as far as the evolution of me as a human being.
1:40:01> I am so much nicer.
1:40:02> I'm so much more aware of things.
1:40:05> I'm so much more conscious of the way other people think and feel.
1:40:09> I'm just a totally different person than I was in 2009, which is hard to recognize.
1:40:16> It's hard to believe.
1:40:17> That's really cool.
1:40:17> And that is just an inevitable consequence of this unexpected education that I've received.
1:40:25> Did the empathy kind of like come on linearly? Yeah.
1:40:28> That was not a.
1:40:29> No, it just came.
1:40:30> It came on recognized.
1:40:32> Well, first of all, it came on recognizing that the interact the negative interactions on social media that I was doing.
1:40:39> They didn't help me.
1:40:40> They didn't help the person.
1:40:42> And then having compassion for this person that's fucked up or done something stupid.
1:40:46> Like, it's not good to just dunk on people.
1:40:48> Like, there's no benefit there other than to give you some sort of social credit and get a bunch of likes.
1:40:53> It didn't make me feel good.
1:40:55> Like that's not good.
1:40:57> And then also a lot of psychedelics.
1:40:59> A ton of psychedelic experiences from 2009 on and with everyone, a greater understanding of the impact.
1:41:06> Like I had one recently.
1:41:07> And when I had the one recently, like the overwhelming message that I was getting through this was that everything I say and do ripples off into all the people that I interact with.
1:41:24> And then if I'm not doing something with at least the goal of overall good or overall understanding that I'm doing bad and that that bad is a real thing as much as you try to ignore it because you don't interface with it instantly.
1:41:41> And you're still creating unnecessary negativity.
1:41:47> And that I should avoid that as much as possible.
1:41:50> It was like an overwhelming message that this cycle.
1:41:54> The psychedelic experience was giving me.
1:41:56> And I took it because I was just particularly anxious that day about the state of the world, particularly anxious about Ukraine and Russia and China and the political system that we have in this country and this incredibly polarizing way that the left and the right engage with each other.
1:42:19> And God, it just seems so just tormented.
1:42:24> And so I was just, some days I just get, I think too much about it.
1:42:29> I'm like, I need something.
1:42:30> Yeah.
1:42:31> Crack me out of this.
1:42:32> So I took the psychedelics.
1:42:34> Are you surprised psychedelic therapy has not made from what you thought would happen in the early 2010s? Don't are you surprised it has not made more progress sort of on a path to legalization as a medical treatment? No.
1:42:48> No, I'm not because there's a lot of people that don't want it to be in place.
1:42:53> And those people have tremendous power over our medical system and over a regulatory system.
1:42:58> And those people have also not experienced these psychedelics.
1:43:02> There's very few people that have experienced profound psychedelic experiences that don't think there's an overall good for those things.
1:43:10> So the problem is you're having these laws and these rules implemented by the people who are completely ignorant about the positive effects of these things.
1:43:21> And if you know the history of psychedelic prohibition in this country, it all took place during 1970 and it was really to stop the civil rights movement.
1:43:33> And it was really to stop the anti-war movement.
1:43:36> And they tried to find a way to make all these things that these people were doing that was causing them to thinking these very different ways, is to tune in, turn on, drop out.
1:43:47> They just wanted to put a fucking halt to that.
1:43:49> What better way to lock everyone who participates in that in cages? Find the people who are producing it, lock them in cages, put them in jail for the rest of their life, make sure it's illegal, arrest people, put the bus on television, make sure that people are aware.
1:44:03> And then there's also you connect it to drugs that are inherently dangerous for society and detrimental, the fentanyl crisis, you know, the cocaine crisis that experienced in the 90s, like all of those things, they're under the blanket of drugs.
1:44:18> Psychedelic drugs are also talked about like drugs, even though they have these profound spiritual and psychological changes that they, you know, invite them.
1:44:31> I remember when I was in elementary school and I was in like drug education, they talked about, you know, marijuana is really bad because it's a gateway to these other things.
1:44:39> And there's this bad one, that bad one, heroin, whatever.
1:44:41> And the very end of the line, the worst possible thing is LSD.
1:44:44> Did you take LSD and go, oh, they're lying.
1:44:49> Psychedelic therapy was definitely one of the most important things in my life.
1:44:54> And I, I assumed given how powerful it was for me, like I, you know, I struggled with like all kinds of anxiety and other negative things into like, watch all of that go away in like that.
1:45:09> Like I traveled to another country for like a week, did a few things, came back.
1:45:14> And totally different person.
1:45:16> And I was like, I've been lied to my whole life.
1:45:18> Yeah.
1:45:19> I'm so grateful that this happened to me now.
1:45:20> Talked a bunch of other people, all similar experiences.
1:45:23> I assume this was a while ago.
1:45:25> I assumed it was, and I was like, you know, very interested in what was happening in the US.
1:45:31> I was like, particularly like looking at where MDMA and silo, cyber, and where on the path.
1:45:37> And I was like, all right, this is going to get through like this is, and this is going to like change the mental health of a lot of people in a really positive way.
1:45:44> And I am surprised we have not made faster progress there, but I'm still optimistic we will.
1:45:48> Well, we have made so much progress from the time of the 1990s.
1:45:54> In the 1990s, you never heard about psychedelic retreats.
1:45:58> You never heard about people taking these vacations.
1:46:01> You never heard about people getting together in groups and doing these things and coming back with these profound experiences that they relate to other people and literally seeing people change, seeing who they are, change, seeing people become less, less selfish, less toxic, less mean, you know, you, and more empathetic and more understanding.
1:46:23> Yeah.
1:46:24> It's, I mean, I can only talk about it from a personal experience.
1:46:28> It's been a radical change in my life.
1:46:30> But as well as again, having all these conversations with different people, I feel so fortunate to be able to do this, that I've had so many different conversations with so many different people that think so differently and so many exceptional people that have accomplished so many incredible things.
1:46:44> And you get to sort of understand the way their mind works and the way they see the world, the way they interface with things.
1:46:51> It's awesome.
1:46:52> It's pretty fucking cool.
1:46:54> And that is one of the cooler things about being a human that you can find a way to mitigate all the negative aspects of the monkey body.
1:47:04> And that there are tools that are in place.
1:47:06> But unfortunately, in this very prohibitive society, this society of prohibition, we were denied those and we're denied ones that have never killed anybody, which is really bizarre when, you know, OxyContin can still be prescribed.
1:47:23> What's the deal with why we can't make, if we leave like why we can't get these medicines that have transformed people's lives, like more available? What's the deal with why we can't stop the opioid crisis? Or like, it seems like just an unbelievable crisis for San Francisco.
1:47:43> You remember when the beginning of the conversation, when you said that AI will do a lot of good overall good, but also not no harm.
1:47:52> If we legalize drugs, all drugs, that would do the same thing.
1:47:59> Would you advocate to legalize all drugs? It's a very complicated question because I think you're going to have a lot of addicts that wouldn't be addicts.
1:48:07> You're going to have a lot of people's lives destroyed because it's legal.
1:48:10> There's a lot of people that may not be psychologically capable of handling things.
1:48:14> Maybe they already have like that's the thing about psychedelics.
1:48:17> They do not ever recommend them for people that have a slippery grasp on reality as it is.
1:48:22> People that are struggling, people that are already on a bunch of medications that allow them to just keep a steady state of existence in the normal world.
1:48:32> If you just fucking bombard them with psilocybin, who knows what kind of an effect that's going to have and whether or not they're psychologically too fragile to recover from that.
1:48:43> I mean, there's many, many stories of people taking too much acid and never coming back.
1:48:47> Yeah.
1:48:49> Yeah, these are like powerful doesn't seem to like begin to cover it.
1:48:57> Right.
1:48:57> Yeah.
1:48:58> But there's also what is it about humans that are constantly looking to perturb their normal state of consciousness constantly, whether it's we're both drinking coffee, you know, people smoke cigarettes.
1:49:10> They they they do all they take out or all they do all sorts of different things to change and enhance their normal state of consciousness.
1:49:18> It seems like whether it's meditation or yoga, they're always doing something.
1:49:22> Yeah.
1:49:23> They try to get out of their own way or get in their own way or distract themselves from the pain of existence.
1:49:29> And it's it seems like a normal part of humans and even monkeys, like vervet monkeys get addicted to alcohol.
1:49:37> They get addicted to fermented fruits and alcohol and they become drunks and alcoholics.
1:49:41> It just it's what do you think is the deep lesson there? Well, we're not happy exactly.
1:49:48> You know, we're and then some things can make you happy sort of for like a couple of drinks makes you so happy for a little bit until you're an alcoholic until you destroy your liver, until you crash your car, until you're, you know, you're involved in some sort of a violent encounter that you would never be involved with if you weren't drunk.
1:50:06> You know, I love caffeine, which clearly is a drug alcohol like I like, but I often am like, yeah, this is like, yeah, you know, this is like doling me and I wish I hadn't had this drink.
1:50:21> And then other stuff like I mostly would choose to avoid.
1:50:26> But that's because you're smart.
1:50:28> Um, and you're probably aware of the pros and cons and you're also probably aware of how it affects you and what's doing good for you and what is detrimental to you.
1:50:38> But that's a decision that you can make as an informed human being that you're not allowed to make if everything's illegal.
1:50:45> Right.
1:50:46> Yeah.
1:50:48> Right.
1:50:48> And also when things are illegal criminals sell those things because it's you're not tampering the desire by making it illegal.
1:50:58> You're just making access to it much more complicated.
1:51:01> What I was going to say is if fentanyl is really great, I don't want to know.
1:51:04> Apparently it is.
1:51:06> Apparently it is.
1:51:07> Yeah.
1:51:07> Peter Berg was on the podcast and he produced that painkiller documentary for Netflix about the the the docu drama about the Sackler family.
1:51:15> It's an amazing piece.
1:51:18> But he said that he took Oxycontin once recreationally and was like, Oh my God, it's amazing.
1:51:25> He's like, keep this away from me.
1:51:28> It feels so good.
1:51:29> Yeah.
1:51:30> And that's part of the problem is that, yeah, it will wreck your life.
1:51:33> Yeah, it will it will capture you.
1:51:35> But it's just so unbelievable.
1:51:36> But the feeling like what had Lenny Burst describe it? I think he described heroin as getting a warm hug from God.
1:51:44> Yeah, I think the feeling that it gives you is probably pretty spectacular.
1:51:49> I don't know if legalizing that is going to solve the problems, but I do know that another problem that we're not paying attention to is the rise of the cartels and the fact that right across our border where you can walk, there are these enormous, enormous organizations that make who knows how much money, untold uncalculable amounts of money, selling drugs and bringing them into this country.
1:52:17> And one of the things they do is they put fentanyl and everything to make things stronger and they do it for like street Xanax.
1:52:24> There's people that have overdosed thinking they're getting Xanax and they fucking die for fentanyl.
1:52:28> Yeah, they do it with cocaine.
1:52:31> Of course, they do it with everything.
1:52:33> There's so many things that have fentanyl in them and they're cut with fentanyl because fentanyl is cheap and insanely potent.
1:52:42> And that wouldn't be a problem if things were legal.
1:52:44> So would you net out towards saying, all right, let's just leave it.
1:52:47> Yeah, I would I would net out towards that, but I would also put into place some serious mitigation efforts like in terms of counseling drug addiction and Ibogaine therapy, which is another thing that someone was just telling me about how transformative this was for them.
1:53:01> Yeah, I haven't experienced that personally, but Ibogaine for many of my friends that have had pill problems and I have a friend, my friend, Ed Clay, who started an Ibogaine center in Mexico because he had an injury and he got hooked on pills and he couldn't kick it.
1:53:18> Did Ibogaine gone one time done, one time done, 24 hour super uncomfortable experience.
1:53:24> It's supposed to be a horrible experience, right? Yeah, it's supposed to be not very recreational, not exactly something you want to do on the weekend with friends.
1:53:31> It's something you do because you're fucked and you need to figure out how to get out of this fuckness.
1:53:35> And that like we think about how much money is spent on rehabs in this country and what's the relapse rate? It's really high.
1:53:43> I mean, I have many friends that have been to rehab for drug and alcohol abuse.
1:53:48> And quite a few of them went right back to it.
1:53:52> Quite a few.
1:53:53> It doesn't seem to be that effective.
1:53:54> It seems to be effective to people when people have like they really hit rock bottom and they have a strong will and then they get involved in a program, some sort of a 12 step program, some sort of an narcotics anonymous program.
1:54:05> And then they get support from other people and they eventually build this foundation of other types of behaviors and ways to find other things, to focus on to the whatever aspect of their mind that allows them to be addicted to things.
1:54:20> Now it's focused on exercise, meditation, yoga, whatever it is, that's your new addiction and it's a much more positive and beneficial addiction.
1:54:29> But the reality of the physical addiction that there are mitigation efforts, like there's so many people that have taken psilocybin and completely quit drugs, completely quit cigarettes, completely quit a lot because they realize like, oh, this is what this is.
1:54:44> This is why I'm doing this.
1:54:46> Yeah, that's, that's why I was more optimistic that the world would have made faster progress towards acceptance of, you hear so many stories like this.
1:54:55> I would say like, all right, clearly a lot of our existing mental health treatment at best doesn't work.
1:55:01> Clearly our addiction programs are ineffective.
1:55:05> If we have this thing that in every scientific study or most scientific studies we can see is delivering these like unbelievable results, it's going to happen.
1:55:15> Yeah.
1:55:16> And it, yeah, I still am excited for it.
1:55:20> I still think it'll be a transformative positive development, but it'll change politics.
1:55:25> It'll, it'll absolutely change the way we think of other human beings.
1:55:30> It'll absolutely change the way we think of society and culture as a whole.
1:55:33> It'll absolutely change the way people interact with each other if it's, if it becomes legalized and it's slowly becoming legalized.
1:55:40> Like think of marijuana, which is like, you know, the gateway drug.
1:55:43> Marijuana is now legal recreationally in how many states? 23 and then medically and many more.
1:55:53> And, you know, it's really easy to get a license medically.
1:55:58> In California, it's just, I got one in 1996.
1:56:02> You used to be able to just go somewhere and go, I got a headache.
1:56:04> That's it.
1:56:07> Yeah, I get headaches.
1:56:08> I'm in pain a lot, you know, I do a lot of martial arts.
1:56:11> I'm always injured.
1:56:11> I need some medication.
1:56:13> I don't like to get pain pills.
1:56:14> BAM.
1:56:14> You got a legal prescription for weed.
1:56:16> I used to have to go to Inglewood to get it.
1:56:18> I used to have to go to the hood to the Inglewood Wellness Center.
1:56:21> And I was like, this is crazy.
1:56:24> Like marijuana is now kind of sort of legal.
1:56:27> And then in 2016, it became legal in California recreationally.
1:56:32> And it just changed everything.
1:56:34> I have all these people that were like right wing people that were taking edibles to sleep.
1:56:39> You know, I'm like, this is because now that it's legal, they thought about it in a different way.
1:56:44> And I think that that drug, which is a fairly mild psychedelic also has enhancing effects.
1:56:52> It makes people more compassionate.
1:56:54> It makes people more kind and friendly.
1:56:56> It's sort of the opposite of a drug that that enhances violence.
1:57:01> It doesn't enhance violence at all.
1:57:02> It's just it does the alcohol does that cocaine does that.
1:57:05> Just say a thing that'll make me very unpopular.
1:57:07> I hate marijuana.
1:57:08> It does not sit well with me at all.
1:57:10> What does it do to you that you don't like? It makes me tired and slow for a long time after it.
1:57:14> My thing also is biological variability is right.
1:57:18> Like some people, like my wife, she does not do well with alcohol.
1:57:22> She can get drunk off one drink, but it's biological.
1:57:25> Like she she got some sort of a genetic to forget what it's called.
1:57:28> Something about Billy Rubin.
1:57:29> Like some something that her body just doesn't process alcohol very well.
1:57:33> So she's a cheap date.
1:57:34> Oh, all I meant is that genetically I got whatever the mutation is that makes it an unpleasant experience.
1:57:39> Yeah.
1:57:40> But what I was saying is for me, that's the opposite.
1:57:41> Alcohol doesn't bother me at all.
1:57:43> I could I could drink three, four drinks and I'm sober in 20 minutes.
1:57:46> And my body just my liver is like a blast.
1:57:49> Just goes through it.
1:57:50> Just goes right through it.
1:57:51> I can sober up real quick, but I also don't need it.
1:57:55> Like I'm doing sober October, like for the whole month.
1:57:58> I don't feel good.
1:57:58> Yeah.
1:57:59> Did shows last night? Great.
1:58:00> No problems.
1:58:01> Not having alcohol doesn't seem to bother me at all.
1:58:04> But I do like it.
1:58:06> I do like it a glass of wine.
1:58:08> It's a nice thing at the end of the day.
1:58:09> I like it.
1:58:10> Speaking of that and psychedelics in general, I, you know, many cultures have had a place for some sort of psychedelic time in someone's life or rite of passage.
1:58:21> But as far as I can tell, most of them are under.
1:58:24> There's some sort of ritual about it.
1:58:28> And I do worry that.
1:58:30> And I think these these things are so powerful that I worry about them just being like kind of.
1:58:36> Yeah, all over the place all the time.
1:58:39> Yeah.
1:58:39> And I hope that we as a society, because I think this is not going to happen even if it's slow, find a way to treat this with.
1:58:47> The respect that it needs.
1:58:50> Yeah.
1:58:51> We'll see how that goes.
1:58:52> Agreed.
1:58:53> Yeah.
1:58:54> I think set and setting is very important.
1:58:57> And thinking about what you're doing before you're doing it, why you're doing it.
1:59:02> Like I was saying the other night when I had this psychedelic experience, I was just like, sometimes I just think too much about the world and that it's so fucked.
1:59:11> And you have kids and you wonder like, what, what kind of a world are they going to grow up in? And what is and it was just one of those days where I was just like, God, there's so much anger and so much this and that.
1:59:21> And then it's just it took it away from me the rest of the day.
1:59:25> Like that night I was so friendly and so happy and I just wanted to hug everybody.
1:59:29> I just really got it.
1:59:31> I go, Oh my God, that does not think about it wrong.
1:59:34> Do you think the anger in the world is way higher than it used to be? Or we just it's like all these dynamics from social media we were talking about.
1:59:41> I think the dynamics in social media certainly exacerbated anger in some people.
1:59:46> But I think anger in the world is just a part of frustration, inequality, problems that are so clear but are not solved and all the issues that people have.
2:00:00> I mean, it's not a coincidence that a lot of the mass violence that you're seeing in this country, mass looting and all these different things are being done by poor people.
2:00:08> Do you think AGI will be equalizing force for the world or further inequality? I think it would be it depends on how it's implemented.
2:00:16> My my concern is again, what we're talking about before with some sort of a neural interface that it will increase your ability to be productive to a point where you can control resources so much more than anyone else and you will be able to advance your your economic portfolio and your influence on the world through that your amount of power that you can acquire.
2:00:39> It will before the other people can get involved because I would imagine financially it'll be like cell phones in the beginning.
2:00:49> You remember when the movie Wall Street when he had that big brick cell phone, I was like, look at him.
2:00:55> He's out there on the beach with a phone.
2:00:57> That was crazy.
2:00:58> No one had one of those things back then.
2:00:59> And they were so rare.
2:01:01> I got one in 1994 when I first moved to California and I thought I was living in the fucking country.
2:01:06> No, it was a Motorola Star TAC.
2:01:08> That was a cool phone.
2:01:09> I actually had one on in my car in 1988.
2:01:12> I was one of the first people to get a cell phone.
2:01:14> I got one in my car.
2:01:16> And it was great because my friend, my friend Bill Blumenreich, who runs the comedy connection, he would call me because he knew he could get a hold of me.
2:01:25> Like if someone got sick or fell out, I could get a gig because he could call me.
2:01:29> So I was in my car.
2:01:30> I was like, Joe, what are you doing? Do you have a spot tonight? And I'm like, no, I'm open.
2:01:34> He's like, fantastic.
2:01:35> And so he'd give me gigs.
2:01:37> So I got a bunch of gigs through this phone where it kind of paid itself.
2:01:41> But I got it just because it was cool.
2:01:44> Like I could drive down the street and call me, but dude, I'm driving and I'm calling you like it was nuts to be able to drive.
2:01:50> And I had a little antenna, little squirrely.
2:01:52> I went a little square with a little tailbone with a tailbone on my car on the roof of the car.
2:01:55> But now everyone has one.
2:01:58> You know, you can go to a third world country and, you know, people in small villages have phones.
2:02:04> It's super common.
2:02:07> It's everywhere.
2:02:08> Essentially more people have phones than don't have phones.
2:02:10> There's more phones than there are human beings, which is pretty fucking wild.
2:02:15> And I think that that initial cost problem, it's going to be prohibitively expensive initially.
2:02:24> And the problem is the wealthy people are going to be able to do that.
2:02:27> Yeah.
2:02:27> And then the real crazy ones that wind up getting the holes drilled in their head.
2:02:31> And if that stuff is effective, maybe it's not, maybe there's problems with generation one, but generation two is better.
2:02:37> There's going to be a time where you have to enter into the game.
2:02:42> There's going to be a time where you have to sell your stocks.
2:02:44> Like, you don't don't wait too long.
2:02:45> Hang on there.
2:02:47> Go.
2:02:48> And once that happens, my concern is that the people that have that will have such a massive advantage over everyone else that the gap between the haves and have nots will be even further.
2:03:02> And it'll be more polarized.
2:03:04> This is something I've changed my mind on.
2:03:06> I, you know, someone, it opened the eyesets me a few years ago.
2:03:10> Like you really can't just let some people merge without a plan because it could be such an incredible distortion of power.
2:03:19> And then we're going to have to have some sort of societal discussion about this.
2:03:23> Yeah.
2:03:23> That seems real.
2:03:25> That seems like, yeah, especially if it's as effective as AGI is or as, excuse me, chat GPT is chat GPT is so amazing.
2:03:39> When you enter into it information, you ask it questions and it can give you answers and you could ask it to code a website for you.
2:03:45> And it doesn't instantly and it solves problems.
2:03:47> I literally you would have to take decades to try to solve and it gets to it right away.
2:03:53> This is the dumbest it will ever be.
2:03:55> Yeah, that's what's crazy.
2:03:57> That's what's crazy.
2:03:58> So imagine something like that, but even more advanced multiple stages of improvement and innovation forward.
2:04:07> And then it interfaces directly with the mind, but it only does it with the people that can afford it.
2:04:12> Yeah.
2:04:13> And those people are just regular humans.
2:04:15> So they haven't been there's they haven't been enhanced.
2:04:19> We haven't we haven't evolved physically.
2:04:23> We still have all the human reward systems in place.
2:04:25> We're still basically these territorial primates.
2:04:28> And now we have, you know, you just imagine some fucking psychotic billionaire who now gets this implant and decides to just completely hijack our financial systems, acquire all the resources, set into place regulations and influences that only benefit them and then make sure that they can control it from their own.
2:04:51> How much do you think this actually though, even requires like a physical implant or like a physical merge versus just some people have access to GPT seven and can spend a lot on the inference compute for it.
2:05:04> And some don't.
2:05:06> I think that's going to be very transformative too.
2:05:08> But my thought is that once I mean, we have to think of what are the possibilities of a neural enhancement? If you think about the human mind and how the human mind interacts with the world, how you interact with language and thoughts and facts and something that is exponentially more powerful than that.
2:05:33> But it also allows you to use the same emotions, the same ego, the same desires and drives, jealousy, lust, hate, anger, all of those things.
2:05:46> But with this God-like power, when one person can read minds and other people can't, when one person has a completely accurate forecast of all of the trends in terms of stocks and resources and commodities and they can make choices based on those.
2:06:06> I totally see all of that.
2:06:08> The only thing I'm, I feel a little confused about is, you know, human talking and listening bandwidth or typing and reading bandwidth is not very high.
2:06:22> But it's high enough for if you can just say like, tell me everything that's going to happen in the stock market.
2:06:27> If I want to go make all the money, what should I do right now? And then it just shows you on the screen.
2:06:32> Even without a neural interface, you're kind of a lot of the way to the scenario you're describing.
2:06:37> Sure, with stocks, or with like, you know, tell me how to like invent some new technology that will change the course of history.
2:06:45> Yeah.
2:06:46> Yeah.
2:06:48> All those things.
2:06:51> Like, I think what somehow matters is access to massive amounts of computing power, especially like differentially massive amounts, maybe more than the interface itself.
2:07:00> I think that certainly is going to play a massive factor in the amount of power and influence a human being has, having access to that.
2:07:09> My concern is that what neural interfaces are going to do is now you're not a human mind interacting with that data.
2:07:20> Now you are some massively advanced version of what a human mind is.
2:07:29> And it has just profound possibilities that we can't even imagine.
2:07:37> We can imagine, but we can't.
2:07:40> Yeah.
2:07:40> We can't truly conceptualize them because we don't have the context.
2:07:46> We don't have that ability and that possibility currently.
2:07:49> We could just we can just guess.
2:07:51> But when it does get implemented, that you're dealing with a completely different being.
2:07:58> The only true thing is I can say is I don't know.
2:08:04> Yeah.
2:08:04> Do you wonder why it's you? Do you ever think like, how am I at the forefront of this spectacular change? Um.
2:08:17> Well, first of all, I think it's very much like, I think this is, you could make the statement from many companies, but none is it as true for his opening eyes.
2:08:31> Like the CEO is far from the most important person in the company.
2:08:34> Like in our case, there's a large handful of researchers, each of which are individually more critical to the success we've had so far and that we will have in the future than me.
2:08:44> Um, but even that, and I bet those people like really are like, hmm, this is weird to be them, but.
2:08:54> It's certainly weird enough for me that it like ups my simulation hypothesis probability someone.
2:08:59> Mmm.
2:09:01> What, when, if you had a give a guess, what? When you think about the possibility of simulation theory, what, what, what kind of percentage do you, I've never known how to put any number on it.
2:09:14> Like, you know, it's see every argument that I've read written explaining why it's like super high probability.
2:09:21> That all seems reasonable to me feels impossible to reason about the.
2:09:25> What about you? Yeah.
2:09:27> Same thing.
2:09:28> I go maybe, but it's still what it is.
2:09:32> And I have to.
2:09:33> That's, that's the main thing is I think it doesn't matter.
2:09:35> I think it's like a, okay.
2:09:36> It kind of, it kind of, it definitely matters, I guess, but there's not a way to know currently and also what matters.
2:09:46> Well, if, if this really is, I mean, our inherent understanding of life is that we are these biological creatures that interact with other biological creatures.
2:09:55> We, we may in breed and that this creates more of us and that hopefully as society advances and we acquire more information, more understanding and knowledge, this next version of society will be superior to the version that preceded it, which is just how we look at society today.
2:10:13> Nobody wants to live in 1860 where you died of a cold and there's no cure for infections.
2:10:19> It's much better to be alive now.
2:10:21> You're like just inarguably, right? There's unless you really do prefer the simple life that you see on Yellowstone or something like there's, it's like what we're dealing with now in term, first of all, access to information, the, the lack of ignorance.
2:10:39> If you're, if you choose to seek out information, you have so much more access to it now than ever before.
2:10:47> That's so cool.
2:10:47> And over time, like if you go back to the beginning of written history to now, one of the things that is clearly evident is the more access to information, the better choices people can make.
2:11:00> They don't always make better choices, but they certainly have much more of a potential to make better choices with more access to information.
2:11:08> You know, we think that this is just this biological thing, but imagine if that's not what's going on.
2:11:14> Imagine if this is a program and that you are just consciousness that's connected to this thing that's creating this experience that is indistinguishable from what we like to think of as a real biological experience from carbon-based life forms interacting with solid physical things in the real world.
2:11:38> It's still unclear to me what I'm supposed to do differently or think of different ways.
2:11:44> Yeah, there's no answer.
2:11:45> Yeah, you're 100% right.
2:11:46> What can you do differently? I mean, if you exist as if it's a simulation, if you just live your life as if it's a simulation, is that I don't know if that's the solution.
2:11:57> You know, I don't, I think, I mean, it's real to me, no matter what.
2:12:01> Mm-hmm.
2:12:02> True.
2:12:03> Yeah.
2:12:03> I'm going to live it that way.
2:12:05> And that will be the problem with an actual simulation if and when it does get implemented.
2:12:10> Yeah.
2:12:11> If we do create an actual simulation that's indistinguishable from real life, like, what are the rules of the simulation? What are the, how does it work? Is that simulation fair and equitable and much more reasonable and peaceful? Does, is there no war in that simulation? Should we all agree to hook up to it? Because we will have a completely different experience in life.
2:12:35> And all the, the, the angst of crime and violence and the things that we truly are terrified of, there will be non-existent in the simulation.
2:12:44> Yeah.
2:12:46> I mean, if we keep going, it seems like if we just look, if you can extrapolate from where VR is now, did you see the podcast that Lex Friedman did with Mark Zuckerberg? I saw some clips, but I haven't got to watch all this.
2:13:00> I mean, I think it's a good thing to see.
2:13:05> I think it's a good thing to see.
2:13:07> I think it's a good thing to see.
2:13:09> I think it's a good thing to see.
2:13:11> I think it's a good thing to see.
2:13:13> I think it's a good thing to see.
2:13:15> I think it's a good thing to see.
2:13:17> I think it's a good thing to see.
2:13:19> I think it's a good thing to see.
2:13:21> I think it's a good thing to see.
2:13:23> I think it's a good thing to see.
2:13:25> I think it's a good thing to see.
2:13:27> The inevitable thing to me is that we will create a life form that is an artificial, intelligent life form that's far more advanced than us and once it becomes sentient, it will be able to create a far better version of itself.
2:13:42> And then as it has better versions of itself, it will keep going.
2:13:48> And if it keeps going, it will reach God-like capabilities.
2:13:53> The complete understanding of every aspect of the universe and the structure of it itself.
2:14:01> How to manipulate it, how to travel through it, how to communicate.
2:14:07> And that if we keep going, if we survive 100 years, 1000 years, 10 years, and we're still on this same technological exponential increasing in capability path, that's God.
2:14:22> We become something like God.
2:14:25> And that might be what we do.
2:14:27> That might be what intelligent, curious, innovative life actually does.
2:14:32> It creates something that creates the very universe that we live in.
2:14:38> That creates the next simulation.
2:14:40> Yeah, maybe that's the birth of the universe itself, is creativity and intelligence.
2:14:45> And that it all comes from that.
2:14:47> I just have this joke about the Big Bang.
2:14:50> Like, what if the Big Bang is just a natural thing? Like humans get so advanced that they create a Big Bang machine.
2:14:58> And then, you know, we're so autistic and riddled with Adderall that we have no concept or worry of the consequences.
2:15:05> And someone's like, "I'll fucking press it." And they press it and, "Shh, boom!" We start from scratch every 14 billion years.
2:15:13> And then that's what a Big Bang is.
2:15:18> I mean, I don't know where it goes, but I do know that if you looked at the human race from afar, if you were an alien life form, completely detached from any understanding of our culture, any understanding of our biological imperatives, and you just looked at, like, what is this one dominant species doing on this planet? It makes better things.
2:15:41> That's what it does.
2:15:42> Yeah, that I agree.
2:15:43> It goes to war.
2:15:44> It, you know, it steals.
2:15:46> It does a bunch of things that it shouldn't do.
2:15:48> It pollutes.
2:15:49> It does all these things that are terrible.
2:15:51> But it also consistently and constantly creates better things, whether it's better weapons going from the catapult to the rifle to the cannonballs to the rocket ships to the hypersonic missiles to nuclear bombs.
2:16:06> It creates better and better and better things.
2:16:09> That's the number one thing it does.
2:16:11> And it's never happy with what it has.
2:16:14> And you add that to consumerism, which is baked into us, and this desire, this constant desire for new or better things, well, that fuels that innovation because that gives it the resources that it needs to consistently innovate and constantly create newer and better things.
2:16:31> Well, if I was an alien life form, I was like, "Oh, what is it doing? It's trying to create better things." Well, what is the forefront of it? Technology.
2:16:39> Technology is the most transformative, the most spectacular, the most interesting thing that we create and the most alien thing.
2:16:46> The fact that we just are so comfortable that you can face time with someone in New Zealand, like instantly.
2:16:52> We can get used to anything pretty quickly.
2:16:54> Yeah.
2:16:55> Anything.
2:16:56> And take it for granted almost.
2:16:57> Yeah.
2:16:58> And well, if you were an alien life form and you were looking at us, you're like, "Well, what is it doing? Oh, it keeps making better things.
2:17:04> It's going to keep making better things." Well, if it keeps making better things, it's going to make a better version of a thinking thing.
2:17:11> And it's doing that right now.
2:17:12> Yeah.
2:17:13> And you're a part of that.
2:17:14> It's going to make a better version of a thinking thing.
2:17:16> Well, that better version of a thinking thing, it's basically now in the amoeba stage, just in the small multi-cellular life form stage.
2:17:24> Well, what if that version becomes a fucking Oppenheimer? What if that version, if it scales up so far that it becomes so hyper-intelligent that it is completely alien to any other intelligent life form that has ever existed here before? And it constantly does the same thing, makes better and better versions of it.
2:17:45> Well, where does that go? It goes to a God.
2:17:48> It goes to something like a God.
2:17:50> And maybe God is a real thing.
2:17:52> But maybe it's a real consequence of this process that human beings have of consistently, constantly innovating and constantly having this desire to push this envelope of creativity and of technological power.
2:18:11> I guess it comes down to maybe a definitional disagreement about what you mean by it becomes a God.
2:18:18> I can totally, I think it becomes something much, like unbelievably much smarter and more capable than we are.
2:18:26> And what does that thing become if that keeps going? And maybe the way you mean it as a God-like force is that that thing can then go create, can go simulate in a universe.
2:18:37> Yes.
2:18:38> Okay.
2:18:39> That I can resonate with.
2:18:40> Yeah.
2:18:41> I think whatever we create will still be subject to the laws of physics in this universe.
2:18:45> Right.
2:18:46> Yeah, maybe that is the overlying fabric that God exists in.
2:18:50> The God word is a fucked up word because it's just been so co-opted.
2:18:54> But I was having this conversation with Stephen Meyer who is a physicist.
2:19:00> I believe he's a physicist.
2:19:02> And he's also religious.
2:19:04> It was a real weird conversation, very fascinating conversation.
2:19:07> What kind of religion? In Christ.
2:19:09> Yeah, he even believes in the resurrection, which I found very interesting.
2:19:14> But it's interesting communicating with him because he has these little pre-designed speeches that he's encountered all these questions so many times.
2:19:27> That he has these very well-worded, very articulate responses to these things that I sense are like bits.
2:19:33> When I'm talking to a comic, they argue this bit on train travel.
2:19:39> They just don't.
2:19:40> They tell you the bit.
2:19:41> That's what it's like, he has bits on why he believes in Jesus and why he believes.
2:19:46> And very, very intelligent God.
2:19:48> But I propose the question when we're thinking about God.
2:19:52> What if instead of God created the universe, what if the universe is God and the creative force of all life and everything is the universe itself? Instead of thinking that there's this thing that created us.
2:20:06> This is like close to a lot of the Eastern religions.
2:20:08> I think this is an easier thing to wrap my mind around than any other religions for me.
2:20:13> And that is when I do psychedelics, I get that feeling.
2:20:17> I get that feeling like there's this insane soup of innovation and connectivity that exists all around us.
2:20:27> But our minds are so primal.
2:20:30> We're this fucking thing.
2:20:32> This is what we used to be.
2:20:35> What is that? There's a guy named Shane against the machine who's this artist who created this.
2:20:41> It's a chimpanzee skull that he made out of ziljan symbols.
2:20:44> So you see the little ziljan logo.
2:20:47> He left it on the back and he just made this dope art piece.
2:20:50> Cool.
2:20:51> It's just cool.
2:20:52> But I wonder if our limitations are that we are an advanced version of primates.
2:20:59> We're still, we still have all these things that we talk about jealousy and anxiety, lust, fear, fear of violence, all these things that are detrimental, but were important for us to survive and get to this point.
2:21:13> And that as time goes on, we will figure out a way to engineer those out.
2:21:19> And that as intelligent life becomes more intelligent and we create a version of intelligent life that's far more intelligent than what we are.
2:21:28> We're far more capable of what we are.
2:21:30> If that keeps going, if it just keeps going, I mean chat GPT.
2:21:35> Even if you go to chat GPT and go back to Socrates and show him that, explain to him that and show him a phone and put it on a phone and have access to it.
2:21:44> He'd be like, "What have you done? Like, what is this?" I bet he'd be much more impressed with the phone than chat GPT.
2:21:51> I think he would be impressed with the phone's abilities to communicate for sure, but then the access to information would be so profound.
2:21:58> I mean, back then, I mean, look, you're dealing with the time when Galileo was put on her house arrest because he had the gumption to say that the earth is not the center of the universe.
2:22:10> Well now we fucking know it's not.
2:22:12> Like, we have satellites.
2:22:14> We send literal cameras into orbit to take photos of things.
2:22:18> No, I totally get that.
2:22:20> I just meant that we kind of know what it's like to talk to a smart person.
2:22:24> And so in that sense, you're like, "Oh, all right.
2:22:26> I didn't think you could like talk to a not person and have them be person-like in some responses some of the time, but a phone.
2:22:32> Man, if you just like woke up after 2,000 years and there was like a phone, that would be a no model for that.
2:22:38> You didn't get to get there gradually." Yeah, no.
2:22:40> You didn't get it.
2:22:41> My friend Eddie Griffin has a joke about that.
2:22:45> He's about how Alexander Graham Bell had to be doing Coke.
2:22:48> He goes because only someone on Coke will be like, "I want to talk to someone who's not even here." And that's what a phone is.
2:22:58> Is that something Coke makes people want to do? I don't know.
2:23:00> I've never done Coke.
2:23:01> I would imagine it is.
2:23:02> It seems to me like it just makes people angry and chaotic.
2:23:06> Yeah, a little of that, but they also have ideas.
2:23:12> Yeah, I mean, back to this, where does it go? If it keeps going, it has to go to some impossible level of capability.
2:23:23> I mean, just think of what...
2:23:24> That I believe is going to happen.
2:23:26> What we're able to do now with nuclear power and nuclear bombs and hypersonic missiles, just the insane physical things that we've been able to take out of the human creativity and imagination and through engineering and technology implement these physical devices that are indistinguishable from magic if you brought them 500 years ago.
2:23:52> Yeah.
2:23:53> I think it's quite remarkable.
2:23:55> I think it's...
2:23:56> So keep going.
2:23:57> Keep going 100 years from now.
2:23:58> If we're still here, if something like us is still here, what can it do? In the same way that I don't think Socrates would have predicted the phone, I can't predict that.
2:24:09> No, I'm probably totally off.
2:24:11> But maybe that's also why comets exist.
2:24:13> Maybe it's a nice reset to just leave a few around, give them a distant memory of the utopian world that used to exist, have them go through thousands of years of barbarism, of horrific behavior, and then re-establish society.
2:24:29> I mean, this is the Younger Dryas Impact Theory that allowed 11 years ago at the end of the Ice Age that we were hit by multiple comets that caused the instantaneous melting of the ice caps over North America.
2:24:43> Flood everything.
2:24:44> Flooded everything.
2:24:45> The source of the flood myths from Epic of Gilgamesh and the Bible and all those things.
2:24:52> And also there's physical evidence of it.
2:24:54> When they do coarse samples, there's high levels of iridium, which is very common in space, very rare on Earth.
2:25:00> There's microdiamonds that are from impacts, and it's like 30% of the Earth, like there has evidence of this.
2:25:07> And so it's very likely that these people that are proponents of this theory are correct, and that this is why they find these ancient structures that they're now dating to like 11, 12 years ago when they thought people were hunter-gatherers.
2:25:19> And they go, okay, maybe our timeline is really off, and maybe this physical evidence of impacts.
2:25:24> Yeah, I've been watching that with interest.
2:25:25> Yeah.
2:25:26> Randall Carlson is the greatest guy to pay attention to.
2:25:28> Randall Carlson.
2:25:29> Yeah.
2:25:30> He's kind of dedicated his whole life to it, which by the way happened because of a psychedelic experience.
2:25:36> He was on acid once.
2:25:37> When he was looking at this immense canyon, and he had this vision that it was created by instantaneous erosions of the polar caps, and that it just washed this wave of impossible water through the Earth.
2:25:52> It just caught these paths.
2:25:55> And now there seems to be actual physical evidence of that.
2:25:58> That is probably what took place.
2:26:01> And that we're just the survivors.
2:26:04> And that we have re-emerged in that society and human civilization occasionally gets set back to a primal place.
2:26:14> Yeah.
2:26:15> You know, who knows? If you're right, that what happens here is we kind of edit out all of the impulses in ourselves that we don't like.
2:26:22> We get to, that world seems kind of boring.
2:26:24> So maybe that's when we have to make a new simulation to watch people think they're going through some dramas.
2:26:29> Or maybe it's just we get to this point where we have this power.
2:26:34> But the haves and the have-nots, the divide is too great.
2:26:37> And that people did get a hold of this technology and use it to oppress people who didn't have it.
2:26:43> And that we didn't mitigate the human biological problems, the reward systems that we have.
2:26:51> I got to have more and you got to have less.
2:26:53> Yeah.
2:26:54> That's this sort of natural inclination that we have for competition.
2:26:58> And that someone hijacks that.
2:26:59> I think this is going to be such a hugely important issue to get ahead of before the first people push that.
2:27:05> Yeah.
2:27:06> What do you think about, like when Elon was causing calling for a pause on AI? And he was like starting an AGI company while he was doing that.
2:27:17> Yeah.
2:27:18> Didn't he start it like after he was calling for the pause? I think before, but I don't remember.
2:27:24> Was it in any case? Is it one of those you can't beat him, join him, things? I think the instinct of saying like we've really got to figure out how to make this safe and good and like widely good is really important.
2:27:43> But I think calling for a pause is like naive at best.
2:27:53> I kind of think you can't make progress on the safety part of this as we mentioned earlier by sitting in a room and thinking hard.
2:28:03> You've got to see where the technology goes.
2:28:05> You've got to have contact with reality.
2:28:08> And then when you like, but we're trying to like make progress towards AGI conditioned on it being safe and conditioned on it being beneficial.
2:28:15> And so when we hit any kind of like block, we try to find a technical or a policy or a social solution to overcome it that could be about the limits of the technology and something not working and hallucinates or it's not getting smarter or whatever.
2:28:29> Or it could be there's this like safety issue and we've got to like redirect our resources to solve that.
2:28:34> But it's all like for me, it's all this same thing of like we're trying to solve the problems that emerge at each step as we get what we're trying to go.
2:28:44> And you know, maybe you can call it a pause if you want, if you pause on capabilities to work on safety.
2:28:49> But in practice, I think the field has gotten a little bit wander on the axle there and safety and capabilities are not these two separate things.
2:28:59> This is like, I think one of the dirty secrets of the field.
2:29:02> It's like we have this one way to make progress.
2:29:04> You know, we can understand and push on deep learning more and that can be used in different ways.
2:29:13> But it's, I think it's that same technique that's going to help us eventually solve the safety.
2:29:18> That, all of that said, is like a human.
2:29:22> Emotionally speaking, I super understand why it's tempting to call for a pause.
2:29:26> It happens all the time in life, right? This is moving too fast.
2:29:29> Right.
2:29:30> We got a pause here.
2:29:32> Yeah.
2:29:33> How much of a concern is it in terms of national security that we are the ones that come up with this first? Well, I would say that if an adversary of ours comes up with it first and uses it against us and we don't have some level of capability, that feels really bad.
2:29:56> But I hope that what happens is this can be a moment where to tie it back to the conversation, we kind of come together and overcome our base impulses and say like, let's all do this as a club together.
2:30:10> That would be better.
2:30:11> That would be nice.
2:30:12> And maybe through AGI and through the implementation of this technology, it will make translation instantaneous and easy.
2:30:23> So well, that's already happened.
2:30:24> Right.
2:30:25> But I mean, it hasn't happened in real time, the point where you can accurately communicate.
2:30:32> Very soon.
2:30:33> Very soon.
2:30:34> Very soon.
2:30:35> Yeah.
2:30:36> I do think for what it's worth that the world is going to come together here.
2:30:44> I don't think people have quite realized the stakes.
2:30:47> But this is like, I don't think this is a geopolitical.
2:30:50> If this comes down to like a geopolitical fight or race, I don't think there's any winners.
2:30:55> And so I'm optimistic about people coming together.
2:30:59> Yeah, I am too.
2:31:01> I mean, I think most people would like that if you asked the vast majority of the human beings that are alive.
2:31:09> Wouldn't it be better if everybody got along? You know, maybe you can't go all the way there and say we're just going to have one global effort.
2:31:22> But I think at least we can get to a point where we have one global set of rules, safety standards, organization that makes sure everyone's following the rules, we did this for atomic weapons, been similar things in the world of biology.
2:31:35> I think we'll get there.
2:31:37> That's a good example, the nuclear weapons, because we know the destructive capability of them.
2:31:46> And because of that, we haven't detonated once since 1947.
2:31:50> Pretty incredible.
2:31:51> Pretty incredible.
2:31:52> Other than tests.
2:31:54> We haven't used one in terms of war.
2:31:57> When was the end of the World War II? Wasn't it 47? When they dropped the bombs? I think that was 45.
2:32:06> I was wondering if there was more after that I didn't know about it.
2:32:08> No, it might be 45.
2:32:10> I think it was 45.
2:32:11> So from 1945, which is pretty extraordinary.
2:32:14> That's pretty remarkable.
2:32:15> I would not have predicted that.
2:32:16> I think I could teleport back to 45.
2:32:19> No.
2:32:20> I would have thought, oh my God, this is just going to be something that people do.
2:32:23> Just launch bombs on cities.
2:32:25> Yeah.
2:32:26> And I would have said, we're not going to survive this for very long.
2:32:30> And there was a real fear of that.
2:32:31> For sure.
2:32:32> It's pretty extraordinary that they've managed to stop that.
2:32:35> This threat of mutually assured destruction, self-destruction, destruction, the whole world.
2:32:41> We have enough weapons to literally make the world uninhabitable.
2:32:45> Totally.
2:32:47> And because of that, we haven't done it.
2:32:50> Which is a good story.
2:32:51> I think the iciness, I think that should give some hope.
2:32:53> Yeah, it should.
2:32:54> I mean, Steven Pinker gets a lot of shit for his work because he just sort of downplays violence today.
2:33:03> But it's not that he's downplaying violence today.
2:33:04> He's just looking at statistical trends.
2:33:06> If you're looking at the reality of life today versus life 100 years ago, 200 years ago, it's far more safer.
2:33:14> Why do you think that's a controversial thing? Why can't someone say, sure, we still have problems, but it's getting better? Because people don't want to say that.
2:33:21> Especially people who are activists.
2:33:23> They're completely engrossed in this idea that there's problems today.
2:33:28> And these problems are huge.
2:33:29> And there's Nazis.
2:33:32> But no one's saying there's not.
2:33:34> Huge problems today.
2:33:35> No one's saying there's not.
2:33:36> But just to say things are better today.
2:33:37> Yeah, I guess that.
2:33:38> Some people, they just don't want to hear that.
2:33:40> But those are also people that are addicted to the problems.
2:33:42> The problems become their whole life.
2:33:44> Solving those problems become their identity.
2:33:47> Being involved in the solutions or what they believe are solutions to those problems become their life's work.
2:33:53> And someone comes along and says, actually, life is safer than it's ever been before.
2:33:56> Interaction, please, safer.
2:33:57> Yeah, that's deeply invalidating.
2:34:00> Yeah.
2:34:01> But also true.
2:34:03> And again, what is the problem? Why can't people recognize that? Well, it's the primate brain.
2:34:10> It's all the problems that we highlighted earlier.
2:34:12> And that that might be the solution to overcoming that is through technology.
2:34:19> And it might be the only way we can do it without a long period of evolution.
2:34:23> Because biological evolution is so relatively slow in comparison to technological evolution and that that might be our bottleneck.
2:34:34> We just still are dealing with this primate body.
2:34:37> And that something like artificial general intelligence or something like some implemented form of engaging with it, whether it's a neural link, something that shifts the way the mind interfaces with other minds.
2:34:55> Isn't it wild that speaking of biological evolution, there will be people, I think, who are alive for the invention or discovery, whatever you want to call it, of the transistor.
2:35:05> There will also be a live for the creation of AGI, like one human lifetime.
2:35:09> Yeah.
2:35:10> You want to know a wild one from the implementation from the Orville and Wilbur Wright flying the plane, it was less than 50 years before someone dropped an atomic bomb out of it.
2:35:21> That's wild.
2:35:22> That's crazy.
2:35:23> That's crazy.
2:35:24> Less than 40, right? That's crazy.
2:35:28> Yeah.
2:35:29> Bananas.
2:35:30> 60 something years to land on the moon.
2:35:35> Nuts.
2:35:36> Nuts.
2:35:37> Where is it going? I mean, it's just guesswork.
2:35:42> But it's interesting.
2:35:43> For sure.
2:35:44> I mean, it's the most fascinating thing of our time, for sure.
2:35:47> It's fascinating.
2:35:48> And I also think it is one of these things that will be tremendously beneficial.
2:35:55> Yeah.
2:35:56> Like, we've been talking a lot about problems in the world.
2:36:00> I think that's just always a nice reminder of how much we get to improve and we're going to get to improve a lot.
2:36:06> And I think this will be the most powerful tool we have yet created to help us go do that.
2:36:13> I think you're right.
2:36:15> And this is an awesome conversation.
2:36:17> Thanks for having us.
2:36:18> Thank you for being here.
2:36:19> Really, really appreciate it.
2:36:20> And thanks for everything.
2:36:21> Keep us posted.
2:36:22> And if you create how, give you a call.
2:36:25> Let us know.
2:36:26> All right.
2:36:27> Thank you.
2:36:28> Thank you.
2:36:29> Bye, everybody.
2:36:30> (upbeat music) (upbeat music) (laughing) [Music]
"""

# speech_lines = speech.splitlines()
# speech_lines = [line.strip() for line in speech_lines]

# speech_lines = [line for line in speech_lines if line != '']
# speech_lines = [line for line in speech_lines if '-->' not in line]
# combined = ' '.join(speech_lines)
tokens = tiktoken.encoding_for_model('gpt-3.5-turbo-16k').encode(speech)
print(len(tokens))

# split text into chunks of 14k tokens
chunks = []
for i in range(0, len(tokens), 999999999):
    chunks.append(tokens[i:i+999999999])

for chunk in chunks:
    file = open(f"speech.chunk.{chunks.index(chunk)}.txt", "w")
    decoded = tiktoken.encoding_for_model('gpt-3.5-turbo-16k').decode(chunk)
    file.write(decoded)
