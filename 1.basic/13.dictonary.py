# WELCOME TO HEY KYA KARU. DON'T FORGET TO SUBSCRIBE CHANEL TO GET NEW UPDATES

# मैं अनलाइन ट्रैनिंग भी देता हु तो अगर किसी को अनलाइन ट्रैनिंग करनी है तो मुझे कान्टैक्ट कर सकता है heykyakaru@gmail.com पर।

# HEY KYA KARU यूट्यूब के जरूरी लिंक 
# 1. Python Basic and Advance ट्यूटोरियल प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QikS9PMYrGZXz1HlE1KZLD3
# 2. PHP Projects प्लेलिस्ट https://www.youtube.com/playlist?list=PLK6wiPavf7QiEj6IPc3lkjz1wR4w9RM6B
# 3. GitHubट्यूटोरियल प्लेलिस्ट  https://www.youtube.com/watch?v=LUyVs2MTlTM&list=PLK6wiPavf7Qjydpc5v-hdIoqCx2V19pHP

# dictonary

dictonaryval = {'name':'ram','course':'python'}

# Accessing Items
print('\nName: ',dictonaryval['name'])
print('\nCourse: ',dictonaryval.get('course'))

# Change Values
dictonaryval['name'] = 'Mr. Ram'

# Dictionary Length len()

# Adding Items
dictonaryval['mobile'] = 987989879

# Removing Items
dictonaryval.pop('mobile')
dictonaryval.popitem()

# del
del dictonaryval

dictonaryval = {'name':'ram','course':'python'}

# Copy a Dictionary
copydictonary = dictonaryval.copy()

# clear()
dictonaryval.clear()

print('\n\nDetails: ',copydictonary)

# Nested Dictionaries
details = {
'ram': {
    'course':'python',
    'mobile':89798979,
    'email':'ram@gamil.com'
},
'shyam': {
    'course':'python',
    'mobile':89798979,
    'email':'ram@gamil.com'
}
}

print('\nRam',details['ram'])
print('\nShyam',details['shyam'])