#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
	cleaned_data = []

    ### your code goes here
	for i in range(0,81):
		tup = (ages[i], net_worths[i], (net_worths[i] - predictions[i])**2)
		cleaned_data.append(tup)
	for i in range(81,90):
		error = (net_worths[i] - predictions[i])**2
		for j in range(0,81):
			if(error < cleaned_data[j][2]):
				tup_new = (ages[i], net_worths[i], (net_worths[i] - predictions[i])**2)
				cleaned_data[j] = tup_new
				break
	print len(cleaned_data)
	return cleaned_data



