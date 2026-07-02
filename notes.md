# Dev Notes

These are development notes for the developer. Nothing of importance for you will be found here.

Notes: [DEP] means depends on if needed, [WIP] means work-in-progress feature for a later version that should be ignored for now, pop means people/population

## Quotation Formatting Logic

- "" for code
- '' for prints/returns

## Turn Logic

- aging
- resource production calculations (minus factory/tool)
    - food/coal deficit storage in appropriate variables
- factory/tool reduction calculation [DEP]
- factory/tool production calculation
- food/coal deficit calculations [DEP]
    - pop leaving calculations
- unrest [DEP]
- natural disaster [WIP]

## Error Formating Logic

The basis is that if a person doesn't try again, it will waste the least amount of resources possible in the case of multiple errors. Later, it will be reworked into a system that outputs all errors at once.

- not enough resources
- not enough structures
- not enough people

## Error Formating Idea

create an empty string to store errors. If it is empty at the end, give the success message and run the success code. Else, return the error string.

## markdown formatting notes (for the notes and README)

break<br>
break

**bold**

*italics*

> blockquote

1. ordered
2. list

- unordered
- list

[Link](https://zelda.fandom.com/wiki/Link)