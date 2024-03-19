---
title: "My First Prototype"
last_modified_at: 2024-03-10T16:20:02-05:00
author: "James Thompson"
categories: blog
tags: university personal computers
---

*I should preface this that the blog post should of been published around the end of 2023. But due to me letting it slip through the gaps it is here now, better late then never is something that I have heard somewhere before.*

This is a story about my first prototype. My first real piece of software that went through a __proper__ development cycle (whatever that is) with real stakeholders and money involved. I have done various university assignments and built some large systems within google app scripts and google drive, however this one felt unique. It is an ongoing story of a project that started relatively small but has carried on now for almost a year.

# Start

As part of my studies at Massey University I had to complete a final year project. This was completed during July to October. It constitued a third of my workload for that semester. In choosing my project I wanted something that was both novel and hard. This made me reluctant to accept any of the professors "prepared projects" as they were nothing new and just larger assignments. There was an opportunity to do a project on some education software which seemed somewhat interesting. But before commiting to this I was speaking to my father who worked at the [Transport Accident Investigation Commision](https://www.taic.org.nz/). He was looking to build a tool that uses some of the new AI technology (namely ChatGPT) to make the investigation process easier and smarter. I thought that this sounded like a challenge that ticked the boxes of what I was looking for. Therefore a [proposal](https://github.com/1jamesthompson1/TAIC-report-summary/blob/3f74fc8bb91d20d4ce84065a65f3c3ade7613b98/Project%20documents/Uni%20documents/Proposal.pdf) was written up and accepted by my advisor and work commenced.

# Project

## Goal 

The end goal was to have a tool that would help agencies like the New Zealand Transport Accident Investigation Commsions. It would help them in two ways by supporting them in conducting inqueries and writing the reports as well as increasing the insights and effectiveness of each published report. The more direct goal of the project was to read use a LLM from OpenAI and read each of the reports and produce a data set of a report with various summaries and ratings. This would consititue a proof of concept to show me, my father and potentially TAIC that it was possible and even useful.

## Progress

I was completing this project as a requirement of a paper I was taking. This meant that I had to devote a third of my study time to it with the rest taken up by my other courses in Mathematics and Programming. However this project also took on the role as my partime job meaning I could devote another 5-10 hours to it a week. Lastly I was living in a Campervan in Wanaka NZ so I could train for my Snowboarding competitions. Thus with 3 days up the mountain I was having very busy evenings and 4 days "at home" (If a campervan counts). The first goal was simply to have somethat that could demonstrate it worth.

Firstly data scrpping and cleaning had to be done. This invotidlved the use of Beatifuul Soup to find all the PDF reports on the TAIC website. There was nothing really new or interesting here. But the cleaning of the PDFs into clean text files were more frustrating then meets the eye. The world uses PDFS as they look clean nd are snazzy and quite portable. but your in trouble if you need to read a lot of them programmitcally. 

Now quickly I learntthat you cant just give the whole report to a LLMs model because a report is about 50 pages which is just way above the context limmt of the LLLMs at the time GPT 3.5 etc. This meaning that Secondly I was going to need to extract the "useful" stuff of the reports. I followed guidance from an investigator that it is only the analysisand fidnings sections of a report that have important bits of inforrmtion.

Lastl was doing something userful with the engine. My first idea was about maknig the engine use the smartness to summarise the reports and create a dataset where further analaysis will really extract out the insights. This meant that I wanted the model to assignn a percent for how much a given theme was invoivled in the accident. This worked surpprsinly well. However the immediate question was what should these predefined themes be. This made me want to go back to GPT 3.5 and ask it after it has read all the reports what it thinks themain  themes are. To do this I asked gpt 3.5 to summarise each reports safety themes, then from there I gave it all the summaries and asked it to generate global themes.

Now with all of this done it was time that I could show my father and see what he thought about it. Obviousaly I had been discussing with him throughout but what is better than an inperson demo. So I sat down openned up my laptop had it ready to go with vscode and I start showing some tabs of code and the output folders and it was going great for maybe 3-5 seconds. Then I realized that I am speaking to a Marine accident investigatot not a fellow proogrammer. So I let the demo be "postponed". Then I rapidly strated building a webinterface that gave a userfirendly expereience to using the engine. Thus the Viewer was born and my project turned from just python script files to a complete app!

This was more or less the end of my University project work. There is a much longer report that can be found [here](https://github.com/1jamesthompson1/TAIC-report-summary/blob/main/Project%20documents/Uni%20documents/Final%20Report/21011195_159333_Final_Report.pdf).

## TAIC extension

Now that I had completd the work it was time to have a meeting with TAIC. As we were only dealing with a rough prototype this was a small meeting with some researchers at TAIC rather than an offical demo to leadership. Even though I didn't check anything before hand fate was on my side and the pproof of conept software worked exactly as I needed when giving a mini demo, the stars must of been lined up that day.

This exetenstion was about a month and took me from Mid November to 22nd of December which was going to be D-day. There were a fews item they wanted to accomplish in this sprin. These were:

1. Expand support to aviation and rail
2. Upgrade the web viewer to be more user friendly
3. strengthen analysis by adding quotes and reaonings to the weighings.

Firstly the challenge of adding in avaition and rail. Due to my attempts at following good programming practice adding in these reports was akin to jsut adding in two extra input pipes into the data pipeline. If you have ever worked on a project longer term these little wins make yu want to tip your hat at your past self. Now would be the place where I link the commit where I changed 3 characters or something however I wdidnt have the best branch displine meaning the commit is a sqauashed commit with allsorts f things going on. But as you might of huessed this was completed quite quicly without hassle.

Secondly was making the webapp something that could be used by a inverstigator/researcher. Now this was a difficult part not becuase it required a great feet of software engineering but simply becuase it is so far outside my expertise. THis meant that the work here involed a fight between me and various python web app frameworks. Good news I won with the help of LLMI upgraded the webapp to be pretty and profressional looking. Howeve in doing so there is definetly some technical dept taken on board as a proper app should of been built a proper way.

The last big ticket item was strenthingthe engines analyis. This is due to the ever present question of "how can we trust what this model says". Now there were two ways that this problem can be tackled from. Firstly is in the generation pahase, that is I can make something that is not only correct but verifiable. Seoncdly it can be done by actually verifing the output from the model. This idea is the bread and butter of models where you check it with what you want to be saying. I had done this when doing the initial university project and it showed the otuputs were familiar. However as I changed the output of the model the validation set would have to be recreated and due to time constraints this was not possible. Going into the this TAIC extension I wanted to focus on the first method to make each of the summaries, ranking etc self containted and human verifiable.

Making it human verifiable means that I needed to have reaoning and more importantly quotes. Changing the GPT 4 prompts so that it was ouptuting reasoning and quotes as well was not hard. The problem was to make sur that it wan't just making things up. This part is what took the time. Fortunately checking a quote is possible as we have the referenc material. Therefore it is in theory we just need to check the reference material at the given location and see if we can find the reference. Yet as with all oof life theory is easier than practice. The main problem was really just getting the GPT to output the qutoes and references in a format that was consitant and machine readable. However after a good battle with the prompts and doing a bit of prompt engineering I got smewhere that works well enough. It cant verify and find all quotes but a vast majority of them and even reppair the ones that have problems!  

# Further work

At the end of this work there was a meeting organised for the 22nd of Decemeber with te leadershp of TAIC (CEO, ceif investigator etc). Unlike my othr meetings this was a proper product demo. There was diahrams, power points the whole lot. However one of the craziest things about it was that I would say things in the presentation and then the whole room would eruopt in squigles and typing as bpeopel would note down what I said! The presentation went well from a technical persepctive as almost everything worked (except aslly filter results to only include reports from ciertain year range, not sure what happened as I couldn't for the life of me recreate the error at home later). From a"business perspecctive" it also went well as the CEO was very keen on it and wanted to sign me up again with another contract.

However I had a 2 month trip around europe booked so it would have to wait until I got back. This is where I am right now just returning from europe and about to get started on Monday with further work.

This further work is going to focus its efforts on expanding the analysed reports to also have other none NZ transport accident investigation commissino. Likely Australian Transport Safety Bureau.

Where the future of this project wll lead is unknown however I am excited to still be working on my University project and making it better with every sprint.

# Conclusion

This project has had some unique aspects to it that I have not had to deal with before. I learnt and experience a much more sophiisticated development cycle which involved lots of writing proposals, reports etc. but it has also gien me an opporunity to really focus on a project with my full attention for some non trivial time.

If Istarted this again there would clearlt be things I would do different from the start. I also am frsutrated that I havent been able to incorperate true learning into this model. It has turned into what feels more like a software eingering prject that happens to use GPT models. However I have no idea what is a real machine learning project or what not. Luckily life moves forwards so I have opportunties to do more as well as refine what has already been done.

If you have managed to power through al of this you may be interested in all the documents that have been written in realtion to tthis project. These can be found inside hte github repo here: https://github.com/1jamesthompson1/TAIC-report-summary/tree/main/Project%20documents.