Use case:

- `if` statement has no trailing else
- function exits immediately after `if` executes
- Missing branch coverage suggests failure to "naturally exit" function (e.g. `22->exit`)
