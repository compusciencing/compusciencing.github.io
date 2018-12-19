---
layout: post
title: "How to write a post"
categories: ["How To", "Meta"]
tags: ["blog"]
author: "Anthony J. Clark"
---

This is a short description of the posting process for this blog. It will be updated as we find better methods or add new features.

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

# <Submit a pull request on GitHub> or use https://hub.github.com/
```

In the above, you will need to replace:

- `post-how-to-post` with `post-<YOUR_POST_NAME>`,
- `2018-10-08-how-to-write-a-post.md` with `<DATE>-<YOUR_POST_NAME>`,
- `"Added a new post..."` with your commit message, and
- `YOUR_USER` with your GitHub username

You should be able to preview your post by pushing your markdown to your forked repository and viewing on GitHub, or you can look at the resources section below for more information. In either case, though, you will not see the same formatting and it will not include any custom CSS or JS.

# Post template

I have added a simple template post in the root directory named `post-template.md`. You can use this or base your post off of another post.

You have a few key things to remember:

1. You must include [front matter](https://jekyllrb.com/docs/front-matter/){:target="_blank"} at the top of your post. You should include at least the following fields: `layout`, `title`, `author`, `categories`, and `tags`. For example, if you are writing this post for the Missouri State University CSC 596 course, at minimum you should include the category `"Missouri State University"` and the tag `csc596` (you should also include any other relevant categories and tags).
2. You should write your post in Markdown.

# Review process

After you submit your post via a pull request, it will be reviewed and you might be asked to fix grammar or some of your text. This will be done using the [GitHub pull request functionality](https://help.github.com/articles/about-pull requests/){:target="_blank"} (see also [Creating a Pull Request](https://help.github.com/articles/creating-a-pull-request/){:target="_blank"}).

Once the review process is complete, you should delete the git branch you created to make your post. You can delete your remote branch on GitHub by clicking the `Delete branch` button that appears on the pull request after it has been merged.

You can delete your local branch with the following:

```bash
git branch -d post-how-to-post
```

# Updating your local repository

If you want to update your local repository (for example, to prepare to submit a new post), you should follow these steps, which assume that you used the process above to clone and fork the repository.

```bash
# Fetch the updated files from the compusciencing repository
git fetch origin

# Checkout your local master branch and merge the origin files
git checkout master
git merge origin/master

# Create a new branch (as described above) to create a new post
```

# Resources

- [Jekyll Documentation on Posts](https://jekyllrb.com/docs/posts/){:target="_blank"}
- [Markdown Documentation](https://daringfireball.net/projects/markdown/){:target="_blank"} (Markdown is the preferred format for writing posts)
- [Previewing Your Markdown Post](http://lmgtfy.com/?q=markdown+editor){:target="_blank"} (you can use any Markdown editor to view a version of your post locally before you submit; **the styling will be different though**)
