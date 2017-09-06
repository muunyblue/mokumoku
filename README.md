# Dependency

```
pip install pelican
pip install Markdown
pip install mdx_embedly
pip install ghp-import
# plubins
git clone https://github.com/getpelican/pelican-plugins
cd pelican-plugins
git submodule update --init always_modified
```

Theme: [yymm/mokumoku: Pelican theme for もくもくブログ](https://github.com/yymm/mokumoku "yymm/mokumoku: Pelican theme for もくもくブログ")

```
git submodule init && git submodule update
```

# Deploy

```
pelican content -s pelicanconf.py -t mokumoku
ghp-import output
git push git@github.com:muunyblue/muunyblue.github.io.git gh-pages:master
```
