print('Weclome to my final grade calculator!\nPlease enter your current grade:')
currentGrade = float(input())
print('Enter in the percentage of your grade the final is worth (eg. 30 for 30%):')
finalPercent = float(input())
print('Finally, enter the grade you want to get in the class:')
finalGrade = float(input())
x = (finalGrade - currentGrade*(1-(finalPercent/100)))/(finalPercent/100)
print(x)

