import tiktoken

speech = """
00:00:02.120 --> 00:00:07.080
Joe Rogan Podcast. Check it out. The Joe Rogan Experience Train by day Joe

00:00:07.120 --> 00:00:09.520
Rogan Podcast by night, all day.

00:00:13.160 --> 00:00:17.520
Alright Sam, what's happening? Not much. Thanks for coming in here. Appreciate. Thanks for having me.

00:00:17.520 --> 00:00:22.320
So what have you done? Like ever? No, I mean, what have you

00:00:22.320 --> 00:00:26.560
done with AI? I mean, it's one of the things

00:00:27.960 --> 00:00:32.560
about this is, I mean I think everyone is fascinated by it. I mean,

00:00:32.560 --> 00:00:36.880
everyone is absolutely blown away at the current capability

00:00:37.640 --> 00:00:41.680
and wondering what the potential for the future is and whether or not that's a good thing.

00:00:45.320 --> 00:00:50.160
I think it's going to be a great thing, but I think it's not going to be all a great thing and that that is

00:00:50.160 --> 00:00:54.930
where I think. That's where all of the

00:00:54.930 --> 00:00:59.690
complexity comes in for people. It's not this like clean story of we're going to do this and it's all going to be

00:00:59.690 --> 00:01:04.609
great. It's we're going to do this. It's going to be net great, but it's going to be like a

00:01:04.609 --> 00:01:09.530
technological revolution. It's going to be societal revolution. And those always come

00:01:09.530 --> 00:01:14.290
with change. And even if it's like net wonderful, you know, there's things we're going to lose

00:01:14.290 --> 00:01:19.290
along the way. Some kinds of job, some kinds parts of our way of life, some parts of the way we live are going to change

00:01:19.290 --> 00:01:24.239
or go away and. Eat. No matter how tremendous the upside is

00:01:24.239 --> 00:01:28.799
there. And I and I believe it will be tremendously good. You know, there's a lot of stuff we got to navigate through to make sure

00:01:30.799 --> 00:01:35.680
that's that's a complicated thing for anyone to wrap their heads

00:01:35.680 --> 00:01:40.360
around. And there's, you know, deep and super understandable emotions around that. That's a very honest

00:01:40.360 --> 00:01:44.360
answer that it's not all going to be good, but

00:01:45.739 --> 00:01:50.459
it seems inevitable at this point. It's yeah, I mean it's definitely inevitable. My

00:01:50.580 --> 00:01:55.580
my view of the world, you know when you're like a kid in school, you learn about this technological

00:01:55.580 --> 00:02:00.260
revolution and then that one and then that one. And my view of the world now sort of looking backwards and

00:02:00.260 --> 00:02:04.420
forwards is that this is like 1 long technological revolution.

00:02:05.459 --> 00:02:09.979
And we had sure like first we had to figure out agriculture so that we had the

00:02:10.219 --> 00:02:15.150
resources and time to figure out how to build machines. Then we got this industrial revolution. And that made us learn

00:02:15.150 --> 00:02:20.110
about a lot of stuff and a lot of other scientific discovery too. Let us do the computer revolution. And that's

00:02:20.110 --> 00:02:24.909
now letting us, as we scale up to these massive systems, do the AI revolution. But it really is

00:02:24.909 --> 00:02:29.870
just one long story of humans discovering science and technology and

00:02:29.870 --> 00:02:34.750
coevolving with it. And I think it's the most exciting story of all time. I think it's how we

00:02:34.750 --> 00:02:39.599
get to this world of abundance and although. You

00:02:39.599 --> 00:02:44.560
know, although we do have these things to navigate in there, there will be these downsides. If, if you think about what it means for

00:02:44.560 --> 00:02:48.160
the world and for people's quality of lives. If we can get to a world

00:02:49.240 --> 00:02:54.160
where the the cost of intelligence and the abundance that comes

00:02:54.160 --> 00:02:59.120
with that, the cost dramatically falls, the abundance goes

00:02:59.120 --> 00:03:03.960
ways up, goes way up. I think we'll do the same thing with energy. And I think those are the two sort of key inputs

00:03:04.159 --> 00:03:08.280
to everything else we want. So if we can have abundant and cheap energy and intelligence.

00:03:09.199 --> 00:03:13.400
That will transform people's lives largely for the better. And I think it's going to,

00:03:14.199 --> 00:03:19.000
in the same way that if we could go back now 500 years and look at someone's life, we'd say, well, there there's some great things,

00:03:19.000 --> 00:03:24.000
but they didn't have this, they didn't have that. Can you believe they didn't have modern medicine? That's what people are going

00:03:24.000 --> 00:03:28.639
to look back at us like. But in 50 years, when you think about the people that

00:03:28.639 --> 00:03:33.080
currently rely on jobs that a I will replace,

00:03:33.639 --> 00:03:38.560
when you think about whether it's truck drivers or automation workers, people that work

00:03:38.560 --> 00:03:42.919
in factory assembly lines, what, if

00:03:42.919 --> 00:03:47.120
anything, what strategies can be put to mitigate the negative

00:03:47.120 --> 00:03:51.120
downsides of those jobs being eliminated by AI?

00:03:52.080 --> 00:03:56.919
So I'll talk about some general thoughts,

00:03:56.919 --> 00:04:01.360
but I find making very specific predictions difficult

00:04:01.360 --> 00:04:06.090
because. The way the technology goes has been so different than even my own

00:04:06.569 --> 00:04:11.330
intuitions, or certainly my own intuitions. Can we? Maybe we should stop there and back up a little

00:04:11.729 --> 00:04:16.569
what we What were your initial thoughts? If you had asked me 10

00:04:16.569 --> 00:04:21.370
years ago, I would have said first AI is going to come for blue

00:04:21.370 --> 00:04:25.889
collar labor. Basically it's going to drive trucks and do factory work and you know it'll

00:04:26.329 --> 00:04:30.730
handle heavy machinery. Then maybe after that it'll do like.

00:04:31.579 --> 00:04:36.420
Some kinds of cognitive labor, kind of, you know, but not it won't be off

00:04:36.420 --> 00:04:41.180
doing what I think of personally as the really hard stuff. It won't be off Proving new mathematical

00:04:41.180 --> 00:04:45.980
theorems won't be off. You know, discovering new science won't be off

00:04:45.980 --> 00:04:50.899
writing code. And then eventually maybe, but maybe last of all, maybe never,

00:04:50.899 --> 00:04:55.819
because human creativity is this magic special, special thing. Last of all, it'll come for the

00:04:55.819 --> 00:05:00.220
creative jobs. That's what I would have said, now A.

00:05:01.019 --> 00:05:05.980
It looks to me like, and for a while A I is much better doing tasks than doing

00:05:05.980 --> 00:05:10.620
jobs. It can do these little pieces super well, but sometimes it goes off the

00:05:10.620 --> 00:05:15.420
rails, can't keep like very long coherence. So people are

00:05:15.420 --> 00:05:20.339
instead just able to do their existing jobs way more productively. But you really still

00:05:20.339 --> 00:05:25.139
need the human there today. And then B, it's going exactly the direction could do the creative work first.

00:05:25.420 --> 00:05:30.139
Stuff like coding. Second are they can do things like other kinds of cognitive labor

00:05:30.139 --> 00:05:33.670
Third. And we're the furthest away from like humanoid robots.

00:05:35.990 --> 00:05:40.589
So back to the initial question. If we do

00:05:40.589 --> 00:05:45.350
have something that completely eliminates factory workers,

00:05:45.350 --> 00:05:50.310
completely eliminates truck drivers, delivery drivers, things along those

00:05:50.310 --> 00:05:54.629
lines, that creates this massive vacuum in our

00:05:54.629 --> 00:05:59.430
society. So I think there's things that. We're

00:05:59.430 --> 00:06:04.350
going to do that are good to do but not sufficient. So I think at some point

00:06:04.430 --> 00:06:08.829
we will do something like a Ubi or some other kind of like very

00:06:08.949 --> 00:06:13.629
longterm unemployment insurance something but we'll have some way of giving

00:06:13.629 --> 00:06:18.470
people like redistributing money in society and as a cushion for

00:06:18.470 --> 00:06:23.149
people as people figure out the new jobs. But, and I maybe I should touch on that

00:06:24.029 --> 00:06:28.829
I'm not a believer at all that there won't be lots of new jobs. I I think human.

00:06:29.379 --> 00:06:34.339
Creativity, desire for status, wanting different ways to compete, invent new things,

00:06:34.339 --> 00:06:38.740
feel part of a community, feel valued. That's not going to go anywhere.

00:06:39.139 --> 00:06:43.500
People have worried about that forever. What happens is we get better tools and

00:06:44.220 --> 00:06:49.060
we just invent new things and more amazing things to do. And there's a big universe out there and and I think

00:06:49.500 --> 00:06:54.459
I mean that like literally in that there's like space is really big, but also there's

00:06:54.459 --> 00:06:59.180
just so much stuff we can all do if we do get to this world of. Abundant

00:06:59.180 --> 00:07:03.540
intelligence where you can sort of just think of a new idea and it it gets created. But

00:07:06.980 --> 00:07:11.860
but again that doesn't to the point we started with that that that that doesn't provide like

00:07:11.860 --> 00:07:16.860
great solace to people who are losing their jobs today. So saying there's going to be this

00:07:16.860 --> 00:07:21.139
great indefinite stuff in the future. People like what are we doing today. So

00:07:21.899 --> 00:07:26.689
you know, well, I think we will as a society do things like. Ubi

00:07:26.689 --> 00:07:31.569
and other ways of redistribution, but I don't think that gets at the core of what people want. I think

00:07:31.569 --> 00:07:36.209
what people want is like agency, self determination, the ability to

00:07:36.569 --> 00:07:41.290
play a role in architecting the future along with the rest of society, the ability to express

00:07:41.290 --> 00:07:46.050
themselves and create something meaningful to them.

00:07:46.569 --> 00:07:51.410
And also, I think a lot of people work jobs they

00:07:51.410 --> 00:07:56.399
hate. And I think there's. We as a society are always a little bit confused about whether we want to

00:07:56.399 --> 00:08:01.399
work more, work less, but but somehow that

00:08:02.959 --> 00:08:07.839
we all get to do something meaningful and we all get to play our role in

00:08:07.839 --> 00:08:12.439
driving the future forward, That's really important. And what I hope is as those truck

00:08:12.439 --> 00:08:17.199
driving, long haul truck driving jobs go away, which you know people have been wrong

00:08:17.199 --> 00:08:22.120
about predicting how fast that's going to happen, but it's going to happen, we figure out not

00:08:22.120 --> 00:08:26.850
just a way to. Solve the economic

00:08:26.850 --> 00:08:31.490
problem by like giving people the equivalent of money every month.

00:08:31.889 --> 00:08:36.570
But that there's a way that, and we've got a lot of ideas about this, there's a way that we like

00:08:36.570 --> 00:08:40.610
share ownership and decision making over the future.

00:08:42.009 --> 00:08:46.970
I think I say a lot about a GI is that everyone, everyone realizes we're going to

00:08:46.970 --> 00:08:51.960
have to share the benefits of that, but we also have to share like. The decision making

00:08:51.960 --> 00:08:56.440
over it and access to the system itself. Like I'd be more excited about a world where we say,

00:08:56.840 --> 00:09:01.840
rather than give everybody on earth like 1/8 billionth of the a GI money, which we should do that

00:09:01.840 --> 00:09:06.720
too, we say you get like 1-8 billionth of a 18 billionth

00:09:06.720 --> 00:09:11.639
slice of the system. You can sell it to somebody else.

00:09:11.639 --> 00:09:16.559
You can sell it to a company, You can pool it with other people. You can use it for whatever creative pursuit you want. You can use

00:09:16.559 --> 00:09:21.299
it to figure out how to start some new business. And with that you get sort of like

00:09:22.779 --> 00:09:27.419
a voting right over how this is all going to be used. And so the better the AGI gets, the more your

00:09:27.419 --> 00:09:32.340
little 18 billionth ownership is is worth to you. We were joking around the other day

00:09:32.379 --> 00:09:36.860
on the podcast where I was saying that what we need is an AI government

00:09:37.500 --> 00:09:42.299
that the we should have what is the AI president and have AI. Just make all the decisions.

00:09:42.620 --> 00:09:47.220
I have something that's completely unbiased, absolutely rational. Has

00:09:47.759 --> 00:09:52.480
the accumulated knowledge of the entire human history at its disposal,

00:09:52.480 --> 00:09:57.399
including all knowledge of psychology and psychological

00:09:57.399 --> 00:10:02.320
study including Ubi. Cuz that comes with a host of you know pitfalls and and

00:10:02.480 --> 00:10:07.279
and issues that people have with it. So I'll say something there. I think we're still very

00:10:07.279 --> 00:10:11.919
far away from a system that is capable enough and reliable enough

00:10:12.279 --> 00:10:15.960
that you that any of us would want that. But I'll tell you something I love about that.

00:10:17.440 --> 00:10:22.360
Someday, let's say that thing gets built. The fact that it can go around and talk to every person on

00:10:22.360 --> 00:10:27.360
earth, understand their exact preferences at a very deep level, You know, how they think about this

00:10:27.360 --> 00:10:32.360
issue and that one and how they balance the trade-offs and what they want. And then understand all of that and

00:10:32.360 --> 00:10:37.320
and like collectively optimized, optimized for the collective

00:10:37.320 --> 00:10:42.320
preferences of humanity or of citizens of the US, That's awesome. As long

00:10:42.360 --> 00:10:47.220
as it's not coopted. Right, our government currently is coopted.

00:10:47.220 --> 00:10:51.700
That's for sure. We know for sure that our government is heavily influenced by special

00:10:51.700 --> 00:10:56.259
interests. If we could have an artificial

00:10:56.259 --> 00:11:01.220
intelligence government that has no influence, nothing has influence on it. What? A

00:11:01.259 --> 00:11:05.700
fascinating idea. It's possible, and I think it might be the only way

00:11:06.419 --> 00:11:11.379
where you're going to get completely objective, the absolute

00:11:11.379 --> 00:11:16.350
most intelligent decision for virtually every problem,

00:11:16.429 --> 00:11:21.350
every dilemma that we face currently in society. Would you truly be comfortable handing over,

00:11:21.350 --> 00:11:25.909
like, final decision making and say, all right, AI, you got it? No, no. But I'm not

00:11:26.070 --> 00:11:31.029
comfortable doing that with anybody, right. You know, I mean, I don't, right. I was uncomfortable

00:11:31.029 --> 00:11:35.669
with the Patriot Act. I'm uncomfortable with, you know, many decisions that are being made.

00:11:36.429 --> 00:11:41.200
It's just there's so much obvious evidence that decisions that are being

00:11:41.200 --> 00:11:46.200
made are not being made in the best interest of the overall well of the people. It's being made in the

00:11:46.200 --> 00:11:51.200
decisions of whatever gigantic corporations

00:11:51.360 --> 00:11:55.519
that have donated to and what whatever the military industrial complex and

00:11:56.039 --> 00:12:00.879
pharmaceutical industrial complex and and it's just the money. It's that's really what

00:12:00.879 --> 00:12:05.840
we know today, that the money has a massive influence on on our society and the choices that get

00:12:05.840 --> 00:12:10.429
made and the overall good or bad for the population. Yeah, I I have no

00:12:10.429 --> 00:12:15.309
disagreement at all that the current system is super broken not working for

00:12:15.309 --> 00:12:20.190
people, super corrupt corrupt and for sure like unbelievably run by

00:12:20.190 --> 00:12:24.870
money and and I think there is a way to

00:12:25.389 --> 00:12:29.789
do a better job than that with a I to in some way.

00:12:30.309 --> 00:12:35.149
But, and this might just be like a factor of sitting with the systems all day and watching all of the ways they

00:12:35.149 --> 00:12:39.840
fail. We got a long way to go, a long way to go, I'm sure. But when you

00:12:39.840 --> 00:12:44.559
think of AGI, when you think of the possible

00:12:44.559 --> 00:12:49.480
future, like where it goes to, do you ever extrapolate? Do you ever, like,

00:12:49.480 --> 00:12:54.399
sit and pause and say, well, if this if this becomes sentient and it has the

00:12:54.399 --> 00:12:59.080
ability to make better versions of itself, how long before we're

00:12:59.080 --> 00:13:04.080
literally dealing with a God? So the way that I think about

00:13:04.080 --> 00:13:09.049
this is. It used to be that like a GI was this very binary moment. It was

00:13:09.049 --> 00:13:14.049
before and after, and I think I totally wrong about that. And the right way to

00:13:14.049 --> 00:13:18.450
think about it is this continue continuum of intelligence, this

00:13:18.610 --> 00:13:23.049
smooth exponential curve back all the way to that sort of smooth curve curve of

00:13:23.049 --> 00:13:28.049
technological revolution. The the amount of compute power

00:13:28.049 --> 00:13:32.809
we can put into the system, the scientific ideas about how to make it more efficient and smarter

00:13:33.169 --> 00:13:37.419
to give it. The ability to do reasoning to think about how to improve itself

00:13:38.059 --> 00:13:42.940
that will all come but my my model for a long time I I

00:13:42.940 --> 00:13:47.820
think if you look at the world of a GI thinkers there's there's sort of two

00:13:48.460 --> 00:13:53.019
particular around the safety issues you're talking about. There's two axes that matter. There's the

00:13:53.419 --> 00:13:58.419
short what called short timelines or long timelines you know to the first milestone

00:13:58.419 --> 00:14:03.129
of a GI whatever that's going to be. Is that going to happen in? A few years, a few

00:14:03.129 --> 00:14:08.090
decades, maybe even longer, although at this point I think most people are a few years or few decades and then there's takeoff

00:14:08.090 --> 00:14:12.970
speed once we get there from there to that point you were talking about where it's capable of the rapid self

00:14:12.970 --> 00:14:17.850
improvement, is that a slower, a fast process. The the

00:14:17.850 --> 00:14:22.730
world that I think we're heading that we're in and also the world that I think is the

00:14:22.730 --> 00:14:27.090
most controllable and the safest is the short

00:14:27.169 --> 00:14:30.850
timelines and slow takeoff quadrant and.

00:14:32.620 --> 00:14:37.460
I think we're going to have, you know, there were a lot of very smart people for a while. We're like the thing you were just

00:14:37.460 --> 00:14:42.460
talking about happens in a day or three days. And I don't. That doesn't seem likely to me given

00:14:42.460 --> 00:14:47.340
the shape of the technology as we understand it now. Now, even if that happens

00:14:47.340 --> 00:14:52.100
in a decade or three decades, I still like the blink of an eye from a

00:14:52.100 --> 00:14:57.100
historical perspective, and they're going to be some real challenges

00:14:57.100 --> 00:15:00.299
to getting that right and the decisions we make.

00:15:01.940 --> 00:15:06.740
The the sort of safety systems and the and the checks that the world puts in place,

00:15:07.019 --> 00:15:11.700
how we think about global regulation or

00:15:11.700 --> 00:15:16.379
rules of the road from a safety perspective for those projects. It's super important because you can

00:15:16.379 --> 00:15:20.139
imagine many things going horribly wrong. But I've been,

00:15:21.779 --> 00:15:26.500
I feel cheerful about the progress the world is making towards taking this seriously.

00:15:26.659 --> 00:15:31.570
And you know, it reminds me of. What I've read about the conversations that the

00:15:31.570 --> 00:15:36.450
world had right around the development of nuclear weapons, it seems to me

00:15:36.450 --> 00:15:41.009
that this is, at least in terms of public consciousness, this is emerged very

00:15:41.009 --> 00:15:46.009
rapidly where I don't think anyone was really aware, People that were

00:15:46.009 --> 00:15:51.009
aware of the concept of artificial intelligence, but they didn't think that it was going

00:15:51.009 --> 00:15:55.730
to be implemented so comprehensively so quickly.

00:15:56.340 --> 00:16:00.980
So ChatGPT is on what, 4.5 now 4/4?

00:16:01.340 --> 00:16:06.340
And with 4.5 they'll be some sort of an exponential increase in its abilities.

00:16:06.340 --> 00:16:11.340
It'll be somewhat better each step, you know, from each like half

00:16:11.340 --> 00:16:16.299
step like that you you kind of humans have this ability to like get used

00:16:16.299 --> 00:16:20.820
to any new technology so quickly. The thing that I think was unusual about the launch of

00:16:20.820 --> 00:16:25.730
ChatGPT 3.5 and then four was that. People hadn't

00:16:25.730 --> 00:16:30.730
really been paying attention, and that's part of the reason we deploy. We think it's very important that people

00:16:30.730 --> 00:16:35.370
and institutions have time to gradually understand this, react,

00:16:35.850 --> 00:16:40.809
codesign, the society that we want with it. And if you just build AGI and secret in a lab and

00:16:40.809 --> 00:16:45.649
then drop it on the world all at once, I think that's a really bad idea. So we we had been

00:16:45.649 --> 00:16:50.610
trying to talk to the world about this for a while. People, if you don't give people something

00:16:50.610 --> 00:16:55.509
they can feel and use in their lives, they don't quite take it seriously. Everybody's busy. And

00:16:55.509 --> 00:16:59.990
so there was this big overhang from where the technology was to where public consciousness was.

00:17:00.710 --> 00:17:05.430
Now that's caught up. We've deployed. I think people understand it. I

00:17:05.430 --> 00:17:10.430
don't expect the few, the jump from like 4 to whenever we finished 4.5, which would be

00:17:10.430 --> 00:17:15.390
a little while. I don't expect that to be the crazy.

00:17:15.430 --> 00:17:20.349
I think the crazy switch, the crazy adjustment that people have had to go through has has mostly happened.

00:17:20.589 --> 00:17:25.289
I think most people have gone from thinking that a GI was. Science fiction and very far off.

00:17:25.650 --> 00:17:30.490
Just something that is going to happen. And that was like a one time reframe. And now you

00:17:30.490 --> 00:17:35.130
know, every year you get a new iPhone. Over the 15 years or whatever. Since the launch, they've gotten

00:17:35.130 --> 00:17:40.130
dramatically better. But iPhone to iPhone you're like, yeah, OK, it's a little better. But now if you go hold up

00:17:40.130 --> 00:17:44.849
the first iPhone to the 15 or whatever, that's a big difference. GPT 3.5 to a

00:17:44.890 --> 00:17:49.250
GI, that'll be a big difference, but along the way it'll just get incrementally better.

00:17:49.849 --> 00:17:54.849
Do you think about the convergence of things like neural link

00:17:54.890 --> 00:17:59.170
and there's a few competing technologies where they're trying to implement

00:17:59.250 --> 00:18:04.009
some sort of some sort of a connection

00:18:04.009 --> 00:18:08.569
between the human biological system and technology?

00:18:09.450 --> 00:18:14.289
Do you want one of those things in your head? I don't. Until everybody does.

00:18:14.910 --> 00:18:19.789
And you know, I have a joke about it, but it's like that. The idea is like, once it gets, you have

00:18:19.789 --> 00:18:23.589
to kind of because everybody's going to have it. So one of the hard

00:18:24.509 --> 00:18:29.470
questions about the all of the related merge stuff is exactly what

00:18:29.470 --> 00:18:34.430
you just said. Like as a society, are we going to let some people merge

00:18:34.430 --> 00:18:39.269
with a GI and not others? And if we do,

00:18:39.470 --> 00:18:44.250
then, and you choose not to like, what does that mean for you? Right. And will you be

00:18:44.250 --> 00:18:49.210
protected? How you get that moment right? You know, if we'd

00:18:49.210 --> 00:18:53.970
like, imagine like all the way out to the scifi future. I've been a lot of

00:18:53.970 --> 00:18:58.930
scifi books written about how you get that moment right. You know, who gets to do that first? What about people who don't want to? How do you

00:18:58.930 --> 00:19:03.849
make sure the people that do it first, like, actually help lift everybody up together? How do you make sure people

00:19:03.849 --> 00:19:08.650
who want to just like, live their very human life get to do that? That stuff is really

00:19:08.690 --> 00:19:13.630
hard. And honestly? So far off from my problems of the day that I don't

00:19:13.630 --> 00:19:16.589
get to think about that as much as I'd like to because I do think it's super interesting.

00:19:18.470 --> 00:19:23.269
I. But yeah, it seems like if we just think

00:19:24.150 --> 00:19:28.470
logically, that's going to be a huge challenge at some point and

00:19:29.269 --> 00:19:34.150
people are going to want wildly

00:19:34.150 --> 00:19:39.109
divergent things. But there is a societal question about

00:19:39.109 --> 00:19:43.980
how we're going to like. The questions of fairness that come there

00:19:44.299 --> 00:19:49.299
and what it means for the people who don't do it super, super complicated.

00:19:49.819 --> 00:19:54.700
Anyway, on the neural interface side, I'm in the short term like before we figure out how to

00:19:56.420 --> 00:20:00.019
upload someone's consciousness into a computer, if that's even possible at all, which I think there's

00:20:01.180 --> 00:20:05.180
plenty of sides you could take on. Why it's not the

00:20:06.779 --> 00:20:11.319
the thing that I find myself most interested in is. What we can

00:20:11.519 --> 00:20:16.400
do without drilling a hole in someone's head? How much of the inner

00:20:16.400 --> 00:20:20.839
monologue can we read out with an externally mounted device? And if we have a

00:20:21.359 --> 00:20:25.880
imperfect low bandwidth, low accuracy neural interface,

00:20:26.359 --> 00:20:31.079
can people still just learn how to use it really well in a way that's like quite powerful

00:20:31.240 --> 00:20:36.039
for what they cannot do with a new computing platform? And my guess is we'll figure that out.

00:20:36.660 --> 00:20:41.619
I'm sure you've seen that headpiece that there's a demonstration where there's someone asking

00:20:41.619 --> 00:20:46.380
someone a question, they have this headpiece on, they think the question and then they

00:20:46.380 --> 00:20:51.380
literally Google the question and get the answers through their head. That's the kind of thing we've been. That's the kind of direction we've been exploring.

00:20:51.539 --> 00:20:56.380
Yeah, that seems to me to be step one. That's the pong

00:20:56.539 --> 00:21:01.259
of the eventual immersive 3D video games. Like you're you're going to get

00:21:01.259 --> 00:21:05.960
these first steps and they're going to seem sort of crude and slow. I mean, it's

00:21:05.960 --> 00:21:10.559
essentially slower than just asking Siri. I think if someone

00:21:11.119 --> 00:21:16.119
built a system where you could think words, doesn't

00:21:16.119 --> 00:21:20.519
have to be a question. It could just be your passive rambling in our monologue, but certainly could be a question.

00:21:21.000 --> 00:21:25.680
And that was being fed into G PT5 or six. And in your field of

00:21:25.680 --> 00:21:30.240
vision, the words in response were being displayed. That would be the palm. Yeah,

00:21:30.680 --> 00:21:35.200
that's still soup. That's a very valuable tool to have. And that seems like that's inevitable.

00:21:36.789 --> 00:21:41.789
There's hard work to get there on the neural interface side, but I believe it will happen. Yeah, I think

00:21:41.789 --> 00:21:46.750
so too. And my, my concern is that the initial adopters of this will have such a massive

00:21:46.750 --> 00:21:51.589
advantage over the general population. Well, that doesn't concern me because that's like a, you know,

00:21:51.589 --> 00:21:56.430
that's not, you're not, that's just like better, that's a better computer. You're

00:21:56.430 --> 00:22:01.390
not like jacking your brain into something in a high risk thing. You know what you do when you don't want them, when you take

00:22:01.390 --> 00:22:06.359
off the glasses. So that feels fine. Well, this is just

00:22:06.359 --> 00:22:11.359
the external device then. Oh, I think we can do the kind of like read your thoughts

00:22:11.359 --> 00:22:16.319
with an external device at some point, read your internal monologue. Interesting.

00:22:16.480 --> 00:22:20.920
And do you think we'll be able to communicate with an external device as well telepathically

00:22:21.319 --> 00:22:25.559
or semi telepathically through technology? I do, yeah. Yeah, I do.

00:22:26.519 --> 00:22:30.799
I think so too. My my real concern is

00:22:31.000 --> 00:22:35.769
that. Once we take the step to use an

00:22:35.769 --> 00:22:39.930
actual neural interface, when when there's an actual operation and they're

00:22:41.049 --> 00:22:46.009
using some sort of an implant, and then that implant becomes more sophisticated, it's not the

00:22:46.009 --> 00:22:50.930
iPhone one. Now it's the iPhone 15. And as these things get better and better,

00:22:52.210 --> 00:22:56.960
we're on the road to cyborgs. We're we're on the road to like, why would you

00:22:56.960 --> 00:23:01.960
want to be a biological person? Do you really want to live in a fucking log cabin when you can be

00:23:01.960 --> 00:23:06.920
in the Matrix? I mean, it seems like we're not. We're on this

00:23:06.920 --> 00:23:11.880
path. We're already a little bit

00:23:12.359 --> 00:23:17.079
down that path, right? Like if you take away someone's phone and they have to go function in the world today,

00:23:17.599 --> 00:23:22.579
they're at a disadvantage relative to everybody else. So that's that's like a maybe

00:23:22.579 --> 00:23:27.539
that's like the lightest weight version of Emerge we could imagine. But I think it's worth, like if we

00:23:27.539 --> 00:23:32.500
go back to that earlier thing about the one exponential curve, I think it's worth saying we've like lifted off the

00:23:32.500 --> 00:23:36.660
X axis already down this path the tiniest bit. And

00:23:38.220 --> 00:23:43.180
yeah, even if you don't go all the way to like a narrow interface, VR will get so good that

00:23:43.180 --> 00:23:46.819
some people just don't want to take it off that much. And

00:23:49.910 --> 00:23:54.869
that's fine for them. As long as we can solve this question of how do

00:23:54.869 --> 00:23:59.309
we, like, think about what a balance of power means in the world. I think there will be many people,

00:24:00.509 --> 00:24:05.470
I'm certainly one of them, who's like, actually the human body and the human experience is pretty great. That log heaven in

00:24:05.470 --> 00:24:10.470
the woods? Pretty awesome. I don't want to be there all the time. I'd love to go play the great video game, but like,

00:24:11.029 --> 00:24:16.029
I'm really happy to get to go there sometimes. Yeah, there's still human

00:24:16.029 --> 00:24:20.609
experiences that are just. Like, great human experience. Just

00:24:20.890 --> 00:24:25.890
laughing with friends, you know, kissing someone that you've never kissed before,

00:24:25.890 --> 00:24:30.450
that you you're on a first date, that guy. Those kind of things are the real

00:24:30.490 --> 00:24:35.490
moments. It just laughs. Yeah, having a glass of wine with a friend. Just

00:24:35.490 --> 00:24:40.410
laughing. Not quite the same in VR, yeah. When the VR goes super far so you can't,

00:24:40.410 --> 00:24:45.210
you know, it's like you are jacking on your brain and you can't tell what's real and what's not.

00:24:46.369 --> 00:24:51.369
And then everybody gets like super deep on the simulation hypothesis or the like Eastern religion or

00:24:51.369 --> 00:24:56.049
whatever. And I don't know what happens at that point. Do you ever fuck around with simulation theory? Because

00:24:56.450 --> 00:25:01.170
the real problem is when you combine that with probability theory and you talk to the people that say,

00:25:01.170 --> 00:25:06.049
well, if you just look at the numbers, that the probability that we're already in a

00:25:06.049 --> 00:25:09.130
simulation is much higher than the probability that we're not,

00:25:12.369 --> 00:25:17.329
it's never been clear to me what to do about it. It's like, OK,

00:25:17.660 --> 00:25:22.539
right. That into that intellectually makes a lot of sense. Yeah, I think probably sure, right. That

00:25:22.539 --> 00:25:27.420
seems convincing. But but this is my reality. This is my life, and I'm going to live it.

00:25:27.619 --> 00:25:32.539
And I I've, you know, from

00:25:32.539 --> 00:25:37.420
like 2:00 AM in my college freshman dorm hallway. Till now, I've

00:25:37.420 --> 00:25:42.140
made no more progress on it than that. Well, it seems like

00:25:42.140 --> 00:25:46.460
one of those it's there's no.

00:25:47.430 --> 00:25:52.029
You know, it's if it is a possibility, if it is real. First of all,

00:25:52.390 --> 00:25:57.069
once it happens, what are you going to do? I mean that that is the new reality. And in many

00:25:57.069 --> 00:26:01.670
ways our new reality is as alien to,

00:26:02.109 --> 00:26:06.630
you know, hunter gatherers from 15,000 years ago as

00:26:06.910 --> 00:26:11.670
that would be to us now. I mean, we're we're already, we've already entered into some

00:26:11.670 --> 00:26:16.569
very bizarre territory where. You know, I was just having a conversation with my kids. We're

00:26:16.609 --> 00:26:21.569
asking questions about something and you know, I always say, let's guess what percentage

00:26:21.569 --> 00:26:26.250
of that is this? And then we just Google it and then just ask Siri and we pull it up. Like, look at

00:26:26.250 --> 00:26:31.009
that. Like that alone is so bizarre compared to

00:26:31.130 --> 00:26:36.130
how it was when I was 13 and you had to go to the library and hope that

00:26:36.130 --> 00:26:41.049
the book was accurate. I I was very annoyed this more. I was reading

00:26:41.049 --> 00:26:45.940
about how horrible systems like Chachi, BT, and Google are from an environmental impact because

00:26:45.940 --> 00:26:50.180
it's, you know, using like some extremely tiny amount of energy for each query

00:26:50.700 --> 00:26:55.619
and you know how we're all destroying the world. And I was like before that people drove to the library, let's talk

00:26:55.619 --> 00:27:00.500
about how much carbon they burned to answer this question versus what it takes now. Come on. Those, but that's just people

00:27:00.500 --> 00:27:05.339
looking for some reason why something's bad. That's not a logical totally perspective.

00:27:05.700 --> 00:27:10.339
Well, we should be looking at is the spectacular changes that are

00:27:10.339 --> 00:27:15.250
possible through this. And all the problems, the insurmountable problems that we have

00:27:15.250 --> 00:27:20.250
with resources, with the environment, with cleaning up the ocean, climate

00:27:20.250 --> 00:27:25.049
change, there's so many problems that we need this to solve, all of everything else. And that's

00:27:25.049 --> 00:27:30.009
why we need president AI. If if AI could

00:27:30.289 --> 00:27:34.769
make every scientific discovery but we still had human presidents, you think would be okay.

00:27:35.490 --> 00:27:40.329
No. Because those creeps would still be pocketing money and they'd have offshore accounts

00:27:40.369 --> 00:27:45.329
and it would, it would always be a weird thing of corruption and how to mitigate

00:27:45.329 --> 00:27:50.130
that corruption, which is also one of the fascinating things about the current state of technology, is that we're so much

00:27:50.130 --> 00:27:54.890
more aware of corruption. We're so much more. There's so much independent

00:27:54.890 --> 00:27:59.490
reporting and we're so much more cognizant of the actual

00:27:59.490 --> 00:28:03.930
problems that are in place. This is really great. One of the thing,

00:28:04.609 --> 00:28:09.450
one of the things that I've observed, obviously many other people too, is corruption is

00:28:09.450 --> 00:28:14.329
such an incredible hindrance to getting anything done in a society to make it forward progress.

00:28:14.329 --> 00:28:19.329
And you know, my my worldview had been more US centric when I was

00:28:19.329 --> 00:28:24.250
younger. And as I've just studied the world more and had to work in

00:28:24.250 --> 00:28:29.210
more places in the world, like it's amazing how much corruption there still is. But the shift

00:28:29.289 --> 00:28:33.809
to a technologically enabled world, I think is a major force against it because

00:28:33.809 --> 00:28:38.809
everything is it's harder to hide stuff. And I do think corruption

00:28:38.809 --> 00:28:42.970
in the world will keep trending down. Because of its

00:28:42.970 --> 00:28:47.769
exposure, yeah. Through technology, if I mean that it comes at a

00:28:48.210 --> 00:28:53.130
cost and I think the loss that like I am very worried about how far the surveillance

00:28:53.130 --> 00:28:58.009
state could go here. But in a world where

00:28:59.730 --> 00:29:04.730
payments, for example, are no longer like bags of cash but done somehow digitally,

00:29:05.130 --> 00:29:09.809
and somebody, even if you're using Bitcoin, can like watch those flows, I think that's

00:29:09.809 --> 00:29:14.809
like a corruption reducing thing. I agree, but I'm very worried

00:29:14.809 --> 00:29:19.450
about central bank digital currency and that being tied to a social credit

00:29:19.450 --> 00:29:24.329
score. Super, super against. Yeah, that scares the shit out of me. Super against. And

00:29:24.329 --> 00:29:29.269
that the push to that is not. That's not for the overall good of society. That's for

00:29:29.269 --> 00:29:34.150
control. Yeah, I I think like, I mean there's many

00:29:34.309 --> 00:29:38.789
things that I'm disappointed that the US government has done

00:29:38.910 --> 00:29:43.789
recently. But the the war on crypto, which I think is a like we can't give

00:29:43.789 --> 00:29:48.789
this up. Like we're going to control this and all this like that. That's like, make

00:29:48.789 --> 00:29:53.759
that. That's the thing that like, makes me quite sad about the country. It makes me quite sad about the country too. But then you

00:29:53.759 --> 00:29:58.119
also see with things like FTX, like, Oh well, this can get without

00:29:58.119 --> 00:30:02.680
regulation and without someone overseeing it, this can get really

00:30:02.680 --> 00:30:07.680
fucked. Yeah, I'm I'm not antiregulation. Like, I

00:30:07.680 --> 00:30:11.960
think there's clearly a role for it. And

00:30:13.119 --> 00:30:18.079
I also think FTX was like a sort of comically bad situation.

00:30:18.119 --> 00:30:23.009
Yeah, we shouldn't like we're much from either, yeah. Yeah, but it's a fun one. Like, it's

00:30:23.009 --> 00:30:26.490
totally fun and. I love that story. I mean you. Clearly,

00:30:28.569 --> 00:30:33.250
I really do. I love the fact that they were all doing drugs and having sex with each other. No, no, it had every

00:30:33.250 --> 00:30:38.130
part of the dramas of a like. I mean, it's a gripping story because they had

00:30:38.130 --> 00:30:43.049
everything there. They did their taxes with like what was the the program that they used,

00:30:44.170 --> 00:30:49.049
Quick books. They're dealing with billions of dollars. I don't

00:30:49.049 --> 00:30:53.799
know why I think the word polycule is so funny, but polycule, that was what they like when you

00:30:53.799 --> 00:30:58.519
call a relationship like a Poly but closed like polyamorous

00:30:58.599 --> 00:31:03.519
molecule put together. Oh, I see. So they were like, this is our polycule. So there's nine of them and they're Poly or

00:31:03.519 --> 00:31:08.400
ten of them or whatever. Yeah, you call that a polycule. And I thought that was the funny, like, that became like a

00:31:08.400 --> 00:31:12.960
meme in Silicon Valley for a while that I thought was hilarious. You clearly want enough

00:31:12.960 --> 00:31:17.279
regulation that that can't happen, but they're.

00:31:18.119 --> 00:31:23.109
Like, well, I'm not against that happening. I'm against them doing what they did with the money, that's what I

00:31:23.109 --> 00:31:27.869
mean. Probably cool is kind of fun. Go for it. No, no, I mean you want enough thing that like FTX can't

00:31:27.869 --> 00:31:32.670
lose all of its depositors money. But, but I think there's an important point here which is you

00:31:32.670 --> 00:31:37.430
have all of this other regulation that people and and it didn't keep us safe

00:31:38.349 --> 00:31:43.230
and the basic thing which was like you know let's do that, that was

00:31:43.230 --> 00:31:48.230
not all of the crypto stuff people were talking about. Yes.

00:31:48.750 --> 00:31:53.750
I mean the the real fascinating crypto is Bitcoin to me. I mean that's the one that

00:31:53.750 --> 00:31:58.509
I think has the most likely possibility of becoming

00:31:59.430 --> 00:32:04.269
a universal viable currency. And it's, you know, it's

00:32:04.269 --> 00:32:08.910
limited in the amount that there can be. It's, you know, you people

00:32:08.910 --> 00:32:13.829
mind it with their own. It's like that to me is very fascinating and I love the fact

00:32:13.829 --> 00:32:18.690
that it's been implemented. And that at least something like I've had Andreas

00:32:18.690 --> 00:32:22.329
Antonopoulos on the podcast and he's when he talks about it,

00:32:23.410 --> 00:32:28.410
he's living it. He's spending all of his money. Everything he

00:32:28.410 --> 00:32:33.049
has paid is in Bitcoin. He pays his rent in Bitcoin. Everything he does is in Bitcoin. I

00:32:33.049 --> 00:32:36.490
I helped start a project called Worldcoin a few years ago.

00:32:37.690 --> 00:32:41.769
That's and so I've gotten to like, learn more about the space.

00:32:43.160 --> 00:32:47.880
I'm excited about it for the same reasons I'm excited about Bitcoin too. But I think this idea that we

00:32:47.880 --> 00:32:52.880
have a global currency that is outside of the control of any

00:32:52.880 --> 00:32:57.599
government is a super logical and important step

00:32:57.839 --> 00:33:02.759
on the tech tree. Yeah, agreed. I mean, why should the government control currency? I

00:33:02.759 --> 00:33:07.519
mean, the government should be dealing with all the pressing environmental, social,

00:33:07.519 --> 00:33:12.460
infrastructure issues, foreign policy issues, economic issues. The things that

00:33:12.460 --> 00:33:17.339
we need to be governed in order to have a peaceful and prosperous

00:33:17.339 --> 00:33:22.140
society that's equal and equitable. What do you think happens to money and

00:33:22.140 --> 00:33:27.099
currency after AGI? I I've wondered about that because I feel

00:33:27.099 --> 00:33:31.380
like with money, especially when money goes digital, the bottleneck is

00:33:31.380 --> 00:33:36.339
access. If we get to a point where all information

00:33:36.339 --> 00:33:41.180
is just freely shared everywhere, there are no secrets. There are no

00:33:41.180 --> 00:33:45.700
boundaries. There are no borders. We're reading minds. We have

00:33:45.700 --> 00:33:49.900
complete access to all of the information, of

00:33:49.980 --> 00:33:54.339
everything you've ever done, everything everyone's ever said. There's no hidden secrets.

00:33:55.230 --> 00:33:59.910
What is money then? Money is this digital thing. Well, how can you possess it?

00:34:00.069 --> 00:34:05.069
How can you possess this digital thing if there is literally no bottleneck?

00:34:05.069 --> 00:34:09.710
There's no barriers to anyone accessing any information because

00:34:09.710 --> 00:34:14.670
essentially it's just ones and zeros. Yeah. I mean, another way, I think the information frame

00:34:14.670 --> 00:34:19.670
makes sense. Another way is that like money is like a sort

00:34:19.670 --> 00:34:24.599
of way to trade labor or trade like a limited number of hard assets

00:34:24.599 --> 00:34:29.440
like land and houses and whatever. And if you think

00:34:29.440 --> 00:34:34.199
about a world where, like intellectual labor is just readily available

00:34:34.559 --> 00:34:39.360
and super cheap, then that's somehow

00:34:39.360 --> 00:34:44.119
very different. I I think there will always be goods that we want to be

00:34:44.119 --> 00:34:49.119
scarce and expensive, but it'll only be those goods that we want to be scarce and expensive that's in

00:34:49.119 --> 00:34:54.090
services that still are. And so money in a world like that, I think it's just a it's

00:34:54.090 --> 00:34:58.849
a very curious idea. Yeah, it becomes a different thing. I mean, it's not a bag of

00:34:58.849 --> 00:35:03.849
gold in a leather pouch that you're carrying around. I'm going to. Do. It's not going

00:35:03.849 --> 00:35:08.369
to do much good. But then the question becomes, how is that money distributed? And how do we

00:35:08.369 --> 00:35:13.170
avoid some horrible Marxist society where there's one

00:35:13.210 --> 00:35:18.050
totalitarian government that just don't? Yeah, that would be bad. I think you've got to like

00:35:19.289 --> 00:35:24.130
my my current best idea and maybe there's something better is I think you act like if if we are

00:35:24.130 --> 00:35:28.769
right, a lot of reasons we could be wrong. But if we are right that like the a GI

00:35:28.769 --> 00:35:33.730
systems of which there will be a few become the high order bits of sort

00:35:33.730 --> 00:35:37.769
of influence whatever in the world. I think you do need like,

00:35:39.489 --> 00:35:44.449
not to just redistribute the money, but the access so that people can make their own decisions about how to use it

00:35:44.530 --> 00:35:49.469
and how to govern it. And if you've got one idea, you get to do this. If I've got one idea,

00:35:49.469 --> 00:35:54.190
I get to do that, and I have like rights to basically do whatever I want with

00:35:54.190 --> 00:35:58.949
my part of it. And if I come up with better ideas than you, I get rewarded. But for that by whatever the

00:35:58.949 --> 00:36:03.829
society is or vice versa. You know, the the hardliners, the people that are

00:36:03.829 --> 00:36:07.829
against like welfare and against any sort of you G

00:36:09.150 --> 00:36:13.909
universal basic income, Ubi. What they're what they're really concerned with is human

00:36:13.909 --> 00:36:18.909
nature. Right. They believe that if you remove incentives, if you just

00:36:18.909 --> 00:36:23.630
give people free money, they become addicted to it. They become lazy. But isn't

00:36:23.630 --> 00:36:28.110
that a human biological and psychological bottleneck?

00:36:28.469 --> 00:36:32.710
And perhaps with the implementation

00:36:33.349 --> 00:36:38.269
of artificial intelligence combined with some

00:36:38.269 --> 00:36:42.030
sort of neural interface, whether it's external or internal.

00:36:43.550 --> 00:36:48.190
It seems like that's a problem that can be solved

00:36:48.710 --> 00:36:53.550
that you can essentially, and this is where it gets really spooky. You can

00:36:53.550 --> 00:36:58.469
reengineer the human biological system and you can remove

00:36:58.710 --> 00:37:03.710
all of these problems that people have that are essentially problems that date back

00:37:03.710 --> 00:37:08.670
to human reward systems when we were tribal people. Hunter, gatherer, people, whether it's

00:37:08.670 --> 00:37:13.510
jealousy, lust, envy, all these all these variables that come

00:37:13.510 --> 00:37:18.110
into play when you're dealing with money and status and social status,

00:37:18.909 --> 00:37:23.750
if those are eliminated with technology and essentially we become a

00:37:23.750 --> 00:37:28.590
next version of what the human species is possible like, look,

00:37:29.269 --> 00:37:33.309
we're very, very far removed from tribal

00:37:33.429 --> 00:37:38.159
brutal. Societies of cave people, we all

00:37:38.159 --> 00:37:42.440
agree that this is a way better way to live. It's a it's a it's it's way

00:37:42.440 --> 00:37:47.199
safer. You know, we were like, I I was talking about this in my comedy club last night

00:37:47.440 --> 00:37:51.920
because we're because my wife was. We were talking about DNA and

00:37:52.360 --> 00:37:57.119
my wife was saying that, look, everybody came from cave people, which is kind of a fucked up thought that everyone

00:37:57.119 --> 00:38:01.760
here is here because of cave people. Well, that, all that still in our DNA,

00:38:02.039 --> 00:38:07.010
all that, still that and these. Reward systems can be hijacked,

00:38:07.010 --> 00:38:11.929
and they can be hijacked by just giving people money. And like, you don't have to work, you don't have to do anything, you don't have to

00:38:11.929 --> 00:38:16.530
have ambition, you'll just have money and just just lay around and do drugs.

00:38:17.010 --> 00:38:21.730
That's what the that's the fear that people have of giving people free money. But

00:38:22.690 --> 00:38:26.889
if we can figure out how to literally

00:38:26.889 --> 00:38:31.889
engineer the human biological vehicle and

00:38:31.889 --> 00:38:36.260
remove? All those pitfalls, if we can

00:38:36.619 --> 00:38:40.579
enlighten people technologically, maybe enlightened is the wrong word.

00:38:40.860 --> 00:38:45.860
But advance the human species to the point where

00:38:45.860 --> 00:38:50.659
those are no longer dilemmas, because those are easily solvable through

00:38:50.659 --> 00:38:55.500
coding. They're easily solvable through enhancing the human

00:38:55.500 --> 00:39:00.420
biological system, perhaps raising dopamine levels to the point where anger and

00:39:00.420 --> 00:39:05.340
fear and hate are impossible. They don't exist. And

00:39:05.340 --> 00:39:10.179
if I mean if you just had everyone on Mali, how many wars would there be? There

00:39:10.380 --> 00:39:15.139
would be 0 wars. I mean, I think if you could get everyone on earth to all do Mali

00:39:15.579 --> 00:39:20.420
once on the same day, that'd be a tremendous thing. If you got everybody on earth to do Molly every day, that

00:39:20.539 --> 00:39:25.420
would be a real loss. But what if they did a low dose of Molly where you just get

00:39:25.460 --> 00:39:30.380
to where everybody greets people with love and

00:39:30.380 --> 00:39:35.019
affection and there's no longer concerned about competition. Instead

00:39:35.260 --> 00:39:40.219
the concern is about the fascination of innovation and creation and

00:39:40.219 --> 00:39:45.139
creativity. Man, we could talk the rest of the time about this one topic. It's

00:39:45.139 --> 00:39:47.019
it's so interesting. I I I think

00:39:50.900 --> 00:39:55.619
if I could like push a button to like remove all human striving

00:39:55.780 --> 00:40:00.380
and conflict, I wouldn't do it. First of all, like I think that's a

00:40:00.659 --> 00:40:05.659
very important part of our story and experience and and

00:40:05.659 --> 00:40:10.019
also I think we can see both from our own biological

00:40:10.179 --> 00:40:14.570
history and also from. What we know about a I that

00:40:14.769 --> 00:40:19.530
very simple goal systems, fitness

00:40:19.530 --> 00:40:23.369
functions, reward models, whatever you want to call it, lead to incredibly

00:40:23.849 --> 00:40:28.730
impressive results. You know, if the biological imperative is survive and

00:40:28.730 --> 00:40:33.650
reproduce, look how far that has somehow gotten us as a

00:40:33.650 --> 00:40:38.130
society. All of this, all this stuff we have, all this technology, this building, whatever else like

00:40:40.449 --> 00:40:44.889
that, that got here

00:40:45.530 --> 00:40:50.250
through an extremely simple goal in a very complex

00:40:50.250 --> 00:40:55.010
environment, leading to all of the richness and complexity of people

00:40:56.690 --> 00:41:01.210
fulfilling this biological imperative to some degree and wanting to impress each other.

00:41:03.050 --> 00:41:08.050
So I think, like, evolutionary fitness is a simple and unbelievably powerful idea. Now,

00:41:09.730 --> 00:41:14.449
could you carefully edit out every individual manifestation of that?

00:41:16.690 --> 00:41:21.570
Maybe. But I I don't want to, like, live in a Society of drones where everybody is just sort of

00:41:21.570 --> 00:41:26.449
like, on Molly all the time either. Like, that doesn't seem

00:41:26.530 --> 00:41:31.409
like the right answer. Like, I want us to get you to strive. I want us to continue

00:41:31.409 --> 00:41:36.289
to push back the frontier and go out and explore. And I actually think something's

00:41:36.289 --> 00:41:40.039
already gotten a little off track in society

00:41:41.079 --> 00:41:46.039
about all of that. And we're. I don't know. I think

00:41:46.159 --> 00:41:51.000
like I'm, I don't thought I'd be older by the time I felt like the

00:41:51.000 --> 00:41:55.280
old guy complaining about the youth. But I think we've

00:41:55.960 --> 00:42:00.840
lost something and I think that we need

00:42:00.840 --> 00:42:05.599
more striving, maybe more risk taking, more like

00:42:06.969 --> 00:42:09.889
explorer spirit. What do you mean by you think we've lost something?

00:42:18.289 --> 00:42:22.610
I mean, here's like a version of it very much from my

00:42:23.250 --> 00:42:27.730
own lens. I was a startup investor for a long time, and it

00:42:28.050 --> 00:42:32.369
often was the case that the very best startup founders were

00:42:32.969 --> 00:42:37.809
in their early or mid 20s or late 20s maybe even. And now they skew much

00:42:37.809 --> 00:42:42.800
older. And what I want to know is in the world today where the Super

00:42:42.800 --> 00:42:47.760
great 25 year old founders and there are few, it's not fair to say there are none, but there are less than they were

00:42:47.760 --> 00:42:49.760
before. And

00:42:53.519 --> 00:42:58.480
I think that's bad for society at all levels. I mean like tech company founders is one example,

00:42:58.480 --> 00:43:03.480
but like people who go off and create something new who push on a disagreeable or

00:43:03.480 --> 00:43:07.280
controversial idea, we need that to drive forward.

00:43:08.480 --> 00:43:13.400
We need that sort of spirit. We need people to be able to, you

00:43:13.400 --> 00:43:18.360
know, put out ideas and be wrong and not be ostracized from society for it or

00:43:18.360 --> 00:43:23.280
not have it be like, you know, something that they get cancelled for or or whatever. We need people to be able

00:43:23.280 --> 00:43:28.000
to take a risk in their career because they believe in some important scientific

00:43:28.000 --> 00:43:32.400
quest that may not work out or may sound like really controversial or bad or whatever.

00:43:33.719 --> 00:43:38.639
You know, certainly when we started opening eye and we were saying we think this a GI thing is

00:43:38.639 --> 00:43:43.539
is real and could be, you know, could be done. Unlikely, but so important if it happens.

00:43:43.980 --> 00:43:48.860
And all of the older scientists in our field were saying those people are irresponsible,

00:43:48.940 --> 00:43:53.739
you shouldn't talk about e.g. I. That's like, you know, they're like selling a scam or they're like,

00:43:54.179 --> 00:43:59.059
you know, they're kind of being reckless and it's going to lead to an A GI winter.

00:43:59.099 --> 00:44:04.019
Like we said, we believed. We said at the time we knew it was unlikely, but it was an important quest

00:44:04.619 --> 00:44:09.340
and we were going to go after it and kind of like fuck the haters. That's important to a

00:44:09.340 --> 00:44:14.190
society. What do you think is the origin Like

00:44:14.190 --> 00:44:19.070
what? Why do you think there are less young people that are doing

00:44:19.070 --> 00:44:22.949
those kind of things now as opposed to a decade or two ago?

00:44:25.550 --> 00:44:30.469
I'm so interested in that topic. I'm tempted to blame the education

00:44:30.469 --> 00:44:35.150
system, but I sure that I think that like, interacts with society

00:44:36.949 --> 00:44:41.570
in all of these strange ways. It's funny, there was this like

00:44:41.570 --> 00:44:46.170
thing all over my Twitter feed recently trying to talk about like what? You know what? Like

00:44:46.809 --> 00:44:51.730
what caused the drop in testosterone in American men over the last few decades. And no one was

00:44:51.730 --> 00:44:56.730
like, this is a symptom, not a cause. And everyone was

00:44:56.730 --> 00:45:01.730
like, oh, it's the microplastics, it's the birth control pills, it's the whatever, it's the whatever. It's the whatever. And I think

00:45:01.730 --> 00:45:05.769
this is like not at all the most important

00:45:07.510 --> 00:45:11.510
piece of this topic, but it was just interesting to me sociologically

00:45:12.469 --> 00:45:16.829
that there was, there was only talk about it being

00:45:17.829 --> 00:45:22.349
about what what caused it, not about it being an effect of some sort of change in society.

00:45:24.869 --> 00:45:29.269
But isn't what caused it? Well, there's biological

00:45:29.829 --> 00:45:34.070
reasons why, like when we talk about the phthalates and microplastic

00:45:34.070 --> 00:45:38.940
pesticides, environmental factors. Those are real. Totally. And I don't like

00:45:38.940 --> 00:45:43.739
again, I'm so far out of my depth and expertise here. This was it was just interesting to me that the only

00:45:43.739 --> 00:45:48.179
talk was about like biological factors and not that somehow society can have

00:45:48.940 --> 00:45:53.920
some sort of effect. Well, society most certainly has an effect. Do you know what the answer to this is?

00:45:54.000 --> 00:45:58.840
I. I don't. I mean, I I've I've had a podcast with Doctor Shanna Swan

00:45:58.840 --> 00:46:03.599
who wrote the book Countdown, and that is all about the introduction of petrochemical

00:46:03.599 --> 00:46:08.599
products and the correlating drop in testosterone rise

00:46:08.599 --> 00:46:12.960
in miscarriages. The fact that these are ubiquitous endocrine

00:46:12.960 --> 00:46:17.530
disruptors that. When they do blood tests on people, they find

00:46:17.530 --> 00:46:22.530
some insane number. It's like 90 plus percent of people have phthalates in

00:46:22.530 --> 00:46:27.210
your system. And you, I appreciate the metal cups. Yeah, we, we, we try to

00:46:27.690 --> 00:46:32.650
mitigate it as much as possible. But I mean, you're getting it. If you're microwaving food, you're you're fucking

00:46:32.650 --> 00:46:37.289
getting it. You're get, you're just getting it. You get if you eat processed food, you're getting it. You're getting a certain amount of

00:46:37.289 --> 00:46:42.280
microplastics in your diet and. Estimates have been that it's as high as a credit

00:46:42.280 --> 00:46:47.280
card of microplastics. In your body, you consume a credit card of that a

00:46:47.280 --> 00:46:52.199
week. The real concern is with mammals, because the

00:46:52.199 --> 00:46:57.199
introductions, when they've done studies with mammals and they've introduced phthalates into their

00:46:57.199 --> 00:47:02.119
body, there's a correlating one thing that happens

00:47:02.119 --> 00:47:06.690
is the the these animals, they're taint shrink. Like the

00:47:06.690 --> 00:47:11.250
taint of, yeah, the mammal. When you look at males, it's 50% to

00:47:11.250 --> 00:47:16.130
100% larger than the females. With the introduction of thalids on the males, the taints

00:47:16.250 --> 00:47:21.130
start shrinking, the penises shrink, the testicles shrinks, sperm count shrinks. So we know

00:47:21.130 --> 00:47:25.170
there's a direct biological connection between the the,

00:47:26.250 --> 00:47:30.369
this, these chemicals and how they interact with with bodies.

00:47:31.250 --> 00:47:36.099
So that's that's a real one and it's also. The amount of

00:47:36.099 --> 00:47:40.619
petrochemical products that we have, the amount of plastics that we use, it's

00:47:41.139 --> 00:47:45.940
it is such an integral part of our culture and our society, our civilization.

00:47:46.539 --> 00:47:51.539
It's everywhere. And I've wondered if you think about

00:47:51.940 --> 00:47:56.260
how these territorial

00:47:56.380 --> 00:48:00.860
apes evolve into this new

00:48:00.940 --> 00:48:05.590
advanced species. Wouldn't one of the very

00:48:05.590 --> 00:48:10.269
best ways be to get rid of one of the things that

00:48:10.269 --> 00:48:14.789
causes the most problems, which is testosterone? We need testosterone where we need

00:48:14.789 --> 00:48:19.349
aggressive men and protectors. But why do we need them? We need them because there's other

00:48:19.349 --> 00:48:23.909
aggressive men that are evil, right? So we need protectors from

00:48:23.949 --> 00:48:28.869
ourselves. We need the good, strong people to protect us from the bad,

00:48:28.869 --> 00:48:33.800
strong people. But if we're. In the process of integrating with

00:48:33.800 --> 00:48:38.639
technology, if technology is an inescapable part of our life, if it

00:48:38.639 --> 00:48:43.480
is everywhere you're using it, you have the Internet of everything that's in your microwave and

00:48:43.480 --> 00:48:47.519
your television, your computers, everything you use.

00:48:48.599 --> 00:48:53.599
As time goes on, that will be more and more part of your life. And as these

00:48:53.599 --> 00:48:58.199
plastics are introduced into the human biological system, you're seeing a

00:48:58.199 --> 00:49:02.460
feminization of the males of the species. You're seeing a

00:49:02.460 --> 00:49:07.019
downfall in birth rate. You're seeing all these correlating factors

00:49:07.539 --> 00:49:11.539
that would sort of lead us to become this more

00:49:12.179 --> 00:49:17.019
peaceful, less violent, less aggressive,

00:49:17.260 --> 00:49:22.059
less ego driven thing, which the world is definitely

00:49:22.059 --> 00:49:26.780
becoming more time. And I'm all for less violence,

00:49:26.820 --> 00:49:30.380
obviously, but I don't

00:49:35.090 --> 00:49:39.090
look obviously testosterone has many great things to say for it and some

00:49:40.050 --> 00:49:44.650
bad tendencies too. But I don't think a world, if we, if we leave that out of the

00:49:44.650 --> 00:49:46.849
equation and just say like a world that has a a

00:49:49.050 --> 00:49:53.050
spirit that you know, we're going to

00:49:53.809 --> 00:49:58.809
defend ourselves, we're going to, we're

00:49:58.809 --> 00:50:03.659
going to find a way to like protect ourselves and our tribe and

00:50:03.659 --> 00:50:08.579
our society into this future, which you can get with lots of other ways. I think that's an important

00:50:08.900 --> 00:50:12.500
impulse. More than that though, what I meant

00:50:15.579 --> 00:50:20.579
is about if we go back to the issue of like where are the young founders, why don't

00:50:20.579 --> 00:50:25.460
we have, why don't we have more of those. And I don't think it's just the tech startup industry. I

00:50:25.460 --> 00:50:30.349
think you could say that about like young scientists or or many other categories. Those are maybe just the ones that I,

00:50:30.349 --> 00:50:31.349
I know the best

00:50:35.190 --> 00:50:40.030
in a world with any amount of

00:50:40.030 --> 00:50:44.949
technology. I still think we we've got it. It is our

00:50:44.949 --> 00:50:49.869
destiny in some sense to stay on this, on this curve, and we

00:50:49.869 --> 00:50:54.590
still need to go figure out what's next and after the next hill and after the next hill. And

00:50:54.670 --> 00:50:59.190
it would be. My

00:50:59.190 --> 00:51:04.190
perception is that there is some longterm societal change happening here, and I think it makes

00:51:04.190 --> 00:51:08.949
us less happy to. Right. It may

00:51:08.949 --> 00:51:13.789
make us less happy, but what I'm saying is, if the human species does

00:51:13.789 --> 00:51:18.750
integrate with technology, wouldn't a great way to facilitate that

00:51:18.989 --> 00:51:23.780
to be to kind of feminize the the primal apes? And

00:51:23.780 --> 00:51:28.460
to sort of downplay the role, you mean like the tech, like should the AGI?

00:51:29.380 --> 00:51:34.099
Well, maybe. I don't know if it's AGI. I mean, maybe it's just an inevitable, inevitable consequences

00:51:34.420 --> 00:51:39.139
of technology, because especially the type of technology that we use,

00:51:39.139 --> 00:51:43.940
which does have so much plastic in it. And then on top of that, the technology that's

00:51:43.940 --> 00:51:48.940
involved in food systems, preservatives, all these different things that we use to make sure that people don't starve

00:51:48.940 --> 00:51:53.639
to death, we've made incredible strives in that. There are very few people in this

00:51:53.639 --> 00:51:57.960
country that starve to death. Yeah, it is not. It's not a primary issue, but

00:51:57.960 --> 00:52:02.559
violence is a primary issue. But our our

00:52:02.559 --> 00:52:07.440
concerns about violence are in Our concerns about testosterone and

00:52:07.440 --> 00:52:12.199
strong men and powerful people is only because we need to

00:52:12.199 --> 00:52:17.159
protect. Against we need to protect against others, same thing. Is that really the only

00:52:17.159 --> 00:52:21.809
reason? Sure. I mean, how many, like, incredibly violent women are out there running

00:52:21.809 --> 00:52:23.730
gangs? No, no, that part for sure. Yeah,

00:52:26.690 --> 00:52:31.010
what I meant more is, is that the only reason that society values like strong

00:52:31.010 --> 00:52:35.730
masculinity? Yeah, I think so. I think it's a biological imperative, right?

00:52:35.969 --> 00:52:40.889
And I think that biological imperative is because we used to have to defend against incoming tribes

00:52:40.889 --> 00:52:45.570
and predators and animals and and we we needed someone who was

00:52:45.570 --> 00:52:50.440
stronger than most to defend the rest. And like that's the concept of the

00:52:50.440 --> 00:52:55.159
military. That's why Navy SEAL training so difficult. We want the strongest of the

00:52:55.159 --> 00:53:00.119
strong to be at the tip of the spear. But that's only because there's people like

00:53:00.119 --> 00:53:04.519
that out there that are bad if general and artificial general

00:53:04.519 --> 00:53:08.840
intelligence and the implementation of some sort of a device that changes the

00:53:08.840 --> 00:53:13.840
biological structure of human beings to the point where that is no longer a

00:53:13.840 --> 00:53:18.440
concern. Like if you are me and I am you, and I know this because of

00:53:18.440 --> 00:53:23.280
technology, violence is impossible. Look, by the time if this goes all the way down the

00:53:23.280 --> 00:53:28.280
scifi path and we're all like merged into this one single, like planetary, universal, whatever

00:53:28.280 --> 00:53:32.880
consciousness, then, then then yes, you don't. You don't need testosterone. Need

00:53:32.880 --> 00:53:37.280
testosterone. But. Especially if we can reproduce through other methods.

00:53:38.110 --> 00:53:42.630
Like, this is the alien hypothesis, right? Like, why do they look so spindly and without any

00:53:42.630 --> 00:53:47.269
gender? And you know when they have these big heads and they don't need physical strength. They don't need physical

00:53:47.269 --> 00:53:51.829
strength. They they have some sort of a telepathic way of communicating. They probably don't need

00:53:51.829 --> 00:53:56.750
sounds with their mouths, and they don't need this urge that

00:53:56.750 --> 00:54:01.469
we have to conquer and to spread our DNA. Like that's so much of what

00:54:01.469 --> 00:54:06.389
people do, is these reward systems that were established when we were

00:54:06.389 --> 00:54:10.000
territorial apes. There's a question to me about how much you can

00:54:12.119 --> 00:54:16.519
ever get rid of rid of that if you make

00:54:17.079 --> 00:54:21.599
an A GI and it decides actually, we don't need to

00:54:21.599 --> 00:54:26.559
expand. We don't need more territory. We're just like, happy we at this point, you and me, it the

00:54:26.559 --> 00:54:31.480
whole thing altogether all merge in. We're happy here on Earth. We don't need to get any bigger. We don't

00:54:31.480 --> 00:54:36.469
need to reproduce. We don't need to grow. We're just going to sit here and run a That

00:54:36.469 --> 00:54:41.309
sounds like a boring life. I don't agree with that. I don't agree that that would be the logical

00:54:41.309 --> 00:54:46.030
conclusion. I think the logical conclusion would be they

00:54:46.030 --> 00:54:50.949
would look for problems and frontiers that are

00:54:50.989 --> 00:54:55.949
insurmountable to our current existence, like intergalactic communication

00:54:55.949 --> 00:55:00.909
and transportation. What happens when it meets another AGI? The other Galaxy over? What happens if it meets

00:55:00.909 --> 00:55:04.989
an AGI that's a million years more advanced or that like, what does that look like?

00:55:06.000 --> 00:55:10.679
Yeah, that's what I've I've often wondered if we are I I call ourselves the

00:55:10.679 --> 00:55:15.480
biological caterpillars that create the electronic butterfly, that we're making a cocoon. Right

00:55:15.480 --> 00:55:19.599
now, we don't even know what we're doing. And I think it's also tied into consumerism,

00:55:20.159 --> 00:55:25.159
because what does consumerism do? Consumerism facilitates the creation of newer and

00:55:25.159 --> 00:55:29.840
better things because you always want the newest, latest, greatest. So you have more

00:55:29.840 --> 00:55:34.650
advanced technology and automobiles and computers and cell phones and. And

00:55:34.650 --> 00:55:37.570
all of these different things including medical science,

00:55:40.809 --> 00:55:45.809
that's all for sure true. The thing I was like reflecting on as you

00:55:45.809 --> 00:55:48.409
were saying that is I don't think I

00:55:51.730 --> 00:55:55.090
I'm not as optimistic that we can or even should

00:55:56.130 --> 00:56:01.130
overcome our biological base to the degree that I think you

00:56:01.130 --> 00:56:06.110
think we can. And you know to even go back one further level like I

00:56:06.110 --> 00:56:10.989
I think I think society is happiest where there's

00:56:10.989 --> 00:56:15.750
like roles for strong femininity and strong masculinity in the same people and in different

00:56:15.750 --> 00:56:20.429
people. And and I don't

00:56:20.510 --> 00:56:25.469
like and I don't think

00:56:25.469 --> 00:56:30.190
a lot of these, like deep seated things are going to

00:56:30.469 --> 00:56:34.840
be able to get pushed aside very easily and still have

00:56:35.400 --> 00:56:40.079
a system that works. Like sure, we can't really think about what if there were

00:56:40.079 --> 00:56:44.800
consciousness in a machine someday or whatever, what that would be like. And

00:56:44.800 --> 00:56:49.719
maybe maybe I'm just like thinking too smallmindedly. But I think there

00:56:49.719 --> 00:56:54.639
is something about us that

00:56:54.639 --> 00:56:59.440
has worked in a super deep way and it took evolution a

00:56:59.440 --> 00:57:03.750
lot of search space to get here. But I wouldn't discount it too easily.

00:57:04.349 --> 00:57:08.630
But don't you think that cave people would probably have those same logical conclusions

00:57:09.469 --> 00:57:14.469
about life and sedentary lifestyle And sitting in front of a computer and not interacting with each other except

00:57:14.469 --> 00:57:17.829
through text? Well.

00:57:19.489 --> 00:57:23.969
I mean, isn't that like what you're saying is correct? How different do you think our motivations are

00:57:23.969 --> 00:57:28.849
today and kind of what really brings us genuine joy and how we're how we're

00:57:28.849 --> 00:57:33.690
wired at some deep level differently than cave people? Clearly lots of other things have changed. We've got

00:57:33.690 --> 00:57:38.170
better, much better tools. But how different do you think he really is? I think

00:57:38.849 --> 00:57:43.570
that's the problem is that genetically at the base level, there's not much

00:57:43.570 --> 00:57:47.760
difference. And that these reward systems are all

00:57:48.400 --> 00:57:52.800
there. We interact with all of them. Whether it's ego,

00:57:53.000 --> 00:57:58.000
lust, passion, fury, anger, jealousy, all

00:57:58.000 --> 00:58:02.679
these different things that you think will be. Some people will upload and edit those out. Yes,

00:58:03.400 --> 00:58:08.199
yeah, I think that our concern with losing this aspect of

00:58:08.199 --> 00:58:13.110
what it means to be a person. This like the idea that we should always have conflict and

00:58:13.110 --> 00:58:17.550
struggle, because conflict and struggle is how we facilitate progress, which is true,

00:58:17.909 --> 00:58:22.789
right? And combating evil is how the good gets greater and stronger if the good

00:58:22.789 --> 00:58:27.429
wins. But my concern is that that is all predicated on the

00:58:27.429 --> 00:58:31.909
idea that the biological system that we have right now is

00:58:32.670 --> 00:58:37.590
correct and optimal. And I think.

00:58:37.960 --> 00:58:42.960
One of the things that we're dealing with, with the heightened states of depression and anxiety and the

00:58:42.960 --> 00:58:47.559
lack of meaning and existential angst that people experience, a lot of that is

00:58:47.559 --> 00:58:52.000
because the biological reality of being a human

00:58:52.000 --> 00:58:56.719
animal doesn't really integrate that well with this

00:58:56.719 --> 00:59:01.320
world that we've created, that's for sure. Yeah, and I

00:59:01.320 --> 00:59:06.119
wonder if the solution to that is not find

00:59:06.119 --> 00:59:10.110
ways. To find meaning with the biological,

00:59:11.110 --> 00:59:15.789
you know, vessel that you've been given, but rather engineer

00:59:15.789 --> 00:59:20.550
those aspects that are problematic out of the system.

00:59:21.630 --> 00:59:26.550
To create a truly enlightened being. Like one of the things, if you ask someone today, what are the

00:59:26.590 --> 00:59:30.989
odds that in three years there will be no war in the world? It's

00:59:30.989 --> 00:59:35.750
zero. Like nobody thinks. No, there's never been a time in human history where we

00:59:35.750 --> 00:59:40.190
haven't had war. If you had to say what is our number one problem as a

00:59:40.190 --> 00:59:45.150
species, well, I would say our number one problem is, is war. Our number

00:59:45.150 --> 00:59:50.150
one problem is this idea that it's okay to send massive groups

00:59:50.150 --> 00:59:54.670
of people who don't know each other. They go murder massive groups of people that are somehow opposed

00:59:54.909 --> 00:59:59.869
because of the government, because of wines in the sand territory. It's

00:59:59.869 --> 01:00:04.230
an insane thing. How do you get rid of that? Well, one of the ways you get rid of that is to

01:00:04.230 --> 01:00:08.869
completely engineer out all the human reward systems that pertain

01:00:09.070 --> 01:00:14.070
to the acquisition of of resources. So what's left at that point? Well,

01:00:14.070 --> 01:00:18.630
we're a new thing. I think we've become a new. And what does that thing do want?

01:00:18.949 --> 01:00:23.550
I think that new thing would probably want to interact with other new things that are even more

01:00:23.550 --> 01:00:26.829
advanced than it. I do believe that.

01:00:29.159 --> 01:00:33.639
Scientific curiosity can drive quite That can be a great

01:00:33.639 --> 01:00:38.639
frontier for a long time. Yeah, I think

01:00:38.639 --> 01:00:43.440
it can be a great frontier for a long time as well. I just wonder if what we're seeing

01:00:43.440 --> 01:00:48.190
with the drop in testosterone because of microplastics, which sort of just

01:00:48.190 --> 01:00:53.150
snuck up on us, we didn't even know that it was an issue until people started studying. How certain is that

01:00:53.150 --> 01:00:57.949
at this point that that's what's happening? I don't want. To study it's it's a very good question.

01:00:57.989 --> 01:01:02.829
Doctor Shanna Swann believes that it's the primary driving factor of

01:01:02.829 --> 01:01:07.110
the sort of drop in testosterone and all miscarriage issues and

01:01:07.750 --> 01:01:12.630
low birth weights. The the all those things seem to have a direct there's a seems to be a direct

01:01:12.630 --> 01:01:17.429
factor environmentally. I'm sure there's other factors too. I mean the the drop in

01:01:17.429 --> 01:01:22.309
testosterone, I mean it's it's been shown that you can increase males testosterone through

01:01:22.309 --> 01:01:27.269
resistance training and through making. There's certain things you can do like one

01:01:27.269 --> 01:01:32.150
of the big ones they found through a study in Japan is cold water immersion before

01:01:32.150 --> 01:01:36.949
exercise radically increases testosterone. So you cold

01:01:36.949 --> 01:01:41.869
water immersion and then exercise. I wonder why that. Yeah, I don't see you can find

01:01:41.869 --> 01:01:46.829
that but it's it's a fascinating field of study. But I think it

01:01:46.829 --> 01:01:51.590
has something to do with resilience and resistance and the fact that your body has to combat this

01:01:51.989 --> 01:01:56.789
external factor that's very extreme, that causes the body to go into

01:01:56.909 --> 01:02:01.909
this state of preservation. And the the the implementation of

01:02:01.909 --> 01:02:06.820
cold shock proteins and the reduction of inflammation, which also enhances

01:02:06.820 --> 01:02:11.619
the body's endocrine system. But then on top of that, this imperative that you have to become more

01:02:11.619 --> 01:02:16.500
resilient to survive this external factor that you've introduced into your

01:02:16.500 --> 01:02:21.099
life every single day. So there's ways

01:02:21.820 --> 01:02:26.219
obviously that you can make a human being more robust.

01:02:26.780 --> 01:02:31.019
You know, we know that we can do that through strength training and that all that stuff actually does raise

01:02:31.019 --> 01:02:35.460
testosterone. Your diet can raise testosterone and the

01:02:36.219 --> 01:02:41.139
a poor diet will lower it and will hinder your integrin system, will hinder your ability to

01:02:41.139 --> 01:02:45.380
produce growth hormone, melatonin and all all these different factors.

01:02:46.019 --> 01:02:50.420
That seems to be something that we can fix in terms or at least

01:02:50.420 --> 01:02:55.260
mitigate in terms with with decisions and choices and effort. But

01:02:55.260 --> 01:03:00.059
the fact that these petrochemical, like there's a graph that

01:03:00.219 --> 01:03:05.099
Doctor Shanna Swan has in her book that shows during the 1950s when they

01:03:05.099 --> 01:03:10.099
start using petrochemical products and everything microwave, plastic, Saran

01:03:10.099 --> 01:03:14.820
wrap, all this different stuff. There's a direct correlation between the

01:03:14.820 --> 01:03:19.579
implementation and the dip, and it all seems to line up

01:03:19.579 --> 01:03:24.480
like that seems to be a primary factor. Does it

01:03:24.480 --> 01:03:28.960
have an equivalent impact on like estrogen related hormones? That's a good

01:03:28.960 --> 01:03:33.679
question. Some of them actually. I know some of

01:03:33.679 --> 01:03:38.639
these chemicals that they're talking about actually increase estrogen in men, I don't

01:03:38.639 --> 01:03:43.480
know, but I do know that it increases miscarriages. So I just

01:03:43.480 --> 01:03:48.039
think it's overall disruptive to the. Definitely a societal wide

01:03:48.440 --> 01:03:53.349
disruption of the endoconsistent in a short period of time seems like a just. Bad

01:03:53.349 --> 01:03:58.030
and sure difficult to wrap our heads. And then pollutants and and environmental

01:03:58.030 --> 01:04:02.230
toxins on top of the pesticides and herbicides and all these other things and

01:04:02.230 --> 01:04:06.590
microplastics. There's a lot of factors that are leading our system to not work well.

01:04:08.789 --> 01:04:13.630
But I I just really wonder if this

01:04:13.789 --> 01:04:18.750
like, are we just clinging on to this monkey body? Are we deciding? I like my monkey body. I

01:04:18.750 --> 01:04:23.500
do too. Listen. I love it. But I'm also, I try to be very

01:04:23.500 --> 01:04:28.420
objective. And when I objectively look at it in terms of like if you take where

01:04:28.420 --> 01:04:33.340
we are now and all of our problems and you look towards the future and like

01:04:33.699 --> 01:04:38.500
what would be one way that you could mitigate a lot of these? And

01:04:38.500 --> 01:04:42.820
well, it would be the implementation of some sort of a telepathic technology where

01:04:43.559 --> 01:04:48.440
you know, you couldn't just text someone or tweet at someone something mean. Because you would

01:04:48.440 --> 01:04:53.400
literally feel what they feel when you put that energy out there. And

01:04:53.400 --> 01:04:57.480
you would, you would be repulsed and and then

01:04:57.880 --> 01:05:02.719
violence would be if you were committing violence on someone and you

01:05:02.719 --> 01:05:07.199
literally felt the reaction of that violence in your own being.

01:05:08.679 --> 01:05:13.429
And you would also have no motivation for violence if we had

01:05:13.429 --> 01:05:18.389
no aggressive tendencies, no primal chimpanzee tendencies. You know,

01:05:18.389 --> 01:05:23.070
it's it's true that violence in the world has obviously gone down a lot over the

01:05:23.070 --> 01:05:28.070
decades, but emotional violence is up a lot and the Internet has been horrible for that.

01:05:28.510 --> 01:05:33.429
Like, I don't walk. I'm not going to walk over there and punch you because you look like a big strong guy. You're going to punch me back. And also there's a

01:05:33.590 --> 01:05:38.449
societal convention not to do that. But. If I didn't know you, I might like

01:05:38.610 --> 01:05:42.570
send a mean tweet about you and I feel nothing on that. And

01:05:43.130 --> 01:05:48.010
clearly that has become like a mega epidemic in society

01:05:48.010 --> 01:05:51.369
that we did not evolve the biological

01:05:53.570 --> 01:05:56.570
constraints on somehow. And

01:05:58.530 --> 01:06:03.280
I'm actually very. Worried about how much that's already destabilized?

01:06:03.280 --> 01:06:08.280
Dustin made us all miserable. It's certainly accentuated it. It's exacerbated

01:06:08.280 --> 01:06:13.239
all of our problems. It's, I mean, if you read Jonathan Hates book, The Cotton of the American Mind,

01:06:13.239 --> 01:06:18.159
if you read a great book, yeah, it's great book. And it's, it's very damaging to women, particularly young

01:06:18.159 --> 01:06:22.920
girls, young girls growing up. There's a direct correlation between the invention of social media,

01:06:23.239 --> 01:06:27.760
the introduction to the iPhone, self harm, suicide, online

01:06:27.760 --> 01:06:32.670
bullying. You know, like people have always talked shit about people when no one's around. I think the

01:06:32.670 --> 01:06:36.989
fact that they're doing it now openly to to harm people.

01:06:37.190 --> 01:06:42.190
Horrible, obviously. I think it's super damaging to men to maybe they just like, talk about it less, but I

01:06:42.190 --> 01:06:46.989
don't think any of us are like, yeah, set up for this. No, no one's set up for it. And, you know, I

01:06:46.989 --> 01:06:51.989
think famous people know that more than anyone. We all get used to it, Yeah. You just get numb to

01:06:51.989 --> 01:06:56.989
it and or if you're wise, you don't engage. You know, I don't engage. I don't even have any apps on

01:06:56.989 --> 01:07:01.949
my new phone. Yeah, I've decided I got a new phone and I decided, OK, nothing that's really smart. No

01:07:01.949 --> 01:07:06.789
Twitter. So I have a separate phone that if I have to post someone, I'll something I pick

01:07:06.789 --> 01:07:11.349
up. But all I get on my new phone is text messages. And is that more

01:07:11.829 --> 01:07:16.670
just to, like, keep your mind pure and uncluded? Yeah, and not tempt myself. And to just you know

01:07:17.429 --> 01:07:22.309
what? Many fucking times I've got up to go to the bathroom first thing in the morning and spent an hour

01:07:22.869 --> 01:07:27.550
just sitting on the toilet scrolling through Instagram like for nothing does 0 for me.

01:07:27.980 --> 01:07:32.619
And there's this thought that I'm going to get something out of it. I was

01:07:32.739 --> 01:07:37.699
thinking actually just yesterday about how, you know, we all have talked

01:07:37.699 --> 01:07:41.900
for so long about these algorithmic feeds are going to manipulate us in these big ways. And

01:07:43.619 --> 01:07:48.539
that will happen, but in the small ways already where like scrolling Instagram is

01:07:48.539 --> 01:07:53.260
not even that fulfilling. Like you finish that hour and you're like, I know that was a waste of my time,

01:07:55.380 --> 01:08:00.110
but it was like over the threshold where you couldn't quite. It's hard to put the phone down right, you just

01:08:00.110 --> 01:08:04.469
hoping that the next one's going to be interesting. And every now and then the problem is

01:08:04.789 --> 01:08:09.510
every like 30th or 40th reel that I click on is wild.

01:08:09.590 --> 01:08:14.389
I wonder, by the way, if that's more powerful than if everyone was

01:08:14.389 --> 01:08:19.310
wild, if everyone was great, You know, it's like the slob you have to mine for gold. Yeah, you don't just

01:08:19.310 --> 01:08:24.149
go out and pick it like Daisy. That's what's out the field. If the algorithm is like intentionally feeding you some

01:08:24.149 --> 01:08:28.920
shit along the way, yeah, well there's just a lot of shit out there

01:08:28.920 --> 01:08:33.560
unfortunately. But it's all it's just in terms of, you know, I was talking

01:08:33.560 --> 01:08:38.359
to Sean O'Malley, who's this UFC fighter who's, you know, obviously has a very strong mind,

01:08:38.359 --> 01:08:43.000
really interesting guy. But one of the things that Sean said is like I get this like low level

01:08:43.000 --> 01:08:47.800
anxiety from scrolling through things and I don't know why, Like what is that?

01:08:48.319 --> 01:08:53.319
And I think it's part of the logical mind realizes is a massive waste of

01:08:53.319 --> 01:08:58.180
your resources. I also deleted a bunch of that stuff off my phone because I just

01:08:58.180 --> 01:09:03.020
didn't have the Selfcontrol. I mean, I had the Selfcontrol to delete it, but, like, not to stop once I was scrolling

01:09:03.220 --> 01:09:07.300
through it. And so I I think we're just like,

01:09:09.739 --> 01:09:14.699
yeah, we're getting attention hacked in some ways. There's some good to it, too, but

01:09:14.699 --> 01:09:19.579
we don't yet have the stuff in place, the tools, the

01:09:19.579 --> 01:09:24.409
societal norms, whatever. To modulate it well, right. And we're not designed

01:09:24.409 --> 01:09:28.930
for it. So this is a completely new technology that again

01:09:28.930 --> 01:09:33.850
hijacks are human reward systems and hijacks all of the

01:09:34.729 --> 01:09:39.729
checks and balances that are in place for communication, which historically has

01:09:39.729 --> 01:09:44.590
been one-on-one. Historically, communication has been one person to another. And when

01:09:44.590 --> 01:09:49.270
people write letters to each other, it's generally things like if someone likes a

01:09:49.390 --> 01:09:54.350
love letter or, you know, they miss you. Like they're writing this thing

01:09:54.350 --> 01:09:59.189
where they're kind of exposing a thing that maybe they have a difficulty in expressing in front of you.

01:09:59.630 --> 01:10:04.630
And it was not. It did. You know, generally, unless the person was a psycho, they're not hateful

01:10:04.630 --> 01:10:09.630
letters. Whereas the ability to just communicate fuck that guy, I hope he gets hit by a

01:10:09.630 --> 01:10:14.539
bus is so simple and easy and and you

01:10:14.539 --> 01:10:19.260
don't experience. Twitter seems to be particularly horrible for this. As

01:10:19.460 --> 01:10:24.460
the mechanics work it, it really rewards in ways that I don't

01:10:24.460 --> 01:10:28.260
think anybody fully understands that like taps into something about human psychology

01:10:29.140 --> 01:10:34.060
where but that's kind of like that's how you get engagement, that's how

01:10:34.060 --> 01:10:38.899
you get like followers, that's how you get what like, you know, the dopamine

01:10:38.899 --> 01:10:41.060
hits or whatever. And.

01:10:45.289 --> 01:10:49.970
Like the people who I know that spend all day on Twitter, more of them are unhappy about it than

01:10:49.970 --> 01:10:54.869
happy. Oh yeah, they're the most unhappy. I mean, there's quite a few people that

01:10:54.869 --> 01:10:59.869
I follow that I only follow because they're crazy. And then I'll go and check in on them and see

01:10:59.869 --> 01:11:04.829
what the fuck they're tweeting about. And some of them are on there 810 hours a day. I'll I'll

01:11:04.829 --> 01:11:09.670
see tweets all day long and I know that person cannot be

01:11:09.670 --> 01:11:14.390
happy. They're unhappy and they cannot stop. You can't stop. And it seems like

01:11:15.270 --> 01:11:20.050
it's their life, it's it's A and they get, they get

01:11:20.050 --> 01:11:24.729
meaning out of it in terms of reinforcement. You know, they get

01:11:24.729 --> 01:11:29.489
shortterm. Yeah. I think maybe each day you go to bed feeling like you accomplished

01:11:29.489 --> 01:11:34.489
something and got your dopamine and the end of each decade, you probably are like, where that decade ago. Yeah, I was talking to a friend of mine who

01:11:34.489 --> 01:11:39.449
was having a real problem with it. He's saying he would be literally walking down the street and he'd have to check his phone to see who's

01:11:39.449 --> 01:11:44.119
replying. And it wasn't even looking where he's walking. It was just like caught up in the

01:11:44.119 --> 01:11:48.920
anxiety of these exchanges. And it's not because of the nice things people say. No,

01:11:48.920 --> 01:11:53.920
no, no, no. It's all. And with him, he was recognizing that, you know, he was dunking on

01:11:53.920 --> 01:11:58.640
people. And then, yeah, seeing. People respond to the dunking. And yeah,

01:11:58.760 --> 01:12:03.680
I stopped doing that a long time ago. I stopped interacting with people on Twitter in a negative way. I just won't do

01:12:03.680 --> 01:12:08.680
it. Just even if I disagree with someone else, say something I have like as. Peacefully as possible. I

01:12:08.680 --> 01:12:13.560
have, like more of an Internet troll streak than I would like to admit. And so I try to just

01:12:13.560 --> 01:12:17.960
like, not give myself too much the temptation. But I slip up sometimes. Yeah, it's so

01:12:18.199 --> 01:12:22.880
tempting. Totally. It's so tempting to. And it's fun. It's fun to just say something shitty.

01:12:23.800 --> 01:12:28.640
I mean, again, whatever this biological system we were talking about earlier that get that that gets a positive reward.

01:12:28.840 --> 01:12:33.840
Well, in the moment there's a react and you know, there's reactions. You say something outrageous

01:12:33.840 --> 01:12:38.720
and someone's going to react. In that reaction is like energy, and there's there's all these

01:12:38.720 --> 01:12:42.220
other human beings engaging with your idea, but

01:12:42.619 --> 01:12:47.579
ultimately it's just not productive for most

01:12:47.579 --> 01:12:51.659
people, and it's psychologically, it's just

01:12:52.220 --> 01:12:56.979
fraught with peril. There's just so much going on. I don't know anybody who engages all day

01:12:56.979 --> 01:13:00.859
long that's happy. Certainly not. I don't like.

01:13:03.180 --> 01:13:07.720
I mean, I think I've watched it. Like destroys too strong of a word. But like. Knock off

01:13:07.720 --> 01:13:11.960
track the careers or life or happiness or human

01:13:11.960 --> 01:13:16.640
relationships of people that are like good, smart, conscientious people.

01:13:17.279 --> 01:13:22.000
Just like Got couldn't fight this demon. Like Hacked there. And COVID

01:13:22.000 --> 01:13:26.880
really accentuated that because people were alone and isolated. And that made

01:13:26.880 --> 01:13:31.880
it even worse, because then they felt they felt even better

01:13:31.880 --> 01:13:36.319
saying shitty things to. People, I'm unhappy. I'm gonna say even worse things about you.

01:13:36.779 --> 01:13:40.939
And then there was a psychological aspect of it, like the angst that came from being

01:13:41.340 --> 01:13:46.140
socially isolated and terrified about this invisible disease that's going to kill us all

01:13:46.619 --> 01:13:51.420
And you know, and that so you have it like, and then you're interacting with people on tour, and then you're

01:13:51.420 --> 01:13:56.140
caught up in that anxiety and you're doing it all day. And I know quite a few people, especially

01:13:56.140 --> 01:14:00.579
comedians, that really lost their minds and lost their respect to their

01:14:00.579 --> 01:14:05.579
peers by doing that. I have a lot of sympathy for people who lost their minds during COVID

01:14:05.779 --> 01:14:10.479
because. What a natural thing for us all to go through. And isolation was just

01:14:10.600 --> 01:14:15.159
brutal. But a lot of people did and I don't think the Internet

01:14:15.960 --> 01:14:20.680
in particularly not the kind of like social dynamics of things like Twitter. I don't think that like,

01:14:20.680 --> 01:14:25.560
brought anyone's best. But I mean, some people, I think if they're

01:14:25.840 --> 01:14:30.399
they're not they, they're not inclined to be shitty to people. I think some people did

01:14:30.930 --> 01:14:35.930
seek comfort and they did interact with people in positive ways. I see there's plenty

01:14:35.930 --> 01:14:40.369
of positive. I think The thing is that the negative interactions are so much more

01:14:40.810 --> 01:14:45.529
impactful. Yeah, I look, I think there are a lot of people who use these systems for

01:14:45.529 --> 01:14:49.930
wonderful things. Didn't mean to imply that's not the case. But that's not what drives

01:14:51.090 --> 01:14:55.529
people's emotions after getting off the platform at the end of the day, right? Right. And it's also

01:14:55.529 --> 01:15:00.090
probably not. If you looked at a pie chart of the amount of interactions

01:15:00.680 --> 01:15:05.439
on Twitter, I would say a lot of them are shitting on people and being angry about. That how

01:15:05.439 --> 01:15:10.159
many of the people that you know that use Twitter, those 8 or 10 hours a day, are just saying

01:15:10.199 --> 01:15:14.720
wonderful things about other people all day versus the virulent? Very few, Yeah,

01:15:15.279 --> 01:15:19.880
very few. I don't know any of them. I know. But

01:15:20.239 --> 01:15:25.210
then again, I wonder with the implementation of some new

01:15:25.210 --> 01:15:30.210
technology that makes communication a very different thing than we're occurring like what

01:15:30.210 --> 01:15:34.609
we're doing now with communication is less immersive than

01:15:34.609 --> 01:15:39.329
communicating one-on-one. You and I are talking. We're looking into each other's eyes, we're getting

01:15:39.329 --> 01:15:44.289
social cues, we're smiling at each other, we're laughing. It's it's a very natural way

01:15:44.289 --> 01:15:49.130
to talk. I wonder if through the information of technology, if

01:15:49.880 --> 01:15:54.479
it becomes even more immersive than a Oneonone

01:15:54.479 --> 01:15:58.880
conversation, even more interactive and eat. You will

01:15:58.880 --> 01:16:03.000
understand even more about the way a person feels, about what you say

01:16:03.479 --> 01:16:08.239
about that person's memory, that person's life, that

01:16:08.239 --> 01:16:13.119
person's history, their education, how it comes out

01:16:13.199 --> 01:16:17.779
of their mind, how their mind interacts with your mind. And you

01:16:17.779 --> 01:16:22.739
see them, you really see them. I wonder if that. I wonder if

01:16:22.739 --> 01:16:27.619
what we're experiencing now is just like the first time people invented guns. They

01:16:27.619 --> 01:16:32.460
just started shooting at things, you know? Yeah. If you can, like, feel what I feel when you

01:16:32.460 --> 01:16:37.220
say something mean to me or nice to me, like that's clearly going to change

01:16:38.579 --> 01:16:43.279
what you decide to say. Yeah, yeah. Unless you're a psycho. And

01:16:43.279 --> 01:16:47.720
then what causes someone to be a psycho and can that be

01:16:47.720 --> 01:16:52.640
engineered out? Imagine what we're talking about when

01:16:52.640 --> 01:16:57.039
we're dealing with the human mind, we're dealing with various diseases, bipolar,

01:16:57.079 --> 01:17:02.079
schizophrenia. Imagine a world where we can

01:17:02.079 --> 01:17:06.439
find the root cause of those things and through

01:17:06.800 --> 01:17:11.760
coding and some sort of an implementation implementation of technology

01:17:11.760 --> 01:17:16.720
that elevates dopamine and serotonin and and does some things to

01:17:16.720 --> 01:17:21.279
people that eliminates all of those problems and

01:17:21.319 --> 01:17:24.560
allows people to communicate in a very pure way.

01:17:27.119 --> 01:17:31.520
It sounds great. It sounds great, but you're not going to have any rock'n'roll. You'll stand up. Comedy will die.

01:17:33.920 --> 01:17:38.670
You'll have no violent movies. You know you there's a lot of things that are going to go out the window,

01:17:38.750 --> 01:17:43.710
but maybe that is also part of the process of our evolution to the next stage of existence.

01:17:46.149 --> 01:17:51.109
Maybe I feel genuinely confused on this. Well, I think you should be. I mean

01:17:51.109 --> 01:17:56.069
to be. We're going to find out, yeah. I mean, to be sure that it's good. Does the same. But I

01:17:56.069 --> 01:18:00.789
don't even have like hubris beyond belief, right? I mean, you just you from the

01:18:00.989 --> 01:18:05.930
when did Open AI? When did you first start this project? I. Like the very

01:18:05.930 --> 01:18:10.930
beginning and end of 2015, early 2016, and when you initially started

01:18:10.930 --> 01:18:15.930
this project, what kind of timeline did you have

01:18:15.930 --> 01:18:20.649
in mind? And has it stayed on that timeline, or is it just wildly out of control?

01:18:22.569 --> 01:18:27.449
I remember talking with John Schulman, one of our cofounders, early

01:18:27.449 --> 01:18:32.329
on and he was like, yeah, I think it's going to be about a 15 year project and I was like, yeah, sounds about right to me

01:18:33.050 --> 01:18:37.829
and. I've always sort of thought since then, now I no longer think of like a

01:18:37.829 --> 01:18:42.670
GI is quite the end point. But to get to the point where we like accomplish the thing we

01:18:42.670 --> 01:18:47.590
set out to accomplish, I you know that would take us to like 20-30, twenty 31.

01:18:48.189 --> 01:18:52.909
That has felt to me like all the way through kind of

01:18:55.149 --> 01:18:59.510
a reasonable estimate with huge error bars and I kind of think we're on the

01:18:59.710 --> 01:19:04.479
trajectory. I sort of would have assumed and what did you think

01:19:04.680 --> 01:19:09.520
the impact on society would be like? Did you

01:19:09.520 --> 01:19:14.159
when you when you first started doing this and you said okay. If we are successful

01:19:14.600 --> 01:19:18.840
and we do create some massively advanced a GI,

01:19:19.359 --> 01:19:24.359
what, what is the implementation and how? What is the impact on society

01:19:24.640 --> 01:19:29.479
have? Did you did you sit there and have like a graph like you? You had the

01:19:29.479 --> 01:19:34.350
pros on one side, the cons on the other. Did you just sort of abstractly consider? Well,

01:19:35.590 --> 01:19:40.390
we, we definitely talked a lot about the cons. You know, many of

01:19:40.390 --> 01:19:44.350
us were super worried about and still are about

01:19:46.149 --> 01:19:51.069
safety and alignment. And if we build these systems, we can all see the great future. That's easy

01:19:51.069 --> 01:19:55.829
to imagine, but if something goes horribly wrong, it's like really horribly wrong. And

01:19:55.829 --> 01:20:00.569
so there was a lot of discussion about and and really. A big part of the

01:20:00.569 --> 01:20:05.489
finding spirit of this is like, how are we going to solve this safety problem? What does that even mean?

01:20:06.130 --> 01:20:11.130
One of the things that we believe is that the greatest minds in the world cannot sit there and solve that

01:20:11.210 --> 01:20:15.890
in a vacuum. You've got to, like, have contact reality. You've got to see where the technology

01:20:15.890 --> 01:20:20.890
goes. Practice plays out in a stranger way than theory, and

01:20:20.890 --> 01:20:25.770
that's certainly proven true for us. But we had a long list of, well, I

01:20:25.770 --> 01:20:30.619
don't know if we had a long list of cons. We had a very intense list of cons because, you

01:20:30.619 --> 01:20:35.619
know, there's like all of the last decades of scifi telling you about how this goes wrong and why

01:20:35.619 --> 01:20:40.500
you're supposed to shoot me right now and. I'm sure you've seen the the John

01:20:40.500 --> 01:20:45.460
Connor chat. GPTI haven't mean what is it? It's

01:20:45.779 --> 01:20:50.659
it's like, you know John Connor from the Terminator, the kid looking at you

01:20:50.659 --> 01:20:55.220
when you open up ChatGPT. Yeah.

01:20:55.460 --> 01:21:00.140
So that stuff we were like very clear in our minds on. Now

01:21:00.539 --> 01:21:05.380
I think we understand there's a lot of work to do, but we understand more

01:21:05.380 --> 01:21:10.180
about how to make a I safe in the A I

01:21:10.180 --> 01:21:15.140
safety gets overloaded. Like, you know, does it mean don't say so many people find offensive or does it mean not don't destroy

01:21:15.140 --> 01:21:19.939
all of humanity or some continuum. And I think the the word is like

01:21:19.939 --> 01:21:24.899
gotten overloaded but in in terms of the like not destroy all of humanity version of it.

01:21:25.489 --> 01:21:30.369
We have a lot of work to do but I think we have finally more ideas about what can

01:21:30.369 --> 01:21:34.609
work and and given the way the systems are going we have a lot more

01:21:34.850 --> 01:21:39.569
opportunities available to us to solve it than I thought we would have given the

01:21:39.569 --> 01:21:44.369
direction that we initially thought the technology was going to go. So that's good. On the positive

01:21:44.369 --> 01:21:49.289
side, the thing that I was most excited about then and remain

01:21:49.289 --> 01:21:53.930
most excited about now is what if this system can

01:21:54.939 --> 01:21:58.939
dramatically increase the rate of scientific knowledge in society.

01:21:59.939 --> 01:22:04.460
That is a I think that kind of like all

01:22:04.739 --> 01:22:08.539
real sustainable economic growth, the future getting better

01:22:09.340 --> 01:22:14.140
progress in some sense comes from increased scientific and

01:22:14.140 --> 01:22:19.140
technological capacity so we can solve all the problems. And if the AI can help us

01:22:19.140 --> 01:22:24.060
do that, that's always been the thing I've been most excited about. Well, it certainly

01:22:24.060 --> 01:22:29.020
seems like that is the greatest potential, greatest positive potential of a I.

01:22:29.539 --> 01:22:34.300
It's is to solve a lot of the problems that human beings have had

01:22:34.300 --> 01:22:39.180
forever, a lot of the societal problems that seem to be. I mean that's what I was talking

01:22:39.180 --> 01:22:43.859
about an A I president. I'm kind of not joking because I feel like if

01:22:43.859 --> 01:22:48.699
something was hyperintelligent and aware of all the variables with

01:22:48.699 --> 01:22:53.520
no human bias and no incentives. No, other

01:22:53.520 --> 01:22:58.399
than here's your program, The greater good for the community of the United

01:22:58.399 --> 01:23:03.399
States and the greater good for that community as it interacts

01:23:03.399 --> 01:23:08.079
with the rest of the world. The elimination

01:23:08.479 --> 01:23:12.680
of these dictators, these whether they're

01:23:13.640 --> 01:23:17.890
elected or nonelected, who impose their will. On the

01:23:17.890 --> 01:23:22.850
population because they have a vested interest in protecting special

01:23:22.850 --> 01:23:27.649
interest groups and and industry. I think. I think as long

01:23:27.649 --> 01:23:32.449
as the thing that I find scary, when you say that is, it does, It feels

01:23:32.449 --> 01:23:37.449
like it's humanity not in control. And I reflexively

01:23:37.449 --> 01:23:41.880
don't like that. But if it's if it's

01:23:41.920 --> 01:23:46.319
instead like it is the collective will of humanity being expressed

01:23:46.319 --> 01:23:51.119
without the mistranslation and corrupted influences along the way, yeah, then I can see it.

01:23:51.720 --> 01:23:56.520
Is that possible? It seems like it would be, it seems like, if it was programmed in

01:23:56.520 --> 01:24:01.489
that regard to do the greater good for humanity. And and take into

01:24:01.489 --> 01:24:06.409
account the values of humanity, the needs of humanity, there's something

01:24:06.409 --> 01:24:10.970
about the phrase do the greater good for. I know. It terrifies me. It's very Orwellian. All of it is

01:24:11.489 --> 01:24:16.369
but. Also, so is Artificial General Intelligence for sure. Open the door. I

01:24:16.369 --> 01:24:21.289
wish, I wish I had worked on, you know, something that was less morally fraught. But

01:24:21.289 --> 01:24:26.229
do you? Because it's really exciting. I mean, I can't imagine. I I cannot imagine a cooler thing to

01:24:26.229 --> 01:24:30.630
work on. I feel unbelievably, I feel like the luckiest person on earth. That's awesome. It is not.

01:24:32.829 --> 01:24:37.789
It's not on easy mode. Let's say that this is not life on easy mode. No, no, no, no. I mean you

01:24:37.789 --> 01:24:42.310
are at the forefront of one of the most spectacular

01:24:42.310 --> 01:24:47.310
changes in human history. And I would say as

01:24:47.350 --> 01:24:51.670
no, I would say more spectacular than the implementation of the Internet.

01:24:52.489 --> 01:24:57.130
I think the implementation of the Internet was the first baby steps of

01:24:57.130 --> 01:25:01.729
this and that Artificial general intelligence is, yeah, it

01:25:01.810 --> 01:25:06.409
is the Internet on steroids. It's the Internet in

01:25:06.489 --> 01:25:11.449
hyper space. What I would say is, it's the next step and there will

01:25:11.449 --> 01:25:16.000
be more steps after, but it's our most exciting step yet. Yeah, my my wonder is

01:25:16.319 --> 01:25:21.039
what are those next steps after? Isn't that so exciting to think about? It's very

01:25:21.039 --> 01:25:25.920
exciting. I think we're the last people. I really do. I think we're the last of the

01:25:25.920 --> 01:25:30.399
biological people. With all the biological problems. I think there's

01:25:31.319 --> 01:25:36.159
and. Do you feel excited about that? I just think that's just what it is. You're

01:25:36.159 --> 01:25:41.140
just fine. With it, it is what it is, you know, I mean that. I

01:25:41.140 --> 01:25:46.100
don't think you can control it at this point, other than some massive natural disaster that resets us back

01:25:46.100 --> 01:25:51.060
to the Stone Age, which is also something we should be very concerned with because it seems like that happens a lot.

01:25:51.060 --> 01:25:55.899
We're not aware of it because the timeline of a human body is so small. You know the timeline of the human

01:25:55.899 --> 01:26:00.819
existence as a person is 100 years if you're lucky, but yet the timeline

01:26:00.899 --> 01:26:05.140
of the Earth is billions of years. And if you look at how many times?

01:26:05.760 --> 01:26:10.439
Life on Earth has been reset by comets slamming into the

01:26:10.479 --> 01:26:15.159
Earth and just completely eliminating all technological

01:26:15.159 --> 01:26:19.560
advancement. It seems like it's happened multiple times in recorded history.

01:26:22.439 --> 01:26:25.479
I do think. I always think we don't think about that quite enough.

01:26:29.800 --> 01:26:34.680
We talked about the simulation hypothesis earlier. It's had this big resurgence in the tech industry recently. One of the

01:26:34.680 --> 01:26:39.319
things, one of the new takes on it as we get closer to a GI is that, you know, if

01:26:39.439 --> 01:26:44.119
ancestors were simulating us, the time they'd want to simulate again and again is right up to the,

01:26:44.840 --> 01:26:49.840
you know, right up right the lead up to the creation of a GI. So it seems very crazy we're living

01:26:49.840 --> 01:26:54.800
through this time, but it's not a coincidence at all. You know, this is the time. That is after we

01:26:54.800 --> 01:26:59.760
had enough cell phones out in the world, like recording tons of video to train the video model of the world. That's all being,

01:26:59.760 --> 01:27:04.680
like, jacked into us now via brain implants or whatever. And before, everything was really crazy

01:27:04.680 --> 01:27:09.560
with a GI. And it's also this interesting time to simulate, like, can we get through,

01:27:10.399 --> 01:27:15.359
does the asteroid come right before we get there for dramatic tension? Like, do we figure how to make this safe? Do we figure

01:27:15.359 --> 01:27:20.279
how to societally agree on it? So that's led to like a lot more people believe in it than before, I think.

01:27:20.960 --> 01:27:25.920
Yeah, for sure. And again, I think this is just where it's

01:27:25.920 --> 01:27:30.680
going. I mean, I don't know if that's a good thing or a bad thing. It's just a

01:27:30.680 --> 01:27:35.600
thing. But it's certainly better to live now. I would not want to live in the 1800s

01:27:35.600 --> 01:27:40.600
and be in a covered wagon trying to make my way across the country. Yeah, we got the most exciting time

01:27:40.600 --> 01:27:45.560
in history yet. It's the best, it's the best, but it's also has the most problems,

01:27:45.560 --> 01:27:49.920
the most social problems, the the most awareness of social

01:27:50.039 --> 01:27:54.960
environmental infrastructure, the, the, the issue. We have to go. We have to go solve them.

01:27:55.199 --> 01:27:59.869
Yeah. And I intuitively, I think I feel

01:27:59.869 --> 01:28:04.789
something somewhat different than you, which is I

01:28:04.789 --> 01:28:09.789
think humans in something close to this form are going to

01:28:09.789 --> 01:28:14.149
be around for a lot longer than

01:28:14.989 --> 01:28:18.069
I don't think we're the last humans. How long do you think we have?

01:28:22.789 --> 01:28:27.689
Like longer than a time frame I can reason about. Really. Now there may be, like, I could

01:28:27.689 --> 01:28:32.569
totally imagine a world where some people decide to merge and

01:28:32.609 --> 01:28:37.489
go off exploring the universe with a I and there's a big universe out there. But like,

01:28:38.010 --> 01:28:42.770
can I really imagine a world where, short of a natural disaster, they are not humans?

01:28:43.409 --> 01:28:47.970
Pretty similar to humans from today on Earth doing humanlike

01:28:47.970 --> 01:28:52.970
things and the sort of spirit of humanity merged into these other things that

01:28:52.970 --> 01:28:57.880
are out there doing their thing in the universe. It's very hard for me to

01:28:57.880 --> 01:29:02.880
actually see that happening. And maybe that means I'm like going to turn out

01:29:02.880 --> 01:29:07.239
to be a dinosaur and Luddite and horribly wrong in this prediction. But I would say I feel it

01:29:07.439 --> 01:29:11.760
more over time as we make progress with AI, not less. Yeah, I don't feel that at all.

01:29:12.439 --> 01:29:17.279
I feel like we're done in like a few years. No2 decades, maybe a

01:29:17.279 --> 01:29:22.079
generation or two. It'll probably be a gradual change, like wearing of

01:29:22.079 --> 01:29:26.710
clothes. You know, I don't think everybody wore clothes and they invented clothes. I think it probably took a

01:29:26.710 --> 01:29:31.390
while. And someone figured out shoes. I think that probably took a while when they figured out

01:29:31.390 --> 01:29:36.270
structures, doors, houses, cities, agriculture, all those things

01:29:36.310 --> 01:29:41.069
were slowly implemented over time. And then now we come everywhere. And I think

01:29:41.229 --> 01:29:46.229
this is far more transformative and it's part of that because you don't think there will be an

01:29:46.310 --> 01:29:51.310
option for some people not to merge. Just like there's not an option for some people to not have

01:29:51.310 --> 01:29:56.189
telephones anymore. It's like I used to have friends. Like I don't even have e-mail. Those, those three

01:29:56.189 --> 01:30:01.149
people don't exist anymore. They all have e-mail, right? Everyone has a phone, at least a flip phone. I know some people

01:30:01.149 --> 01:30:06.079
that they just can't handle social media and all that jazz. They went to a flip phone. Good.

01:30:06.119 --> 01:30:10.880
I don't know if this is true or not. I've heard you can't, like, walk into an AT&T store anymore and still buy a flip phone. I heard they just

01:30:10.880 --> 01:30:15.840
changed. You can. Oh, really? Someone told me this but I don't know if it's. Verizon still has them. I was

01:30:15.840 --> 01:30:20.760
just there. They they still have flip phones. I was like, I like it. I like this fucking little thing that you just

01:30:20.760 --> 01:30:25.520
call people, and I always like romanticize about going to that. But my step

01:30:25.520 --> 01:30:30.239
was to go to a phone that has nothing on it but text messages, and that's been a few

01:30:30.239 --> 01:30:34.850
days feeling good so far. Yeah, it's good, you know. I still have my other

01:30:34.850 --> 01:30:39.289
phone that I use for social media, but when I pick that motherfucker up, I start

01:30:39.289 --> 01:30:44.170
scrolling through YouTube and watching videos and scrolling through TikTok or

01:30:44.170 --> 01:30:49.130
Instagram. And I don't have TikTok, but I've I have. I tried

01:30:49.130 --> 01:30:54.050
threads for a little while, but I'm like, I was just like fucking ghost town, so I went right back to

01:30:54.090 --> 01:30:59.090
X I I live on a ranch during the weekends and there's Wi-Fi in the

01:30:59.090 --> 01:31:03.489
house, but there's no cell phone coverage anywhere else, and

01:31:04.920 --> 01:31:09.600
it's every week I forget how nice it

01:31:09.600 --> 01:31:14.439
is and what a change it is to go for a walk with no cell phone coverage. It's

01:31:14.520 --> 01:31:18.960
good for your mind, for it's unbelievable for your mind. And I think we have like

01:31:19.560 --> 01:31:24.560
so quickly lost something like out of service just doesn't happen

01:31:24.560 --> 01:31:29.159
that doesn't have any airplanes anymore, you know, like, but that

01:31:30.800 --> 01:31:35.140
like hours where your phone just cannot buzz. Yeah,

01:31:35.779 --> 01:31:40.779
no text message either. Nothing. I think that's a really healthy

01:31:40.779 --> 01:31:45.619
thing. I dropped my phone once when I was in Lanai, and I think it was the last time I

01:31:45.619 --> 01:31:50.380
dropped the phone. The phone was like, we're done and it just started calling people randomly.

01:31:50.579 --> 01:31:55.539
Like it would just call people and I'd hang it up and call another person. I'd hang it up and I was showing my

01:31:55.539 --> 01:32:00.510
wife. I was like, look at this. This is crazy. It's just calling people. And so the phone was broken. And so I

01:32:00.510 --> 01:32:05.069
had an order a phone and we were on vacation for like 8 days, and it took three

01:32:05.069 --> 01:32:09.510
days for Apple to get me a phone. I bet you had a great three days. It was amazing. It was

01:32:09.510 --> 01:32:14.310
amazing because when I was hanging out with my family, I was totally present.

01:32:14.470 --> 01:32:19.310
There's no options and I wasn't thinking about checking my phone because it didn't

01:32:19.310 --> 01:32:24.109
exist. I didn't have one, and there was a alleviation of Again,

01:32:24.109 --> 01:32:29.079
what would? Sean was talking about that low level of anxiety, this sort

01:32:29.079 --> 01:32:34.039
of like that you have when you always want to check your

01:32:34.039 --> 01:32:38.680
phone. Yeah, I think, I think that thing, it's so bad. We have not

01:32:38.680 --> 01:32:43.680
figured out yet. Like the technology has moved so fast. Biology moves very

01:32:43.680 --> 01:32:48.600
slowly. We have not figured out how we're going to function in this society. And get those

01:32:48.600 --> 01:32:53.399
occasional times when you know your phone is broken for three days or you go for a walk with no

01:32:53.399 --> 01:32:55.930
service. But it's like,

01:32:59.569 --> 01:33:03.770
I very much feel like my phone controls me, not the other way around.

01:33:04.489 --> 01:33:09.369
And I hate it, but I haven't figured out what to do about it. Well, that's what I'm worried

01:33:09.369 --> 01:33:13.970
about with future technology is that this, which was so

01:33:13.970 --> 01:33:18.569
unanticipated, if you'd imagine a world, when you imagine going up to someone

01:33:19.729 --> 01:33:24.409
in 1984 and pointing to a phone and saying one day that'll be in your pocket, it's going to ruin your life.

01:33:25.029 --> 01:33:29.989
Like what? Like, yeah, One day people are going to be jerking off to that thing. Like what?

01:33:30.550 --> 01:33:35.470
One day people are going to be watching people get murdered on Instagram. I haven't seen so many murders on Instagram over the last few

01:33:35.470 --> 01:33:40.390
months. Really, I've never seen. Been a bad timeline. Me and my friend Tom Segura.

01:33:41.270 --> 01:33:46.029
Every morning we text each other the worst things that we find on Instagram for fun. He's a

01:33:46.029 --> 01:33:51.029
comedian. We're all comedian. That's fun to you. Yeah, this is fucking just ridiculous.

01:33:51.390 --> 01:33:55.850
I mean. I mean. Just crazy car accidents. People get gored by

01:33:55.850 --> 01:34:00.649
bulls and like every, like we try to top each other, so every day, he said. To me the

01:34:00.649 --> 01:34:05.369
most, every day when I wake up and I check Tom fuck when you got, you know, Can you

01:34:05.369 --> 01:34:09.930
explain what's fun about that? Well, he's a comic, and I'm a

01:34:09.930 --> 01:34:14.289
comic. And comics like chaos. We like. We like

01:34:14.409 --> 01:34:19.409
ridiculous, outrageous shit that is just so far

01:34:19.409 --> 01:34:24.399
beyond the norm of what you experience in a regular day. Just and also

01:34:24.880 --> 01:34:29.680
the understanding of the wide spectrum of human behavior.

01:34:29.840 --> 01:34:34.640
If you're a nice person and you surround yourself with nice people, you very rarely see

01:34:34.640 --> 01:34:39.560
someone get shot. You very rarely see people get stabbed for

01:34:39.560 --> 01:34:43.079
no reason, randomly on the street. But on Instagram you see that every day

01:34:45.319 --> 01:34:49.779
and there's something about that which just reminds you. Oh, the we're

01:34:49.779 --> 01:34:54.500
crazy like the the human species. Like there's a certain percentage of us that are just

01:34:54.699 --> 01:34:59.619
off the rails and just out there just causing

01:34:59.619 --> 01:35:04.579
chaos and jumping dirt bikes and landing on your neck. And like, all that stuff is

01:35:04.699 --> 01:35:09.220
out there. Even to hear that makes me like physically, like, I know that happens, of course.

01:35:11.899 --> 01:35:16.850
And I know, like not looking at it doesn't make it not happen right? But it makes me so uncomfortable and

01:35:16.850 --> 01:35:20.770
unhappy to watch. Oh yeah, it makes me uncomfortable too. But yeah, we do each other every day

01:35:23.250 --> 01:35:27.409
and it's not good. It's definitely not good. But it's also, I'm not going to stop. It's fun.

01:35:28.090 --> 01:35:32.569
But why is it fun? It's fun because it's my friend Tom, and we're both kind of the same in that way. Which,

01:35:33.489 --> 01:35:38.329
just look at that. Look at this. Yeah, look at this. And it's just a thing we started doing a few months ago. It

01:35:38.329 --> 01:35:43.319
just can't stop. And Instagram has like, learned that you do that, so just keep showing you more.

01:35:43.319 --> 01:35:47.960
And more, Instagram knows when I my search page is a mess. When I go to the

01:35:47.960 --> 01:35:52.600
Discover, it's just crazy. But The thing is, it shows up in your feed

01:35:52.600 --> 01:35:57.600
too. That's what I understand about the algorithm. It shows it. It knows you're fucked up. So it shows up in your

01:35:57.600 --> 01:36:02.319
feed of things like, even if they're they're not people I follow, but

01:36:02.319 --> 01:36:07.039
Instagram shows them to me anyway. I heard an interesting thing a few days ago by

01:36:07.039 --> 01:36:11.689
Instagram and the feed, which is if you use it at off hours when they have

01:36:11.689 --> 01:36:16.609
more processing capability available because less people are using it, you get better recommendations so

01:36:16.609 --> 01:36:21.529
your feet will be better in like the middle of the night. What is better though? Doesn't your feed more

01:36:21.529 --> 01:36:26.529
addictive to you or whatever? So for me, better would be more murders, more animal

01:36:26.529 --> 01:36:31.130
attacks. Sounds horrible. It's. It's, But it's just, it

01:36:31.130 --> 01:36:35.649
seems to know that's what I like. It seems to know that that's what I

01:36:35.689 --> 01:36:39.170
interact with, so it's just sending me that most of the time.

01:36:40.949 --> 01:36:45.789
Yeah, that probably has all kinds of crazy psychological. I'm sure, yeah, I'm sure. That's

01:36:45.789 --> 01:36:50.390
also one of the reasons why I want to get rid of it and move away from it. Yeah, so maybe

01:36:50.430 --> 01:36:55.350
maybe it went too far. I don't even know if it's too far, but what

01:36:55.350 --> 01:37:00.270
it is, is it's showing me the darker regions

01:37:00.430 --> 01:37:05.310
of society, of civilization, of human behavior. But you think we're

01:37:05.310 --> 01:37:10.020
about to edit all that out? I wonder if that is a solution. I really do

01:37:10.300 --> 01:37:14.939
because I don't think it's outside the realm of possibility. If we really,

01:37:14.939 --> 01:37:19.500
truly can engineer that, like one of the talks about neural link that's really

01:37:19.500 --> 01:37:23.140
promising is people with spinal cord issues,

01:37:24.220 --> 01:37:29.020
injuries, people that can't move their body and being able to Hotwire that

01:37:29.260 --> 01:37:34.180
where essentially it controls all these parts of your body that you couldn't

01:37:34.180 --> 01:37:38.779
control anymore. And so that would be an amazing thing for people that are injured.

01:37:39.109 --> 01:37:44.109
For amazing thing for people that are you know they're they're paralyzed

01:37:44.109 --> 01:37:49.069
they have all sorts of neurological conditions that that is probably one of

01:37:49.069 --> 01:37:54.029
the 1st and that's what Elon's talked about as well when the first implementations the the

01:37:54.109 --> 01:37:58.989
restoration of site you know cognitive function enhanced

01:37:58.989 --> 01:38:03.670
from people that have brain issues that's tremendously exciting. Yeah.

01:38:04.069 --> 01:38:08.470
And and like many other technologies, I don't think we can stop neural interfaces

01:38:09.050 --> 01:38:13.649
nor because of the like great good that's going to happen along the way. But I also don't think we know where it

01:38:13.729 --> 01:38:18.529
goes. It's Pandora's box for sure. And I think when we open

01:38:18.529 --> 01:38:23.489
it, it's just we're not going to go back. Just like we're not going to go back to know computers without some

01:38:23.489 --> 01:38:28.489
sort of natural disaster. By the way, I, and I mean this is a great compliment. You are one

01:38:28.489 --> 01:38:33.489
of the most neutral people I have ever heard. Talk about the merge coming. You're

01:38:33.489 --> 01:38:37.970
just like, yeah, I think it's going to happen. You know, it's be good in these ways, bad in these ways, but

01:38:38.909 --> 01:38:43.909
you seem like unbelievably neutral about it, which is always something I admire. I try

01:38:43.909 --> 01:38:48.909
to be as neutral about everything as possible, except for corruption, which I think is just

01:38:48.909 --> 01:38:53.550
like one of the most massive problems with the the the way our our

01:38:53.550 --> 01:38:58.470
culture is governed. Then corruption is such is just

01:38:58.710 --> 01:39:03.520
the influence of money. Such is just a giant, terrible issue. But in terms of, like,

01:39:03.520 --> 01:39:08.319
social issues and in terms of the way human beings

01:39:08.319 --> 01:39:12.680
believe and think about things, I try to be as neutral as possible.

01:39:13.159 --> 01:39:18.079
Because I think the only way to really, truly understand the way other people think about

01:39:18.079 --> 01:39:23.039
things is try to look at it through their mind. And if you have this inherent bias and this,

01:39:24.399 --> 01:39:29.399
you have this like very rigid view of what's good

01:39:29.399 --> 01:39:34.390
and bad and right and wrong. I don't think that serves you very well for

01:39:34.390 --> 01:39:39.390
understanding why people differ. And so I try to be as neutral and as

01:39:39.390 --> 01:39:44.350
objective as possible. When I look at anything, this is a skill that I've learned. This is not something I

01:39:44.350 --> 01:39:49.270
had in 2009 when I started this podcast, this podcast. I started just fucking around with

01:39:49.270 --> 01:39:54.229
friends and I had no idea what it was. I mean, there's no way I could have ever known and

01:39:54.229 --> 01:39:59.149
but also had no idea what it was going to do to me and as far as the

01:39:59.189 --> 01:40:03.720
evolution of me as a human being. I am so much nicer. I'm so much

01:40:03.720 --> 01:40:08.600
more aware of things. I'm so much more conscious of the way other people

01:40:08.600 --> 01:40:12.600
think and feel. I'm just a totally different person than I was in

01:40:12.600 --> 01:40:17.119
2009, which is hard to recognize. It's hard to believe. That's

01:40:17.880 --> 01:40:22.159
really cool, but if that it's just an inevitable consequence of this

01:40:22.399 --> 01:40:27.239
unexpected education that I've received. Did the empathy kind of like come on

01:40:27.239 --> 01:40:32.229
linearly? Yes. And that was not a no. It just came it came on recognize. Well,

01:40:32.229 --> 01:40:36.750
first of all it came on recognizing that the interact, the negative

01:40:36.750 --> 01:40:41.550
interactions on social media that I was doing, they didn't help me. They didn't help the

01:40:41.550 --> 01:40:46.310
person. And then having compassion for this person that's fucked up or done something stupid like it

01:40:46.310 --> 01:40:50.909
doesn't. It's not good to just dunk on people like it's so there's no benefit there other than to

01:40:51.149 --> 01:40:56.119
give you some sort of social credit and get a bunch of likes. It didn't make me feel good. Like

01:40:56.119 --> 01:41:01.039
that's not good. And also a lot of psychedelics, a ton of psychedelic experiences

01:41:01.039 --> 01:41:05.960
from 2009 on, and with everyone a greater understanding of the

01:41:05.960 --> 01:41:10.720
impact. Like I had one recently and when I had the one recently.

01:41:11.119 --> 01:41:16.039
Like the overwhelming message that I was getting through this was that

01:41:16.199 --> 01:41:21.039
everything I say and do ripples

01:41:21.039 --> 01:41:25.619
off into all the people that I interact with. And then if I'm not

01:41:25.619 --> 01:41:30.539
doing something with at least the goal of overall good

01:41:30.859 --> 01:41:35.779
or overall understanding that I'm doing bad and

01:41:35.779 --> 01:41:40.699
that that bad is a real thing, as much as you try to ignore it because you don't interface with it

01:41:40.899 --> 01:41:45.779
instantly and you're still creating

01:41:45.779 --> 01:41:50.500
unnecessary negativity and that I should avoid that as much as

01:41:50.500 --> 01:41:55.210
possible. It's like an overwhelming message that this cycle, this psychedelic

01:41:55.210 --> 01:41:59.729
experience was giving me. And and I I took it because I was just

01:42:00.369 --> 01:42:05.090
particularly anxious that day about the state of the world, particularly anxious

01:42:05.090 --> 01:42:09.770
about Ukraine and Russia and China and the the

01:42:10.250 --> 01:42:14.569
the political system that we have in this country and this incredibly

01:42:14.569 --> 01:42:19.289
polarizing way that the left and the right engage with each

01:42:19.289 --> 01:42:23.300
other and God, just it just seems so just

01:42:23.939 --> 01:42:28.859
tormented. And so I was just some days I just get I think too

01:42:28.859 --> 01:42:33.779
much about it. I just, I'm like I need something crack me out of this. So I I took

01:42:33.819 --> 01:42:38.699
these psychedelics. Are you surprised psychedelic therapy has not made

01:42:39.539 --> 01:42:44.500
from what you thought would happen in the, say, the early 20 Tens till now? Are you surprised it has not made

01:42:44.500 --> 01:42:49.229
more progress, sort of, on a path to legalization as a medical treatment? No, no, I'm not.

01:42:49.229 --> 01:42:54.189
Because there's a lot of people that don't want it to be in place and those people

01:42:54.189 --> 01:42:58.630
have tremendous power over our medical system and over our regulatory system.

01:42:58.989 --> 01:43:03.909
And those people have also not experienced these psychedelics. There's very few

01:43:03.909 --> 01:43:08.750
people that have experienced profound psychedelic experiences that don't think there's an

01:43:08.750 --> 01:43:12.949
overall good for those things. So you're the problem is you're having

01:43:13.619 --> 01:43:18.619
these laws and these rules implemented by people

01:43:18.619 --> 01:43:23.619
who are completely ignorant about the positive effects of these things. And if you know the

01:43:23.619 --> 01:43:28.300
history of psychedelic prohibition in this country,

01:43:28.579 --> 01:43:33.500
it all took place during 1970 and it was really to stop the civil rights movement

01:43:33.819 --> 01:43:38.659
and it was really to stop the anti war movement. And they they tried to find a way to

01:43:38.659 --> 01:43:43.300
make all these things that these people were doing that was causing them to thinking these very

01:43:43.300 --> 01:43:48.260
different ways is TuneIn turn on drop out. They just wanted to put a

01:43:48.260 --> 01:43:52.739
fucking halt to that. What better way than the lock everyone who participates in that in

01:43:52.739 --> 01:43:57.699
cages find the people are producing it. Lock them in cages put them in jail for the rest of their

01:43:57.699 --> 01:44:02.539
life, make sure it's illegal, arrest people, put the bus on television. Make sure that

01:44:02.539 --> 01:44:07.140
people are aware. And then there's also you connect it to drugs that are

01:44:07.140 --> 01:44:11.899
inherently dangerous for society and detrimental. The fentanyl crisis, you know, the

01:44:11.899 --> 01:44:16.659
crack cocaine crisis that we experienced in the 90s, like all of those things, they're under the

01:44:16.659 --> 01:44:21.260
blanket of drugs. Psychedelic drugs are also

01:44:21.380 --> 01:44:25.699
talked about like drugs, even though they have these profound

01:44:25.979 --> 01:44:30.260
spiritual and psychological changes that they you know.

01:44:31.310 --> 01:44:35.750
I remember when I was in elementary school and I was in, like, drug education. They talked about, you know,

01:44:36.310 --> 01:44:41.189
marijuana is really bad because it's a gateway to these other things. And there's this bad one, that bad one, heroin,

01:44:41.189 --> 01:44:44.550
whatever. And the very end of the line, the worst possible thing is LSD.

01:44:47.350 --> 01:44:51.949
Did you take LSD and go oh, they're lying. Psychedelic therapy was

01:44:52.029 --> 01:44:56.750
definitely one of the, like, most important things in my life and I I

01:44:56.750 --> 01:45:01.520
assumed, given how powerful it was. For me, like, I,

01:45:01.960 --> 01:45:06.800
you know, I struggled with like all kinds of anxiety and other negative things until like watch

01:45:06.800 --> 01:45:11.680
all of that go away. And like that, like I traveled to my country for

01:45:11.680 --> 01:45:16.439
like a week, did a few things, came back a totally different person. And

01:45:16.720 --> 01:45:21.680
I was like, I've been lied to my whole life and I'm so grateful that this happened to me now. Talked a

01:45:21.680 --> 01:45:26.359
bunch of other people, all similar experiences. I assumed this was a while ago. I

01:45:26.359 --> 01:45:30.840
assumed it was. And I was like, you know, very interested in. What was happening in the

01:45:30.840 --> 01:45:35.840
USI was like particularly like looking at where MDMA

01:45:35.840 --> 01:45:40.520
and psilocybin were on the path. And I was like, all right, this is going to get through like this is and this is going to like

01:45:40.600 --> 01:45:45.319
change the mental health of a lot of people in a really positive way. And I am

01:45:45.319 --> 01:45:50.119
surprised we have not made faster progress there. But I'm still optimistically well, well, we have made

01:45:50.119 --> 01:45:54.880
so much progress from the time of the 1990s.

01:45:55.359 --> 01:46:00.359
In the 1990s, you never heard about psychedelic retreats. You never heard about people

01:46:00.359 --> 01:46:05.279
taking these vacations. You never heard about people getting together in groups and doing these things and

01:46:05.279 --> 01:46:10.199
coming back with these profound experiences that they relate to other people and literally seeing

01:46:10.199 --> 01:46:14.960
people change, seeing who they are change. Seeing people become

01:46:14.960 --> 01:46:19.359
less less selfish, less toxic, less mean,

01:46:19.880 --> 01:46:24.479
you know, you. And. And more empathetic and more understanding. Yeah,

01:46:24.600 --> 01:46:29.470
it's. I mean, I can only talk about it from a personal experience. It's been a radical change in

01:46:29.470 --> 01:46:34.390
my life as well as, again, having all these conversations with different people. I feel so

01:46:34.390 --> 01:46:39.390
fortunate to be able to do this that I've had so many different conversations with so many different people

01:46:39.390 --> 01:46:43.989
that think so differently and so many exceptional people that have accomplished so many

01:46:43.989 --> 01:46:48.909
incredible things. And you get to sort of understand the way their mind works and the

01:46:48.909 --> 01:46:53.829
way they see the world, the way they interface with things. It's awesome. It's pretty fucking

01:46:53.829 --> 01:46:58.439
cool. And that is one of the cooler things about being a human that you

01:46:58.439 --> 01:47:03.000
can find a way to mitigate all the negative aspects of the monkey

01:47:03.000 --> 01:47:07.000
body and that you there are tools that are in place. But

01:47:07.000 --> 01:47:11.840
unfortunately, in this very prohibitive society, this Society of

01:47:12.399 --> 01:47:17.399
prohibition, we we're denied those and we're denied ones

01:47:17.399 --> 01:47:22.350
that have never killed anybody, which is really bizarre when you know, Oxycontin can still

01:47:22.350 --> 01:47:27.189
be prescribed. What? What's the deal with why we can't make

01:47:28.310 --> 01:47:32.510
if we leave? Like why we can't get these medicines that have transformed people's lives like

01:47:33.270 --> 01:47:38.229
more available What? What's the deal with why we can't stop the the opioid crisis

01:47:38.989 --> 01:47:43.710
or like fatal Seems like just an unbelievable crisis for San Francisco. You

01:47:43.750 --> 01:47:48.510
remember when the beginning of the conversation when you said that a I will do a

01:47:48.510 --> 01:47:52.729
lot of good, overall good, but also not no harm

01:47:53.529 --> 01:47:58.489
if we legalize drugs, all drugs that would do

01:47:58.489 --> 01:48:03.289
the same thing. Would you advocate to legalize all drugs? It's a very complicated question

01:48:03.609 --> 01:48:08.449
because I think you're going to have a lot of addicts that wouldn't be addicts. You're going to have a lot of people's lives

01:48:08.449 --> 01:48:13.130
destroyed because it's legal. There's a lot of people that may not be psychologically

01:48:13.130 --> 01:48:18.039
capable of handling things maybe they already have. Like that's the thing about psychedelics. They

01:48:18.039 --> 01:48:23.039
do not ever recommend them for people that have a slippery grasp on reality as it is. People that

01:48:23.039 --> 01:48:28.039
are struggling, people that are already on a bunch of medications that allow them just

01:48:28.399 --> 01:48:33.279
keep a steady state of existence in the normal world. If

01:48:33.279 --> 01:48:38.279
you just fucking bombard them with psilocybin, who knows what

01:48:38.279 --> 01:48:43.159
kind of an effect that's going to have and whether or not they're psychologically too fragile to recover

01:48:43.159 --> 01:48:47.789
from that. I mean, there's many, many stories of people taking too much acid and never coming back.

01:48:49.350 --> 01:48:50.869
Yeah, yeah. These are like

01:48:55.189 --> 01:48:59.630
a powerful doesn't seem to like, begin to cover it, right? Yeah, but there's also

01:48:59.869 --> 01:49:04.710
what is it about humans that are constantly looking to perturb their normal

01:49:04.710 --> 01:49:09.689
state of consciousness? Constantly. Whether it's we're both drinking coffee, you know,

01:49:09.689 --> 01:49:14.649
people smoke cigarettes. They they they do all, they take Adderall, they do all sorts of different

01:49:14.649 --> 01:49:19.609
things to change and enhance their normal state of consciousness. It seems like whether it's

01:49:19.609 --> 01:49:24.289
meditation or yoga, they're always doing something to try to get out of their own

01:49:24.289 --> 01:49:29.170
way or get in their own way or distract themselves from the pain of

01:49:29.170 --> 01:49:33.810
existence. And it's it seems like a normal part of humans and even

01:49:33.810 --> 01:49:38.750
monkeys, like vervet monkeys, get addicted to alcohol, they get addicted to fermented

01:49:38.750 --> 01:49:43.750
fruits and alcohol, and they become drunks and Alcoholics. It just it's. It's

01:49:43.750 --> 01:49:48.710
What do you think is the deep lesson there? Well, we're not happy exactly. You

01:49:48.710 --> 01:49:53.630
know, we're. And then some things can make you happy. Sort of for like a couple of drinks makes you so happy

01:49:54.029 --> 01:49:58.789
for a little bit. Until you're an alcoholic, until you destroy your liver, until you crash your car,

01:49:58.789 --> 01:50:03.149
until you're you know you're involved in some sort of a violent

01:50:03.430 --> 01:50:08.329
encounter that you would never be involved with if you weren't drunk. You know, I

01:50:08.329 --> 01:50:13.050
love caffeine, which clearly is a drug. Alcohol,

01:50:13.050 --> 01:50:17.409
like I like. But I often am like, yeah, this is like, you know,

01:50:18.130 --> 01:50:22.890
this is like dulling me and I wish I hadn't had this drink. And then other stuff

01:50:22.890 --> 01:50:27.890
like I mostly would choose to avoid, but that's because you're

01:50:27.890 --> 01:50:32.649
smart and you're probably aware of the pros and cons and and you're also

01:50:32.649 --> 01:50:37.489
probably aware of how it affects you and what's doing good for you and what

01:50:37.489 --> 01:50:42.289
is detrimental to you. But that's a decision that you can make as an informed

01:50:42.289 --> 01:50:46.649
human being that you're not allowed to make if everything's illegal. Right.

01:50:48.010 --> 01:50:52.770
Yeah. And also, when things are illegal, criminals

01:50:52.770 --> 01:50:57.409
sell those things because it's you're not tampering the desire by

01:50:57.409 --> 01:51:02.250
making it illegal, you're just making access to it much more complicated. What I was going to

01:51:02.250 --> 01:51:07.250
say is, if fentanyl's really great, I don't want to know. Apparently it is. Apparently it

01:51:07.250 --> 01:51:11.649
is, yeah. Peter Berg was on the podcast and he produced that Painkiller

01:51:11.649 --> 01:51:16.130
documentary for Netflix about the the, the, the docudrama about the Sackler family. It's

01:51:16.289 --> 01:51:21.050
amazing piece. But he said that he took Oxycontin

01:51:21.050 --> 01:51:25.850
once recreationally and he was like, Oh my God, it's amazing.

01:51:26.289 --> 01:51:31.229
He's like keep this away from me. It feels so good. Yeah. And that's part of the

01:51:31.229 --> 01:51:36.229
problem is that, yeah, it will wreck your life. Yeah, it will. It will capture you. But it's. Just so

01:51:36.310 --> 01:51:41.270
unbelievable. But the feeling like what? How did Lenny Burst describe it? I think you described heroin

01:51:41.270 --> 01:51:46.109
as getting a warm hug from God. I think the

01:51:46.109 --> 01:51:51.069
feeling that it gives you is probably pretty spectacular. I don't

01:51:51.069 --> 01:51:55.710
know if legalizing that is going to solve the

01:51:55.710 --> 01:52:00.640
problems. But I do know that another problem that we're not paying attention to is the rise

01:52:00.640 --> 01:52:05.359
of the cartels. And the fact that right across our border where you can walk, there are

01:52:05.359 --> 01:52:10.119
these enormous, enormous organizations that make

01:52:10.640 --> 01:52:15.520
who knows how much money, untold, uncalculable amounts of money

01:52:15.760 --> 01:52:20.640
selling drugs and bring them into this country. And one of the things they do is they they put fentanyl and everything to

01:52:20.640 --> 01:52:25.619
make things stronger. And they they do it for like street Xanax. There's people that have

01:52:25.619 --> 01:52:30.300
overdosed thinking they're getting Xanax and they fucking die from fentanyl. Yeah, they they do it with

01:52:30.300 --> 01:52:35.100
cocaine, Of course. They do it with everything. There's so many things that

01:52:35.100 --> 01:52:39.420
have fentanyl in them and they're cut with fentanyl because fentanyl is cheap and

01:52:39.460 --> 01:52:44.340
insanely potent. And that wouldn't be a problem if things were

01:52:44.340 --> 01:52:49.260
legal. So do you, would you net out towards saying, all right, let's just leave, Yeah, I would. I would net out

01:52:49.260 --> 01:52:54.220
towards that. But I would also put into place some serious mitigation efforts like in

01:52:54.220 --> 01:52:59.220
terms of counseling, drug addiction and I began therapy, which is another thing that's. Someone

01:52:59.220 --> 01:53:03.859
was just telling me about how transformative this was for them. Yeah, I haven't experienced that personally, but I

01:53:03.859 --> 01:53:08.699
began for many of my friends that have had pill problems. And I have a friend, my

01:53:08.699 --> 01:53:13.270
friend Ed Clay, who started an ibogaine center in

01:53:13.270 --> 01:53:18.270
Mexico because he had an injury and he got hooked on pills and he couldn't kick

01:53:18.270 --> 01:53:22.869
it. Did ibogaine gone? One time done, One time done. 24 hour

01:53:22.869 --> 01:53:27.029
super uncomfortable. It's supposed to be a horrible experience, right? Yeah, It's supposed to be not very

01:53:27.029 --> 01:53:32.029
recreational. Not exactly something you want to do on the weekend with friends. It's something you do

01:53:32.029 --> 01:53:36.510
because you're fucked and you need to figure out how to get out of this fuckness and

01:53:36.510 --> 01:53:41.380
that. So like we think about how much money is spent on rehabs in this country and what what's the

01:53:41.539 --> 01:53:46.300
relapse rate? It's really high. I mean I have many friends that have been to

01:53:46.300 --> 01:53:51.140
rehab for drug and alcohol abuse and quite a few of them

01:53:51.340 --> 01:53:56.060
went right back to it. Quite a few. It doesn't seem to be that effective. It seems to be effective to

01:53:56.060 --> 01:54:01.060
people when people have like they really hit rock bottom and they have a strong will and then they get

01:54:01.060 --> 01:54:05.699
involved in a program, some sort of a 12 step program, some sort of a Narcotics anonymous program.

01:54:06.020 --> 01:54:10.550
And then they they get support from other people and they eventually build this

01:54:10.550 --> 01:54:15.310
foundation of other types of behaviors and ways to find other

01:54:15.310 --> 01:54:20.069
things to focus on to the whatever aspect of their mind that allows them to be

01:54:20.069 --> 01:54:24.989
addicted to things. Now it's focused on exercise, meditation, yoga, whatever it is,

01:54:25.229 --> 01:54:29.789
that's your new addiction. And it's a much more positive and beneficial addiction. But the

01:54:29.789 --> 01:54:34.779
reality of the physical addiction that there are mitigation

01:54:34.899 --> 01:54:39.659
efforts. Like, there's so many people that have taken psilocybin and completely quit drugs, completely quit

01:54:39.659 --> 01:54:44.539
cigarettes, completely quit a lot because they realize like, oh, this is what this is,

01:54:44.539 --> 01:54:49.300
This is why I'm doing this. Yeah, that's that's why I was more

01:54:49.300 --> 01:54:54.180
optimistic that the world would have made faster progress towards acceptance of

01:54:54.539 --> 01:54:59.300
your so many stories like this. So I would say, like, all right, clearly a lot of our existing mental health

01:54:59.300 --> 01:55:03.949
treatment at best doesn't work. Clearly, our addiction programs are

01:55:04.430 --> 01:55:09.229
ineffective. If we have this thing that in every scientific study or

01:55:09.229 --> 01:55:13.510
most scientific studies we can see is delivering these like unbelievable results.

01:55:14.630 --> 01:55:19.470
It's gonna happen. Yeah. And it. Yeah, I

01:55:19.470 --> 01:55:24.430
still am excited for it. I still think it'll be a transformatively positive development. But it'll

01:55:24.430 --> 01:55:29.329
change politics. It'll it'll absolutely change the way we think of other

01:55:29.329 --> 01:55:33.970
human beings. It'll absolutely change the way we think of society and culture as a whole. It'll

01:55:33.970 --> 01:55:38.529
absolutely change the way people interact with each other. If it's if it becomes

01:55:38.529 --> 01:55:43.409
legalized and it's slowly becoming legalized. Like think of marijuana, which is like, you know, the gateway

01:55:43.409 --> 01:55:48.050
drug. Marijuana is now legal recreationally in how many

01:55:48.050 --> 01:55:52.250
states? 23 and and then

01:55:52.250 --> 01:55:57.109
medically and many more. And you know, it's really easy to

01:55:57.109 --> 01:56:02.109
get a license medically in California. Used to just, I got one in 1996.

01:56:02.430 --> 01:56:07.430
Used to be able to just go somewhere and go. I got a headache. That's it. Yeah, I

01:56:07.430 --> 01:56:12.189
get headaches. I'm in pain a lot. You know, I do a lot of martial arts. I'm always injured. I need

01:56:12.350 --> 01:56:17.310
some medication. I don't like taking paying pills. Bam, you got a legal prescription for weed. I used to have to go

01:56:17.310 --> 01:56:21.430
to Englewood to get it. I used to have to go to the hood to the Englewood Wellness Center

01:56:22.590 --> 01:56:27.470
and I was like, this is crazy. Like marijuana is now kind of sort of legal.

01:56:27.909 --> 01:56:32.869
And then in 2016 it became legal in California recreationally and it just

01:56:32.869 --> 01:56:37.789
changed everything. I have all these people that were like right wing people

01:56:38.029 --> 01:56:42.989
that were taking edibles to sleep, You know, I'm like, this is because now that it's legal, they

01:56:42.989 --> 01:56:47.880
thought about it in a different way. And I think that that drug,

01:56:47.880 --> 01:56:52.680
which is a fairly mild psychedelic, also has enhancing effects.

01:56:52.960 --> 01:56:57.960
It makes people more compassionate. It makes people more kind and friendly. It's sort of

01:56:57.960 --> 01:57:02.920
the opposite of a drug that that enhances violence. It doesn't enhance violence at all. It's just it

01:57:02.920 --> 01:57:07.699
doesn't like alcohol does that, Cocaine does that. To say a thing that'll make me very unpopular. I

01:57:07.699 --> 01:57:12.340
hate marijuana. It does not sit well with me at all. What does it do to you that you don't? Like it makes me

01:57:12.340 --> 01:57:17.180
tired and slow for a long time after it. Well, I think also there's biological

01:57:17.180 --> 01:57:22.119
variabilities, right? Like some people like my wife, she does not do

01:57:22.119 --> 01:57:27.119
well with alcohol. She can get drunk off 1 drink but it's biological like she she got some sort of

01:57:27.119 --> 01:57:31.920
a genetic. I forget what it's called something about bilirubin, like some something that her body just

01:57:31.920 --> 01:57:36.920
doesn't process alcohol very well so she's a cheap date. Oh, all I meant is that genetically, I got

01:57:36.920 --> 01:57:41.680
whatever the mutation is. That makes it an unpleasant experience. Yeah, but what I was saying is for me, that's the opposite.

01:57:41.960 --> 01:57:46.760
Alcohol doesn't bother me at all. I could. I could drink 3-4 drinks and I'm sober in 20 minutes

01:57:47.319 --> 01:57:52.319
and my body just my liver or just like a blast. It just goes right through it. I can sober up real quick,

01:57:52.840 --> 01:57:57.680
but I also don't need it like I'm doing sober October the for the whole

01:57:57.680 --> 01:58:02.680
month. I don't feel good. Yeah, did shows last night great, no problems that. Not having

01:58:02.680 --> 01:58:07.600
alcohol doesn't seem to bother me at all. But I do like it. I do like a

01:58:07.760 --> 01:58:12.520
glass of wine. Nice thing. At the end of the day, I like it. Speaking of that,

01:58:12.680 --> 01:58:17.439
and psychedelics in general, I, I you know, many cultures have had a place for.

01:58:17.840 --> 01:58:22.680
Some sort of psychedelic time in someone's life or rite of passage. But as

01:58:22.720 --> 01:58:27.359
far as I can tell, most of them are under. There's some sort of

01:58:27.359 --> 01:58:31.920
ritual about it. And I do worry that. And I think

01:58:32.119 --> 01:58:36.680
these these things are so powerful that I worry about them just being like kind of,

01:58:37.760 --> 01:58:42.760
yes, used all over the place all the time. And I hope that we as a society,

01:58:42.760 --> 01:58:47.279
because I think this is not going to happen, even if it's slow, find a way to treat this with.

01:58:48.210 --> 01:58:52.689
The respect that it needs, Yeah, we'll see how that goes.

01:58:52.770 --> 01:58:57.569
Agreed. Yeah, I I think set and setting is very important

01:58:57.890 --> 01:59:02.810
and thinking about what you're doing before you're doing it and why you're doing it. Like I

01:59:02.810 --> 01:59:07.170
was saying the other night when I had this psychedelic experience, I was just like, yeah,

01:59:07.170 --> 01:59:12.130
sometimes I just think too much about the world and that it's so fucked and you have kids

01:59:12.130 --> 01:59:17.050
and you wonder, like, what? What kind of a world are they going to grow up in? And what is? And it was just one of

01:59:17.050 --> 01:59:21.810
those days where I was just like, God, there's so much anger and there's so much this and that and then it's just

01:59:23.010 --> 01:59:28.010
it took it away from me the rest of the day. Like that night I was so friendly and so happy and

01:59:28.010 --> 01:59:32.890
I just wanted to hug everybody. I just really, I got it. I go, Oh my God, that does not

01:59:33.489 --> 01:59:38.409
thinking about it wrong. Do you think the anger in the world is way higher than it used to be? Or

01:59:38.409 --> 01:59:43.289
we just It's like all these dynamics from social media we were talking about. I think the dynamics in social

01:59:43.289 --> 01:59:48.090
media certainly exacerbated anger in some people, but I think anger in the

01:59:48.090 --> 01:59:51.819
world is just a part of frustration.

01:59:51.939 --> 01:59:56.659
Inequality problems that are so clear

01:59:56.659 --> 02:00:01.539
but are not solved, and all the issues that people have. I mean, it's not a

02:00:01.539 --> 02:00:06.020
coincidence that a lot of the mass violence that you're seeing in this country, mass

02:00:06.020 --> 02:00:10.659
looting and all these different things are being done by poor people. Do you think AGI will be a

02:00:10.739 --> 02:00:15.619
equalizing force for the world or further inequality? I think it would be. It depends on how

02:00:15.619 --> 02:00:20.560
it's implemented. My, my concern is again what we're talking about before

02:00:20.560 --> 02:00:25.119
with some sort of a neural interface that it will increase your

02:00:25.119 --> 02:00:30.079
ability to be productive to a point where you can control resources so much more than anyone

02:00:30.079 --> 02:00:35.000
else. And you will be able to advance your your economic

02:00:35.000 --> 02:00:39.720
portfolio and your influence in the world through that, your amount of power that you can acquire.

02:00:40.960 --> 02:00:45.680
It will before the other people can get involved, because I would

02:00:45.680 --> 02:00:50.039
imagine financially it'll be like cell phones in the beginning. You remember when

02:00:50.640 --> 02:00:55.560
the movie Wall Street, when he had that big brick cell phone. It's like, look at him, He's

02:00:55.560 --> 02:01:00.289
out there on the beach with a phone. That was crazy. No one had one of those things back then. And they were

02:01:00.289 --> 02:01:05.170
so rare. I got one in 1994 when I first moved to California, and I thought I was

02:01:05.170 --> 02:01:10.170
living in the fucking no. It was a Motorola Star TAC. That was a cool phone, I actually. Had one on

02:01:10.250 --> 02:01:15.210
in my car in 1988. I was one of the first people to get a cell phone. I got

02:01:15.210 --> 02:01:20.170
one in my car and it was great because my friend, my friend Bill Blumenwright, who

02:01:20.170 --> 02:01:25.130
runs The Comedy Connection, he would call me because he knew

02:01:25.130 --> 02:01:29.850
he could get a hold of me. Like if someone got sick or fell out, I could get a gig. Because he could call me.

02:01:30.210 --> 02:01:35.050
So I was in my car. I was like, Joe, what are you doing? Do you, do you have a spot tonight? And I'm like, no, I'm open. He's like,

02:01:35.050 --> 02:01:40.010
fantastic. And so he'd give me gigs. So I got a bunch of gigs through this phone where

02:01:40.010 --> 02:01:44.850
it kind of paid itself, but I got it just because it was cool. Like, I could drive down the

02:01:44.850 --> 02:01:49.689
street and call people. Dude, I'm driving and I'm calling you like, it was nuts to be able to

02:01:49.689 --> 02:01:54.689
drive. And I had a little antenna, a little squirrelly pigtail antenna on my car, on

02:01:54.689 --> 02:01:58.869
the roof of the car. But. Now everyone has one.

02:02:00.149 --> 02:02:04.989
You know, you can go to a third world country and you know, people in small villages have phones.

02:02:05.149 --> 02:02:09.909
It's it's super common. It's everywhere. Essentially, more people have phones

02:02:10.109 --> 02:02:14.750
than don't have phones. There's more phones than there are human beings, which is pretty fucking

02:02:14.750 --> 02:02:19.069
wild. And I think that that initial

02:02:19.510 --> 02:02:24.310
cost problem, it's going to be prohibitively expensive initially.

02:02:24.829 --> 02:02:29.550
And the problem is the wealthy people are going to be able to do that. And then the real crazy

02:02:29.550 --> 02:02:34.350
ones that wind up getting the holes drilled in their head. And if that stuff is effective, maybe it's

02:02:34.350 --> 02:02:37.869
not. Maybe there's problems with Generation One, but Generation 2 is better.

02:02:39.069 --> 02:02:43.510
There's going to be a time where you have to enter into the game. There's going to be a time where you have to sell your

02:02:43.510 --> 02:02:48.149
stocks like that. You don't, don't wait too long, Hang on there, go.

02:02:48.630 --> 02:02:53.350
And once that happens, my concern is that the people that have that will

02:02:53.350 --> 02:02:58.220
have. Such a massive advantage over everyone else that the

02:02:58.220 --> 02:03:03.100
have the gap between the haves and have nots will be even further and it'll be

02:03:03.100 --> 02:03:07.340
more polarizing. This is something I've changed my mind on. I, you know,

02:03:08.060 --> 02:03:12.899
someone, it opened and I said to me a few years ago, like you, you really can't just let

02:03:13.140 --> 02:03:17.220
some people merge without a plan because it could be such an incredible

02:03:18.539 --> 02:03:23.420
distortion of power. And then we're going to have to have some sort of societal discussion about this.

02:03:24.260 --> 02:03:27.619
That seems real. That seems like, yeah.

02:03:28.899 --> 02:03:33.739
Especially if it's as effective as a GI is

02:03:33.859 --> 02:03:38.819
or as excuse me ChatGPT is chat. GPT is so amazing

02:03:39.260 --> 02:03:44.100
when you enter into it information, you ask it questions and it can give you answers and you can

02:03:44.100 --> 02:03:49.060
ask it to code a website for you and it doesn't instantly and it solves problems that literally you would have to

02:03:49.060 --> 02:03:54.029
take decades. To try to solve and it and it gets to it right away, this is

02:03:54.029 --> 02:03:58.829
the dumbest it will ever be. Yeah, that's what's crazy. That's what's crazy. So

02:03:58.829 --> 02:04:03.189
imagine something like that, but even more advanced, multiple

02:04:03.949 --> 02:04:08.229
stages of improvement and innovation forward. And then

02:04:08.829 --> 02:04:13.710
it interfaces directly with the mind, but it only does it with the people that can afford it. And

02:04:13.789 --> 02:04:18.750
those people are just regular humans. So they haven't been there's, they haven't

02:04:18.750 --> 02:04:23.710
been enhanced. We haven't. We haven't evolved physically. We still have

02:04:23.710 --> 02:04:28.630
all the human reward systems in place. We're still basically these territorial primates.

02:04:29.229 --> 02:04:34.029
And now we have, you know, you just imagine some fucking psychotic

02:04:34.029 --> 02:04:38.470
billionaire who now gets this implant and

02:04:38.590 --> 02:04:42.989
decides to just completely hijack our financial systems,

02:04:42.989 --> 02:04:47.909
acquire all the resources. Set into place regulations and influences that only

02:04:47.909 --> 02:04:52.789
benefit them, and then make sure that they can control it from there on. How much do you think this

02:04:52.789 --> 02:04:57.630
actually, though? Even requires like a physical implant or like a physical

02:04:57.630 --> 02:05:02.510
merge versus just? Some people have access to GPT 7 and can spend a

02:05:02.510 --> 02:05:07.310
lot on the inference compute for it, and some don't. I think that's going to be very

02:05:07.310 --> 02:05:11.909
transformative too. But my thought is that once,

02:05:13.069 --> 02:05:17.529
I mean, we have to think of. What are the possibilities of a neural

02:05:17.529 --> 02:05:22.329
enhancement? If you think about the human mind and how the human mind interacts with the

02:05:22.329 --> 02:05:26.649
world, how you interact with the language and thoughts and facts

02:05:27.729 --> 02:05:32.649
and something that is exponentially more powerful

02:05:32.649 --> 02:05:37.210
than that. But it it also allows you to use the same

02:05:37.210 --> 02:05:41.729
emotions, the same ego, the same desires and drives

02:05:41.729 --> 02:05:46.109
jealousy, lust, hate, anger. All of those things.

02:05:46.550 --> 02:05:51.470
But with this godlike power, when one person can read

02:05:51.470 --> 02:05:54.909
minds and other people can't, when one person has a

02:05:56.069 --> 02:06:00.750
completely accurate forecast of all of the trends in terms of

02:06:00.750 --> 02:06:05.270
stocks and and resources and commodities, and they can make

02:06:05.270 --> 02:06:09.670
choices based on those, I totally see all of that. The only thing I'm,

02:06:10.989 --> 02:06:12.949
I feel a little confused about is,

02:06:16.449 --> 02:06:21.369
you know, human talking and listening bandwidth or typing and reading bandwidth is

02:06:21.369 --> 02:06:26.369
not very high, but it's high enough where if you can just say like tell me everything that's going to happen in

02:06:26.369 --> 02:06:31.170
the stock market, If I want to go make all the money, what should I do right now? And it goes and then just shows you on the

02:06:31.170 --> 02:06:35.729
screen. Even without a neural interface, you're kind of a lot of the way to

02:06:36.409 --> 02:06:41.170
this. Now you're describing. Sure. With, with stocks or with like, you know, tell me how to

02:06:41.170 --> 02:06:45.100
like, invent some new technology that will change the course of history.

02:06:46.380 --> 02:06:51.380
Yeah, yeah, all those things. Like, I

02:06:51.380 --> 02:06:55.340
think what somehow matters is access to massive amounts of computing power,

02:06:56.460 --> 02:07:01.300
especially like differentially massive amounts. Maybe more than the interface itself. I think

02:07:01.300 --> 02:07:05.979
that certainly is going to play a massive factor in the amount of

02:07:05.979 --> 02:07:10.930
power and influence a human being has having access to that. My

02:07:10.930 --> 02:07:14.890
concern is that what neural interfaces are going to do

02:07:15.449 --> 02:07:20.329
is now you're not a human mind interacting with that

02:07:20.329 --> 02:07:25.329
data. Now you are some massively advanced

02:07:25.329 --> 02:07:30.329
version of what a human mind is, and

02:07:30.569 --> 02:07:35.289
it has just profound possibilities

02:07:35.489 --> 02:07:40.130
that we can't even imagine. We can imagine, but we can't.

02:07:41.970 --> 02:07:46.890
We can't truly conceptualize them because we don't have the context. We don't have

02:07:46.890 --> 02:07:51.850
that ability in that possibility currently. We could just, we can just guess. But

02:07:51.850 --> 02:07:56.770
when it does get implemented that you're dealing with a completely

02:07:56.770 --> 02:07:57.770
different being.

02:08:02.289 --> 02:08:07.130
The only true thing is I could say is, I don't know, yeah. Do you

02:08:07.890 --> 02:08:12.630
wonder why it's you? Do you ever think, like, how am I

02:08:12.869 --> 02:08:16.229
at the forefront of this spectacular change?

02:08:21.510 --> 02:08:26.430
Well, first of all, I think it's very much like I think this is. You could make the

02:08:26.430 --> 02:08:31.310
statement for many companies, but none is it as true for is opening eyes like

02:08:32.149 --> 02:08:36.909
the CEO is far from the most important person in the company. Like in our case, there's a

02:08:36.909 --> 02:08:41.670
large handful of researchers, each of which are individually more critical to the

02:08:41.670 --> 02:08:46.670
success we've had so far and that we will have in the future than me. But even

02:08:47.149 --> 02:08:51.989
that, and I bet those people like really are like, this is a weird to be them.

02:08:52.470 --> 02:08:57.470
But it's certainly weird enough for me that it, like, ups

02:08:57.470 --> 02:08:59.789
my simulation hypothesis probability somewhat.

02:09:03.390 --> 02:09:07.390
What? When? If you ought to give a guess, what.

02:09:08.920 --> 02:09:13.920
When you think about the possibility of simulation theory, what? What? What kind of percentage do you? I've never known how to put

02:09:13.920 --> 02:09:18.880
any number on it, like, you know, it's See every argument that I've read

02:09:18.880 --> 02:09:23.720
written explaining why it's like super high probability. That all seems reasonable to me. Feels

02:09:23.720 --> 02:09:28.640
impossible to reason about though. What about you? Yeah, same thing.

02:09:28.880 --> 02:09:33.880
I go maybe, but it's still what it is and I have to. That's that's

02:09:33.880 --> 02:09:38.850
the main thing is I think it doesn't matter. I think it's like a OK. It kind

02:09:38.850 --> 02:09:43.529
of it, kind of. It definitely matters I guess, but there's not a way to

02:09:43.529 --> 02:09:48.489
know currently. And also what what matters though. Well, if if this really

02:09:48.489 --> 02:09:53.210
is, I mean our inherent understanding of life is that we are these biological creatures

02:09:53.210 --> 02:09:58.090
that interact with other biological creatures we we mate and breed, and

02:09:58.090 --> 02:10:02.909
that this creates more of us. And that hopefully, as society advances and we

02:10:02.909 --> 02:10:07.670
acquire more information, more understanding and knowledge, this next version of society will be

02:10:07.670 --> 02:10:12.430
superior to the version that preceded it, which is just how we look at

02:10:12.430 --> 02:10:16.909
society today. Nobody wants to live in 1860 where you died of a

02:10:16.909 --> 02:10:21.590
cold and there's no cure for infections. It's much better to be alive now.

02:10:22.069 --> 02:10:26.229
Like, just inarguably, there's.

02:10:27.079 --> 02:10:32.079
Unless you really do prefer the simple life that you see on Yellowstone or something like there's

02:10:32.399 --> 02:10:37.000
it's like what we're dealing with now in terms first of all, access to

02:10:37.000 --> 02:10:41.920
information. The the the lack of ignorance. If you're if you choose

02:10:42.960 --> 02:10:47.359
to seek out information, you have so much more access to it now than ever before.

02:10:48.119 --> 02:10:52.960
And overtime. Like if you go back to the beginning of written history to now.

02:10:54.029 --> 02:10:58.470
One of the things that is clearly evident is the more access to

02:10:58.470 --> 02:11:03.430
information, the better choices people can make. They don't always make better choices, but they certainly have much

02:11:03.430 --> 02:11:06.989
more of a potential to make better choices with more access to information.

02:11:08.390 --> 02:11:13.350
You know, we think that this is just this biological thing, but imagine if

02:11:13.350 --> 02:11:18.109
that's not what's going on. Imagine if this is a program and that you are

02:11:18.109 --> 02:11:22.460
just consciousness that's connected to this thing. That's

02:11:22.460 --> 02:11:26.500
creating this experience that is

02:11:26.500 --> 02:11:30.979
indistinguishable from what we like to think of as a real

02:11:30.979 --> 02:11:35.579
biological experience from carbon based life forms interacting with solid

02:11:35.579 --> 02:11:38.380
physical things in the real world.

02:11:41.699 --> 02:11:46.460
It's still unclear to me what I'm supposed to do differently or think. Yeah, there's no answer. Yeah, you're 100%

02:11:46.460 --> 02:11:51.020
right. What can you do differently? I mean, if you exist as if it's a

02:11:51.020 --> 02:11:55.939
simulation, if you just live your life as if it's a simulation, is that. I don't

02:11:55.939 --> 02:12:00.899
know if that's the solution, you know, I don't. I think. I mean, it's real to

02:12:00.899 --> 02:12:05.220
me no matter what. It's real. Yeah. I'm going to live it that way.

02:12:05.739 --> 02:12:10.619
And that will be the problem with an actual simulation if and when it does get implemented.

02:12:11.100 --> 02:12:16.020
If we do create an actual simulation, that's indistinguishable from real

02:12:16.020 --> 02:12:20.930
life. Like, what are the rules of the simulation? What is it? What? How

02:12:20.930 --> 02:12:25.810
does it work? Is that simulation fair and equitable and much more reasonable and

02:12:25.810 --> 02:12:30.409
peaceful does. Is there no war in that simulation? Should we all agree to

02:12:31.050 --> 02:12:35.930
hook up to it because we were will have a completely different experience in life and all the

02:12:36.170 --> 02:12:40.770
the the angst of crime and violence and the the things we truly are

02:12:40.770 --> 02:12:44.489
terrified of there will be nonexistent in the simulation,

02:12:46.090 --> 02:12:50.949
yeah. I mean, if we keep going, it seems like if you just look, if you just

02:12:50.949 --> 02:12:54.670
extrapolate from where VR is now. Did you see the podcast that

02:12:55.829 --> 02:13:00.470
Lex Friedman did with Mark Zuckerberg? I saw some clips but I haven't got. To watch those bizarre,

02:13:00.789 --> 02:13:05.189
right? So they're they're they're essentially using like very realistic physical

02:13:05.189 --> 02:13:09.270
avatars in the Metaverse like that's.

02:13:09.949 --> 02:13:14.630
That's step one. That's maybe that's step three. Yeah, maybe it's a little bit. Unpong at that. Yeah, maybe it's

02:13:14.630 --> 02:13:19.550
Atari, Maybe you're playing Space Invaders now. But whatever it is,

02:13:19.550 --> 02:13:24.390
it's on the path to this thing that will be indistinguishable. That seems

02:13:24.390 --> 02:13:29.310
inevitable. Those two things seem inevitable to me. The the inevitable thing to me is

02:13:29.310 --> 02:13:33.750
that we will create a life form that is an artificial.

02:13:34.439 --> 02:13:39.439
Intelligent life form that's far more advanced than us and once it becomes sentient

02:13:39.720 --> 02:13:44.279
it will be able to create a far better version of itself. And then as it

02:13:44.279 --> 02:13:49.119
has better versions of itself, it will keep going. And if it keeps

02:13:49.119 --> 02:13:53.560
going, it will reach God like capabilities, the

02:13:53.560 --> 02:13:58.199
complete understanding of every aspect of the

02:13:58.199 --> 02:14:03.109
universe and the structure of it itself. How to manipulate it, How to

02:14:03.109 --> 02:14:08.069
travel through it, How to communicate. And that, you

02:14:08.069 --> 02:14:12.989
know, if we keep going, if we survive 100 years, 1000 years, 10,000

02:14:12.989 --> 02:14:17.989
years and we're still on this same technological exponential increasing in

02:14:17.989 --> 02:14:22.989
capability path, that's God. We become

02:14:22.989 --> 02:14:27.970
something like a God. And that might be. What we do, that

02:14:27.970 --> 02:14:32.890
might be what intelligent, curious, innovative life actually does. It

02:14:32.890 --> 02:14:36.810
creates something that creates the very universe that we live in,

02:14:38.489 --> 02:14:43.369
that creates the next simulation and. Then yeah, maybe that's the birth of the universe itself

02:14:43.369 --> 02:14:48.250
is creativity and intelligence, and that it all comes from that. I just have this

02:14:48.250 --> 02:14:53.149
joke about The Big Bang. Like what if? What if The Big Bang is

02:14:53.149 --> 02:14:58.069
just a a natural thing? Like humans get so advanced that they create a Big Bang machine. And

02:14:58.069 --> 02:15:02.670
then, you know, we're so autistic and and riddled with Adderall that we'd have

02:15:02.789 --> 02:15:07.149
no concept or worry of the consequences. And someone's like, I'll fucking press it.

02:15:07.989 --> 02:15:12.750
And they press it and boom, we start from scratch every 14 billion

02:15:12.750 --> 02:15:15.590
years. And then that's what a Big Bang is.

02:15:18.319 --> 02:15:23.279
I mean, I don't know where it goes, but I do know that if you looked at the human race

02:15:23.279 --> 02:15:27.640
from afar, if you were an alien life form, completely detached from

02:15:28.800 --> 02:15:33.680
any understanding of our culture, any understanding of our biological

02:15:33.680 --> 02:15:38.600
imperatives, and you just looked at like, what is this one dominant species doing on

02:15:38.600 --> 02:15:43.479
this planet? It makes better things. That's what it does. It goes

02:15:43.479 --> 02:15:48.369
to war. It. You know, it steals. It does a bunch of things that it shouldn't do

02:15:48.369 --> 02:15:52.649
it. It pollutes, does all these things that are terrible. But it also

02:15:53.170 --> 02:15:57.890
consistently and constantly creates better things. Whether it's better

02:15:57.890 --> 02:16:02.729
weapons, going from the catapult to the rifle to the cannonballs to the

02:16:02.810 --> 02:16:07.569
rocket ships, to the hypersonic missiles to nuclear bombs, it creates better and

02:16:07.569 --> 02:16:12.529
better and better things. That's the number one thing it does. And it's never happy with what it

02:16:12.529 --> 02:16:17.470
has and the you. You add that to consumerism,

02:16:17.470 --> 02:16:22.470
which is baked into us, and this desire, this constant desire for newer,

02:16:22.470 --> 02:16:26.869
better things, well, that fuels that innovation because that gives it the resources that it needs to

02:16:26.869 --> 02:16:31.829
consistently innovate and constantly create newer and better things. Well, where if I was an

02:16:31.829 --> 02:16:36.590
alien life form, I was like, oh, what is it doing? It's trying to create better. Well, what is the

02:16:36.590 --> 02:16:41.069
forefront of IT? Technology. Technology is the most transformative, the most

02:16:41.069 --> 02:16:45.479
spectacular, the most interesting thing that we create. And the the most

02:16:45.600 --> 02:16:50.520
alien thing, The fact that we just are so comfortable that you can FaceTime with someone in New

02:16:50.520 --> 02:16:55.440
Zealand, like instantly we can. We can get used to anything pretty quickly, you know,

02:16:55.479 --> 02:17:00.479
Anything. Take it for granted. Almost. Yeah, and well, if you were an alien life form and

02:17:00.479 --> 02:17:05.399
you were looking at us, you're like, what is it doing? Keeps making better things. It's going to keep making better

02:17:05.399 --> 02:17:10.319
things. Well, if it keeps many making better things, it's going to make a better version of a thinking thing.

02:17:10.989 --> 02:17:15.989
And it's doing that right now. And you're a part of that. It's going to make a better version of a thinking thing. Well,

02:17:15.989 --> 02:17:20.510
that better version of a thinking thing, It's basically now in the amoeba stage. It's in the, you know,

02:17:20.510 --> 02:17:24.950
small multicellular life form stage. What if that

02:17:25.110 --> 02:17:29.389
version becomes a fucking Oppenheimer? What if that version,

02:17:29.829 --> 02:17:34.469
if it scales up so far that it becomes so hyper

02:17:34.469 --> 02:17:39.180
intelligent that it is? Completely alien to any other

02:17:39.180 --> 02:17:44.139
intelligent life form that has ever existed here before. And it constantly does the same thing, makes

02:17:44.139 --> 02:17:49.139
better and better versions of it. Well, where does that go? It goes to a God. It goes

02:17:49.139 --> 02:17:53.940
to something like a God. And maybe God is a real thing, but maybe it's a

02:17:53.940 --> 02:17:58.579
real consequence of this process that human beings have

02:17:58.860 --> 02:18:03.649
of consistently, constantly innovating. And constantly having this

02:18:03.649 --> 02:18:08.209
desire to to push this envelope of of

02:18:08.209 --> 02:18:12.930
creativity and of technological power, I guess it comes down to

02:18:13.530 --> 02:18:18.530
maybe a definitional disagreement about what you mean by it. It becomes a God like I can

02:18:18.530 --> 02:18:23.209
totally. I think it becomes something much like

02:18:23.290 --> 02:18:28.049
unbelievably much smarter and more capable than we are. And what does that thing become

02:18:28.329 --> 02:18:33.149
if that keeps going, and maybe the way you mean it, as a God like

02:18:33.149 --> 02:18:37.950
forces that that thing can then go create, can go simulate in a universe. Yes, OK.

02:18:38.110 --> 02:18:42.950
That that that I can resonate with. I think whatever we create will still be subject to the

02:18:42.950 --> 02:18:47.389
laws of physics in this universe. Right. Yeah, maybe that is the overlying

02:18:47.389 --> 02:18:52.350
fabric that God exists in. The God word is a fucked up word because it's just

02:18:52.350 --> 02:18:57.069
been so Co opted. But you know, I I was having this conversation with Stephen Meyer,

02:18:57.110 --> 02:19:01.700
who is. He's a physicist. I believe he's a physicist. He's a physicist

02:19:02.180 --> 02:19:06.940
and he's also religious. It was a real weird conversation, very fascinating

02:19:06.940 --> 02:19:11.579
conversation. Believer in Christ. Yeah, he, he even believes in the resurrection,

02:19:12.059 --> 02:19:16.979
which I found very interesting. But you know, it's it's interesting

02:19:16.979 --> 02:19:20.340
communicating with him because he has these little pre

02:19:22.379 --> 02:19:27.059
designed speeches that he's encountered all these questions so many times.

02:19:27.370 --> 02:19:32.370
That he has these very well worded, very articulate responses to these things that

02:19:32.370 --> 02:19:37.170
I sense are like bits. You know, like when I'm talking to a comic in like a comic. Like they

02:19:37.290 --> 02:19:42.209
all got this bit on train travel and they tell you, they tell you the bit. Like that's what it's like. He has

02:19:42.209 --> 02:19:46.770
bits on why he believes in Jesus and why he believes. And

02:19:46.809 --> 02:19:51.809
very, very intelligent guy. But I propose the question when we're thinking about

02:19:51.809 --> 02:19:56.090
God, what if the instead of God created the universe? What if the universe is God?

02:19:57.079 --> 02:20:01.719
And the creative force of all life and all everything is the universe

02:20:01.719 --> 02:20:05.799
itself. Instead of thinking that there's this thing that created.

02:20:06.600 --> 02:20:11.559
This is like close to a lot of the Eastern religions. I think this is an easier thing to wrap my mind around than any

02:20:11.600 --> 02:20:16.479
other religions for me. And that is the when I do psychedelics, I get

02:20:16.479 --> 02:20:21.000
that feeling. I get that feeling like there's this insane soup.

02:20:21.549 --> 02:20:26.549
Of like innovation and and and connectivity that exists all

02:20:26.549 --> 02:20:31.229
around us, but our minds are so primal. We're this

02:20:31.229 --> 02:20:36.229
fucking thing, you know? This is this is what we used to be. And that. What is that? It's

02:20:36.950 --> 02:20:41.750
there's a guy named Shane against the machine who's this artist who created this. It's a

02:20:41.750 --> 02:20:46.629
chimpanzee skull that he made out of Ziljan symbols. So I see that it's got a little Ziljan.

02:20:47.229 --> 02:20:51.649
He left it on the back and he just made this dope art piece. Cool. It's just cool.

02:20:52.450 --> 02:20:57.450
But I wonder if our limitations are that we are

02:20:57.450 --> 02:21:02.329
an advanced version of primates. We're still we still have all these things we talked

02:21:02.329 --> 02:21:07.209
about, jealousy and the anxiety, lust, anger, fear, violence. All these

02:21:07.209 --> 02:21:12.170
things that are the detrimental but were important for us to survive and get to

02:21:12.170 --> 02:21:17.129
this point. And that as time goes on, we will figure out a way to

02:21:17.129 --> 02:21:21.709
engineer those out. And that as intelligent life

02:21:21.709 --> 02:21:26.389
becomes more intelligent and we create a version of intelligent life that's

02:21:26.389 --> 02:21:31.350
far more intelligent than what we are, We're far more capable of what we are. If that keeps

02:21:31.350 --> 02:21:36.190
going, if it just keeps going, I mean ChatGPT. Imagine if you go to

02:21:36.190 --> 02:21:41.149
ChatGPT and go back to Socrates and show them that, explained

02:21:41.149 --> 02:21:46.010
that and show them a phone and you know and put it on the phone and have access to it. He'd be like. What

02:21:46.010 --> 02:21:50.329
have you done? Like, what is this like? I bet he'd be much more impressed with the phone than ChatGPT.

02:21:51.489 --> 02:21:56.209
I think you'd be impressed with the phone's abilities to communicate, for sure. But then the

02:21:56.250 --> 02:22:00.969
access to information would be so profound. I mean, back then, I mean, look,

02:22:01.329 --> 02:22:06.010
you're you're dealing with a time when Galileo was put under house arrest because he

02:22:06.049 --> 02:22:10.969
had the gumption to say that the Earth is not the center of the universe. Well, now we

02:22:10.969 --> 02:22:15.520
fucking know. It's not like we we have satellites. We have, we send. Literal

02:22:15.520 --> 02:22:20.479
cameras into orbit take photos of things. No, I totally get that. I just

02:22:20.479 --> 02:22:25.399
meant that we kind of know what it's like to talk to a smart person. And so in that sense, you're like,

02:22:25.479 --> 02:22:30.399
oh, all right, I didn't think you could like talk to a not person and have them be person like in some

02:22:30.399 --> 02:22:35.360
responses some of the time. But a phone, man, if you just like woke up after 2000 years

02:22:35.360 --> 02:22:40.159
and there was like a phone that would, you have no model for that you didn't get to get there gradually. Yeah,

02:22:40.319 --> 02:22:45.270
no, you didn't get My friend Eddie Griffin has a joke about that. It

02:22:45.430 --> 02:22:50.309
is about how Alexander Graham Bell had to be doing coke, he goes. Because only someone on

02:22:50.309 --> 02:22:53.510
coke would be like, I want to talk to someone who's not even here.

02:22:56.950 --> 02:23:01.909
And that's what phone is. Is that something Coke makes people want to do? I don't know. I've never done coke, but I would

02:23:01.909 --> 02:23:06.829
imagine it is. I mean, it seems to me like it just makes people like, angry and chaotic.

02:23:06.870 --> 02:23:09.709
Yeah, a little of that. But they also have ideas, you know?

02:23:12.590 --> 02:23:17.110
Yeah, I mean, But back to this. Where does it go? If it keeps

02:23:17.110 --> 02:23:22.069
going, it has to go to some impossible level of

02:23:22.069 --> 02:23:27.069
capability. I mean, just think of that. That, I believe, is going to happen. What we're able to

02:23:27.069 --> 02:23:31.670
do now with nuclear power and nuclear bombs and and and

02:23:31.670 --> 02:23:36.590
hypersonic missiles, and that's just the insane physical things that we've

02:23:36.590 --> 02:23:41.069
been able to take out of the human creativity and imagination and through

02:23:41.069 --> 02:23:45.909
engineering. And technology implement these physical devices

02:23:46.389 --> 02:23:51.309
that are indistinguishable for magic. If you brought them 500

02:23:51.309 --> 02:23:56.270
years ago, yeah, I think, I think it's quite remarkable. So keep

02:23:56.270 --> 02:24:01.030
going, keep going. 100,000 years from now, if we're still here, if something like us is still

02:24:01.030 --> 02:24:05.950
here, what can it do? In the same way that I don't think

02:24:05.950 --> 02:24:10.350
Socrates would have predicted the phone. I can't predict that. No, I'm probably totally off.

02:24:11.069 --> 02:24:15.709
But maybe that's also why comets exist. Maybe it's a nice reset, just like

02:24:15.709 --> 02:24:20.590
leave a few around, give them a distant memory of the

02:24:20.590 --> 02:24:25.030
utopian world that used to exist, have them go through thousands of years of

02:24:25.030 --> 02:24:30.030
barbarism, of horrific behavior, and then reestablish society. I mean

02:24:30.030 --> 02:24:35.030
this is the Younger Dryest impact theory that allow 11,800 years ago at the end of the Ice Age

02:24:35.350 --> 02:24:39.829
that we were hit by multiple comets that they caused the instantaneous.

02:24:41.280 --> 02:24:46.000
Melting of the ice caps over North America flooded everything is the the

02:24:46.000 --> 02:24:50.959
source of the flood myths from Epic of Gilgamesh in the Bible and all those things

02:24:51.000 --> 02:24:55.559
and that this and and also there's physical evidence of it when they do core samples. There's

02:24:55.879 --> 02:25:00.600
high levels of Iridium which is very common in space very rare on earth. There's

02:25:00.600 --> 02:25:05.360
micro diamonds that are from impacts and that it's like 30% of the earth like that

02:25:05.360 --> 02:25:10.149
has evidence of this. And so it's very likely that these people that are proponents of

02:25:10.149 --> 02:25:15.069
this theory are correct and that This is why they find these ancient structures that they're

02:25:15.069 --> 02:25:20.069
now dating to like 11,012 thousand years ago when they thought people are hunter gatherers and they go

02:25:20.069 --> 02:25:24.549
okay. Maybe our timeline is really off and maybe this physical evidence watching that with

02:25:25.030 --> 02:25:29.829
interest. Yeah, Randall Carlson is the greatest guy to pay attention to that. Yeah,

02:25:30.190 --> 02:25:35.069
he's kind of dedicated his whole life to it, which by the way, happened because of a psychedelic experience.

02:25:35.909 --> 02:25:40.270
He was on acid once. And he was looking at this immense Canyon

02:25:40.590 --> 02:25:45.469
and he had this vision that it was created by instantaneous erosions of the

02:25:45.670 --> 02:25:50.309
the polar caps. And then it just washed this wave of impossible

02:25:50.309 --> 02:25:54.229
water through the the earth. It just caught these paths.

02:25:55.069 --> 02:25:59.829
And now there seems to be actual physical evidence of that, that that is probably what

02:25:59.829 --> 02:26:04.229
took place and that, you know, we we're just the survivors.

02:26:04.719 --> 02:26:09.159
And that we have reemerged in that society and human civilization

02:26:10.000 --> 02:26:14.200
occasionally gets set back to a primal place. Yeah,

02:26:14.879 --> 02:26:19.840
you know, who knows if you're if you're right that what happens here is we kind of edit

02:26:19.840 --> 02:26:24.719
out all of the impulses in ourselves that we don't like. We get to that world seems kind of boring. So

02:26:24.719 --> 02:26:29.200
maybe that's when we have to make a new simulation to watch people think they're going through some drama or?

02:26:29.600 --> 02:26:34.389
Or maybe it's just. We get to this point where we have this power, but

02:26:34.389 --> 02:26:38.790
the haves and the have nots. The divide is too great and that people did

02:26:39.229 --> 02:26:44.030
get a hold of this technology and use it to oppress people who didn't have it, and that that

02:26:44.229 --> 02:26:48.149
we didn't mitigate the human biological

02:26:49.309 --> 02:26:53.909
problems, the reward systems that we have. I got to have more. You got to. Have less yes. This is

02:26:54.389 --> 02:26:59.069
this sort of natural inclination that we have for competition. And that someone

02:26:59.069 --> 02:27:03.950
hijacks that I think this is going to be such a hugely important issue to get ahead of

02:27:03.950 --> 02:27:08.829
before the first people. Push them, Yeah. What do you think about like when Elon was

02:27:08.829 --> 02:27:11.430
causing calling for a pause on AI and

02:27:14.069 --> 02:27:18.989
he was like starting an AGI company while I was doing that? Yeah, well, didn't he

02:27:18.989 --> 02:27:23.870
start it like after he was calling for the pause, I think before that, I

02:27:23.870 --> 02:27:26.590
don't remember in any case. Is it one of those? You can't beat him. Join them things.

02:27:30.280 --> 02:27:34.440
I think the instinct of saying like, we've really got to figure out how to

02:27:37.639 --> 02:27:42.479
make this safe and good and like widely good is really

02:27:42.479 --> 02:27:47.200
important. But I think calling

02:27:47.200 --> 02:27:52.159
for a pause is like naive at best.

02:27:53.879 --> 02:27:58.770
I kind of like, I kind of think you can't make

02:27:58.930 --> 02:28:03.809
progress on the safety part of this. As we mentioned earlier, by sitting like in the room and thinking hard, you've

02:28:03.809 --> 02:28:08.530
got to see where the technology goes. You've got to have Contra reality and then when you

02:28:08.530 --> 02:28:13.409
like. But we're trying to like make progress towards a GI conditioned on it being

02:28:13.409 --> 02:28:18.129
safe and conditioned on it being beneficial. And so when we hit any kind of like block,

02:28:18.489 --> 02:28:23.409
we try to find a technical or a policy or a social solution to overcome it.

02:28:23.909 --> 02:28:28.750
That could be about the limits of the technology and something not working and, you know, hallucinates or it's not getting smarter,

02:28:28.750 --> 02:28:33.629
whatever. Or it could be there's this like safety issue and we've got to like redirect our resources to

02:28:33.629 --> 02:28:38.430
solve that. But it's all like for me, it's all this same thing of like we're

02:28:38.430 --> 02:28:43.350
trying to solve the problems that emerge at each step as we get where we're trying to go.

02:28:43.909 --> 02:28:48.909
And, you know, maybe you can call it a pause if you want, a few pause on capabilities to

02:28:48.909 --> 02:28:53.780
work on safety. But in practice, I think the field has gotten a little bit

02:28:53.780 --> 02:28:58.620
wander on the axle there and safety and capabilities are not these

02:28:58.620 --> 02:29:03.579
two separate things. This is like I think one of The Dirty secrets of the field. It's like we have this one way to

02:29:03.579 --> 02:29:08.260
make progress. You know we can understand and push on deep learning more and

02:29:09.500 --> 02:29:14.299
that can be used in different ways. But it's I think it's that same

02:29:14.299 --> 02:29:19.260
technique that's going to help us eventually solve the safety. That all of

02:29:19.260 --> 02:29:23.700
that said, as like a human, emotionally speaking, I

02:29:23.700 --> 02:29:28.540
super understand why it's tempting to call for a pause. Happens all the time in life,

02:29:28.540 --> 02:29:33.020
right? This is moving too fast, right? We got to take a pause here. Yeah.

02:29:34.059 --> 02:29:38.819
How much of A concern is it in terms of national security that we are the ones

02:29:39.219 --> 02:29:43.940
that come up with this first? Well,

02:29:44.459 --> 02:29:49.459
I would say that if an adversary of ours comes up with it first

02:29:50.000 --> 02:29:54.719
and uses it against us, and we don't have some level of capability, that feels really

02:29:54.719 --> 02:29:59.440
bad, Yeah. But I hope that what happens is this can be a

02:29:59.440 --> 02:30:04.079
moment where to tie it back to the

02:30:04.079 --> 02:30:09.040
conversation, we kind of come together and overcome our base impulses and say like, let's all do this as a

02:30:09.040 --> 02:30:13.799
club together. That would be better. That would be nice and maybe

02:30:14.079 --> 02:30:19.079
through. AGI and through the implementation of this technology, it

02:30:19.079 --> 02:30:24.000
will make translation instantaneous and easy. So, well, that's already

02:30:24.000 --> 02:30:28.719
happened. Right. But I mean, it hasn't happened in real time, the point where

02:30:29.079 --> 02:30:33.920
you can accurately communicate very soon, very soon, very soon.

02:30:34.360 --> 02:30:39.360
Yeah, I I do think, for what it's worth,

02:30:39.440 --> 02:30:43.879
that the world is going to come together here.

02:30:44.760 --> 02:30:48.840
I don't think people have quite realized the stakes. But this is like, I don't think this is a

02:30:48.840 --> 02:30:53.520
geopolitical, if this comes down to like a geopolitical fighter race, I don't think there's any winners.

02:30:55.319 --> 02:31:00.239
And so I'm I'm optimistic about people coming together. Yeah,

02:31:00.280 --> 02:31:04.920
I am too. I mean, I think most people would like that.

02:31:05.399 --> 02:31:10.360
If you asked the vast majority of the human beings that are alive, wouldn't it be better if everybody got

02:31:10.360 --> 02:31:14.860
along? You know, maybe you can't

02:31:16.819 --> 02:31:21.700
go all the way there and say we're just going to have one global effort.

02:31:22.540 --> 02:31:27.459
But I I think at least we can get to a point where we have one global set of rules,

02:31:27.659 --> 02:31:32.659
safety, standards, organization that makes sure everyone's following the rules. We did this for atomic weapons,

02:31:33.340 --> 02:31:37.940
been similar things in the world of biology. I think we'll get there. That's a good

02:31:37.940 --> 02:31:41.540
example, the nuclear weapons, because.

02:31:42.920 --> 02:31:47.760
We know the destructive capability of them, and because of that we haven't detonated

02:31:47.760 --> 02:31:52.719
once since 1947. Pretty incredible, Pretty incredible. Other

02:31:52.719 --> 02:31:57.280
than tests, we haven't used one in terms of WAR

02:31:57.280 --> 02:32:02.239
45 or 47. When was the end of the World War 2? Wasn't it 47

02:32:03.159 --> 02:32:08.159
when they dropped the bombs? I think that was 45. I was wondering if there's more after that I didn't know about.

02:32:08.159 --> 02:32:13.100
It no might be. I think it was. 45 So from 1945, which

02:32:13.100 --> 02:32:17.780
is pretty extraordinary. That's right. It's remarkable. I would not have predicted that, I think, if I could teleport back to

02:32:18.540 --> 02:32:23.299
45. No, I would have thought, Oh my God, this is just going to be something that people do

02:32:23.620 --> 02:32:28.540
just launch bombs on cities. Yeah, I mean, I would have said like, we're

02:32:28.540 --> 02:32:33.540
not going to survive this for very long. And there was a real fear of that for sure. It's pretty extraordinary

02:32:33.540 --> 02:32:38.540
that they've managed to stop that, this, this threat of mutually assured destruction. Self

02:32:38.540 --> 02:32:43.379
destruction, destruction universe. I mean the whole world. We have enough weapons to literally

02:32:43.860 --> 02:32:48.780
make the world inhabitable, uninhabitable totally. And because of that, we haven't done

02:32:48.780 --> 02:32:53.500
it, which is a good, I think that isaacness, I think that should give some hope.

02:32:53.700 --> 02:32:58.620
Yeah, it should. I mean, Steven Pinker gets a lot of shit for his work because he just like

02:32:58.700 --> 02:33:03.680
sort of downplays. Violence today. But it's not that

02:33:03.680 --> 02:33:08.600
he's downplaying violence today. He's just looking at statistical trends. If you look at the reality of life

02:33:08.600 --> 02:33:13.280
today versus life 100 years ago, 200 years ago, it's far more

02:33:13.280 --> 02:33:18.040
safer. Why do you think that's a controversial thing? Like, why can't someone say, Sure, we still have

02:33:18.040 --> 02:33:22.840
problems, but it's getting better. Because people don't want to say that they're especially people are activists.

02:33:23.280 --> 02:33:28.239
They're they're completely engrossed in this idea that there's problems today and

02:33:28.239 --> 02:33:33.219
these problems are huge and there's. There's Nazis and there's but no one's saying there's

02:33:33.219 --> 02:33:38.180
not huge problems. Right. No one's saying there's not. But just to say things are better today. Some people,

02:33:38.180 --> 02:33:42.700
they just don't want to hear that, right? But those are also people that are addicted to the problems. The

02:33:42.700 --> 02:33:47.180
problems become their whole life solving those problems become their identity, that being

02:33:47.180 --> 02:33:51.819
involved in the solutions or what they believe their solutions to. Those problems become their life's

02:33:51.819 --> 02:33:56.500
work. And someone comes along and says actually life is safer than it's ever been before.

02:33:56.780 --> 02:34:01.200
Interaction. That's deeply I can see that it's deeply invalidated. Yeah. But

02:34:01.440 --> 02:34:06.239
also true, you know. And again what what is the problem? Why can't why can't

02:34:06.239 --> 02:34:11.159
people recognize that? Well, it's the primate brain and it's, it's all the the problems

02:34:11.159 --> 02:34:15.879
that we highlighted earlier and that that might be the solution

02:34:16.200 --> 02:34:21.000
to overcoming that is through technology. And that might be the only way we can do it

02:34:21.000 --> 02:34:25.719
without a long period of evolution, because biological evolution is so

02:34:25.799 --> 02:34:30.700
relatively slow in comparison to technological evolution. And

02:34:30.700 --> 02:34:35.540
that that might be our bottleneck was that we just still are dealing with this

02:34:35.540 --> 02:34:40.379
primate body and that something like general artificial

02:34:40.379 --> 02:34:44.180
general intelligence or something like some implemented form of

02:34:45.299 --> 02:34:50.100
engaging with it, whether it's neural link, something

02:34:50.459 --> 02:34:54.780
that shifts the way the mind interfaces with other minds.

02:34:55.739 --> 02:35:00.520
Isn't it wild? Speaking of biological evolution, there will be people, I think, who were alive

02:35:00.600 --> 02:35:05.399
for the invention or discovery, whatever you want to call it, of the transistor.

02:35:05.840 --> 02:35:10.760
There will also be alive for the creation of AGI one human lifetime. Yeah, you

02:35:10.760 --> 02:35:15.600
want to know a wild one From the implementation from Orville and Wilbur

02:35:15.600 --> 02:35:20.479
Wright flying the plane. It was less than 50 years for someone dropped an atomic bomb out of it.

02:35:21.479 --> 02:35:26.319
That's wild. That's crazy. That's crazy. Less than 40,

02:35:26.319 --> 02:35:29.629
right? That's crazy. Yeah. Bananas.

02:35:32.590 --> 02:35:36.709
I mean 60 something years to land on the moon. Nuts. Nuts.

02:35:37.309 --> 02:35:41.549
Where, you know, where is it going? I mean, it's just guesswork,

02:35:42.750 --> 02:35:47.750
but it's interesting for sure. I mean, it's the most fascinating thing of our time, for sure. It's fascinating

02:35:48.430 --> 02:35:52.670
intellectually. And I also think it is one of these things that will be

02:35:53.790 --> 02:35:58.670
tremendously net beneficial. Yeah, like, you know, we've been talking a lot about

02:35:59.270 --> 02:36:03.989
problems in the world. And I think that's just always a nice reminder of how much we get to

02:36:03.989 --> 02:36:08.590
improve. And we're going to get to improve a lot. And this will be. I think this will be the most powerful tool

02:36:10.069 --> 02:36:14.510
we have yet created to help us go go do that. I think you're right,

02:36:15.069 --> 02:36:19.989
and this is an awesome conversation. Thanks for having us. Thank you for being, really. Really appreciate it

02:36:20.389 --> 02:36:25.350
and thanks for everything. Keep us posted and we'll do. If you create Hal, I'll give you a call. Let us

02:36:25.350 --> 02:36:28.659
know. All right. Thank you. Thank you. Bye everybody.
"""

speech_lines = speech.splitlines()
speech_lines = [line.strip() for line in speech_lines]

speech_lines = [line for line in speech_lines if line != '']
speech_lines = [line for line in speech_lines if '-->' not in line]
combined = ' '.join(speech_lines)
tokens = tiktoken.encoding_for_model('gpt-3.5-turbo-16k').encode(combined)
print(len(tokens))
