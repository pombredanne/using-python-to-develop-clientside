# Building the navigation

Let's make a common folder, to hold shared [components](https://vuejs.org/v2/guide/components.html).

```bash
mkdir common
cd common
```

## navigation.py

```Python
v = require('vue')
t = require('../tmpl')

v.component('navigation', {
  'template': t['navigation.html'],
  'data': (lambda: {}),
})

```

### Whoa, what we did?!

It gets really hard maintaining inlined HTML, for years developers have campaigned for not including shit like `elem.innerHTML = '<h1>Insanity</h1>'`, I use a simple script to bundle templates into the browser, and **MY HONEST SUGGESTION: DO NOT PLEASE INLINE HTML, I tell that to each React developer I see.**

[The script is available here](../bundletmpl.py)

## So, let's make a folder named tmpls


```bash
mkdir tmpls
```

### tmpls/navigation.html

```html
<md-toolbar>
  <router-link class="md-title mainlinky" to="/">TODO dude</router-link>
</md-toolbar>
```

### Bundle it.

```bash
python bundletmpl.py
```

### Creating the importer

### common/__init__.py

```Python
from common import navigation
```

### main.py

```Python
import common
from url import fmap
```

### Woah, let's give it a shot

Make the app look like this

```html
<div id="app">
  <navigation></navigation>
  <router-view></router-view>
</div>
```

# What happened?

I know, it looks like some weird stuff, that's because we haven't (yet) included the CSS that's required, let's do it.

## index.html

```html
<title>A test project, for fun</title>
<link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,400,500,700,400italic">
<link rel="stylesheet" href="//fonts.googleapis.com/icon?family=Material+Icons">
<link rel="stylesheet" href="https://unpkg.com/vue-material/dist/vue-material.css">
```

Now, reload.

# Dark magick
