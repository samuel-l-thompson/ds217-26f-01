measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Replace this scaffold output with your calculation, loop, decision, and summary.
#converting the review threshold to an integer
review_threshold = int(review_threshold_text)

#Start total and review count at 0
total = 0
review_count = 0

#using a for loop to iterate through the measurements
for measurement in measurements:
    #adding the measurement to the total
    total += measurement

    #checking if the measurement is greater than the review threshold
    if measurement >= review_threshold:
        #Labeling the measurement as needing review
        print(f"Measurement: {measurement} review")
        #incrementing the review count if the measurement is greater than the review threshold
        review_count += 1
    else:
        #Labeling the measurement as not needing review
        print(f"Measurement: {measurement} within range")
#calculate the mean using the actual list length
mean = total / len(measurements)
#print summary labels with comma separated values
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", mean)
print("Review count:", review_count)

