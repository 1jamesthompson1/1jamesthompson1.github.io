---
title: "Test of building blog posts with rmd and Jekyll"
author: "James Thompson"
categories: blog
tags: Meta
---
This is a test to see if I can get my rmd files to get compiled and displayed in a nice format.

If so then this will make the process of producing cool blog posts with data and graphs much superior then other methods. It also means that I can be developing straight into the github repo and pushing it.

I guess I should start using some data that I have been working with for a recent uni project.

Below is R code that will load the library and you can see the code.

{% highlight r %}
library(rethinking)
data(Howell1)
{% endhighlight %}

But this code below that makes the plot is hidden!

![plot of chunk Howell1BasicPlot](/figures/Howell1BasicPlot-1.png)

However I have been told by people who are more knowledgeable then me that actually only the log of weight is relevant to height. Doh silly me. Here goes then Ill even show you what I am doing:

{% highlight r %}
plot(Howell1$height, log(Howell1$weight), xlab="Height", ylab="Log weight")
{% endhighlight %}

![plot of chunk Howell1LogPlot](/figures/Howell1LogPlot-1.png)

I wouldn't want to jump to too many conclusions but it looks to me that when height increases weight decreases? Wait no maybe increases? Always get stumped on these questions Ill let you decide. Now I might just test some console out.

{% highlight r %}
x <- 5 + 14
print(x)
{% endhighlight %}



{% highlight text %}
## [1] 19
{% endhighlight %}

And now lets make sure that nothing shows up or happens at all



Well lets hope that this works.

It is proving to be difficult but I am at least learning!

Problem.
I can get the blogdown::build_site() to make the md file from the rmd file. That works great. Then it will build the site but I cant get the images to work.

I am going to try put them in there original figures folder but include that in the config.yml folder.

I have also had to change the file path to just figures. This hopefully will work if the figures is included in the site.

Well it seems to be that it wants to read the images as binary files I will try putting in a different format photo.

Well that didnt work. I am getting quite stuck but amd going to put it down for the evening. I was supposed to be relaxing today!
