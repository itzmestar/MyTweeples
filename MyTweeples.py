import twitter

api=twitter.Api(consumer_key='',
                consumer_secret='',
                access_token_key='',
                access_token_secret='')

#print(api.VerifyCredentials())

following = api.GetFriends()
following_list = [u.screen_name for u in following]
#print(following_list)

followers = api.GetFollowers()
followers_list = [u.screen_name for u in followers]


print("List of Tweeples not following you:")
unfollow_list=list(set(following_list).difference(set(followers_list)))

for tweeple in unfollow_list:
    ans=input('Unfollow {}?[y/n]'.format(tweeple))
    if ans == 'y':
        print("unfollowed {}".format(tweeple))
        api.DestroyFriendship(screen_name=tweeple)


