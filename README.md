# usecase_markdown
Small python script to convert a file containing an unformatted use case table(from CMPUT 301) to a markdown table for github wiki. 

Takes inputs in a file of the form:
``` 
Covers User Stories
US 01.03.01
Use Case Name
Give book status
Participating Actors
Owner, Borrower
Goal
Give each book a status of one of the following: available, requested, accepted, or borrowed
Trigger
Actor chooses to view the book
Precondition
Book has title, author, and description
Postcondition
Book has one of four statuses
Basic Flow
1. System gets book from database
2. System returns book and displays book status
```

and outputs, either to a file or stdout the following github markdown: 
```
| Use Case Name | GiveBookStatus |
| --- | --- |
| Covers User Stories | US 01.03.01 |
| Participating Actors | Owner, Borrower |
| Goal | Give each book a status of one of the following: available, requested, accepted, or borrowed |
| Trigger | Actor chooses to view the book |
| Precondition | Book has title, author, and description |
| Postcondition | Book has one of four statuses |
| Basic Flow | 1. System gets book from database<br> 2. System returns book and displays book status<br>  |
| Exceptions |  |
| Notes |  |
```

When put into a github wiki page, this produces the following table: 

| Use Case Name | GiveBookStatus |
| --- | --- |
| Covers User Stories | US 01.03.01 |
| Participating Actors | Owner, Borrower |
| Goal | Give each book a status of one of the following: available, requested, accepted, or borrowed |
| Trigger | Actor chooses to view the book |
| Precondition | Book has title, author, and description |
| Postcondition | Book has one of four statuses |
| Basic Flow | 1. System gets book from database<br> 2. System returns book and displays book status<br>  |
| Exceptions |  |
| Notes |  |


### Notes
The input does not need to be in that order of "headings." However, the content/value of each must come after that heading name and before the next heading(or EOF). 
The current "headings" are hard coded, and are: 
Use Case Name
Covers User Stories
Participating Actors
Goal 
Trigger
Precondition
Postcondition
Basic Flow
Exceptions
Notes

Not all headings must appear in the input. However, all will appear in the generated output. 

This was designed for the purposes of copying a completed table with this headings from Google Docs by selecting the full table, and producing the proper github markdown format. 
