def candies(k, score):
  # give one candy to everybody woohoo
  candy = [1 for x in range(n)]
  
  # iterate from start,
  # give one more candy
  # if next preson's score
  # is more than previous person's
  for i in range(1, n, 1):
    if score[i] > score[i-1]:
      candy[i] = candy[i-1] +1
  
  # iterate from the end,
  # give one more candy
  # if next preson's score
  # is more than previous person's
  # and candy is not more than previous person's
  for i in range(n-1, 0, -1):
    if score[i-1] > score[i] and candy[i-1] <= candy[i]:
      candy[i-1] = candy[i] +1
  
  # print(candy)
  
  total = sum(candy)
  
  return total