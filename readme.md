# The Advent of Cow

Cow is a language that aims to be inclusive to cows by only using words that cows can say such as "moo".  
See the [COW webpage](http://bigzaphod.github.com/COW/) for more information.

This project is a python interpreter for Cow and an attempt at a question from the 
[Advent of Code 2020](https://adventofcode.com/)

## Usage

Clone this repo then when you have it on the python path you can run:
   
  ```python cow.py fibonacci.cow --stop=500```

from the command line.  That will produce something like:

```
running Cow script: fibonacci.cow. Format=cow. Will stop after 500 steps
start
1
1
2
3
5
8
13
21
34
Program force exited after 500 steps. Check for infinite loops or increase maximum steps.
end
```

## Transliterating / Cheating

Because I find it hard to remember the cow commands I have my own version of cow that is transliterated to
human. It is still idiomatic cow but with sounds and letters that are more easily distinguished by the human 
ear and eye.

Scripts can be transliterated in either direction with instructions like:

```python translate.py fibonacci.cow```

and

```python translate.py fibonacci.own```

and either version can be run with the cow.py interpreter. The direction that the commands should be 
transliterated is determined by the extension.

## Pre-loading Memory / More Cheating

It can be hard to load data into memory in cow...

## Debugging

For running a script in 'own' format I have added two extra commands:

| Command        | Effect|
| ------------- |-------------|
| ```brk```     | a command which does nothing but you can add a breakpoint that is hit when it is executed. This allows you to stop and inspect the memory near a problem in your code.|
| ```dbg```     | ```prn``` that is toggled by the debug mode of the execution.|
 
 
 