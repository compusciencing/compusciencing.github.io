---
layout: post
title: "Mocking `IPython.display`"
tags: ["ipython", "mocking", "fastai"]
author: "Anthony J. Clark"
---

[fastai](https://docs.fast.ai) is a nice library for quickly getting started with a deep learning project. It was developed for interactive environments (i.e., Jupyter Notebooks) and using interactive environments, see [nbdev](https://nbdev.fast.ai/).
This is nice for most use-cases, however, we eventually run all of our scripts on a headless server without an interactive environment.

This means that we lose some of fastai's functionality. For example, the ability to display the top loss images during image classification. We would still like this information, though, and we've figured out a way to make it work in a non-interactive environment.

Here is some code that causes problems (see the [computer vision intro](https://docs.fast.ai/tutorial.vision.html) for more information):

~~~python
interp = Interpretation.from_learner(learn)
interp.plot_top_losses(9)
~~~

This works fine in an interactive environment, but does not produce an output that we can save in a script. Other functions, like `interp.plot_confusion_matrix()`, work fine because they create a `matplotlib` figure that can be saved. Digging into `interp.plot_top_losses()` leads us to [`display_df`](https://github.com/fastai/fastai/blob/96f0e2027c8fd82eef40984faf14c1c81e0eb031/fastai/torch_core.py#L599), which I've copied below.

~~~python
def display_df(df):
    "Display `df` in a notebook or defaults to print"
    try: from IPython.display import display, HTML
    except: return print(df)
    display(HTML(df.to_html()))
~~~

`display_df` calls `display`, which, as far as I was able to determine, does not produce an output that is easy to consume in a script. So, I created this simplified, two-file example to demonstrate and work on the problem.

~~~python
# fake.py
def fake_plot_top_losses():
    from IPython.display import HTML, display
    display(HTML("<div>df</div>"))
~~~

~~~python
# mocking_ipython.py
from unittest.mock import MagicMock, patch

from fake import fake_plot_top_losses


def my_HTML(html):
    my_HTML.html = html


ipython_display_mock = MagicMock()
ipython_display_mock.HTML = my_HTML

with patch.dict("sys.modules", {"IPython.display": ipython_display_mock}):
    fake_plot_top_losses()

print(my_HTML.html)
~~~

Using the `patch.dict` context manager, we can replace the `IPython.display` module with our own mock. We then provide a replacement for the `HTML` function, which is passed the raw HTML that we want to save.

We are going to adapt this to our [`wandb`](https://wandb.ai) logging setup and add an example below once we have it working.
