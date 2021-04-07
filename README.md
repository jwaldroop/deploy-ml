This repository is for testing/practicing deploying machine learning models.

Getting Started:
  To install the required libraries, run: "pip install -r requirements.txt" (or "pip3 install -r requirements.txt" depending on your version of Python) while in your virtual environment.

Model Fitting:
  In fit-model.ipynb it should be specified that the model should be fit on X and y. Using pipeline.fit, fit X and y to the pipeline. The model can be pickled using the pickle command in the second to last cell; this will saving the model as "model.pkl".

Using the Test File:
  To test on the pickled model, create a new file called newdata.py. Within this file, save the desired number of rows from the data as a list in the variable "newdata". Be sure to save all files. From a shell within the virtual environment, navigate to the directory with the .py files and run "python test_pickled_model.py" (or "python3 test_pickled_model.py").
