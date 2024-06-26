from farcaster import Warpcast

class FollowScript:
    def __init__(self, criteria, warpcast_client: Warpcast):
        self.criteria = criteria
        self.warpcast_client = warpcast_client

    def copy_following(self, username):
        fid = self.warpcast_client.get_user_by_username(username).fid
        users_to_follow = self.warpcast_client.get_all_following(fid).users
        successful_follows = 0

        for user in users_to_follow:
            try:
                self.warpcast_client.follow_user(user.fid)
                successful_follows += 1
            except Exception as e:
                pass
        print("You've successfully copied the following of user: {}. Total follows: {}\n".format(username, successful_follows))

    def follow_new_users(self, count):
        recent_users = self.warpcast_client.get_recent_users(limit=count).users
        successful_follows = 0

        for user in recent_users:
            try:
                self.warpcast_client.follow_user(user.fid)
                successful_follows += 1
            except Exception as e:
                pass
        print("You've successfully followed {} new users.\n".format(successful_follows))

    def follow_collection_owners(self, collection_id, limit=9999):
        collection_owners = self.warpcast_client.get_collection_owners(collection_id=collection_id, limit=limit).users
        successful_follows = 0

        for owner in collection_owners:
            try:
                self.warpcast_client.follow_user(owner.fid)
                successful_follows += 1
            except Exception as e:
                pass
        print("You've successfully followed the owners of collection: {}. Total follows: {}\n".format(collection_id, successful_follows))

    def execute(self):
        if self.criteria == '1':
            username = input("Enter the username to copy following from: ")
            self.copy_following(username)
        elif self.criteria == '2':
            count = int(input("Enter the number of new users to follow: "))
            self.follow_new_users(count)
        elif self.criteria == '3':
            collection_id = input("Enter the collection ID: ")
            self.follow_collection_owners(collection_id)


class UnfollowScript:
    def __init__(self, criteria, warpcast_client: Warpcast):
        self.criteria = criteria
        self.warpcast_client = warpcast_client

    def unfollow_all_users(self):
        following = self.warpcast_client.get_all_following().users
        successful_unfollows = 0

        for user in following:
            try:
                self.warpcast_client.unfollow_user(user.fid)
                successful_unfollows += 1
            except:
                pass  # Ignoring unfollow errors without displaying warning message
        print("You've successfully unfollowed all users. Total unfollows: {}\n".format(successful_unfollows))

    def unfollow_non_follow_back_users(self):
        following = self.warpcast_client.get_all_following().users
        followers = self.warpcast_client.get_all_followers().users

        following_fids = {user.fid for user in following}
        followers_fids = {user.fid for user in followers}

        non_follow_back_fids = following_fids - followers_fids
        successful_unfollows = 0

        for fid in non_follow_back_fids:
            try:
                self.warpcast_client.unfollow_user(fid)
                successful_unfollows += 1
            except:
                pass
        print("You've successfully unfollowed {} users who didn't follow you back.\n".format(successful_unfollows))

    def unfollow_collection_owners(self, collection_id, limit=9999):
        collection_owners = self.warpcast_client.get_collection_owners(collection_id=collection_id, limit=limit).users
        successful_unfollows = 0

        for owner in collection_owners:
            try:
                self.warpcast_client.unfollow_user(owner.fid)
                successful_unfollows += 1
            except:
                pass
        print("You've successfully unfollowed the owners of collection: {}. Total unfollows: {}\n".format(collection_id, successful_unfollows))
        
    def unfollow_no_casters(self):
        counter = 0
