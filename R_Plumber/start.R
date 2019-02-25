library(plumber)
r <- plumb("plumber.R")  # Where 'plumber.R' is the location of the file shown above
r$run(host="127.0.0.1",port=8000, swagger=TRUE)

