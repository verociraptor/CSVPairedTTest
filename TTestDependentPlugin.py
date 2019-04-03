import sys 
import csv
from scipy import stats

class TTestDependentPlugin:
	def input(self, filename):
		self.myfile = filename


	def run(self):
		f = open(self.myfile, 'r')
		csv_f = csv.reader(f)
		next(csv_f)

		self.column1, self.column2 = [], []

		for row in csv_f:
			self.column1.append(row[1])
			self.column2.append(row[2])

		#convert from string list to int list
		self.column1 = [int(i) for i in self.column1]
		self.column2 = [int(i) for i in self.column2]
		


	def output(self, filename):
		t, p = stats.ttest_rel(self.column1, self.column2)
		print(t, p)
