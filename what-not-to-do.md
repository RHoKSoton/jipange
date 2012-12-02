What not to do
==============

I spent a fair bit of time looking at possible Django plugins to handle the clinic feedback stuff, unfortunately for various reasons it wasn't really feasible in the time.

It's worth noting down for future reference.  It would be nice to be able to add general surveys etc., one of which would be the clinic feedback survey.  For now I've implemented it
as a hard-coded model with specific questions instead.

I tried out django-survey and django-crowdsourcing, but unfortunately after a lot of fiddliness required to make them work at all, it turned out they don't play nicely with Django 1.4.

-- amn
