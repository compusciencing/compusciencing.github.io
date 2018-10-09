---
layout: post
title:  "How to write a post"
categories: [blog, travel]
tags: [hot, summer]
---

# How to write a post

This is a short post describing the posting process for this blog. It will be updated as we find better methods or add new features.

Here is the summary:

```bash
# Clone the repository
git clone https://github.com/compusciencing/compusciencing.github.io.git
cd compusciencing.github.io/

# Checkout a new branch to work on (standard GitHub practice)
git checkout -b post-how-to-post

# Create a new post (see resources below)
touch _posts/2018-10-08-how-to-write-a-post.md

# <Edit the post>

# Add post to repository and commit
git add _posts/2018-10-08-how-to-write-a-post.md
git commit -m "Added a new post..."

# <Fork this repository on GitHub> or use https://hub.github.com/

# Add your remote and push your changes
git remote add YOUR_USER git://github.com/YOUR_USER/compusciencing.github.io.git
git push YOUR_USER feature
```

# Resources

- [Jekyll Documentation on Posts](https://jekyllrb.com/docs/posts/)
- [Markdown Documentation](https://daringfireball.net/projects/markdown/) (Markdown is the preferred format for writing posts)

categories: [blog, travel]
tags: [hot, summer]
