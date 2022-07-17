# import mrjob
from mrjob.job import MRJob
# create a class to pass mrjob properties
class Bacon_count(MRJob):
    # create the mapper function to assign the input 
    # to key-value pairs
   def mapper(self, _, line):
    # use split method on each line of text
    # breaks list of words
       for word in line.split():
        # convert to lowercase
           if word.lower() == "bacon":
            # if match the search for bacon string
            # then show the key-value pair
               yield "bacon", 1
                # yield returns a generator object
                # like a lot, but not stored locally
   def reducer(self, key, values):
    # self to represent insance of the class
    # key for key-value pair in mapper
    # values for list of values created in mapper

    # then sum all of these values 
       yield key, sum(values)

# run the program
if __name__ == "__main__":
   Bacon_count.run()