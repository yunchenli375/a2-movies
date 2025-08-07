[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/e0OQHIms)

# CP1404 Assignment 2 - Must-See Movies 2.0 by YUNCHEN_LI

A Python project with GUI and Console programs that (re)use classes to manage a list of movies.

# Project Reflection

## 1. How long did the entire project (assignment 2) take you in working hours?

### Estimate

4 hours

### Actual

3 hours

## 2. What are you most satisfied with?

PyCharm is satisfying to use. Especially after learning its keyboard shortcuts in editor. Checking the references of a variable or function is very useful, so I can quickly ensure the ongoing modification will not break the feature. The integrated debugger allowed me to step through code execution and identify issues efficiently, particularly when debugging the console program. The code completion and syntax highlighting features helped catch errors early in the development process. Additionally, PyCharm's refactoring tools made it easy to rename variables and methods across the entire project while maintaining consistency. The built-in version control integration also streamlined the process of tracking changes and managing different iterations of the code.

## 3. What are you least satisfied with?

Those inexplicably subtle distinction of requirements between assignment 1 and assignment 2 with no reasonable or logical explanation.

1. The watched status in movies_backup.csv from assignment 1 is gratuitously inconsistent from the movies_backup.json from assignment 2. For example, the movie entitled "The Fugitive" is not watched in assignment 1, but watched in assignment 2.
2. The format of watching status is different. In assignment 1, the required format is "6 movies watched. 1 movies still to watch". However, in assignment 2, it becomes "3 movies still to watch, 2 watched".
3. The "Other" category in assignment 1 becomes "Fantasy" in assignment 2.

These capricious changes forcing students juggling with deliberately inconsistent data and meaningless data requirement changes is lazy assignment design that serves little educational purpose and hinders skill development of actual programming concepts. Those superficial variations create busywork wasting valuable learning time on nonsense details.

## 4. What worked well in your development process?

My analysis of the requirement and the design of classes and functions is thorough enough, so there is no large refactor that makes everything rewrite from scratch. The modular approach I took with separating concerns between different classes helped maintain clean code structure. I also effectively reused existing code patterns from previous work, which saved development time. The decoupling of fundamental functionalities and the interactive interfaces is a success.

## 5. What about your process could be improved the next time you do a project like this?

When designing the GUI program, I will draw a diagram to describe the dependencies of objects, properties and widgets, along with those interactions among them. This visual representation would help me better understand the data flow and event handling before implementation, potentially reducing debugging time and improving code organization. I may create some tests to ensure the correctness and robustness of every part of the GUI program, instead of simply trial and error. Setting up a more structured development workflow with regular commits and clear milestone targets would also help track progress more effectively and make it easier to revert changes if needed.

## 6. Describe what learning resources you used and how you used them

The Python documentation. Writing the json representation of an object by hand is very tedious, so does creating an object from the json key-value paris. I found that the internal link of an instance of a class, the built-in associated container dict and the key-value representation in json format. Given a constructor of a class, the double asterisk operator can unpack a built-in dict object, to pass its values as arguments of the constructor, and using the built-in function vars can obtain a dict representation of all data fields from a given object. And the json from the standard library supports the serialization and deserialization processes of dict object. Using this approach makes me write least boilerplate code when interacting with the json data format.

## 7. Describe the main challenges or obstacles you faced and how you overcame them

The main challenge I encountered was the coupling between data field names in the Movie class and the GUI interface requirements. As mentioned in the previous question, I utilized the built-in `vars()` function and dictionary unpacking to handle conversions between Movie objects and dictionary representations, which are essential for JSON serialization and deserialization.

Since the field names in the provided JSON files are immutable, all data field names in the Movie class became frozen constraints. During GUI development, the spinner widget required specific options: "Category, Title, Year, Watched". The critical issue was that "Watched" could not be trivially mapped to the internal field name "is_watched", creating an obstacle where the MoviesApp's sort_fields property couldn't directly utilize the Movie class's data_fields.

To resolve this mapping problem, I implemented a constant dictionary `SPINNER_ITEM_TO_FIELD` that explicitly defines the relationship between spinner display options and their corresponding sorting keywords. This approach indicates that I have to explicitly hard-code the mapping from model layer to view layer. While this solution violates the DRY (Don't Repeat Yourself) principle because I am redefining field names in both movie.py and the mapping dictionary, it effectively bridges the gap between user-facing interface elements and internal data structure naming conventions that is restricted by inflexible external data format requirements.
