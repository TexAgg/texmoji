# TeXMoji
Ever thought your PhD thesis was lacking pizzaz?
Or your paper needed more excitement?
Enter TeXMoji, emojis for LaTeX.

---

## Usage
Use `\texmoji{<n>}`, where `n` is the emoji's number on the chart [here](http://unicode.org/emoji/charts/full-emoji-list.html)

---

## Instructions

### Data
`populate.py` scrapes the [full emoji database](http://unicode.org/emoji/charts/full-emoji-list.html)
using [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
and saves the emojis as images, as well as saving a JSON file.

### Compilation
`main.py` uses Jinja2 to create `texmoji.sty`, so that I don't have to fill it by hand.