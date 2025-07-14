import praw
praw.Reddit.check_for_async = False

# Reddit credentials
client_id = "your_id"
client_secret = "your_secret"
user_agent = "my_reddit_scraper by u/PersonaScraper"

# Reddit user
username = "Hungry-Move-6603"

# Reddit API connect
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

with open(f"{username}.txt", "w", encoding="utf-8") as f:
    f.write(f"User: u/{username}\n\n")

    f.write(" Recent Comments:\n")
    for comment in reddit.redditor(username).comments.new(limit=10):
        f.write("- " + comment.body[:200].replace("\n", " ") + "\n")
        f.write(f"  [Source: https://reddit.com{comment.permalink}]\n\n")

    f.write("\n Recent Posts:\n")
    for post in reddit.redditor(username).submissions.new(limit=10):
        f.write("- " + post.title + "\n")
        f.write(f"  [Source: https://reddit.com{post.permalink}]\n\n")

print(f"\n File '{username}.txt' created successfully.")
