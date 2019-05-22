Hello and welcome to this tutorial, if you're here you probably already know what this is about but if not here's a quick overview
Talon is an app that enables hesitancy in the website powerful hands-free input

essentially allowing you to control your computer completely with your voice and if you so choose a headmounted device to replace your mouse
this is great especially for people who are for whatever reason unable to use their hands for normal computer work or even those who are just looking for a boost in productivity from the highly customizable voice macros that Talon offers

in this tutorial we will
- be covering the very basic set up of talent on my machine. For this video we are using Talon 0.0.8.41 with  Mac OS high Sierra 10.13.6.
- Introduce you to some of the functionality that is included in the community script repository
– briefly touch on modifying and creating your own scripts Sage
32.
So you’ve just installed Talon and the community script package. OK what now?

First things first, assuming you’ve installed everything correctly and Talon is running

You can say click or double click to left click,
You can say righty to right click,
You can say wheel up or wheel down to move your mouse wheel as you would normally.
You can say mission control to access all your windows and desktops.

Great, now we’ve got a way to navigate your computer without any clicking.

Next, let’s open up textedit and play around.

Say “Launch textedit”.
Cool.

Say “Help Alphabet”.
Cool.

Let’s spell some words.

Talon doesn’t understand normal letters like A, B, or C.

Instead, talon uses this word - letter alphabet. It helps prevent ambiguity and errors when spelling quickly.

Let’s spell “hello world”.

Damn that took a while,
Hm. I wonder if there’s a better way.

say “help context”.

“Help context” shows you all the available “contexts” for you to use. In a nutshell, contexts are libraries of voice macros that can be configured to only work for certain apps, or to work globally, regardless of app.

Let’s look at the "formatters" context. You can do that by just saying “help formatters" or "NUMBER”

Interesting.
 so we've got a number of commands here. The one will be interested in is the first one.  on the left hand we have a speaker emoji and some words surrounded by various symbols. The words phrase and say are grouped by parentheses and separated by a pipe. That's that weird longline thing. That means you can say either phrase or say to use this command. The over inside square brackets means that that's an optional portion of the command. So you could just say phrase "hey what's going on" or "phrase hey what's going on over," using the word over to indicate to Talon that you have finished the command.

Let’s try “say hello world OVER”

Great.
Hm. What if I don’t like what a certain letter is configured to?

Let’s open up our favorite text editor and modify the appropriate file.

For example, letters are stored in basic_keys.

Quick note: the speech commands here are my own; the talon community app doesn’t come shipped with Sublime macros.

Edit basic_keys.

Show new settings.

That’s pretty much it
