
# Question 1: By default, are Django signals executed synchronously or asynchronously?

# Signal handler
@receiver(post_save, sender=User)
def handle_post_save(sender, instance, **kwargs):
    print("Signal handler starts execution")
    time.sleep(5)  # Simulate a long-running process
    print("Signal handler finishes execution")

# In a script or view
def create_user():
    print("Creating user")
    user = User.objects.create(username="test_user")  
    print("User created")




# Question 2: Do Django signals run in the same thread as the caller?

# Signal handler
@receiver(post_save, sender=User)
def handle_post_save(sender, instance, **kwargs):
    print("Signal handler starts execution")
    time.sleep(5)  # Simulate a long-running process
    print("Signal handler finishes execution")

# In a script or view
def create_user():
    print("Creating user")
    user = User.objects.create(username="test_user") 
    print("User created")




# Question 3: By default, do Django signals run in the same database transaction as the caller?

# Signal handler
@receiver(post_save, sender=User)
def handle_post_save(sender, instance, **kwargs):
    print("Signal handler: Modifying user's first name")
    instance.first_name = "John"
    instance.save()  # Save inside signal

# In a script or view
def create_user_with_exception():
    try:
        with transaction.atomic():  # Start a transaction block
            user = User.objects.create(username="test_user")
            print("User created, but now raising an exception")
            raise Exception("Rolling back transaction")
    except Exception as e:
        print(f"Exception occurred: {e}")

    
    print(User.objects.filter(username="test_user").exists())
