## ASSERT

`assert`

### Problem Statement

#### divide

Implement the divide function, which checks that the divisor is not equal to 0 and divides the numbers.
* If so – returns the result of the division
* If not – makes an assert with the string "Division by zero"

### Example

```python
>>> divide(1, 2)
0.5
>>> divide(1, 0)
AssertionError: Division by zero
```

### Additional Comments

Use cases for [assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement):

* In tests (for example, in the tests for this task, we can use assert to check that the division returns the correct result)
* For sanity check (debugging) during development

> [!IMPORTANT]
> Do not use assert to alert about real errors inside the program,
because these checks can be cut out by the compiler in optimization mode
