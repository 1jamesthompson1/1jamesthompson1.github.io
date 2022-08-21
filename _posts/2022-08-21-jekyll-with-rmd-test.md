---
title: "Test of building blog posts with rmd and Jekyll"
author: "James Thompson"
categories: blog
tags: meta
---
This is a test to see if I can get my rmd files to get compiled and displayed in a nice format.

If so then this will make the process of producing cool blog posts with data and graphs much superior then other methods. It also means that I can be developing straight into the github repo and pushing it.

I guess I should start using some data that I have been working with for a recent uni project.

Below is R code that will load the library and you can see the code.

{% highlight r %}
library(rethinking)
{% endhighlight %}



{% highlight text %}
## Loading required package: rstan
{% endhighlight %}



{% highlight text %}
## Loading required package: StanHeaders
{% endhighlight %}



{% highlight text %}
## 
## rstan version 2.26.13 (Stan version 2.26.1)
{% endhighlight %}



{% highlight text %}
## For execution on a local, multicore CPU with excess RAM we recommend calling
## options(mc.cores = parallel::detectCores()).
## To avoid recompilation of unchanged Stan programs, we recommend calling
## rstan_options(auto_write = TRUE)
## For within-chain threading using `reduce_sum()` or `map_rect()` Stan functions,
## change `threads_per_chain` option:
## rstan_options(threads_per_chain = 1)
{% endhighlight %}



{% highlight text %}
## Do not specify '-march=native' in 'LOCAL_CPPFLAGS' or a Makevars file
{% endhighlight %}



{% highlight text %}
## Loading required package: cmdstanr
{% endhighlight %}



{% highlight text %}
## This is cmdstanr version 0.5.2
{% endhighlight %}



{% highlight text %}
## - CmdStanR documentation and vignettes: mc-stan.org/cmdstanr
{% endhighlight %}



{% highlight text %}
## - CmdStan path: C:/Users/James/OneDrive/Documents/.cmdstan/cmdstan-2.30.0
{% endhighlight %}



{% highlight text %}
## - CmdStan version: 2.30.0
{% endhighlight %}



{% highlight text %}
## 
## A newer version of CmdStan is available. See ?install_cmdstan() to install it.
## To disable this check set option or environment variable CMDSTANR_NO_VER_CHECK=TRUE.
{% endhighlight %}



{% highlight text %}
## Loading required package: parallel
{% endhighlight %}



{% highlight text %}
## rethinking (Version 2.21)
{% endhighlight %}



{% highlight text %}
## 
## Attaching package: 'rethinking'
{% endhighlight %}



{% highlight text %}
## The following object is masked from 'package:rstan':
## 
##     stan
{% endhighlight %}



{% highlight text %}
## The following object is masked from 'package:stats':
## 
##     rstudent
{% endhighlight %}



{% highlight r %}
data(Howell1)
{% endhighlight %}

But this code below that makes the plot is hidden!

![plot of chunk Howell1BasicPlot](assets/./_posts/2022-08-21-jekyll-with-rmd-test/Howell1BasicPlot-1.png)

However I have been told by people who are more knowledgeable then me that actually only the log of weight is relevant to height. Doh! silly me. Here goes then Ill even show you what I am doing:

{% highlight r %}
plot(Howell1$height, log(Howell1$weight), xlab="Height", ylab="Log weight")
{% endhighlight %}

![plot of chunk Howell1LogPlot](assets/./_posts/2022-08-21-jekyll-with-rmd-test/Howell1LogPlot-1.png)

I wouldn't want to jump to too many conclusions but it looks to me that when height increases weight decreases? Wait no maybe increases? Always get stumped on these questions Ill let you decide. Now I might just test some console out.

{% highlight r %}
x <- 5 + 10
print(x)
{% endhighlight %}



{% highlight text %}
## [1] 15
{% endhighlight %}

And now lets make sure that nothing shows up or happens at all



Well lets hope that this works.
