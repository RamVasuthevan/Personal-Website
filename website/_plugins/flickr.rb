require 'flickraw'

FlickRaw.api_key="560084e59b5e27649a517fc337364c28"
FlickRaw.shared_secret="91eca2425d9a8c89"

flickr.access_token = "72157720890287435-829466205524b763"
flickr.access_secret = "2fe3e5df0e56d187"

# From here you are logged:
login = flickr.test.login
puts "You are now authenticated as #{login.username}"
# http://hanklords.github.io/flickraw/#label-Authentication