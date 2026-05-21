# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]

#Convert the list shelf1_update into a tuple called shelf1_update_tuple
shelf1_update_tuple = tuple(shelf1_update)

#Combine shelf1_update_tuple with shelf1 and store the result in shelf1_concat
shelf1_concat = shelf1 + shelf1_update_tuple
print("Updated Shelf #1:", shelf1_concat)

#Count how many times "celery" appears in shelf1_concat and store it in celery_count
celery_count = shelf1_concat.count("celery")
print("Number of Celery:", celery_count)

#Find the index of the first occurrence of "celery" in shelf1_concat and store it in celery_index
celery_index = shelf1_concat.index("celery")
print("Celery Index:", celery_index)