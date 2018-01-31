# SEDS-HW3
Homework #3 from SEDS


### Due Feb. 1, 2017 at 5PM

_note_ This assignment is also about process, not just the end product.  Keep your notebook clean, but be clear to show your development process, i.e. how you got from your design, to some test lines of code, to the final function.  Use Markdown to document your process.

### Assignment
1. Create a new Jupyter notebook called 'SEDS-HW3.ipynb' and finish the in class excersize of creating a functionalized block of code to compute the pairwise correlation between rows in a pandas data frame.  Use Markdown between cells to document your work.  Be sure to use docstrings for all of your functions.  _Hint / requirement_ You should have three functions.  One for the whole entity `pairwise_correlation`, one for comparing two rows `corr_rowi_rowj`, and one for comparing one row to all the other rows `corr_rowi_vs_all`.
2. Move your functions to `df_utils.py` and import that file and the functions into the notebook.
3. For each function, create cell with _assert_ statements that tests various aspects of your function, including handling oddball inputs, expected outputs (size, shape and values).  Try to have at least three tests per function.
4. Convert the cells to unit test functions and save them to `test_df_utils.py`.  _Hint_ Don't forget to name the functions with the ``test_`` prefix!
5. Run the unit tests with `nosetests` at the command line and paste the output into this README.md below.


### Results of unit tests
```
taiyupan@Tai-Yus-MacBook-Pro:~/Desktop$ nosetests
....
----------------------------------------------------------------------
Ran 4 tests in 0.559s

OK
taiyupan@Tai-Yus-MacBook-Pro:~/Desktop$
```

### Grading rubric
5/5 - solid