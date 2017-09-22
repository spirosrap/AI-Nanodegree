# AI Search and Planning
## 3 developments in AI Search and Planning

(highlighting the relationships between the developments and their impact on the field of AI as a whole.)

### PDDL
STRIPS (Fikes and Nilsson, 1971) was the first major planning system. It used a problem representation language that greately influcenced current representation languages such as the PDDL - Problem Domain Description Language (Ghallab et al., 1998). PDDL is a computer parsable language with standarized syntax that is used to this day for representing planning problems. A commonly acceptable domain description language enabled further progress in the field. *"The adoption of a common formalism for describing planning domains fosters far greater reuse of research and allows more direct comparison of systems and approaches, and therefore supports faster progress in the field."([link](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.15.5965))*
PDDL is also used as the standard language for the International Planning Competition since 1998.


### Goal-regression planning

Early Planners considered only totally ordered sequence of actions. Later planners applied decomposition of the problems. However, they were (for example linear planning) proved to lead to incomplete plans. A complete planner should allow for interleaving of actions from different subplans within a single sequence. On solution was goal-regression planning.
In this technique the steps in each subplan are re-ordered to avoid conflict with the rest of subgoals.
WARPLAN (A case-based reasoning system that used a "skeleton model"[(link)](http://www-cs-students.stanford.edu/~pdoyle/quail/notes/pdoyle/planning.html#WARPLAN)) introduced by Waldinger and Warren. "In WARPLAN a solution to one goal was built and then the plan was constructively modified to achieve the further plans. The goals could be moved backwards through a partial plan to a position that they did not interfere"[(Catalogue of artificial Intelligences tools by ALan Bundy)](https://books.google.gr/books?id=wJCqCAAAQBAJ&pg=PA51&lpg=PA51&dq=WARPLAN+planner+Waldinger&source=bl&ots=p-qACMDiNQ&sig=WNcoEjupDXkrlpDrfnLYmIy0IFs&hl=el&sa=X&ved=0ahUKEwjXo9vZnrnWAhVCfhoKHdtcABsQ6AEINjAB#v=onepage&q=WARPLAN%20planner%20Waldinger&f=false) It was one notable example of a planner that used the programming language prolog. It was only 100 lines of code in Prolog, very small compared to other planners available at the time.


### GRAPHPLAN system

Avrim Blum and Merrick Furst (1995, 1997) introduced their GRAPHPLAN system, which was orders of magnitude faster than the other systems of the time.
