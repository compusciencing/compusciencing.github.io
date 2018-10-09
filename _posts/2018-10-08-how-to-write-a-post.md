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
git remote add YOUR_USER https://github.com/YOUR_USER/compusciencing.github.io.git
git push YOUR_USER post-how-to-post
```

In the above, you will need to replace:

- `post-how-to-post` with `post-<YOUR_POST_NAME>`,
- `2018-10-08-how-to-write-a-post.md` with `<DATE>-<YOUR_POST_NAME>`,
- `"Added a new post..."` with your commit message, and
- `YOUR_USER` with your GitHub username

# Post template

I have added a simple template post in the root directory named `post-template.md`. You can use this or base your post off of another post.

You have a few key things to remember:

1. You must have the post [front matter](https://jekyllrb.com/docs/front-matter/). You should include at least: `layout`, `title`, `categories`, and `tags`. For example, if you are writing this post for the Missouri State University CSC 596 course, at minimum you should include the category `MSU` and the tag `csc596`.
2. You should write your post in Markdown.

# Review process

After you submit your post via a pull-request, if will be reviewed and you might be asked to fix grammar or some of your text. This will be done using the GitHub pull-request functionality.

# Resources

- [Jekyll Documentation on Posts](https://jekyllrb.com/docs/posts/)
- [Markdown Documentation](https://daringfireball.net/projects/markdown/) (Markdown is the preferred format for writing posts)
