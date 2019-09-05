"""
Third Python Task. Flask website used to show python task one and two
Calls the functions from the previous two tasks and displays them
Uses the bootstrap starter template and HTML/CSS examples from https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/snippets

Written by Gabriel Lopez
"""
from flask import Flask, render_template, url_for
from python_tasks.Task1 import task_one
from python_tasks.Task2 import task_two
import pandas as pd
import json

app = Flask(__name__)

#Calls the function from task_one.py to display on the website
task_one.create_csv("gender_submission.csv","Output.csv","Output2.csv")
file_one = pd.read_csv("Output.csv", header=None)
file_two = pd.read_csv("Output2.csv", header=None)

#Calls the function from task_two.py to display on the website
call_result = task_two.get_monthly("https://www.alphavantage.co/query", task_two.params)


#First post for the Flask home page
post_one = [
	{
		'title':"Welcome",
		'content':"This is a website for the EZOPS Python Tasks",
		'date_posted':"August 28 2019"
	}
]
#Second post for the Flask home page
post_two = [
	{
		'title':"Task One",
		'content':"""
			For the first Python Task, I have to take a CSV file and output two CSV files.
			The first output file will be the same as the input
			The second file will have the rows and columns transposed.\n
			The input file is 'gender_submission.csv'
			And the two output files are 'Output.csv' and 'Output2.csv'.\n
		""",
		'outputs':[
			{
				'name':'gender_submission.csv',
				'code':file_one
			},
			{
				'name':'Output.csv',
				'code':file_one
			},
			{
				'name':'Output2.csv',
				'code':file_two
			}
		],
		'date_posted':"August 28 2019"
	}
]
#Third post for the Flask home page
post_three = [
	{
		'title':"Task Two",
		'content':"""
			For the second Python Task, I will contact the Alphavantage API to get the last three months of Microsoft's stock
		""",
		'outputs':[
			{
				'name':'Here is the result of the API call.',
				'code':json.dumps(call_result, indent=4)
			}
		],
		'date_posted':"August 28 2019"
	}
]


@app.route('/')
@app.route('/home')
def home():
	"""
	Creates the home page using the custom template and the first post
	"""
	return render_template('home.html', posts = post_one)

@app.route('/task1')
def task1():
	"""
	Creates the Task one page using the custom template and the second post
	"""
	return render_template('Task1.html', title='Task1', posts = post_two)

@app.route('/task2')
def task2():
	"""
	Creates the Task two page using the custom template and the third post
	"""
	return render_template('Task2.html', title='Task2', posts = post_three)


if __name__ == "__main__":
	app.run(debug=True)